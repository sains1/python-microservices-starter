# python microservices boilerplate

## Dependencies

- [poetry](https://python-poetry.org/docs/)
- [python-polylith](https://davidvujic.github.io/python-polylith-docs/)

## Getting started

1. run `poetry install` from root of repo

2. run the apps

```bash
make api
```

## Docker setup

- The `builder` image in `docker-compose.yaml` defines an image with all dependencies installed (incl. poetry and polylith) which can then be used to build individal services

- All other services then follow the same structure (e.g. see [Api Dockerfile](./projects/api-project/Dockerfile))

1. inherit the builder image
2. use poetry to build the service
3. copy only the resulting .whl file to the final production image layer

To build all images:

```bash
docker compose build --no-cache
```
