import pandas as pd
import plotly.express as px

# Load dataset (update with the correct file path)
df = pd.read_csv("app_data.csv")

# Filter for paid apps only
df_paid = df[df['Type'] == 'Paid']

# Ensure numeric values for calculations
df_paid['Revenue'] = pd.to_numeric(df_paid['Revenue'], errors='coerce')
df_paid['Installs'] = pd.to_numeric(df_paid['Installs'], errors='coerce')

# Drop rows with missing values
df_paid = df_paid.dropna(subset=['Revenue', 'Installs', 'Category'])

# Create scatter plot with trendline
fig = px.scatter(
    df_paid, x='Installs', y='Revenue', color='Category', 
    title='Revenue vs. Installs for Paid Apps',
    labels={'Installs': 'Number of Installs', 'Revenue': 'Revenue ($)'},
    trendline='ols'
)

# Show the figure
fig.show()

# Save plot as HTML
fig.write_html("scatter_plot.html")
