import os
from src.run_vanna import TracedVanna
from vanna.flask import VannaFlaskApp

db_url = os.environ.get('DATABASE_URL', 'devops_data.duckdb')
model = os.environ.get('OLLAMA_MODEL', 'llama3')

vn = TracedVanna(config={'model': model})
vn.connect_to_duckdb(url=db_url)

app = VannaFlaskApp(
    vn,
    title='LLM-powered DX Analytics',
    subtitle='Secure Local Conversational Analytics for Developer Experience with Vanna and Ollama'
).app
