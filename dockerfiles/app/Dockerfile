FROM python:3.11.3-alpine3.18

LABEL maintainer="Asadov Ahmed <zoxon470@gmail.com>"

ARG ENVIRONMENT
ENV TZ=UTC
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.5.0


ENV PATH="$PATH:$POETRY_HOME/bin"

RUN apk add make

RUN pip install poetry==$POETRY_VERSION

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN if [ "$ENVIRONMENT" == "dev" ] ; then \
      poetry install --without test,prod --no-root ; \
    else \
      poetry install --with $ENVIRONMENT --no-root ; \
    fi

COPY . .

ENTRYPOINT ["sh", "./dockerfiles/app/entrypoint.sh"]
