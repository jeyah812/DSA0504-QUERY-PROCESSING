import matplotlib.pyplot as plt

# Data
students = ["A", "B", "C", "D", "E"]
marks = [85, 72, 90, 65, 78]
attendance = [95, 80, 98, 70, 85]
study_hours = [6, 4, 7, 3, 5]

# Create a figure with multiple plots
plt.figure(figsize=(12, 8))

# Plot 1 - Line Chart
plt.subplot(2, 2, 1)
plt.plot(students, marks, marker="o")
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Plot 2 - Bar Chart
plt.subplot(2, 2, 2)
plt.bar(students, attendance)
plt.title("Student Attendance")
plt.xlabel("Students")
plt.ylabel("Attendance (%)")

# Plot 3 - Scatter Plot
plt.subplot(2, 2, 3)
plt.scatter(study_hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

# Plot 4 - Line Chart
plt.subplot(2, 2, 4)
plt.plot(students, study_hours, marker="o")
plt.title("Study Hours")
plt.xlabel("Students")
plt.ylabel("Hours")

# Adjust spacing
plt.tight_layout()

# Display all plots
plt.show()
