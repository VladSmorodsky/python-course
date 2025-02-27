"""
Cassandra provides factors and strategies for replication.

Replication Factors: Cassandra uses the concept of a replication factor,
which defines how many copies (replicas) of each data row will be stored in the cluster.
For example, if the replication factor is set to 3,
the data will be stored on three different nodes.

Replication Strategies: There are two main replication strategies:
- SimpleStrategy: Used for a single availability zone and simply distributes replicas
in order.
- NetworkTopologyStrategy: Used for clusters that have multiple availability zones.
This strategy allows control over the distribution of replicas across zones,
ensuring high availability and fault tolerance.
"""
import os
import traceback
import uuid
from contextlib import contextmanager
from datetime import datetime, timedelta
from typing import Any, Optional, Generator

from cassandra.cluster import Cluster, ConnectionException, NoHostAvailable, Session
from cassandra import InvalidRequest
from cassandra.protocol import SyntaxException
from cassandra.query import BatchStatement
from dotenv import load_dotenv

from customer import Customer

load_dotenv()

cluster_name = os.getenv("CASSANDRA_CLUSTER_NAME", 'localhost')
cluster_port = os.getenv("CASSANDRA_CLUSTER_PORT", 9042)


@contextmanager
def cassandra_session() -> Generator[Session, None, None]:
    """
    Create a Cassandra session.
    :return:
    """
    cluster = Cluster([cluster_name], port=cluster_port)
    session = cluster.connect()
    try:
        yield session
    except ConnectionException | NoHostAvailable | SyntaxException as error:
        print(f"Cluster not available: {error}")
    finally:
        session.shutdown()
        cluster.shutdown()


def create_event_logs_table(session: Session) -> None:
    """
    Create event_logs table
    :param session:
    :return:
    """
    # Create key space (db analog)
    try:
        session.execute("""
        CREATE KEYSPACE IF NOT EXISTS logger
        WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'dc1': 3, 'dc2': 3 }
        """)

        session.set_keyspace('logger')
        session.execute("""
        CREATE TABLE IF NOT EXISTS event_logs_by_type (
            event_id UUID,
            user_id UUID,
            event_type TEXT,
            created_at TIMESTAMP,
            metadata MAP<TEXT, TEXT>,
            PRIMARY KEY ((event_type), created_at)
            )
        """)
        session.execute("""
        CREATE TABLE IF NOT EXISTS event_logs (
            event_id UUID,
            user_id UUID,
            event_type TEXT,
            created_at TIMESTAMP,
            metadata MAP<TEXT, TEXT>,
            PRIMARY KEY (event_id)
            )
        """)
    except InvalidRequest as error:
        print(error)


def insert_event(session: Session, customer: Customer, event_type: str, metadata: Optional[dict[str, Any]] = None,
                 timestamp: datetime = None) -> None:
    """
    Insert an event into the database.
    :param session:
    :param customer:
    :param event_type:
    :param metadata:
    :param timestamp:
    :return:
    """
    try:
        event_id = uuid.uuid4()
        timestamp = timestamp if timestamp is not None else datetime.now()

        session.execute("""
        INSERT INTO event_logs (event_id, user_id, event_type, created_at, metadata)
        VALUES (%s, %s, %s, %s, %s)
        """, (event_id, customer.id, event_type, timestamp, metadata))

        session.execute("""
        INSERT INTO event_logs_by_type (event_id, user_id, event_type, created_at, metadata)
        VALUES (%s, %s, %s, %s, %s)
        """, (event_id, customer.id, event_type, timestamp, metadata))
    except InvalidRequest as error:
        print(error)


def get_daily_events_by_type(session: Session, event_type: str):
    """
    Get all events from the database.
    :param session:
    :param event_type:
    :return:
    """
    try:
        return session.execute("""SELECT * FROM event_logs_by_type WHERE event_type = %s and created_at > %s;""",
                               (event_type, datetime.now() - timedelta(hours=24),), )
    except InvalidRequest as error:
        print(error)


def update_event_metadata(session: Session, event_id: uuid.UUID, metadata: dict[str, Any]) -> None:
    """
    Update the metadata of the event in the database.
    :param session:
    :param metadata:
    :param event_id:
    :return:
    """
    try:
        session.execute(
            """UPDATE event_logs SET metadata = %s WHERE event_id = %s""",
            [metadata, event_id],
        )
        event = session.execute("""SELECT event_type, created_at FROM event_logs WHERE event_id = %s""",
                                [event_id]).one()
        session.execute(
            """UPDATE event_logs_by_type SET metadata = %s WHERE created_at = %s AND event_type = %s""",
            [metadata, event[1], event[0]],
        )
    except InvalidRequest | SyntaxException as error:
        print(error)
        traceback.print_exc()


def delete_events_by_week(session: Session, event_type: str) -> None:
    """
    Delete events from the database, that keeps more than one week.
    :param event_type:
    :param session:
    :return:
    """
    try:
        events = session.execute(
            """SELECT event_id, event_type, created_at FROM event_logs_by_type WHERE event_type = %s AND created_at < %s""",
            [event_type, datetime.now() - timedelta(weeks=1)]).all()
        print(events)

        batch = BatchStatement()

        for event in events:
            batch.add(
                "DELETE FROM event_logs WHERE event_id = %s",
                (event[0],),
            )
            batch.add(
                "DELETE FROM event_logs_by_type WHERE event_type = %s AND created_at = %s",
                (event[1], event[2]),
            )
        session.execute(batch)
    except InvalidRequest as error:
        print(error)
        traceback.print_exc()
