from collections import defaultdict

data_by_year = defaultdict(list)

with open("gas_prices.txt", "r") as file:
    for line in file:
        date, price = line.strip().split(":")
        month, _, year = date.split("-")
        data_by_year[year].append((float(price), month))

def calculate_stats(data):
    low = min(data)[0]
    high = max(data)[0]
    average = sum(price for price, _ in data) / len(data)
    return low, average, high

month_names = {
    "01":"January","02":"February","03":"March","04":"April",
    "05":"May","06":"June","07":"July","08":"August",
    "09":"September","10":"October","11":"November","12":"December"
}

for year, data in sorted(data_by_year.items()):
    low, average, high = calculate_stats(data)
    print(f"{year}:")
    print(f"    Low: ${low:.2f}, Avg: ${average:.2f}, High: ${high:.2f}")
    # Initialize a dictionary to store month-wise averages
    month_averages = {month: [] for month in month_names}
    # Calculate month-wise averages and store them
    for price, month in data:
        month_averages[month].append(price)
    # Print month-wise averages
    for month, prices in sorted(month_averages.items()):
        month_name = month_names[month]
        month_average = sum(prices) / len(prices)
        print(f"    {month_name:{12}}${month_average:.2f}")