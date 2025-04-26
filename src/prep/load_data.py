import duckdb
import pandas as pd

# --- CONFIGURATION ---

# Path to your CSV file
csv_file_path = 'data/devops_synthetic_data.csv'

# Name of your DuckDB database file
duckdb_file_path = 'devops_data.duckdb'

# Table name
table_name = 'devops_synthetic_data'

# --- MAIN SCRIPT ---

# Step 1: Read CSV into a Pandas DataFrame
print("Loading CSV file...")
df = pd.read_csv(csv_file_path)
print(f"CSV loaded successfully with {len(df)} rows.")

# Step 2: Connect to (or create) DuckDB database
print("Connecting to DuckDB database...")
con = duckdb.connect(duckdb_file_path)

# Step 3: Create table (if not exists)
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    change_failure_rate FLOAT,
    cycle_time_in_days FLOAT,
    date DATE,
    developer_satisfaction_agree_count SMALLINT,
    developer_satisfaction_disagree_count SMALLINT,
    developer_satisfaction_neutral_count SMALLINT,
    flow_efficiency FLOAT,
    lead_time_in_days FLOAT,
    prod_deployments_failed_count SMALLINT,
    prod_deployments_success_count SMALLINT,
    through_put FLOAT,
    time_to_restore_in_hours FLOAT,
    total_developer_satisfaction SMALLINT,
    total_incidents_resolved SMALLINT,
    team_lead VARCHAR
);
"""
print("Creating table if not exists...")
con.execute(create_table_query)

# Step 4: Insert DataFrame into DuckDB
print(f"Inserting data into '{table_name}' table...")
con.register('temp_df', df)
con.execute(f"INSERT INTO {table_name} SELECT * FROM temp_df;")

# Step 5: Clean up
con.unregister('temp_df')
con.close()

print("✅ Data successfully loaded into DuckDB database!")
