import plotly.express as px
import pandas as pd

# Example data
data = {
    'Narcissism Subscales': ['Leadership/Authority', 'Grandiose/Exhibitionism', 'Entitlement/Exploitation'],
    'High Achievers': [1.36, 1.21, 1.21],
    'Moderate Achievers': [1.33, 1.28, 1.25],
    'Moral Civic Explorers': [1.25, 1.15, 1.22],
    'Moral Nationals': [1.24, 1.16, 1.20],
    'Civic Nationals': [1.43, 1.37, 1.42]
}

df = pd.DataFrame(data)

# Melt the DataFrame to long format
df_long = df.melt(id_vars=['Narcissism Subscales'], var_name='Profile', value_name='Score')

# Create the radar chart
fig = px.line_polar(df_long, r='Score', theta='Narcissism Subscales', color='Profile', line_close=True)
fig.update_traces(fill='toself')
fig.update_layout(title='Narcissism Subscales Across Profiles')

# Save the radar chart as an image
fig.write_image('narcissism_radar_chart.png')

# Show the radar chart
fig.show()
