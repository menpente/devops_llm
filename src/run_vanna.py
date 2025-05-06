import time
import logging
import os

from setup_vanna import MyVanna
from vanna.flask import VannaFlaskApp

# OpenTelemetry imports
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

# Setup tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())  # Logs spans to console
)

# Setup file logger for traces
logging.basicConfig(
    filename='trace.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True

)
logging.info("Test log message to verify logging setup.")
# --- SQL Error Logger ---
def log_bad_sql(bad_sql, error_message):
    log_file = "bad_sql_log.csv"
    file_exists = os.path.isfile(log_file)

    with open(log_file, "a") as f:
        if not file_exists:
            f.write("bad_sql,error_message,corrected_sql,notes\n")
        f.write(f'"{bad_sql}","{error_message}","",""\n')

# --- Safe SQL Execution ---
def safe_run_sql(vn, sql_query):
    try:
        result = vn.run_sql(sql_query)
        print("✅ SQL ran successfully!")
        return result
    except Exception as e:
        print(f"❌ SQL Error: {e}")
        log_bad_sql(sql_query, str(e))
        return None

# --- Traced Vanna Class ---
class TracedVanna(MyVanna):
    def ask(self, question: str):
        with tracer.start_as_current_span("ask_question") as span:
            start_time = time.time()
            print(f"\n🧠 [TRACE] Asking: {question}")
            logging.info(f"ASK | Question: {question}")

            span.set_attribute("user.question", question)

            response = super().ask(question)

            duration = time.time() - start_time
            print(f"✅ [TRACE] Response in {duration:.2f}s: {response}\n")
            logging.info(f"ASK | Response: {response}")
            logging.info(f"ASK | Duration: {duration:.2f} seconds\n")

            span.set_attribute("llm.response", response)
            span.set_attribute("duration", duration)

            return response

    def ask_sql(self, question: str):
        with tracer.start_as_current_span("ask_sql") as span:
            start_time = time.time()
            print(f"\n🧠 [TRACE] Asking for SQL: {question}")
            logging.info(f"ASK_SQL | Question: {question}")

            span.set_attribute("user.question", question)

            sql_query = super().ask_sql(question)

            duration = time.time() - start_time
            print(f"✅ [TRACE] SQL generated in {duration:.2f}s:\n{sql_query}\n")
            logging.info(f"ASK_SQL | SQL Generated: {sql_query}")
            logging.info(f"ASK_SQL | Duration: {duration:.2f} seconds\n")

            span.set_attribute("llm.sql", sql_query)
            span.set_attribute("duration", duration)

            # Run SQL safely
            result = safe_run_sql(self, sql_query)

            return result

# --- Main App Start ---
def main():
    vn = TracedVanna(config={'model': 'llama3'})
    vn.connect_to_duckdb(url='devops_data.duckdb')

    app = VannaFlaskApp(vn, title='LLM-powered DX Analytics', subtitle='Secure Local Conversational Analytics for Developer Experience with Vanna and Ollama')
    app.run()

if __name__ == "__main__":
    main()
