import matplotlib.pyplot as plt

# Read values from the text file
x = []
y = []

with open("data/test.txt", "r") as file:
    for line in file:
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))

# Draw the line
plt.plot(x, y)

# Add labels and title
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Sample graph")

# Display the graph
plt.show()
