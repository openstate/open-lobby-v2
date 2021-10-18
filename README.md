# OpenDraaideur

Open Draaideur maakt de loopbanen van Tweede Kamerleden inzichtelijk


## Get started

1. `# clone the repo and chdir to there`
2. `cd backend && cp config.py.example config.py && cp config.yaml.example config.yaml`
3. `# Edit config.py and config.yaml accordingly to what you want`
2. `cd ../docker`
3. `docker-compose  up -d`
4. `docker exec openlobby_backend_1 ./manage.py elasticsearch put_templates`
5. `docker exec openlobby_backend_1 alembic upgrade head`

In development mode you can run `./bin/dev.sh` from the base directory, which will launch
the development environment.

To access the local development environment, add the following in `/etc/hosts`:

```
127.0.0.1	api.opendraaideur.nl users.opendraaideur.nl www.opendraaideur.nl app.opendraaideur.nl
```

Then you can go to `http://app.opendraaideur.nl` preferably in a private window, because of HSTS parameters on the live setup.

# deployment

Open Draaideur uses Fabric for deployment. Run `fab deploy`.

# migrations

Open Draaideur uses [alembic](https://alembic.sqlalchemy.org/en/latest/index.html) for migrations

## migrate all up to the latest

`docker exec openlobby_backend_1 alembic upgrade head`

## rollback

`docker exec openlobby_backend_1 alembic downgrade -1`

## create a migration

`docker exec openlobby_backend_1 alembic revision -m "create account table"`

# importing data

# contact

Send an email to breyten@openstate.eu
