# `uv` setup in Docker

## Build Image

```bash
docker build --file Dockerfile.original --build-arg PIP_EXTRA_INDEX_URL=$PIP_EXTRA_INDEX_URL --tag project:original .
docker build --file Dockerfile.local --build-arg PIP_EXTRA_INDEX_URL=$PIP_EXTRA_INDEX_URL --tag project:local .
```

## Run container

```bash
docker run -it --rm project:local bash
```
