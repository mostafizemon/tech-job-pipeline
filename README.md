# 🚀 Automated Data Engineering Pipeline: Job Market Insights

This project is a professional end-to-end data pipeline that extracts real-time job market data, cleans it, and transforms it into an analytical **Star Schema**. It is fully automated and operated using DevOps practices in a cloud-native environment.

## 🏗️ Architecture Overview

This pipeline follows the modern **Medallion Architecture**:

1.  **Bronze Layer (Raw Data):** Data is fetched from the API via a Python script and saved into the `bronze_jobs` table in MotherDuck.
2.  **Silver Layer (Cleaned Data):** JSON data is flattened, duplicates are removed, and data types are fixed using dbt (`stg_jobs`).
3.  **Gold Layer (Star Schema):** Transformed into fact and dimension tables for analysis (`dim_companies`, `dim_locations`, `dim_categories`, `fact_job_postings`).

---

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **Data Warehouse:** MotherDuck (DuckDB)
- **Transformation:** dbt (data build tool)
- **Deployment:** Ubuntu VPS, GitHub Actions (CI/CD)
- **Automation:** Cron Job, Bash Scripting

---

## ⚙️ How It Works (Pipeline Breakdown)

1.  **Extraction:** The `ingest_jobs.py` script collects new job postings from the API daily.
2.  **Loading:** Data is loaded directly into MotherDuck.
3.  **Transformation:**
    - The dbt project automatically takes data from the bronze table and transforms it into the silver and gold layers.
    - Unique IDs are generated for dimension tables using the `md5()` hash function.
4.  **CI/CD:** GitHub Actions is used to ensure automatic code updates and dependency installations on the server with every push.
5.  **Scheduling:** A server cron job (`run_pipeline.sh`) runs the complete pipeline serially every day at midnight.

---

## 🚀 Deployment Guide

### Manual Run:

```bash
# Activate environment
source venv/bin/activate

# Extract & Load
python ingest_jobs.py

# Transform
cd transform_jobs
dbt run
```
