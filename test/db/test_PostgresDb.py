import unittest
from contextlib import closing

import testing.postgresql
import psycopg2
import pg8000

# These tests are dependent on the following third party modules:
#   - pip install testing.postgresql
#   - pip install psycopg2-binary


# create initial data in Postgres as fixtures to be used for testing
def handler(postgresql):
    conn = psycopg2.connect(**postgresql.dsn())
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE hello(id integer, value varchar(256));")
    cursor.execute("INSERT INTO  hello(id, value) VALUES(%s, %s)", (1, 'hello'))
    cursor.execute("INSERT INTO  hello(id, value) VALUES(%s, %s)", (2, 'ciao'))
    cursor.close()
    conn.commit()
    conn.close()

# For other examples of setup and teardown
# https://github.com/tk0miya/testing.postgresql/blob/1.3.0/tests/test_postgresql.py


class PostgresSpec(unittest.TestCase):

    # This is called BEFORE each of the tests below are run
    def setUp(self):
        self.Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True,
                                                               on_initialized=handler)
        self.postgresql_instance = self.Postgresql()

    # This is called AFTER each of the tests below are run
    def tearDown(self):
        self.postgresql_instance.stop()
        self.Postgresql.clear_cache()

    def test_00_can_read_Hello(self):
        with self.postgresql_instance as pgsql:
            conn = pg8000.connect(**pgsql.dsn())
            with closing(conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM hello ORDER BY id;')
                self.assertEqual(cursor.fetchall(), ([1, 'hello'], [2, 'ciao']))
            conn.close()

    def test_01_can_insert_into_and_read_Hello(self):
        with self.postgresql_instance as pgsql:
            conn = pg8000.connect(**pgsql.dsn())
            with closing(conn.cursor()) as cursor:
                cursor.execute("INSERT INTO hello values(3, 'hello again!');")
                cursor.execute('SELECT * FROM hello ORDER BY id;')
                self.assertEqual(cursor.fetchall(), ([1, 'hello'], [2, 'ciao'], [3, 'hello again!']) )
            conn.close()

    def test_02_can_create_and_read_MyTable(self):
        with self.postgresql_instance as pgsql:
            conn = pg8000.connect(**pgsql.dsn())
            with closing(conn.cursor()) as cursor:
                cursor.execute("CREATE TABLE MyTable(id int, value varchar(256));")
                cursor.execute("INSERT INTO mytable values(1, 'hello'), (2, 'ciao');")
                cursor.execute('SELECT * FROM mytable ORDER BY id;')
                self.assertEqual(cursor.fetchall(), ([1, 'hello'], [2, 'ciao']))
            conn.close()


if __name__ == '__main__':
    unittest.main()
