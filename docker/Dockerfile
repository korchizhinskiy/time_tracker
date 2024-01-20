FROM python:3.12.1-bullseye

# Install packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    musl-dev \
    bash \
    zlib1g-dev \
    libjpeg-dev \
    curl \
    gettext \
    netcat

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.6.1 POETRY_HOME=/root/poetry python3 -
ENV PATH="${PATH}:/root/poetry/bin"

# Python environments.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /opt

# Install python packages
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Workdir
COPY . /opt

# Set executable permissions for shell files
RUN chmod +x script/*.sh 
