import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load env vars
load_dotenv()

USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")
DB = os.getenv("POSTGRES_DB")

# Create DB connection
conn_str = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
engine = create_engine(conn_str)

# Compute CSV path relative to project root
project_root = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(project_root, "data", "raw", "sales_data.csv")

# Load and upload
df = pd.read_csv(csv_path)
df.columns = ["order_id", "order_date", "region", "category", "sub_category", "sales", "profit"]
df.to_sql("sales", engine, if_exists="replace", index=False)

print("Data loaded into PostgreSQL!")
