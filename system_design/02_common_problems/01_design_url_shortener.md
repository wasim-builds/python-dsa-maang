# Design a URL Shortener (e.g., TinyURL)

## 1. Requirements
- **Functional:** 
  - Give a long URL, get a short URL.
  - Clicking the short URL redirects to the long URL.
- **Non-Functional:**
  - Highly available (redirects must never fail).
  - Low latency (redirects must be fast).
  - URL cannot be guessable.

## 2. Estimation
- Write heavy or read heavy? Read heavy (10:1 ratio).
- Assume 100 million new URLs generated per month.
- 100M * 10 = 1 Billion redirects per month.
- QPS (Queries Per Second): 1B / (30 days * 24 hours * 3600 seconds) = ~400 reads/sec, ~40 writes/sec.

## 3. High-Level Design
1. **Client** requests to shorten a URL.
2. Request hits a **Load Balancer**.
3. **Web Servers** receive request, talk to **Key Generation Service**.
4. Save the mapping (ShortURL -> LongURL) in the **Database**.
5. When a user visits ShortURL, check **Cache** first. If miss, check **Database**.

## 4. Deep Dive
- **Encoding:** Use Base62 (a-z, A-Z, 0-9). 62^7 characters gives ~3.5 trillion URLs.
- **Key Generation Service (KGS):** Pre-generate keys and store them in a database so web servers can quickly grab a key without worrying about collisions.
- **Database:** Since we don't need complex relations and need massive read scalability, a NoSQL database (like Cassandra or DynamoDB) is perfect.
- **Caching:** Use Redis to store the most popular shortened URLs (80/20 rule: 80% of traffic goes to 20% of URLs).
