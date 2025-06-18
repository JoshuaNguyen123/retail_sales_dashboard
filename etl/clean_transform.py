import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load env vars
load_dotenv()

USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")
DB = os.getenv("POSTGRES_DB")

# Connect to database
conn_str = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
engine = create_engine(conn_str)

# Define SQL query
query = """
SELECT 
    order_date::date AS date,
    region,
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY order_date, region, category
ORDER BY order_date;
"""

# Execute query
df = pd.read_sql(query, engine)

# Save to CSV
output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "cleaned_sales.csv")
df.to_csv(output_path, index=False)

print("Cleaned data exported to data/cleaned_sales.csv")
