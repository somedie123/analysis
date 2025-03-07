import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data.csv")

# Convert the Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Calculate the average sales
average_sales = df["Sales"].mean()

# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Sales"], label="Daily Sales", marker="o", linestyle="-", color="blue")

# Add the average line
plt.axhline(y=average_sales, color="red", linestyle="--", label=f"Average Sales ({average_sales:.2f})")

# Add titles and labels
plt.title("📊 Sales Data Analysis", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Sales", fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)

plt.show()
