from collections import defaultdict

data_by_year = defaultdict(list)

with open("gas_prices.txt", "r") as file:
    for line in file:
        date, price = line.strip().split(":")
        month, _, year = date.split("-")
        data_by_year[year].append((float(price), month))

# print(data_by_year)

# for year, data in sorted(data_by_year.items()):
#     data.sort(key=lambda x: x[1])

def calculate_stats(data):
    low = min(data)[0]
    high = max(data)[0]
    average = sum(price for price, _ in data) / len(data)
    return low, average, high

month_names = {
    "01":"January",
    "02":"February",
    "03":"March",
    "04":"April",
    "05":"May",
    "06":"June",
    "07":"July",
    "08":"August",
    "09":"September",
    "10":"October",
    "11":"November",
    "12":"December"
}

# Write the report to the output file
for year, data in sorted(data_by_year.items()):
    low, average, high = calculate_stats(data)
    print(f"{year}:\n")
    print(f"\tLow: ${low:.2f}, Avg: ${average:.2f}, High: ${high:.2f}\n")

    # Create a dictionary to store month average prices
    #TODO - get month and their average here
    print(data)

    print("\n")