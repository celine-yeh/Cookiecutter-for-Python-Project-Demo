FROM python:3.7.4-stretch AS base
WORKDIR /workspace
RUN pip install pipenv==2018.11.26

FROM base as runtime
COPY Pipfile* ./
RUN pipenv install --system --deploy \
    && rm Pipfile*

FROM runtime AS dev
COPY Pipfile* ./
RUN pipenv install --system --deploy --dev \
    && rm Pipfile*
RUN apt-get update && apt-get install -y --no-install-recommends mysql-client

FROM runtime AS prod
COPY . ./
RUN ln -s /workspace/cookiecutter-for-python-project-demo-cli /usr/local/bin/cookiecutter-for-python-project-demo-cli
