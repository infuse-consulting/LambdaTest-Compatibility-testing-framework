from faker import Faker

def generate_dummy_names():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    return first_name, last_name

