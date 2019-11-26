import os
from app import creat_app, db
# from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = creat_app(os.getenv('FLASK_CONFIG') or 'default')
manage = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manage.add_command("shell", Shell(make_context=make_shell_context()))
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()