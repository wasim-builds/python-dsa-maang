# Design a Rate Limiter

## 1. Requirements
- **Functional:** Limit the number of requests an entity (user, IP) can send to an API within a time window.
- **Non-Functional:** Highly available, low latency (shouldn't slow down the API), accurate.

## 2. Algorithms
1. **Token Bucket:** A bucket holds tokens. Every request costs 1 token. Tokens refill at a fixed rate. (Amazon/Stripe uses this).
2. **Leaky Bucket:** Requests are added to a queue. The queue is processed at a fixed rate.
3. **Fixed Window Counter:** Divides time into fixed windows (e.g., 1:00-1:01) and counts requests. Fails at edges (bursts at 1:00:59 and 1:01:01).
4. **Sliding Window Log:** Keeps a log of timestamps of every request. Very accurate, but memory intensive.
5. **Sliding Window Counter:** Hybrid of Fixed Window and Sliding Window Log.

## 3. High-Level Design
- Client makes a request to the API.
- Request hits the **Rate Limiter Middleware** (often running in Redis).
- Rate Limiter checks Redis for the current count.
  - If limit exceeded: Return HTTP 429 (Too Many Requests).
  - If within limit: Forward to the API servers.

## 4. Deep Dive
- **Where to store rules?** Disk, loaded into a cache (Redis) on startup.
- **Distributed Environments:** When using multiple Rate Limiter servers, we face race conditions. Use Redis Lua scripts or Sorted Sets to ensure atomic operations.
