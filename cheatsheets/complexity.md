# ⏱️ Big-O Complexity Cheat Sheet

In MAANG interviews, you must know the Time and Space complexities of common data structures and algorithms by heart. Use this cheat sheet as a quick reference.

## 🧱 Data Structures

| Data Structure | Access (Avg) | Search (Avg) | Insert (Avg) | Delete (Avg) | Access (Worst) | Search (Worst) | Insert (Worst) | Delete (Worst) | Space (Worst) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Array** | $O(1)$ | $O(N)$ | $O(N)$ | $O(N)$ | $O(1)$ | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ |
| **Stack** | $O(N)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(N)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(N)$ |
| **Queue** | $O(N)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(N)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(N)$ |
| **Singly-Linked List** | $O(N)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(N)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(N)$ |
| **Doubly-Linked List** | $O(N)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(N)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(N)$ |
| **Hash Table** | N/A | $O(1)$ | $O(1)$ | $O(1)$ | N/A | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ |
| **Binary Search Tree** | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ |
| **AVL Tree / Red-Black Tree**| $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(N)$ |

---

## 🔢 Sorting Algorithms

| Algorithm | Time (Best) | Time (Average) | Time (Worst) | Space (Worst) | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Quicksort** | $O(N \log N)$ | $O(N \log N)$ | $O(N^2)$ | $O(\log N)$ | Generally fastest in practice. Unstable. |
| **Mergesort** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ | Stable. Used heavily in linked list sorting. |
| **Heapsort** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(1)$ | In-place. Unstable. |
| **Radix Sort** | $O(NK)$ | $O(NK)$ | $O(NK)$ | $O(N+K)$ | $K$ is the number of digits. Non-comparative. |
| **Insertion Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Best for extremely small or nearly sorted arrays. |

---

## 🌲 Tree / Graph Algorithms

| Algorithm | Time Complexity | Space Complexity |
| :--- | :---: | :---: |
| **Depth First Search (DFS)** | $O(V + E)$ | $O(V)$ |
| **Breadth First Search (BFS)** | $O(V + E)$ | $O(V)$ |
| **Dijkstra's (Shortest Path)** | $O((V + E) \log V)$ | $O(V)$ |
| **Topological Sort** | $O(V + E)$ | $O(V)$ |
| **Union Find (Disjoint Set)** | $O(\alpha(V))$ | $O(V)$ |

*(Note: $V$ = Vertices/Nodes, $E$ = Edges. $\alpha$ is the Inverse Ackermann function, which is nearly $O(1)$)*
