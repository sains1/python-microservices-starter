# python microservices boilerplate

## Dependencies

- [poetry](https://python-poetry.org/docs/)
- [poetry-multiproject-plugin](https://github.com/DavidVujic/poetry-multiproject-plugin)

## Getting started

1. run `poetry install` from root of repo

2. run the apps

```bash
make api
```

3. run observability stack (optional)

`docker-compose.otel.yaml` provides services for logs, traces & metrics using opentelemetry. For higher envs these can be switched out for any otel compatible backend.

```bash
docker-compose -f docker-compose.otel.yaml up -d
```

This starts the following services:

- [jaeger (tracing)](http://localhost:16686)
- [prometheus (metrics)](http://localhost:9090)
- [seq (logs)](http://localhost:5342/)
- [otel-collector (bg service for collection)](localhost:4317)

## Docker setup

The `builder` image in `docker-compose.yaml` defines an image with all dependencies installed (incl. poetry etc) which can then be used to build individual services

All other services then follow the same structure (for example see [Api Dockerfile](./projects/api-project/Dockerfile)):

1. inherit the builder image
2. use poetry to build the service
3. copy only the resulting .whl file to the final production image layer

To build all images:

```bash
docker compose build --no-cache
```

## Other

### Helpful commands

- `poetry add -G dev $pkg_name` add a dev dependency
- `mypy .` run type checker
- `ruff format` run ruff as formatter
- `ruff check` run ruff as linter

### Handy vscode extensions

- [ruff-vscode](https://github.com/astral-sh/ruff-vscode)
- [vscode-mypy](https://github.com/microsoft/vscode-mypy/)
