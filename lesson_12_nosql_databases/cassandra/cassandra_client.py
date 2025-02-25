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


import uuid
from datetime import datetime, timedelta
from typing import Any, Optional

from cassandra.cluster import Cluster

from customer import Customer

cluster = Cluster(['localhost'])
session = cluster.connect()


def create_event_logs_table() -> None:
    """
    Create event_logs table
    :return:
    """
    # Create key space (db analog)
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS logger
    WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'replication_factor' : 3 }
    """)

    session.set_keyspace('logger')
    session.execute("""
    CREATE TABLE IF NOT EXISTS event_logs (
        event_id UUID,
        user_id UUID,
        event_type TEXT,
        timestamp TIMESTAMP,
        metadata MAP<TEXT, TEXT>,
        PRIMARY KEY (event_id, timestamp)
        )
    """)


def insert_event(customer: Customer, event_type: str, metadata: Optional[dict[str, Any]] = None,
                 timestamp: datetime = None) -> None:
    """
    Insert an event into the database.
    :return:
    """
    event_id = uuid.uuid4()
    timestamp = timestamp if timestamp is not None else datetime.now()

    session.execute("""
    INSERT INTO event_logs (event_id, user_id, event_type, timestamp, metadata)
    VALUES (%s, %s, %s, %s, %s)
    """, (event_id, customer.id, event_type, timestamp, metadata))


def get_daily_events_by_type(event_type: str):
    """
    Get all events from the database.
    :return:
    """
    return session.execute("""SELECT * FROM event_logs WHERE event_type = %s and timestamp > %s  ALLOW FILTERING;""",
                           (event_type, datetime.now() - timedelta(hours=24),), )


def update_event_metadata(event_id: uuid.UUID, metadata: dict[str, Any]) -> None:
    """
    Update the metadata of the event in the database.
    :param metadata:
    :param event_id:
    :return:
    """
    rows = session.execute(
        "SELECT event_id, timestamp FROM event_logs WHERE event_id = %s AND timestamp < %s",
        [event_id, datetime.now()],
    )

    for row in rows:
        session.execute(
            "UPDATE event_logs SET metadata = %s WHERE event_id = %s AND timestamp = %s",
            [metadata, row.event_id, row.timestamp]
        )


def delete_old_events() -> None:
    """
    Delete events from the database, that keeps more than one week.
    :return:
    """
    rows = session.execute(
        "SELECT event_id, timestamp FROM event_logs WHERE timestamp < %s ALLOW FILTERING",
        [datetime.now() - timedelta(weeks=1)],
    )

    for row in rows:
        session.execute(
            "DELETE FROM event_logs WHERE event_id = %s AND timestamp = %s",
            [row.event_id, row.timestamp]
        )
