# Enterprise SQL Performance Optimizer

A Streamlit app for analyzing SQL query execution plans and comparing optimized vs unoptimized performance on an SQLite dataset.

## Files
- `app.py`: Streamlit app entry point
- `requirements.txt`: Python dependencies
- `database_schema.sql`: sample schema file
- `notebooks/Query_Performance_Tuning.ipynb`: analysis notebook

## Deploying live

This repository is already connected to GitHub. To make the app live for anyone to access, deploy it using one of these services:

### Option 1: Streamlit Community Cloud
1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Create a new app and point it to this repository
4. Set the entry point to `app.py`

### Option 2: Render
1. Create a new Web Service on https://render.com
2. Connect your GitHub repo
3. Use `python app.py` or `streamlit run app.py --server.port=$PORT --server.headless=true`
4. Set build command: `pip install -r requirements.txt`

### Option 3: Railway / Fly / other Python hosts
Use the same entrypoint and requirements:
- `streamlit run app.py --server.port=$PORT --server.headless=true`

## Note

This repository is designed to be hosted remotely. It does not need to run locally for users to access the live service once hosted.
