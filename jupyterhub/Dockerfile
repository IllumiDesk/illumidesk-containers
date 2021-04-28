ARG BASE_IMAGE=jupyterhub/k8s-hub:0.11.1
FROM "${BASE_IMAGE}"

USER root
RUN apt-get update \
 && apt-get install -y \
    unzip=6.0-25ubuntu1 \
    wget=1.20.3-1ubuntu1 --no-install-recommends \
 && rm -rf /var/lib/apt/lists/*

USER "${NB_UID}"

ENV PATH="/home/${NB_USER}/.local/bin:${PATH}"

ARG ILLUMIDESK_VERSION=3.0.0

# ensure pip is up to date
RUN python3 -m pip install --no-cache-dir --upgrade pip

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /tmp
RUN wget --progress=dot:giga "https://github.com/IllumiDesk/illumidesk/archive/v${ILLUMIDESK_VERSION}.zip" \
 && unzip "/tmp/v${ILLUMIDESK_VERSION}.zip"
WORKDIR "/tmp/illumidesk-${ILLUMIDESK_VERSION}/src/illumidesk/"
RUN python3 -m pip install --no-cache-dir .

WORKDIR /srv/jupyterhub/

COPY illumidesk-80.png /srv/jupyterhub/illumidesk-80.png
COPY jupyterhub_config.py /srv/jupyterhub/
COPY wait-for-postgres.sh /srv/jupyterhub/

CMD ["./wait-for-postgres.sh", "jupyterhub", "--config", "/srv/jupyterhub/jupyterhub_config.py"]

USER root

COPY illumidesk-80.png /usr/local/share/jupyterhub/static/images/illumidesk-80.png

USER "${NB_UID}"
