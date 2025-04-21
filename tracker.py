import matplotlib.pyplot as plt
import datetime
import json
import os

DATA_FILE = "health_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def today():
    return datetime.date.today().isoformat()

def input_data(data):
    date = today()
    print(f"\nEnter your health data for {date}:")

    water = float(input("Water intake (in liters): "))
    sleep = float(input("Sleep (in hours): "))
    steps = int(input("Steps walked: "))
    meals = int(input("Number of meals: "))

    data[date] = {
        "water": water,
        "sleep": sleep,
        "steps": steps,
        "meals": meals
    }

    save_data(data)
    print("✅ Data saved successfully!")

def show_summary(data):
    date = today()
    if date not in data:
        print("⚠️ No data entered for today yet.")
        return

    entry = data[date]
    print(f"\n📋 Summary for {date}:")
    print(f"💧 Water intake: {entry['water']} liters")
    print(f"😴 Sleep: {entry['sleep']} hours")
    print(f"🚶 Steps: {entry['steps']}")
    print(f"🍽️ Meals: {entry['meals']}")

    if entry['water'] < 2:
        print("🔔 Tip: Try to drink at least 2 liters of water daily.")
    if entry['sleep'] < 7:
        print("🔔 Tip: Aim for 7-8 hours of sleep for better health.")
    if entry['steps'] < 5000:
        print("🔔 Tip: Walking more than 5000 steps improves fitness!")

def visualize_data(data):
    
    dates = sorted(data.keys())[-7:]
    if not dates:
        print("⚠️ Not enough data to plot.")
        return

    water = [data[d]['water'] for d in dates]
    sleep = [data[d]['sleep'] for d in dates]
    steps = [data[d]['steps'] for d in dates]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, water, label="Water Intake (L)", marker='o')
    plt.plot(dates, sleep, label="Sleep (hrs)", marker='s')
    plt.plot(dates, steps, label="Steps", marker='^')

    plt.title("📊 Weekly Health Tracker")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def main():
    data = load_data()
    while True:
        print("\n=== 🧠 Healthy Habits Tracker ===")
        print("1. Input today's data")
        print("2. Show today's summary")
        print("3. Visualize last 7 days")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            input_data(data)
        elif choice == "2":
            show_summary(data)
        elif choice == "3":
            visualize_data(data)
        elif choice == "4":
            print("👋 Exiting the tracker. Stay healthy!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
