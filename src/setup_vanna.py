import pandas as pd
from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore

class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        if config is None:
            config = {}
        config["persist_directory"] = "./vanna_chroma_db"
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)

def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def main():
    vn = MyVanna(config={'model': 'llama3'})

    # Connect to DuckDB
    vn.connect_to_duckdb(url='/Users/rubendelafuente/tfm/data/dora_llm.duckdb')

    # Train on info schema
    df_information_schema = vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")
    plan = vn.get_training_plan_generic(df_information_schema)
    vn.train(plan=plan)

    # Train on DDL
    ddl_content = read_file('doc/DDL')
    vn.train(ddl=ddl_content)

    # Train on documentation
    documentation_content = read_file('doc/dictionary')
    vn.train(documentation=documentation_content)

    # Train on SQL examples
    sql_examples = pd.read_csv('test/sample_SQL_queries_and_results.csv')
    for sql_query in sql_examples['query']:
        vn.train(sql=sql_query)

    
    print("✅ Setup and training complete!")

if __name__ == "__main__":
    main()
