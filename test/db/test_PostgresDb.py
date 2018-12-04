import unittest
import testing.postgresql
import psycopg2
import pg8000
from contextlib import closing


# create initial data on create as fixtures into the database
def handler(postgresql):
    conn = psycopg2.connect(**postgresql.dsn())
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE hello(id int, value varchar(256))")
    cursor.execute("INSERT INTO hello values(1, 'hello'), (2, 'ciao')")
    cursor.close()
    conn.commit()
    conn.close()


# Use `handler()` on initialize database
Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True,
                                                  on_initialized=handler)


class PostgresSpec(unittest.TestCase):

    def setUp(self):
        # Use the generated Postgresql class instead of testing.postgresql.Postgresql
        self.postgresql = Postgresql()

    def tearDown(self):
        self.postgresql.stop()
        Postgresql.clear_cache()

    def test_00_can_read_Hello(self):
        with self.postgresql as pgsql:
            conn = pg8000.connect(**pgsql.dsn())
            with closing(conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM hello ORDER BY id')
                self.assertEqual(cursor.fetchall(), ([1, 'hello'], [2, 'ciao']))
            conn.close()


if __name__ == '__main__':
    unittest.main()
