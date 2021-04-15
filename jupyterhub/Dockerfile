ARG BASE_IMAGE=jupyterhub/k8s-hub:0.11.1
FROM "${BASE_IMAGE}"

USER root
RUN apt-get update \
 && apt-get install -y \
    unzip \
    wget \
 && rm -rf /var/lib/apt/lists/*

USER "${NB_UID}"

ENV PATH="/home/${NB_USER}/.local/bin:${PATH}"

# illumidesk package release
ARG ILLUMIDESK_VERSION=3.0.0

# ensure pip is up to date
RUN python3 -m pip install --upgrade pip

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR /tmp
RUN wget "https://github.com/IllumiDesk/illumidesk/archive/v${ILLUMIDESK_VERSION}.zip" \
 && unzip "/tmp/v${ILLUMIDESK_VERSION}.zip"
WORKDIR "/tmp/illumidesk-${ILLUMIDESK_VERSION}/src/illumidesk/"
RUN python3 -m pip install .

WORKDIR /srv/jupyterhub/

COPY illumidesk-80.png /srv/jupyterhub/illumidesk-80.png
COPY jupyterhub_config.py /srv/jupyterhub/
COPY wait-for-postgres.sh /srv/jupyterhub/

CMD ["./wait-for-postgres.sh", "jupyterhub", "--config", "/srv/jupyterhub/jupyterhub_config.py"]
