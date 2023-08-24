from collections import defaultdict

data_by_year = defaultdict(list)

with open("gas_prices.txt", "r") as file:
    for line in file:
        date, price = line.strip().split(":")
        month, _, year = date.split("-")
        data_by_year[year].append((float(price), month))

for year, data in sorted(data_by_year.items()):
    data.sort(key=lambda x: x[1])

def calculate_stats(data):
    low = min(data)[0]
    high = max(data)[0]
    average = sum(price for price, _ in data) / len(data)
    return low, average, high

month_names = [
    None, "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Write the report to the output file
with open("gas_report.txt", "w") as output_file:
    for year, data in sorted(data_by_year.items()):
        low, average, high = calculate_stats(data)
        output_file.write(f"{year}:\n")
        output_file.write(f"    Low: ${low:.2f}, Avg: ${average:.2f}, High: ${high:.2f}\n")

        # Create a dictionary to store month average prices
        #TODO - get month and their average here

        output_file.write("\n")