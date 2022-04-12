FROM python:3.10.4-slim as base

ARG HOMEDIR=/news

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
    pipenv install --deploy --system --ignore-pipfile --dev

WORKDIR ${HOMEDIR}

COPY . ${HOMEDIR}

EXPOSE 5001

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]