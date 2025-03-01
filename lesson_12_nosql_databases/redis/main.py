from customer import Customer
from redis_client import create_session, read_session, update_session, delete_session

customer = Customer(1, 'Test Name')

# Create customer session
customer_session = create_session(customer)
customer.session_token = customer_session.session_token

# Get customer session
customer_session = read_session(customer)
print(customer_session)

# Update customer session
customer_session = update_session(customer)
print(customer_session)

# Delete session
delete_session(customer)
# print(read_session(customer)) # ValueError:  No customer session found.
