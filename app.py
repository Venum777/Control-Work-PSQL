# Python
import datetime
from flask import(
    Flask,
    render_template
) 
# Local
from database.core import Connection
from database.models.users import User


my_connection: Connection = Connection(
    host='localhost',
    port=5432,
    user='postgres',
    password='admin',
    dbname='forum'
)
app = Flask(__name__)

@app.route('/registration')
def registration():
    return render_template(
        template_name_or_list='registration.html'
    )


if __name__ == '__main__':
    my_connection.create_tables()
    # User.create(
    #     conn=my_connection.conn,
    #     first_name='Stanislav',
    #     last_name='Potebenko',
    #     login='Venum',
    #     email='venums@gmail.com',
    #     password='qwerty',
    #     date_of_birth=datetime.datetime(
    #         year=2003,
    #         month=4,
    #         day=30
    #     ),
    #     author=True
    # )
    app.run (
        host='localhost',
        port=8080,
        debug=True
    )