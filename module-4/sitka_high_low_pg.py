import csv
import matplotlib.pyplot as plt
import sys

# Program: Sitka High/Low Temperatures
# Modified by: Perla Garcia Cavazos
# Date: 6/28/2026
# Changes:
# - Added menu (Highs, Lows, Exit)
# - Added loop so user can choose multiple options
# - Added low temperature graph (blue)
# - Added exit message
# - Added sys.exit() for clean exit

filename = "sitka_weather_2018_simple.csv"

dates = []
highs = []
lows = []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        dates.append(row[2])
        highs.append(int(row[5]))
        lows.append(int(row[6]))

def show_highs():
    plt.title("Sitka High Temperatures - 2018")
    plt.plot(dates, highs, c="red")
    plt.xlabel("Date")
    plt.ylabel("Temperature (F)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def show_lows():
    plt.title("Sitka Low Temperatures - 2018")
    plt.plot(dates, lows, c="blue")
    plt.xlabel("Date")
    plt.ylabel("Temperature (F)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main menu loop
while True:
    print("\n--- Sitka Weather Menu ---")
    print("1. High Temperatures")
    print("2. Low Temperatures")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        show_highs()
    elif choice == "2":
        show_lows()
    elif choice == "3":
        print("\nExiting program... Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
