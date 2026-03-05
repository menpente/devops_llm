import os
import pandas as pd
from src.setup_vanna import MyVanna

db_url = os.environ.get('DATABASE_URL', 'devops_data.duckdb')
model = os.environ.get('OLLAMA_MODEL', 'llama3')

log_file = 'bad_sql_log.csv'

if not os.path.isfile(log_file):
    print(f"No {log_file} found. Nothing to retrain.")
else:
    df = pd.read_csv(log_file)
    corrections = df[df['corrected_sql'].notna() & (df['corrected_sql'].str.strip() != '')]

    if corrections.empty:
        print("Applied 0 corrections to training data.")
    else:
        vn = MyVanna(config={'model': model})
        vn.connect_to_duckdb(url=db_url)

        for _, row in corrections.iterrows():
            vn.train(sql=row['corrected_sql'])

        print(f"Applied {len(corrections)} corrections to training data.")
