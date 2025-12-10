FROM node:22 AS node22

WORKDIR /app
RUN mkdir /app/frontend
WORKDIR /app/frontend
COPY ./frontend/package.json ./
RUN yarn
COPY ./frontend/*.* ./
COPY ./frontend/src ./src
RUN yarn build

FROM nginx:latest AS nginx

COPY --from=node22 /app/frontend/dist  /app/client

COPY ./docker/nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./docker/nginx/proxy_params /etc/nginx/proxy_params
COPY ./static /app/static

EXPOSE 80
# CMD ["sleep", "infinity"]
