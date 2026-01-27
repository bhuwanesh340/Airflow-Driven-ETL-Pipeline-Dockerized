from api_request import mock_fetch_data, fetch_data
import psycopg2

# print(mock_fetch_data())

def connect_to_db():
    print("Connecting to the database...")
    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,
            dbname="db",
            user="db_user",
            password="db_password"
        )
        print("Database connection successful.")
        print(conn)
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_table(conn):
    print("Creating table if not exists...")
    try:
        cursor = conn.cursor()
        create_table_query = '''
        CREATE SCHEMA IF NOT EXISTS dev;
        CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100),
            temperature FLOAT,
            weather_description VARCHAR(255),
            wind_speed FLOAT,
            time TIMESTAMP,
            inserted_at TIMESTAMP DEFAULT NOW(),
            utc_offset VARCHAR(10)
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        print("Table created or already exists.")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")


def insert_records(conn, data):
    print("Inserting data into the database...")
    try:
        cursor = conn.cursor()
        insert_query = '''
        INSERT INTO dev.raw_weather_data (city, temperature, weather_description, wind_speed, time, inserted_at, utc_offset)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        '''
        city = data['location']['name']
        temperature = data['current']['temperature']
        weather_description = data['current']['weather_descriptions'][0]
        wind_speed = data['current']['wind_speed']
        time = data['location']['localtime']
        inserted_at = data['location']['localtime']
        utc_offset = data['location']['utc_offset']

        cursor.execute(insert_query, (city, temperature, weather_description, wind_speed, time, inserted_at, utc_offset))
        conn.commit()
        cursor.close()
        print("Data inserted successfully.")
    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")


def main():
    try:
        # data = mock_fetch_data()
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"Error in main: {e}")    
