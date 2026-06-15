# Design Twitter (News Feed)

## 1. Requirements
- **Functional:** 
  - Users can publish tweets.
  - Users can view their News Feed (tweets from people they follow).
- **Non-Functional:**
  - Fast rendering of news feed (< 500ms).
  - Highly available (publishing can fail, but reading should always work).

## 2. High-Level Design
### Feed Generation (Read)
- **Pull Model (Fanout on Load):** When a user requests their feed, fetch all friends, fetch their latest tweets, merge and sort.
  - *Pros:* Simple.
  - *Cons:* Very slow if the user follows 10,000 people.
- **Push Model (Fanout on Write):** When a user tweets, pre-compute the feed for all their followers and push it to their cache.
  - *Pros:* Reading the feed is instantly O(1) from the cache.
  - *Cons:* "Justin Bieber" problem. If someone with 100M followers tweets, it takes immense processing to push to 100M caches.

### Hybrid Model (The Solution)
- For normal users: Use Push Model (Fanout on Write).
- For celebrities (millions of followers): Use Pull Model (Fanout on Load). The celebrity's tweets are pulled and merged into the user's feed at read time.

## 3. Deep Dive
- **Caching:** Redis is heavily used for the News Feed cache.
- **Databases:** Relational DB for User Profiles (strict schema). Graph DB for Follower relationships.
- **Media:** Images/Videos stored in Object Storage (Amazon S3), served via CDN.
