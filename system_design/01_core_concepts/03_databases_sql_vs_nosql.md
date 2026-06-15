# Databases: SQL vs NoSQL

Choosing the right database is often the most critical decision in a System Design interview.

## SQL (Relational Databases)
e.g., MySQL, PostgreSQL
- **Structure:** Tables with strict schemas (rows and columns).
- **Properties:** ACID compliance (Atomicity, Consistency, Isolation, Durability). Guarantees data integrity.
- **Scaling:** Traditionally scale vertically, though sharding allows horizontal scaling (complex).
- **Best For:** Financial systems, billing, relationships (JOINs are necessary).

## NoSQL (Non-Relational Databases)
e.g., MongoDB, Cassandra, DynamoDB
- **Structure:** Key-Value, Document, Wide-Column, or Graph. Flexible schemas.
- **Properties:** BASE compliance (Basically Available, Soft state, Eventual consistency). Prioritizes availability over immediate consistency.
- **Scaling:** Designed to scale horizontally natively.
- **Best For:** Massive data, rapid prototyping, unstructured data, highly distributed systems.

## Database Sharding
Sharding is the process of splitting a large database into smaller, faster, more easily managed parts called data shards.
- **Hash-based Sharding:** Using a hash function on a key (e.g., User ID) to determine the shard.
- **Range-based Sharding:** Dividing data by ranges (e.g., User IDs 1-1000 in Shard A, 1001-2000 in Shard B).
