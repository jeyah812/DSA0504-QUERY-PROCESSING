import matplotlib.pyplot as plt

# X-axis and Y-axis values
x = [0, 10, 20, 30, 40, 50]
y = [5, 35, 65, 95, 125, 155]

# Draw the line
plt.plot(x, y)

# Add labels and title
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Draw a line.")

# Display the graph
plt.show()
