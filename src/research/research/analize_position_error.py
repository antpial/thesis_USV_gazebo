import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# --- Pobranie nazwy pliku jako argument wywołania ---
if len(sys.argv) < 2:
    print("Użycie: python3 script.py <nazwa_pliku.csv>")
    sys.exit(1)

filename = sys.argv[1]
filepath = os.path.join("Sim_output", filename)

if not os.path.exists(filepath):
    print(f"ERROR: Plik nie istnieje: {filepath}")
    sys.exit(1)

# --- Wczytaj plik CSV ---
df = pd.read_csv(filepath)

# Zobacz pierwsze wiersze
print(df.head())

# Oblicz statystyki
lat_mean_error = df['lat_error'].mean()
lon_mean_error = df['lon_error'].mean()
lat_std_error = df['lat_error'].std()
lon_std_error = df['lon_error'].std()

print(f"Średni błąd latitude: {lat_mean_error:.2e}, odchylenie standardowe: {lat_std_error:.2e}")
print(f"Średni błąd longitude: {lon_mean_error:.2e}, odchylenie standardowe: {lon_std_error:.2e}")

# --- Wykres trajektorii ---
plt.figure(figsize=(8, 6))
# plt.plot(df['lon_fix'], df['lat_fix'], 'bo-', label='GPS Fix')
plt.plot(df['lon_perf'], df['lat_perf'], 'ro-', label='GPS Perfect')
plt.xlabel("Długość geograficzna")
plt.ylabel("Szerokośc geograficzna")
plt.title("Trajektoria USV bez kompensacji wiatru")
plt.legend()
plt.grid(True)
plt.axis('equal')   # <<<<<< równoskalowe osie!
plt.show()

# --- Wykres błędów w czasie ---
time = df['timestamp_fix_sec'] + df['timestamp_fix_nanosec'] * 1e-9

plt.figure(figsize=(10, 6))
plt.plot(time, df['lat_error'], label=f'Latitude Error (mean={lat_mean_error:.2e}, std={lat_std_error:.2e})')
plt.plot(time, df['lon_error'], label=f'Longitude Error (mean={lon_mean_error:.2e}, std={lon_std_error:.2e})')
plt.xlabel("Czas [s]")
plt.ylabel("Błąd [deg/meters]")
plt.title("Błędy GPS w czasie")
plt.legend()
plt.grid(True)
plt.show()
