import requests
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# === CONFIGURATION ===
API_KEY = "10065d31c4442c6e066dfe39f59455c3"  # Replace with your real API key
CITY = "Delhi"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# === FETCH DATA ===
response = requests.get(URL)
if response.status_code != 200:
    print("Failed to fetch data. Check your API key and city name.")
    exit()

data = response.json()

# === PARSE DATA ===
dates, temps, humidities = [], [], []
for entry in data['list']:
    date = datetime.datetime.fromtimestamp(entry['dt'])
    dates.append(date)
    temps.append(entry['main']['temp'])
    humidities.append(entry['main']['humidity'])

# === VISUALIZATION ===
sns.set(style="whitegrid")
plt.figure(figsize=(14, 8))

# Temperature Line Chart
plt.subplot(2, 1, 1)
sns.lineplot(x=dates, y=temps, color="orange", marker="o")
plt.title(f"Temperature Forecast for {CITY}")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

# Humidity Line Chart
plt.subplot(2, 1, 2)
sns.lineplot(x=dates, y=humidities, color="blue", marker="s")
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)

# Show Plot
plt.tight_layout()
plt.suptitle(f"5-Day Weather Dashboard for {CITY}", fontsize=16, y=1.02)
plt.show()
