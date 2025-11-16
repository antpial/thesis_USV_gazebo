import pandas as pd

# Wczytaj plik CSV
df = pd.read_csv("gps_compare_output.csv")

# Zobacz pierwsze wiersze
print(df.head())

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.plot(df['lon_fix'], df['lat_fix'], 'bo-', label='GPS Fix')        # niebieskie kółka
plt.plot(df['lon_perf'], df['lat_perf'], 'ro-', label='GPS Perfect')             # czerwone kółka
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Porównanie trajektorii GPS")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['timestamp_fix_sec'] + df['timestamp_fix_nanosec']*1e-9, df['lat_error'], label='Latitude Error')
plt.plot(df['timestamp_fix_sec'] + df['timestamp_fix_nanosec']*1e-9, df['lon_error'], label='Longitude Error')
plt.xlabel("Czas [s]")
plt.ylabel("Błąd [deg/meters]")
plt.title("Błędy GPS w czasie")
plt.legend()
plt.grid(True)
plt.show()
