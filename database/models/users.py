# Python
import datetime

# Local
from database.core import Connection


class User:
    """Object from db. User."""

    id: int
    first_name: str
    last_name: str
    login: str
    email: str
    password: str
    date_of_birth: datetime.datetime
    author: bool

    @staticmethod
    def create(
        conn: Connection,
        first_name: str,
        last_name: str,
        login: str,
        email: str,
        password: str,
        date_of_birth: datetime,
        author: bool
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO users(
                    first_name,
                    last_name,
                    login,
                    email,
                    password,
                    date_of_birth,
                    author
                )
                VALUES (
                    '{first_name}',
                    '{last_name}',
                    '{login}',
                    '{email}',
                    '{password}',
                    '{date_of_birth}',
                    '{author}'
                )
                """
            )

    @staticmethod
    def get(
        conn: Connection,
        **kwargs: dict[str, any]
    ) -> 'User':
        """SELECT * FROM users WHERE id=1 AND user='as'"""

        condition: list[str] = []
        for i in kwargs:
            if isinstance(kwargs[i], str):
                condition.append(
                    f"{i}='{kwargs[i]}'"
                )
            else:
                condition.append(
                    f'{i}={kwargs[i]}'
                )

        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT * FROM users
                WHERE {' AND '.join(condition)}
                LIMIT 1
                """
            )
            return cur.fetchone()

    @staticmethod
    def filter(
        conn: Connection, 
        **kwargs: dict[str, any]
    ) -> 'User':

        condition: list[str] = []
        for i in kwargs:
            if isinstance(kwargs[i], str):
                condition.append(
                    f"{i}='{kwargs[i]}'"
                )
            else:
                condition.append(
                    f'{i}={kwargs[i]}'
                )

        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT * FROM users
                WHERE {' AND '.join(condition)}
                """
            )
            return cur.fetchall()

    
    @staticmethod
    def get_all(conn: Connection) -> 'User':

        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT * FROM users
                """
            )
            return cur.fetchall()