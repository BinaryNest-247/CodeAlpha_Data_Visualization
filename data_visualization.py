import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("books.csv")

# Clean Price column - handle encoding issues with pound symbol
data["Price"] = data["Price"].str.replace(r"[£Â£]", "", regex=True).astype(float)

# 1️⃣ Histogram – Price Distribution
print("\n" + "="*50)
print("GENERATING HISTOGRAM")
print("="*50)
plt.figure(figsize=(10, 6))
plt.hist(data["Price"], bins=15, color='steelblue', edgecolor='black', alpha=0.7)
plt.title("Distribution of Book Prices", fontsize=14, fontweight='bold')
plt.xlabel("Price (£)", fontsize=12)
plt.ylabel("Number of Books", fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("histogram_price_distribution.png", dpi=300, bbox_inches='tight')
print("✓ Histogram saved as 'histogram_price_distribution.png'")
plt.close()

# 2️⃣ Bar Chart – Top 10 Most Expensive Books
print("\n" + "="*50)
print("GENERATING BAR CHART")
print("="*50)
top_books = data.sort_values(by="Price", ascending=False).head(10)

plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(top_books)), top_books["Price"], color='coral', edgecolor='black', alpha=0.7)
plt.title("Top 10 Most Expensive Books", fontsize=14, fontweight='bold')
plt.xlabel("Book Name", fontsize=12)
plt.ylabel("Price (£)", fontsize=12)
plt.xticks(range(len(top_books)), [name[:20] + '...' if len(name) > 20 else name for name in top_books["Book Name"]], rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig("bar_chart_top_10_books.png", dpi=300, bbox_inches='tight')
print("✓ Bar chart saved as 'bar_chart_top_10_books.png'")
plt.close()

print("\n" + "="*50)
print("VISUALIZATION COMPLETE!")
print("="*50)