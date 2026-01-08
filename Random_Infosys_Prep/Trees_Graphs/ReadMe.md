# 🧠 Infosys Trees & Graphs — Personal Checklist

## 🌳 TREE TYPES (ONLY WHAT MATTERS)

### ✅ Rooted Tree

* [ ] One root node
* [ ] Parent → children structure
* [ ] Often given as `parent[]` array
* [ ] Used for:

  * Subtree sum
  * DFS aggregation
  * “In subtree of node u”
* ⚠️ **~90% of Infosys tree problems**

---

### ✅ Binary Tree

* [ ] Each node has ≤ 2 children
* [ ] Used for:

  * Traversals
  * Height / depth
  * Balance checks
* Infosys keeps this **basic**

---

### ✅ Binary Search Tree (BST)

* [ ] `left < root < right`
* [ ] Inorder traversal → sorted
* [ ] Insert / search logic
* Usually **easy-level**

---

### ✅ N-ary Tree

* [ ] Node can have many children
* [ ] Same as rooted tree + adjacency list
* Infosys won’t call it “N-ary”, but it is

---

### ✅ Tree with Values / Weights

* [ ] Values on nodes or edges
* [ ] Used for:

  * Sum / count
  * Conditional DFS
* Logic > structure here

---

### ❌ Trees You Can Ignore (Infosys)

* [ ] AVL Tree
* [ ] Red-Black Tree
* [ ] Segment Tree
* [ ] Fenwick Tree (rare)
* [ ] Trie (very rare)

---

## 🕸️ GRAPH TYPES (FILTERED)

### ✅ Undirected Graph

* [ ] Edges go both ways
* [ ] Used for:

  * Connected components
  * Grouping nodes
* Very common

---

### ✅ Directed Graph

* [ ] Edges have direction
* [ ] Used for:

  * Dependencies
  * Ordering
  * Reachability
* Infosys keeps it simple

---

### ✅ Disconnected Graph

* [ ] Multiple components
* [ ] DFS/BFS from every unvisited node
* Mandatory skill

---

### ✅ Implicit Graph (**IMPORTANT**)

* [ ] Nodes are states, not stored explicitly
* [ ] Edges defined by rules
* Examples:

  * Circular jumps
  * Number transformations
  * `i → i ± A[i]`

---

### ✅ Grid Graph

* [ ] 2D matrix
* [ ] Each cell = node
* [ ] Used for:

  * BFS spread
  * Shortest time
  * Infection problems

---

### ❌ Graphs You Can Ignore (Infosys)

* [ ] Weighted shortest paths (Dijkstra)
* [ ] Minimum Spanning Tree
* [ ] Flow networks
* [ ] SCC algorithms (Kosaraju, Tarjan)

---

## ⚡ 5-Second Identification Rules

* **Input has `parent[]`** → 🌳 Tree
* **Input has edges list** → 🕸️ Graph
* **Input is a matrix** → 🧱 Grid Graph
* **Input has movement rules** → 🧠 Implicit Graph

---

## 📌 Personal Progress Tracker

* [ ] Tree problem 1 solved
* [ ] Tree problem 2 solved
* [ ] Graph problem 1 solved
* [ ] Graph problem 2 solved
* [ ] Full mock coding round completed
