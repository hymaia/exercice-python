FROM fnndsc/python-poetry:1.1.13 as builder

WORKDIR /app

# TODO compléter le Dockerfile pour que la suite fonctionne

FROM python:slim

WORKDIR /app
COPY --from=builder /app/dist/*.whl /app/

RUN pip install *.whl

ENTRYPOINT ["wordcount"]
