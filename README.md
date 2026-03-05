# devops_llm — Conversational Analytics over DevOps Data

**Ask questions in plain English. Get SQL-powered answers from your DORA metrics — entirely on-premise.**

![Python](https://img.shields.io/badge/Python-3.10-blue)
![DuckDB](https://img.shields.io/badge/DuckDB-analytics-orange)
![Vanna](https://img.shields.io/badge/Vanna-text--to--SQL-green)
![Ollama](https://img.shields.io/badge/Ollama-llama3-purple)
![ChromaDB](https://img.shields.io/badge/ChromaDB-vector--store-red)
![Flask](https://img.shields.io/badge/Flask-web--UI-lightgrey)
![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-observability-blueviolet)

## Overview

This is a master's thesis project (Big Data & Business Intelligence) demonstrating how a fully local LLM stack can power conversational analytics over DevOps/DORA metrics. Users type natural language questions; [Vanna](https://vanna.ai) generates SQL via few-shot RAG, queries a DuckDB database, and returns results through a Flask chat UI — with **zero data leaving the machine**.

The architecture was designed with enterprise applicability in mind: confidential metrics never touch an external API, the LLM runs locally via Ollama, and a built-in feedback loop captures bad SQL for incremental retraining.

## Architecture

```
                     Training pipeline
                     ─────────────────
  doc/DDL ──────────┐
  doc/dictionary ───┤──► ChromaDB (RAG embeddings)
  SQL examples ─────┤         │
  INFORMATION_SCHEMA┘         │
                              ▼
  data/devops_synthetic_data.csv          User question
           │                                    │
           ▼                                    ▼
     DuckDB (.duckdb) ◄────── SQL ◄──── Vanna + llama3 (Ollama)
           │                                    │
           └──────────── Result ───────────────►│
                                                ▼
                                        Flask Web UI
                                                │
                               Failed SQL → bad_sql_log.csv
                                                │
                                           make retrain
```

## Why a Local LLM?

Running llama3 through Ollama instead of a cloud API provides three enterprise-grade properties:

- **Data confidentiality** — DevOps metrics, incident data, and team performance never leave the network
- **Cost predictability** — zero per-token charges regardless of query volume or team size
- **Auditability** — full observability via OpenTelemetry spans and a `trace.log`

## Prerequisites

- Python 3.10.12 (see `runtime.txt`)
- [Ollama](https://ollama.ai) running locally: `ollama pull llama3`

## Quickstart

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Copy and configure environment
cp .env.example .env

# 3. Load CSV data into DuckDB
make load-data

# 4. Train Vanna on schema, DDL, dictionary, and SQL examples
make setup

# 5. Start the Flask chat UI
make run
# Open http://localhost:8084
```

For production deployments (e.g. Heroku), `gunicorn app:app` uses the `Procfile` entry point.

## Retraining with Corrections

When Vanna generates bad SQL, it is automatically appended to `bad_sql_log.csv` with columns:

| Column | Description |
|---|---|
| `bad_sql` | The SQL that failed |
| `error_message` | The DuckDB error |
| `corrected_sql` | **Fill this in manually** |
| `notes` | Optional context |

After editing the CSV to add corrected queries:

```bash
make retrain
# Applied N corrections to training data
```

## Data

The dataset (`data/devops_synthetic_data.csv`) is synthetically generated to mirror real corporate DevOps telemetry. It contains DORA and DevEx metrics per team per day:

- **DORA metrics:** change failure rate, lead time, cycle time, deployment counts (success/failed), MTTR
- **DevEx metrics:** developer satisfaction (agree/neutral/disagree counts), flow efficiency, throughput
- **Dimension:** `team_lead` (VARCHAR) for team-level grouping

Training knowledge is stored in:
- `doc/DDL` — raw table DDL
- `doc/dictionary` — business glossary
- `test/sample_SQL_queries_and_results.csv` — example question/SQL pairs

## Tech Stack

| Component | Role |
|---|---|
| [Vanna](https://vanna.ai) | Text-to-SQL framework (RAG + LLM orchestration) |
| [llama3 via Ollama](https://ollama.ai) | Local LLM for SQL generation |
| [ChromaDB](https://www.trychroma.com) | Vector store for few-shot retrieval |
| [DuckDB](https://duckdb.org) | In-process OLAP database |
| [Flask](https://flask.palletsprojects.com) | Web chat UI (via `VannaFlaskApp`) |
| [OpenTelemetry](https://opentelemetry.io) | Distributed tracing for LLM calls |
| pandas | CSV ingestion and correction processing |

## Makefile Reference

```
make load-data   # Load CSV → DuckDB
make setup       # Train Vanna (RAG)
make run         # Start Flask UI
make retrain     # Apply corrected SQL from bad_sql_log.csv
make clean       # Remove ChromaDB vector store (forces full retrain)
```
