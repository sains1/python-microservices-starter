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
