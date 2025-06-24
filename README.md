# Retail Sales Dashboard

This project simulates a retail sales analytics pipeline using **Python**, **PostgreSQL**, and **Tableau**. It generates synthetic sales data, loads it into a relational database, transforms and aggregates it, and visualizes insights in a Tableau dashboard.

## Project Features

- Synthetic Data Generation — 10,000 rows of realistic sales data using Faker
- PostgreSQL Integration — SQL schema setup + secure ETL loading via environment variables
- ETL & Data Cleaning — Grouped and aggregated summaries for analysis
- Tableau Dashboard — Interactive charts and KPIs (sales trends, profits, categories, regions)
- Secure Secrets Management — Credentials are stored in a `.env` file and never pushed to GitHub

## Folder Structure

```
retail_sales_dashboard/
├── data/
│   ├── raw/
│   │   └── sales_data.csv
│   └── cleaned_sales.csv
├── db/
│   └── schema.sql
├── etl/
│   ├── load_to_sql.py
│   └── clean_transform.py
├── dashboard/
│   └── tableau_dashboard.twbx
├── forecast/
│   └── forecast_sales.py
├── generate_fake_sales_data.py
├── run_all.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/retail_sales_dashboard.git
cd retail_sales_dashboard
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up PostgreSQL

Ensure PostgreSQL 17+ is running on `localhost` port `5433`. Then:

```bash
# Inside psql shell
CREATE DATABASE sales_db;
\c sales_db
\i db/schema.sql
```

Or directly:

```bash
"/c/Program Files/PostgreSQL/17/bin/psql.exe" -U postgres -d sales_db -p 5433 -f db/schema.sql
```

### 4. Create Your `.env` File

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
POSTGRES_DB=sales_db
```

### 5. Run the Full Pipeline

```bash
python run_all.py
```

## Tableau Dashboard

Open `dashboard/tableau_dashboard.twbx` or connect to `data/cleaned_sales.csv`.

Dashboard Link: [https://public.tableau.com/views/SalesOverTimeDashboard_17494814623870/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link]

## Future Enhancements

- Forecasting with Prophet or ARIMA
- Live Tableau connection to PostgreSQL
- Dockerized deployment
- Geographic visualization

## Author

**Joshua Nguyen**  
[GitHub](https://github.com/JoshuaNguyen123) · [LinkedIn](https://www.linkedin.com/in/joshua-nguyen-6a812a210)

## 📄 License

MIT License
