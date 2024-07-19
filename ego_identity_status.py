import matplotlib.pyplot as plt
import seaborn as sns

# Example data
profiles = ['High Achievers', 'Moderate Achievers', 'Moral Civic Explorers', 'Moral Nationals', 'Civic Nationals']
exploration_in_breadth = [4.35, 3.90, 4.11, 3.71, 3.19]

plt.figure(figsize=(10, 6))
sns.barplot(x=profiles, y=exploration_in_breadth)
plt.title('Exploration in Breadth Across Profiles')
plt.xlabel('Profiles')
plt.ylabel('Exploration in Breadth')

# Save the bar chart as an image
plt.savefig('exploration_in_breadth.png')

# Show the bar chart
plt.show()
