import csv
import matplotlib.pyplot as plt

products = []
sales = []

# Create CSV file

with open("sales.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Product", "Sales"])

    writer.writerow(["Laptop", 50000])
    writer.writerow(["Phone", 30000])
    writer.writerow(["Headphones", 10000])
    writer.writerow(["Keyboard", 5000])


# Read CSV file

with open("sales.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        products.append(row["Product"])

        sales.append(float(row["Sales"]))


# Display sales report

print("RETAIL SALES DASHBOARD")

for product, amount in zip(products, sales):

    print(product, ":", amount)

total_sales = sum(sales)

print("Total Sales:", total_sales)


# Create bar chart

plt.bar(products, sales)

plt.title("Retail Sales Dashboard")

plt.xlabel("Products")

plt.ylabel("Sales Amount")

plt.show()