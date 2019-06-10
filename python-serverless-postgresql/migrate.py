import app.common.security
import json
import alembic.config

def up(event, context):
    alembicArgs = [
        '--raiseerr',
        'upgrade',
        'head',
    ]
    alembic.config.main(argv=alembicArgs)
