FROM node:16.11-bullseye-slim

WORKDIR /app

COPY . ./
RUN yarn

EXPOSE 8080

ENV HOST=0.0.0.0
ENV PORT=8080

RUN yarn build

CMD [ "yarn", "start" ]