FROM fnndsc/python-poetry:1.1.13 as builder

WORKDIR /app

COPY pyproject.toml pyproject.toml
COPY src src
RUN poetry install

COPY tests tests
RUN poetry run pytest

RUN poetry build

FROM python:slim

WORKDIR /app
COPY --from=builder /app/dist/*.whl /app/

RUN pip install *.whl

ENTRYPOINT ["wordcount"]
