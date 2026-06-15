# Caching and Redis

## What is Caching?
Caching is the process of storing copies of frequently accessed data in a temporary, highly accessible storage layer (usually RAM) to reduce database load and latency.

## Cache Eviction Policies
When the cache is full, how do we decide what to remove?
1. **LRU (Least Recently Used):** Discard the least recently used items first. (Most common)
2. **LFU (Least Frequently Used):** Discard the items used least often.
3. **FIFO (First In First Out):** Discard the oldest items first.

## Redis
Redis is an open-source, in-memory data structure store used as a database, cache, and message broker.
- Extremely fast (reads/writes in sub-milliseconds).
- Supports data structures like Strings, Hashes, Lists, Sets, and Sorted Sets.

## Strategies
- **Cache Aside:** Application asks cache. If miss, asks DB, then writes to cache.
- **Write Through:** Application writes to cache, cache immediately writes to DB.
- **Write Back:** Application writes to cache, cache writes to DB asynchronously.
