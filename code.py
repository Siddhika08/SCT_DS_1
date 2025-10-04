# Task 01: Visualizing Population Distribution using World Bank Data

import pandas as pd
import requests
import matplotlib.pyplot as plt

# Step 1: Fetch data from World Bank API
country = "IN"
indicator = "SP.POP.TOTL"
url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page=1000"

resp = requests.get(url)
data = resp.json()
df = pd.json_normalize(data[1])

# Step 2: Clean data
df = df[['date', 'value']].dropna()
df['date'] = df['date'].astype(int)
df = df.sort_values('date')
df.columns = ['Year', 'Population']

# Step 3: Plot line chart
plt.figure(figsize=(10,6))
plt.plot(df['Year'], df['Population'], marker='o', color='teal', linewidth=2)
plt.title("India: Total Population (1960–2023)", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Population (persons)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Annotate every 10 years
for i, row in df.iterrows():
    if row['Year'] % 10 == 0:
        plt.text(row['Year'], row['Population'], f"{int(row['Population']/1e6):,}M",
                 ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig("images/india_population_trend.png", dpi=300)
plt.show()
