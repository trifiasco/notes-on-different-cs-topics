- [monolithic vs micro-services - medium post 1](https://articles.microservices.com/monolithic-vs-microservices-architecture-5c4848858f59)
- [monolithic vs micro-services - medium post 2 ](https://medium.com/@raycad.seedotech/monolithic-vs-microservice-architecture-e74bd951fc14)

### monolithic architecture

```
A monolithic application has single code base with multiple modules. Modules are divided as either for business features or technical features. It has single build system which build entire application. It also has single executable or deployable binary.
```

#### Challenges
- large codebase
- scaling is problematic
- overloaded IDE
- extremely difficult to change technology or lang or framework
- deployment challenges
- big database
- fault tolerance

### Micro-service architecture

```
A microservices architecture consists of a collection of small, autonomous services. Each service is self-contained and should implement a single business capability.
```

```
The idea is to split your application into a set of smaller, interconnected services instead of building a single monolithic application. Each microservice is a small application.

The Microservice architecture pattern significantly impacts the relationship between the application and the database. Instead of sharing a single database schema with other services, each service has its own database schema

The apps don’t, however, have direct access to the back-end services. Instead, communication is mediated by an intermediary known as an API Gateway. The API Gateway is responsible for tasks such as load balancing, caching, access control, API metering, and monitoring.
```

#### Characteristics
- Services are small, independed and loosely coupled.
- encapsulate a customer or business scenario
- separate codebase, easily manageable.
- independetly deployable.
- each service can have different tech or stack
- communicate with each other using APIs.
- each can have it's own database.
- fault isolation
- granular scaling

#### problems
- complexity - each one is simple, but together it's a complex system
- dev and testing
- data integrity
- network congestion and latency