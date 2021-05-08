import psycopg2

# Connect to cothistory DB
conn = psycopg2.connect(
    host="localhost",
    database="cothistory",
    user='postgres',
    password='contact me for password'
)
cur = conn.cursor()
