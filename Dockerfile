FROM python:3.12

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN pip install poetry>=1.8.*
RUN poetry config virtualenvs.in-project true
RUN poetry self add poetry-multiproject-plugin
RUN poetry self add poetry-polylith-plugin

ADD pyproject.toml poetry.lock poetry.toml workspace.toml ./

RUN poetry install --no-ansi