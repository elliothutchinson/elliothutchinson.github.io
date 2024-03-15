# docker build --target base -t portfolio/web -f docker/Dockerfile .
# docker run -d --name portfolio-web -p 9000:9000 --env-file docker/web.env portfolio/web
# docker start portfolio-web
# docker stop portfolio-web
# docker rm portfolio-web
# docker exec -it portfolio-web bash

FROM python:3.12-bookworm as base

RUN apt update
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && apt-get install -y nodejs

WORKDIR /app

COPY ./web/requirements.txt ./web/requirements.txt
RUN pip install -r web/requirements.txt

COPY ./web ./web

WORKDIR /app/web

EXPOSE 9000
EXPOSE 9001
CMD ["sh", "run-dev.sh"]
