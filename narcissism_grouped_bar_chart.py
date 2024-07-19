import matplotlib.pyplot as plt
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
df.set_index('Narcissism Subscales', inplace=True)

# Custom colors
colors = ['#E49B3C', '#C58BA1', '#955796', '#A99EA2', '#EFA697']

ax = df.plot(kind='bar', figsize=(10, 6), color=colors)

plt.title('Narcissism Subscales Across Profiles')
plt.xlabel('Narcissism Subscales')
plt.ylabel('Score')
plt.legend(title='Profiles')
plt.xticks(rotation=45)

# Save the grouped bar chart as an image
plt.savefig('narcissism_grouped_bar_chart.png')

# Show the grouped bar chart
plt.show()
