FROM oven/bun:1.1.34

WORKDIR /app/frontend

COPY bun.lockb .
COPY package.json .

RUN bun install

COPY . .

EXPOSE 5173

CMD [ "bun", "run", "dev", "--host" ]