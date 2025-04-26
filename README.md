# devops_llm
Project for master's thesis on Big Data and BI, using LLMs to analyze devops data. The goal is to be able to explore devops data in a conversational mode.

## Installation

### Step 1: Install dependencies
pip install -r requirements.txt

### Step 2: Train and save Vanna
make setup

### Step 3: Run Flask app for ad hoc querying
make run


## Data

Initial dataset was generated synthetically inspired on schemas and profiles of corporate datasets. We also generated a DDL, a data dictionary and sample queries that were used to train Vanna on this specific domain. We also set up tracing so that bad SQL queries are captured in a log and can be used to retrain Vanna.

## LLM

This setup uses llama3 locally through Ollama for two reasons:

* Preserve data confidentiality
* Minimize costs in an enterprise-grade environment with hundreds of users
