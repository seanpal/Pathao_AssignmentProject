import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'book_application'
username = 'postgres'
pwd = 'pass'
port_id = 5432
conn = None

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS author');
            cur.execute('DROP TABLE IF EXISTS publisher');
            cur.execute('DROP TABLE IF EXISTS reviews');
            cur.execute('DROP TABLE IF EXISTS checkouts');
            cur.execute('DROP TABLE IF EXISTS addresses');
            cur.execute('DROP TABLE IF EXISTS users');
            cur.execute('DROP TABLE IF EXISTS books');

            create_script = ''' CREATE TABLE users (
                              user_id SERIAL,
                              name varchar(30) NOT NULL,
                              enabled BOOLEAN,
                              last_login timestamp DEFAULT CURRENT_TIMESTAMP,
                              PRIMARY KEY (user_id)
                            );
                            CREATE TABLE addresses (
                              id SERIAL,
                              user_id integer, 
                              street varchar(30),
                              city varchar(30),
                              country varchar(30) NOT NULL,
                              PRIMARY KEY (id),
                              FOREIGN KEY (user_id)
                                  REFERENCES users (user_id)
                                  ON DELETE CASCADE
                            );
                            CREATE TABLE author (
                              author_id SERIAL,
                              author_name varchar(255),
                              author_dob DATE,
                              author_details varchar(100),
                              PRIMARY KEY (author_id)
                            );
                            CREATE TABLE publisher (
                              publisher_id SERIAL,
                              publisher_name varchar(255),
                              publisher_address varchar(255),
                              publisher_phone varchar(255),
                              PRIMARY KEY (publisher_id)
                            );
                            CREATE TABLE books (
                              id SERIAL,
                              title varchar(100) NOT NULL,
                              author_id INT NOT NULL,
                              publisher_id INT NOT NULL,
                              published_date DATE,
                              isbn char(12),
                              PRIMARY KEY (id),
                              UNIQUE (isbn)
                            );
                            CREATE TABLE reviews (
                              id SERIAL,
                              book_id integer NOT NULL,
                              reviewer_name varchar(255),
                              content varchar(255),
                              rating integer,
                              published_date timestamp DEFAULT CURRENT_TIMESTAMP,
                              PRIMARY KEY (id)
                            );
                            CREATE TABLE checkouts (
                              id SERIAL,
                              user_id int NOT NULL,
                              book_id int NOT NULL,
                              checkout_date timestamp,
                              return_date timestamp,
                              PRIMARY KEY (id)
                            );'''
            cur.execute(create_script)
            print("TABLE CREATED SUCCESSFULLY");

            
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()