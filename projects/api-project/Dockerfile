ARG BUILDER_IMAGE

# Builder Image
FROM ${BUILDER_IMAGE} as builder

WORKDIR /app

COPY ./bases/api ./bases/api
COPY ./components/otel ./components/otel
COPY ./projects/api-project ./projects/api-project

WORKDIR /app/projects/api-project

RUN poetry build-project

# Production Image
FROM python:3.12-slim as production

ENV wheel_name=api_project-0.1.0-py3-none-any.whl

RUN python -m pip install --upgrade pip

WORKDIR /app

COPY --from=builder /app/projects/api-project/dist/$wheel_name /app/$wheel_name
RUN pip install --no-cache-dir --upgrade /app/$wheel_name

CMD ["uvicorn", "api.core:app", "--host", "0.0.0.0", "--port", "8000"]