import pandas as pd
import numpy as np
from faker import Faker
import random

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
fake = Faker()
fake.seed_instance(SEED)

NUM_ROWS = 10000
regions = ['East', 'West', 'Central', 'South']
categories = ['Furniture', 'Office Supplies', 'Technology']
sub_categories = {
    'Furniture': ['Chairs', 'Tables', 'Bookcases'],
    'Office Supplies': ['Binders', 'Paper', 'Pens'],
    'Technology': ['Phones', 'Laptops', 'Accessories']
}

data = []

for i in range(NUM_ROWS):
    order_id = fake.unique.bothify(text='ORD#####')
    order_date = fake.date_between(start_date='-2y', end_date='today')
    region = random.choice(regions)
    category = random.choice(categories)
    sub_category = random.choice(sub_categories[category])
    sales = round(random.uniform(20, 1000), 2)
    profit_margin = random.uniform(0.05, 0.3)
    profit = round(sales * profit_margin, 2)

    data.append([
        order_id, order_date, region, category, sub_category, sales, profit
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    'order_id', 'order_date', 'region', 'category', 'sub_category', 'sales', 'profit'
])

# Save to CSV
df.to_csv("data/raw/sales_data.csv", index=False)
print("✅ Generated synthetic sales data!")