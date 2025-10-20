# 🧩 AlgoBench

*A lightweight web platform for benchmarking and visualizing algorithm performance.*

---

## 🚀 Overview

**AlgoBench** is a web-based application that allows users to upload algorithm scripts, run automated benchmarks, and visualize runtime results.
It helps users compare algorithm efficiency (e.g., sorting, searching, graph algorithms) through clear visual charts and data summaries.

The main goal is to bridge **theory and practice** — turning algorithmic knowledge into measurable, visual insights.

---

## 🧱 Tech Stack

| Layer         | Technology                         | Purpose                                          |
| ------------- | ---------------------------------- | ------------------------------------------------ |
| Frontend      | HTML / CSS / JavaScript (or React) | User interface and result visualization          |
| Backend       | Node.js + Express                  | Handles uploads, runs benchmarks, stores results |
| Data          | JSON / CSV                         | Stores performance data                          |
| Visualization | Chart.js or D3.js                  | Renders performance charts                       |

---

## ⚙️ Features (v1)

* 🔹 Upload algorithm files (`.js` or `.py`)
* 🔹 Automatically run performance benchmarks on sample datasets
* 🔹 Display runtime comparison charts
* 🔹 Compare multiple algorithms side-by-side

Future versions will include multi-language support, Docker sandboxing, and automated performance reports.

---

## 📂 Project Structure

```
AlgoBench/
│
├── backend/
│   ├── server.js            # Express main server
│   ├── benchmark.js         # Benchmark runner and performance logic
│
├── frontend/
│   ├── index.html           # Main interface
│   ├── style.css            # Styling
│   ├── script.js            # Frontend logic
│
├── uploads/                 # Uploaded algorithm scripts
├── data/                    # Benchmark results
└── README.md
```

---

## 🧠 Example Use Case

1. Upload `quicksort.js` and `bubblesort.js`
2. Click **Run Benchmark**
3. View the runtime chart (Input size vs Execution time)
4. Compare results:

| Algorithm   | Runtime (ms) |
| ----------- | ------------ |
| Quick Sort  | 48.8         |
| Bubble Sort | 35,678       |

---

## 🪄 Future Plans

* ✅ **v1:** Basic upload + runtime visualization
* 🔜 **v2:** Multi-language support (Python, C++)
* 🔜 **v3:** Docker-based isolated execution
* 🔜 **v4:** Automated report generation & leaderboard

---

## 👩‍💻 Author

**Ivy Swenson**
Computer Science Student @ University of Alaska Fairbanks
Interested in algorithms, system design, and AI-driven data visualization.

---


