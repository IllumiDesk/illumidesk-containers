ARG BASE_IMAGE=python:3.8
FROM "${BASE_IMAGE}"

RUN apt-get update \
 && apt-get install unzip -y \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

# install packages with pip. makes sure pip is up to date.
COPY requirements.txt /tmp/
RUN python -m pip install --upgrade pip \
 && pip install -r /tmp/requirements.txt

# illumidesk package release
ARG ILLUMIDESK_VERSION=3.0.0

# Application directory
ENV APP_DIR=/illumidesk

# app folder
RUN mkdir -p "${APP_DIR}"

# fetch and unpack illumidesk package
RUN wget "https://github.com/IllumiDesk/illumidesk/archive/v${ILLUMIDESK_VERSION}.zip" \
 && unzip "/tmp/v${ILLUMIDESK_VERSION}.zip" \
 && python3 -m pip install "/tmp/illumidesk-${ILLUMIDESK_VERSION}/src/graderservice/."
RUN cp -r "/tmp/illumidesk-${ILLUMIDESK_VERSION}/src/graderservice/graderservice/." "${APP_DIR}/."

WORKDIR "${APP_DIR}"

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "graderservice.wsgi:app"]

HEALTHCHECK CMD curl --fail http://localhost:8000/healthcheck || exit 1
