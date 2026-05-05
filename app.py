import streamlit as st
import pandas as pd
import sqlite3
import time

st.set_page_config(page_title="SQL Performance Analyzer", layout="wide")
st.title("🗄️ Database Query Optimizer & Analyzer")
st.markdown("Analyze SQL execution plans and measure indexing performance in real-time.")

@st.cache_resource
def setup_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE employees (id INTEGER PRIMARY KEY, dept TEXT, salary REAL, joined_date TEXT)''')
    import random
    from datetime import datetime, timedelta
    depts = ['Engineering', 'Sales', 'HR', 'Marketing']
    data = [(i, random.choice(depts), random.uniform(50000, 150000), (datetime.now() - timedelta(days=random.randint(0, 1000))).strftime('%Y-%m-%d')) for i in range(50000)]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", data)
    conn.commit()
    return conn

conn = setup_db()

query = st.text_area("SQL Query", "SELECT dept, AVG(salary) FROM employees WHERE joined_date > '2022-01-01' GROUP BY dept", height=100)

col1, col2 = st.columns(2)

with col1:
    if st.button("Run Unoptimized (Full Table Scan)"):
        conn.execute("DROP INDEX IF EXISTS idx_dept_date")
        start = time.time()
        df = pd.read_sql_query(query, conn)
        duration = time.time() - start
        
        st.error(f"Execution Time: {duration:.4f} seconds")
        st.dataframe(df)
        
        st.subheader("Execution Plan")
        plan = pd.read_sql_query(f"EXPLAIN QUERY PLAN {query}", conn)
        st.table(plan)

with col2:
    if st.button("Run Optimized (With B-Tree Index)"):
        conn.execute("CREATE INDEX IF NOT EXISTS idx_dept_date ON employees(joined_date, dept)")
        start = time.time()
        df = pd.read_sql_query(query, conn)
        duration = time.time() - start
        
        st.success(f"Execution Time: {duration:.4f} seconds")
        st.dataframe(df)
        
        st.subheader("Execution Plan")
        plan = pd.read_sql_query(f"EXPLAIN QUERY PLAN {query}", conn)
        st.table(plan)
