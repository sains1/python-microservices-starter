FROM python:3.12

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN pip install poetry>=1.8.*
RUN poetry config virtualenvs.in-project true
RUN poetry self add poetry-multiproject-plugin

ADD pyproject.toml poetry.lock poetry.toml ./

# turn off package-mode so we can install dependencies without copying all of our packages
RUN sed -i 's/package-mode = true/package-mode = false/g' 'pyproject.toml'

RUN poetry install --no-ansi