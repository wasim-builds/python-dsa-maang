# Proxies and Message Queues

## Proxies
A proxy server sits between a client application and a real server.

1. **Forward Proxy:** Hides the identity of the client. (Used by internal networks to access the internet).
2. **Reverse Proxy:** Hides the identity of the server. (Used by web servers to handle incoming traffic).
   - Nginx and HAProxy are popular reverse proxies.
   - Benefits: Load balancing, SSL termination, caching static content, security.

## Message Queues
A message queue is a form of asynchronous service-to-service communication used in serverless and microservices architectures.
- e.g., **Kafka**, **RabbitMQ**, **AWS SQS**.

### Why use them?
- **Decoupling:** Services don't need to know about each other.
- **Scalability:** If the consumer is overwhelmed, messages just sit in the queue until it catches up.
- **Buffering:** Handles sudden spikes in traffic (e.g., processing video uploads or sending massive email campaigns).
