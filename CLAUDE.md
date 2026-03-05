# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Master's thesis project exploring DevOps data via natural language using a local LLM stack. Users ask questions in plain English; Vanna generates SQL, queries DuckDB, and returns results through a Flask web UI.

**Stack:** Vanna (text-to-SQL framework) + llama3 via Ollama (local LLM) + ChromaDB (vector store) + DuckDB (analytics database) + Flask (web UI)

## Commands

All commands must be run from the **project root** (not from `src/`), as scripts use relative paths.

```bash
# Install dependencies
pip install -r requirements.txt

# One-time: load CSV data into DuckDB
python src/prep/load_data.py

# Train Vanna on the database schema, DDL, data dictionary, and SQL examples
make setup        # runs: python setup_vanna.py (note: makefile uses wrong path; run directly)
# Correct command:
python src/setup_vanna.py

# Run the Flask web app
make run          # runs: python run_vanna.py (same path issue)
# Correct command:
python src/run_vanna.py

# Interactive SQL REPL against DuckDB (for exploration/debugging)
python src/prep/explore_db.py

# Remove the ChromaDB vector store (forces full retrain on next setup)
make clean
```

> **Note:** The Makefile targets `setup` and `run` reference `python setup_vanna.py` / `python run_vanna.py` without the `src/` prefix. Run the `src/` paths directly from root.

## Architecture

### Training pipeline (`src/setup_vanna.py`)
`MyVanna` uses Python multiple inheritance to combine `ChromaDB_VectorStore` (vector storage for RAG) and `Ollama` (LLM backend). Training ingests four knowledge sources in order:
1. `INFORMATION_SCHEMA.COLUMNS` from DuckDB (auto-generated schema plan)
2. `doc/DDL` - raw DDL for the `synthetic_data` table
3. `doc/dictionary` - business glossary / data dictionary
4. `test/sample_SQL_queries_and_results.csv` - example SQL queries

Trained embeddings are persisted in `vanna_chroma_db/` (ChromaDB). The UUID directories at the repo root (`312b8e36-*/`, `8ea4ed34-*/`, `b3a9ebd6-*/`) are ChromaDB segment files.

### Runtime (`src/run_vanna.py`)
`TracedVanna` extends `MyVanna` and wraps `ask()` and `ask_sql()` with OpenTelemetry spans. Failed SQL executions are appended to `bad_sql_log.csv` (columns: `bad_sql`, `error_message`, `corrected_sql`, `notes`) for future retraining. All traces also go to `trace.log`.

`VannaFlaskApp` (from the `vanna` package) provides the full chat UI - no custom Flask routes are defined.

### Data
- Source: `data/devops_synthetic_data.csv` (synthetic DevOps metrics)
- Database: `devops_data.duckdb` (single table: `devops_synthetic_data`)
- Table columns: DORA/DevEx metrics (change failure rate, cycle time, lead time, deployment counts, flow efficiency, MTTR, developer satisfaction, throughput) + `team_lead` (VARCHAR)

### Retraining with corrections
`src/train/train_corrections.py` is intended for feeding corrected SQL from `bad_sql_log.csv` back into Vanna. The file is currently a stub.

## Prerequisites

- Python 3.10.12 (see `runtime.txt`)
- [Ollama](https://ollama.ai) running locally with the `llama3` model pulled (`ollama pull llama3`)
- `devops_data.duckdb` must exist before running `make setup` (run `load_data.py` first if starting fresh)
