## Project setup

```bash
$ npm install
```

## Compile and run the project

```bash
# development
$ npm run start

# watch mode
$ npm run start:dev

# production mode
$ npm run start:prod
```

## Run tests

```bash
# unit tests
$ npm run test

# e2e tests
$ npm run test:e2e

# test coverage
$ npm run test:cov
```

## development process

- Install prisma $npm install prisma -D
- npx prisma init
- Let's run the migration using "$npx prisma migrate dev --name=init"
- After any change in model we need to change the db with "$npx prisma generate"
- Create a resource $nest g res employees, delete the dto and entities
- Controller level valiation with custom dto
- Service level validation with prisma level dto

# Next Scope:
- CORS, Rate limit, logs, exception filtering, DB table relation, caching, file upload,  streaming, session, JWT,
- serializer, task scheduling, queues, ,Fundamentails, microservice, websocket, mailing
