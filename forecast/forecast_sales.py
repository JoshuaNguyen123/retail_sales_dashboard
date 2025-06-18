import pandas as pd
from prophet import Prophet

df = pd.read_csv("../data/cleaned_sales.csv")
df = df.groupby('order_date')[['total_sales']].sum().reset_index()
df.columns = ['ds', 'y']


model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv("../data/forecast/sales_forecast.csv", index=False)

