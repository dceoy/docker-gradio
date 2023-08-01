docker-gradio
================

Dockerfile for Gradio

[![CI to Docker Hub](https://github.com/dceoy/docker-gradio/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/dceoy/docker-gradio/actions/workflows/docker-publish.yml)

Docker image
------------

Pull the image from [Docker Hub](https://hub.docker.com/r/dceoy/gradio/).

```sh
$ docker image pull dceoy/gradio
```

Usage
-----

Run Gradio

```sh
$ docker container run --rm -p 7860:7860 -v ${PWD}:/wd -w /wd \
    dceoy/gradio run.py
```

Run Gradio with docker-compose

```sh
$ docker-compose -f /path/to/docker-gradio/docker-compose.yml up
```
