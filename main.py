from flask import Flask, render_template

from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    db_session.global_init("db/mars_explorer.sqlite")
    session = db_session.create_session()
    raboty = session.query(Jobs).all()
    ekipash = {}
    for job in session.query(Jobs).all():
        for user in session.query(User).filter(User.id == job.team_leader):
            leader = f'{user.name} {user.surname}'
            ekipash[job.team_leader] = leader
    return render_template('index.html', jobs=raboty, names=ekipash)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
