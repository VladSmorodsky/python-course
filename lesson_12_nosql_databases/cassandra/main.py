import uuid
from datetime import datetime, timedelta

from cassandra_client import create_event_logs_table, insert_event, get_daily_events_by_type, update_event_metadata, \
    delete_events_by_week, cassandra_session
from customer import Customer

with cassandra_session() as session:
    # Create event_logs table
    create_event_logs_table(session)

    customer = Customer(uuid.uuid4(), 'Test User')
    customer2 = Customer(uuid.uuid4(), 'Test User2')
    # Login event
    insert_event(session, customer2, 'login', {'ip': '192.168.1.1', 'device': 'mobile'})
    insert_event(session, customer2, 'logout', {'ip': '192.168.2.1', 'device': 'mobile'}, datetime.now() - timedelta(days=9))
    insert_event(session, customer, 'save', {'ip': '192.168.1.1', 'device': 'mobile'})

    # Get daily events with type 'login'
    events = get_daily_events_by_type(session, "login")
    for event in events:
        print(
            f"Event Id: {event.event_id}, User Id: {event.user_id}, Event: {event.event_type}, Time: {event.created_at}")

    # Update event's metadata
    event = get_daily_events_by_type(session, 'save')[0]
    update_event_metadata(session, event.event_id, {"ip": "192.168.120.20", "device": "laptop"})

    # Delete events
    delete_events_by_week(session, 'logout')
