import matplotlib.pyplot as plt

# Sample data
categories = ['Category 1', 'Category 2', 'Category 3']
data1 = [110, 150, 70]
data2 = [60, 110, 60]

plt.bar(categories, data1, label='Data 1', color='blue')
plt.bar(categories, data2, label='Data 2', color='red')

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph with Overlay')

plt.show()