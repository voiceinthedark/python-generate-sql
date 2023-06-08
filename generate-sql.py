import random
import json
import datetime

def load_names_from_file(filename):
    with open(filename) as f:
        return json.load(f)

def generate_random_email(first_name, last_name):
    domains = load_names_from_file('domain-name.json')
    suffixes = load_names_from_file('domain-suffix.json')
    domain = random.choice(domains) + random.choice(suffixes)
    return f'{first_name.lower()}.{last_name.lower()}@{domain}'

def generate_random_name():
    first_names = load_names_from_file('first-names.json')
    last_names = load_names_from_file('last-names.json')
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return f'{first_name} {last_name}'

def generate_random_date():
    start_date = datetime.datetime(2000, 1, 1)
    end_date = datetime.datetime(2023, 12, 31)

    days_between = (end_date - start_date).days
    random_number_of_days = random.randrange(days_between)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    random_time = datetime.time(random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))

    random_datetime = datetime.datetime.combine(random_date.date(), random_time)

    return str(random_datetime)

def generate_random_boolean():
    return random.randint(0, 1)

def generate_insert_query(email, full_name, is_active, created_at):
    return f"INSERT INTO users (email, full_name, is_active, created_at) VALUES ('{email}', '{full_name}', {is_active}, '{created_at}');"

def generate_records(num_records=10):
    records = []
    for _ in range(num_records):
        full_name = generate_random_name()
        email = generate_random_email(full_name.split(' ')[0], full_name.split(' ')[1])
        is_active = generate_random_boolean()
        created_at = generate_random_date()
        records.append(generate_insert_query(email, full_name, is_active, created_at))
    return records

def save_to_file(records, filename='sql_query.sql'):
    with open(filename, 'w') as file:
        for record in records:
            file.write(record + '\n')

# Generate records and save to file
records = generate_records()
save_to_file(records)
