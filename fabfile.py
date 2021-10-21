import os.path

from fabric import Connection, Config, task
from invoke import Exit
import getpass

# Name of the git repository
GIT_REPO = 'open-lobby-v2'

# Path of the directory
DIR = '/home/projects/%s' % (GIT_REPO)

# Container used to compile the assets
NODE_CONTAINER = 'openlobby_node_1'

# App container
APP_CONTAINER = 'openlobby_backend_1'

# Server name
SERVER = 'fluorine'


@task
def deploy(c):
    sudo_pass = getpass.getpass("Enter your sudo password on %s: " % SERVER)
    config = Config(overrides={'sudo': {'password': sudo_pass}})
    c = Connection(SERVER, config=config)

    # Pull from GitHub
    c.run(
        'cd %s && git pull git@github.com:openstate/%s.git' % (
            DIR,
            GIT_REPO
        )
    )

    # build & start new containers
    c.sudo("sh -c 'cd %s && docker-compose build'" % (os.path.join(DIR, 'docker'),))
    c.sudo("sh -c 'cd %s && docker-compose up -d'" % (os.path.join(DIR, 'docker'),))

    # Compile assets
    output = c.sudo(
        'docker inspect --format="{{.State.Status}}" %s' % (NODE_CONTAINER)
    )
    if output.stdout.strip() != 'running':
        raise Exit(
            '\n*** ERROR: The %s container, used to compile the assets, is '
            'not running. Please build/run/start the container.' % (
                NODE_CONTAINER
            )
        )
    c.sudo('docker exec %s yarn' % (NODE_CONTAINER))
    c.sudo('docker exec %s yarn build' % (NODE_CONTAINER))

    # put elasticsearch mapings
    c.sudo('docker exec %s python manage.py elasticsearch put_templates' % (APP_CONTAINER))
    # Reload app
    # c.run('cd %s && touch uwsgi-touch-reload' % (DIR))
