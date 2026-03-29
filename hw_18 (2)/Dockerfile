FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /srv/jupyterhub

RUN apt-get update \
    && apt-get install -y --no-install-recommends nodejs npm \
    && npm install -g configurable-http-proxy \
    && pip install --no-cache-dir jupyterhub jupyterlab notebook \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
