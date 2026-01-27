# Airflow-Driven ETL Pipeline (Dockerized)

A production-style, Dockerized **Apache Airflow ETL pipeline** that orchestrates scheduled data ingestion from external APIs into **PostgreSQL**, demonstrating clean DAG design, containerized infrastructure, and scalable data engineering best practices.

---

## 🚀 Overview

This project showcases how to build and run an **end-to-end ETL pipeline** using:

* **Apache Airflow** for orchestration and scheduling
* **PostgreSQL** as the analytical datastore
* **Docker & Docker Compose** for local, reproducible environments
* **Modular Python code** for maintainability and extensibility

The pipeline is designed to run on a **fixed schedule**, fetch data from an external API, and persist it into a relational database.

---

## 🏗️ Architecture

```
┌──────────────┐
│ External API │
└──────┬───────┘
       │
       ▼
┌────────────────────┐
│ Airflow DAG        │
│ (PythonOperator)   │
└──────┬─────────────┘
       │
       ▼
┌────────────────────┐
│ PostgreSQL         │
│ (Docker Container) │
└────────────────────┘
```

* Airflow runs inside a Docker container
* PostgreSQL runs in a separate container
* Containers communicate via a Docker bridge network
* All orchestration logic lives inside Airflow DAGs

---

## 📁 Project Structure

```
Airflow-Driven-ETL-Pipeline-Dockerized/
├── airflow/
│   └── dags/
│       └── orchestrator.py
│
├── api-request/
│   └── insert_records.py
│
├── postgres/
│   └── airflow_init.sql
│
├── docker-compose.yaml
├── .gitignore
└── README.md
```

### Key Components

* **`orchestrator.py`** – Airflow DAG definition
* **`insert_records.py`** – API ingestion & database logic
* **`airflow_init.sql`** – Database bootstrap script
* **`docker-compose.yaml`** – Multi-container orchestration

---

## ⏱️ Scheduling

* The DAG is configured to run **every minute**
* Uses Airflow’s modern `schedule` parameter (Airflow 3+ compatible)
* Catchup is disabled to avoid historical backfills

---

## ⚙️ Tech Stack

| Component     | Technology             |
| ------------- | ---------------------- |
| Orchestration | Apache Airflow 3.x     |
| Database      | PostgreSQL 14          |
| Language      | Python 3.12            |
| Containers    | Docker, Docker Compose |
| Networking    | Docker Bridge Network  |

---

## 🐳 Running the Project Locally

### Prerequisites

* Docker
* Docker Compose
* Git

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bhuwanesh340/Airflow-Driven-ETL-Pipeline-Dockerized.git
cd Airflow-Driven-ETL-Pipeline-Dockerized
```

---

### 2️⃣ Start the Services

```bash
docker compose up -d
```

This will:

* Start PostgreSQL
* Initialize the database
* Start Airflow (Webserver + Scheduler)
* Auto-migrate Airflow metadata DB

---

### 3️⃣ Access Airflow UI

```
http://localhost:8000
```

**Default credentials:**

```
Username: airflow
Password: airflow
```
<img width="1505" height="794" alt="image" src="https://github.com/user-attachments/assets/198e5a07-2af2-472a-bfb2-3b7ea43fe592" />

---

## 🧪 Verifying the Pipeline

1. Open Airflow UI
2. Enable the **`orchestrator`** DAG
3. Trigger manually or wait for the scheduler
4. View logs to confirm:

   * API request success
   * Database connection
   * Data insertion

---

## 🛑 Stopping the Pipeline

To pause execution:

* Disable the DAG in the Airflow UI

To stop containers:

```bash
docker compose down
```

---

## 🔒 Git & Data Safety

* **PostgreSQL runtime data is excluded from Git**
* Virtual environments are ignored
* Only source code and configuration are tracked

This keeps the repository:

* Lightweight
* Secure
* Production-friendly

---

## 🧠 Key Learnings Demonstrated

* Airflow DAG lifecycle & scheduling
* Docker networking between services
* Containerized Postgres connectivity
* Clean separation of orchestration and business logic
* Production-grade Git hygiene

---

## 📌 Future Enhancements

* Add Airflow Connections & Variables
* Replace PythonOperator with TaskFlow API
* Add retries, SLAs, and alerting
* Introduce data validation & schema checks
* Add CI/CD pipeline
* Migrate to Kubernetes / Helm

---

## 👤 Author

**Bhuwanesh Tripathi**
Data Engineer | Data Scientist | Cloud & MLOps
📌 GitHub: [https://github.com/bhuwanesh340](https://github.com/bhuwanesh340)

---

## ⭐ If you find this useful

Give the repo a ⭐ — it helps and is appreciated!
