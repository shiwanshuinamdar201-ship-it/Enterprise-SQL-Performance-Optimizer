# ⚡ Enterprise SQL Performance Optimizer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

**A database performance tuning framework that cuts complex query latency by 95%**

</div>

---

## 📌 The Problem

Large-scale relational databases frequently suffer from slow query execution due to full table scans, missing indexes, and unoptimized execution plans. These bottlenecks cost real money in production — slow dashboards, delayed reports, and degraded user experience.

This project replicates that production environment and systematically solves it.

---

## 🎯 Results

| Metric | Before Optimization | After Optimization |
|---|---|---|
| Complex aggregation query | ~4,200 ms | **~210 ms** |
| Full table scan queries | Frequent | Eliminated |
| Index coverage | None | B-Tree composite indexes |
| Latency reduction | — | **95%** |

> Tested on a simulated enterprise database with **100,000+ records** replicating real production bottlenecks.

---

## 🏗️ How It Works

```
Raw Database (100K+ rows)
        │
        ▼
EXPLAIN QUERY PLAN diagnosis
        │
        ├── Detected: Full table scans
        ├── Detected: Missing indexes on JOIN columns
        └── Detected: Unoptimized aggregation paths
        │
        ▼
B-Tree Composite Index Strategy
        │
        ▼
Re-run queries → measure latency delta
        │
        ▼
Streamlit Dashboard (live metrics visualization)
```

---

## 🔍 Core Techniques

### 1. Execution Plan Diagnosis
```sql
EXPLAIN QUERY PLAN
SELECT department, AVG(salary), COUNT(*) 
FROM employees 
JOIN departments ON employees.dept_id = departments.id
WHERE hire_date BETWEEN '2018-01-01' AND '2023-12-31'
GROUP BY department;
-- Result: SCAN TABLE employees (~100K rows) ← the problem
```

### 2. B-Tree Composite Index Implementation
```sql
-- Single-column indexes weren't enough
CREATE INDEX idx_emp_dept_date 
ON employees(dept_id, hire_date);  -- composite: covers JOIN + WHERE

CREATE INDEX idx_dept_name 
ON departments(id, department_name);  -- covers GROUP BY
```

### 3. Post-Optimization Result
```sql
EXPLAIN QUERY PLAN ...
-- Result: SEARCH TABLE employees USING INDEX idx_emp_dept_date ✅
-- Rows examined: ~340 instead of ~100,000
```

---

## 📊 Dashboard

The Streamlit dashboard visualizes:
- Query execution time (before vs after)
- Index usage statistics
- Table scan frequency
- Latency distribution across query types

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/shiwanshuinamdar201-ship-it/Enterprise-SQL-Performance-Optimizer.git
cd Enterprise-SQL-Performance-Optimizer

# Install dependencies
pip install -r requirements.txt

# Generate the 100K+ record database
python generate_db.py

# Run the analysis notebook
jupyter notebook analysis.ipynb

# Launch the dashboard
streamlit run dashboard.py
```

### Requirements
```
sqlite3 (built-in)
pandas>=1.5.0
streamlit>=1.20.0
matplotlib>=3.6.0
jupyter>=1.0.0
```

---

## 📁 Project Structure

```
Enterprise-SQL-Performance-Optimizer/
├── generate_db.py          # Synthetic enterprise DB generator (100K+ rows)
├── analysis.ipynb          # Full diagnosis + optimization notebook
├── dashboard.py            # Streamlit performance dashboard
├── queries/
│   ├── before/             # Unoptimized SQL queries
│   └── after/              # Optimized queries with indexes
├── results/
│   └── benchmarks.csv      # Measured latency comparisons
└── requirements.txt
```

---

## 💡 Key Learnings

- `EXPLAIN QUERY PLAN` is the single most powerful tool for SQLite diagnosis — it reveals whether indexes are being used
- **Composite indexes** outperform single-column indexes when queries filter on multiple columns simultaneously
- Index order matters: place the equality-filter column first, range-filter column second
- Over-indexing is also a problem — write benchmarks were not significantly impacted here, but worth monitoring

---

## 🧠 Skills Demonstrated

`SQL Query Optimization` `Database Indexing` `Performance Benchmarking` `SQLite` `Pandas` `Data Visualization` `Streamlit` `Jupyter`

---

<div align="center">
Made by <a href="https://github.com/shiwanshuinamdar201-ship-it">Shiwanshu Inamdar</a> · B.Tech CSE Data Science · D.Y. Patil International University
</div>
