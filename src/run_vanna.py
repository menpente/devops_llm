from setup_vanna import MyVanna
from vanna.flask import VannaFlaskApp

def main():
    vn = MyVanna(config={'model': 'llama3'})
    vn.connect_to_duckdb(url='/Users/rubendelafuente/tfm/data/dora_llm.duckdb')

    app = VannaFlaskApp(vn)
    app.run()

if __name__ == "__main__":
    main()
