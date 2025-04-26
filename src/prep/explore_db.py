import duckdb

# --- CONFIGURATION ---

# Path to your DuckDB database file
duckdb_file_path = 'devops_data.duckdb'

# --- MAIN SCRIPT ---

def run_query_loop():
    print(f"🔗 Connecting to database: {duckdb_file_path}")
    con = duckdb.connect(duckdb_file_path)

    print("\n🚀 Ready to execute SQL queries against devops_data.duckdb")
    print("Type your SQL queries below. Type 'exit' or 'quit' to leave.\n")

    while True:
        query = input("SQL> ").strip()
        if query.lower() in ('exit', 'quit'):
            print("👋 Exiting...")
            break
        try:
            result = con.execute(query).fetchdf()
            if result.empty:
                print("✅ Query executed successfully. No results to display.\n")
            else:
                print(result.to_string(index=False))
                print()
        except Exception as e:
            print(f"❌ Error executing query: {e}\n")

    con.close()

if __name__ == "__main__":
    run_query_loop()
