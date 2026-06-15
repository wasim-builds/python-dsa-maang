# Design a Chat Application (e.g., WhatsApp / Messenger)

## 1. Requirements
- **Functional:**
  - 1-on-1 chatting with low latency.
  - Online/Offline status indicator.
- **Non-Functional:**
  - Real-time experience.
  - Highly available, high consistency for messages.

## 2. High-Level Design
- **WebSockets:** Standard HTTP is stateless and unidirectional (client must pull). We need bidirectional communication. WebSockets keep a persistent connection open between the client and server.
- **Chat Servers:** Maintain the WebSocket connections with active users.
- **Presence Servers:** Dedicated servers just for tracking Online/Offline status.

## 3. Architecture Flow
1. User A sends a message to User B via their persistent WebSocket to Chat Server 1.
2. Chat Server 1 receives the message and assigns an ID.
3. Chat Server 1 checks if User B is online.
   - If User B is connected to Chat Server 2: Message is forwarded to Chat Server 2 (via a Message Queue or Pub/Sub), which pushes it to User B.
   - If User B is offline: Message is sent to Push Notification servers (APNS/FCM) and saved to the DB.

## 4. Deep Dive
- **Database:** Key-Value store (like HBase or Cassandra) is ideal for chat history because access patterns are heavily skewed toward recent messages, and we need high write throughput.
- **Online Presence:** Do not send an update every time someone disconnects/reconnects rapidly. Use a heartbeat mechanism. Client sends a heartbeat every 5 seconds; if the server misses 3 heartbeats, mark offline.
