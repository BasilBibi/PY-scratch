import psycopg2


def query_PostGres():

    conn = None

    try:
        conn = psycopg2.connect("dbname=testdb user=postgres password=postgres")
        cur = conn.cursor()

        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

query_PostGres()