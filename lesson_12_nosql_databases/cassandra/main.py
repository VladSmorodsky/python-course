import uuid
from datetime import datetime, timedelta

from cassandra_client import create_event_logs_table, insert_event, get_daily_events_by_type, update_event_metadata, \
    delete_old_events
from customer import Customer


def get_events_by_type(event_type: str) -> None:
    """
    Return events based on event type
    :param event_type:
    :return:
    """
    events = get_daily_events_by_type(event_type)
    for event in events:
        print(f"Event Id: {event.event_id}, Event: {event.event_type}, Time: {event.timestamp}")


# Create event_logs table
create_event_logs_table()

customer = Customer(uuid.uuid4(), 'Test User')
customer2 = Customer(uuid.uuid4(), 'Test User2')
# Login event
insert_event(customer, 'login', {'ip': '192.168.1.1', 'device': 'mobile'})
insert_event(customer2, 'login', {'ip': '192.168.2.1', 'device': 'mobile'}, datetime.now() - timedelta(weeks=2))
insert_event(customer, 'save', {'ip': '192.168.1.1', 'device': 'mobile'})

# Get daily events with type 'login'
get_events_by_type('login')

# Update event's metadata
event = get_daily_events_by_type('save')[0]
update_event_metadata(event.event_id, {"ip": "192.168.120.20", "device": "laptop"})

# Delete events
delete_old_events()
