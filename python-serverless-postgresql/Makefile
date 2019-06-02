dbcontainer = pypgalembic
pg_user = postgres
pg_password = p0stgres
pg_database = appdb
pg_port = 3543

create update:
	sls deploy

delete:
	sls remove

migrate:
	PYTHONPATH=$(PWD) \
		alembic upgrade head

local:
		sls offline start --stage local

dburl:
	DATABASE_URL=postgres://$(pg_user):$(pg_password)@127.0.0.1:$(pg_port)/$(pg_database)

psql:
	PGHOST=127.0.0.1 \
	PGPORT=$(pg_port) \
	PGUSER=$(pg_user) \
	PGPASSWORD=$(pg_password) \
	PGDATABASE=$(pg_database) \
		psql

startdb:
	docker container run \
		--name $(dbcontainer) \
		--env POSTGRES_USER=$(pg_user) \
		--env POSTGRES_PASSWORD=$(pg_password) \
		--env POSTGRES_DB=$(pg_database) \
		--publish $(pg_port):5432 \
		--detach \
		--rm \
		--interactive \
		--tty \
		postgres:11

stopdb:
	docker container stop \
		$(dbcontainer)
