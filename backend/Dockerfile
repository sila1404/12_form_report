FROM ghcr.io/prefix-dev/pixi:0.34.0 AS build

WORKDIR /app

COPY . .

RUN pixi install

EXPOSE 8000

CMD [ "pixi", "run", "dev" ]