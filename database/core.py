# from typing import Self
import psycopg2


class Connection:
    """
    Connection with PosgreSQL
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(
                Connection, cls
            ).__new__(cls)
        return cls.instance

    def __init__(
        self,
        host: str,
        port: int,
        user: str,
        password: str,
        dbname: str
    ) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.dbname = dbname
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname=self.dbname
            )
            self.conn.autocommit = True
            print('[SUCCESS] Connection is success!')
        except Exception as e:
            print(e)
            print("[ERROR] CONNECTION ERROR!")

    def create_tables(self) -> None:
        try:
            with self.conn.cursor() as cur:
                cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(200) NOT NULL,
            last_name VARCHAR(200) NOT NULL,
            login VARCHAR(20) UNIQUE NOT NULL,
            email VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(14) NOT NULL,
            date_of_birth DATE NOT NULL,
            author BOOLEAN DEFAULT('false')
        );
        CREATE TABLE IF NOT EXISTS articles(
            id SERIAL PRIMARY KEY,
            title VARCHAR(120) UNIQUE NOT NULL,
            heading TEXT NOT NULL,
            date_publication TIMESTAMP DEFAULT(NOW()),
            rate INTEGER DEFAULT(1),
            count_reviews INTEGER DEFAULT(0)
        );
        CREATE TABLE IF NOT EXISTS comments(
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id) NOT NULL,
            aricle_id INTEGER REFERENCES articles(id) NOT NULL,
            text VARCHAR(200) NOT NULL
        );
        '''
    )
        except:
            print('[ERROR] CAN CREATE TABLES')