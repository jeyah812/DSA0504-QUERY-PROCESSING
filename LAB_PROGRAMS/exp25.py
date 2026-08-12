import matplotlib.pyplot as plt

# X-axis values
x = [10, 20, 30, 40]

# Values for two lines
line1 = [20, 40, 30, 10]
line2 = [40, 10, 20, 30]

# Plot first line
plt.plot(
    x,
    line1,
    color="blue",
    linewidth=3,
    label="line1-width-3"
)

# Plot second line
plt.plot(
    x,
    line2,
    color="red",
    linewidth=5,
    label="line2-width-5"
)

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two or More Lines with Different Widths and Colors")

# Display legend
plt.legend()

# Display graph
plt.show()
