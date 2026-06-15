# Load Balancing and Scaling

## Scaling
When a system reaches capacity, you have two choices:

1. **Vertical Scaling (Scale Up)**: Adding more power (CPU, RAM) to your existing server.
   - *Pros:* Simple, no code changes.
   - *Cons:* Hard limit (you can only buy so much RAM), no failover (single point of failure).
2. **Horizontal Scaling (Scale Out)**: Adding more servers to the resource pool.
   - *Pros:* Infinite scaling, high availability.
   - *Cons:* Complex to implement, requires state management and load balancing.

## Load Balancing
A Load Balancer distributes incoming network traffic across multiple servers to ensure no single server bears too much demand.

### Algorithms
- **Round Robin:** Requests are distributed sequentially.
- **Least Connections:** Sends requests to the server with the fewest active connections.
- **IP Hash:** The client's IP address is used to calculate which server receives the request (useful for sticky sessions).

### Types of Load Balancers
- **Layer 4 (Transport):** Routes traffic based on IP address and TCP port. (Fast, simple)
- **Layer 7 (Application):** Routes traffic based on content of the message (HTTP header, URL path). (Slower, but smarter)
