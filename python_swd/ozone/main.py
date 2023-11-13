import pandas as pd
import matplotlib.pyplot as plt

print("Loading data...")

state_codes = {}
with open('./state_codes-1.txt', "r") as file:
    for line in file:
        code, name = line.strip().split(',')
        state_codes[code] = name

counties_by_state = {}
with open('counties.txt', 'r') as f:
    state_name = None
    for line in f:
        if line.strip() and not line.startswith('\t'):
            state_name = line.strip()
            counties_by_state[state_name] = []
        else:
            counties_by_state[state_name].append(line.strip())

df = pd.read_csv('./daily_44201_2021.csv', parse_dates=['Date Local'], low_memory=False)

def plot_aqi(state, county):
    data = df[(df['State Name'] == state) & (df['County Name'] == county)]
    avg_aqi = data['AQI'].mean()

    plt.figure(figsize=(10,5))
    plt.plot(data['AQI'], color='green' if avg_aqi <= 50 else 'red')
    plt.title(f'{county} County, {state} (avg. AQI = {avg_aqi:.0f})')
    plt.xticks([])

    choice = input("Choose destination for plot:\n1. Screen\n2. File\n")
    if choice == '1':
        plt.show()
    elif choice == '2':
        filename = input("Enter file with extension of jpg|png|pdf: ")
        plt.savefig(filename)

def main():
    while True:
        state = input("Enter 2-letter state code (Q to quit): ")
        if state.lower() == 'q':
            break
        try:
            state_name = state_codes[state.upper()]
        except KeyError:
            print('Invalid state code!')
            continue
        counties = counties_by_state[state_name]

        while True:
            for i, county in enumerate(counties, start=1):
                print(f'{i}: {county}')
            county_number = int(input('Enter number for county: '))
            try:
                county_name = counties[county_number - 1]
            except IndexError:
                print('Invalid county number!')
                continue
            plot_aqi(state_name, county_name)
            another_county = input(f'Another {state_name} county? (y/n): ')
            if another_county.lower() == 'n':
                break

if __name__ == "__main__":
    main()
