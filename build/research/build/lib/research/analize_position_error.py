import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import math

# ==========================================
#              KONFIGURACJA
# ==========================================
CUSTOM_TITLE = "Porównanie trajektorii USV"
LABEL_1 = "Surowe dane GPS"  # Plik 1 (Niebieski)
LABEL_2 = "Fzuja danych GPS i IMU"    # Plik 2 (Czerwony)
# ==========================================

# --- Sprawdzenie argumentów ---
if len(sys.argv) < 2:
    print("Użycie:")
    print("  Tryb 1 pliku (Fix vs Perfect): python3 script.py <plik.csv>")
    print("  Tryb 2 plików (Porównanie):    python3 script.py <plik_1.csv> <plik_2.csv>")
    sys.exit(1)

# Ustalenie trybu działania
mode = "SINGLE" if len(sys.argv) == 2 else "COMPARE"

file1_name = sys.argv[1]
path1 = os.path.join("Sim_output", file1_name)

if not os.path.exists(path1):
    print(f"ERROR: Plik nie istnieje: {path1}")
    sys.exit(1)

df1 = pd.read_csv(path1)

# ==========================================
#      OBLICZANIE WSPÓŁCZYNNIKÓW (m/deg)
# ==========================================
ref_lat = -33.721365
ref_lat_rad = math.radians(ref_lat)

# 1 deg szerokości (Latitude) w metrach (Wzór WGS84 przybliżony)
# Na szerokości -33 st. to około 110900 metrów
m_per_deg_lat = 111132.954 - 559.822 * math.cos(2 * ref_lat_rad) + 1.175 * math.cos(4 * ref_lat_rad)

# 1 deg długości (Longitude) w metrach
# Zależy od cosinusa szerokości. Na szerokości -33 st. to około 92600 metrów
m_per_deg_lon = 111319.9 * math.cos(ref_lat_rad)

# ==========================================
#        WYŚWIETLANIE STATYSTYK
# ==========================================

# Funkcja pomocnicza do drukowania, żeby nie kopiować kodu
def print_stats(name, df):
    mae_lat_deg = df['lat_error'].abs().mean()
    mae_lon_deg = df['lon_error'].abs().mean()
    
    # Konwersja MAE na metry
    mae_lat_m = mae_lat_deg * m_per_deg_lat
    mae_lon_m = mae_lon_deg * m_per_deg_lon

    var_lat = df['lat_error'].var()
    var_lon = df['lon_error'].var()
    
    # Odchylenie standardowe w metrach (pierwiastek z wariancji * konwersja)
    std_lat_d = (var_lat**0.5)
    std_lon_d = (var_lon**0.5)
    std_lat_m = (var_lat**0.5) * m_per_deg_lat
    std_lon_m = (var_lon**0.5) * m_per_deg_lon

    print(f"--- {name} ---")
    print(f"Śr. błąd (MAE):")
    print(f"  Lat: {mae_lat_deg:.2e} deg ({mae_lat_m:.3f} m)")
    print(f"  Lon: {mae_lon_deg:.2e} deg ({mae_lon_m:.3f} m)")
    
    print(f"Wariancja (Szum):")
    print(f"  Lat: {var_lat:.2e}")
    print(f"  Lon: {var_lon:.2e}")

    print("Odchylenie standardowe")
    print(f" Lat: {std_lat_d:.3e} deg, {std_lat_m:.3f} m")
    print(f"  Lon: {std_lon_d:.3e} deg, {std_lon_m:.3f} m")
    print("")


# ==========================================
#        TRYB 1: POJEDYNCZY PLIK
# ==========================================
if mode == "SINGLE":
    print(f"--- Tryb POJEDYNCZY: Analiza pliku {file1_name} ---")
    
    series_name_1 = "GPS (Pomiar)"
    series_name_2 = "GPS Perfect (Referencja)"
    plot_title = "Analiza trajektorii: surowe dane GPS"
    
    # Obliczenia statystyk
    lat_mean = df1['lat_error'].mean()
    lon_mean = df1['lon_error'].mean()
    lat_var = df1['lat_error'].var()
    lon_var = df1['lon_error'].var()
    
    print(f"Śr. błąd Lat: {lat_mean:.2e}, Lon: {lon_mean:.2e}")
    print(f"Wariancja Lat: {lat_var:.2e}, Lon: {lon_var:.2e}")

    # Trajektoria
    x1, y1 = df1['lon_fix'], df1['lat_fix']
    style1 = 'r.' 
    alpha1 = 0.5
    lw1 = 1
    
    x2, y2 = df1['lon_perf'], df1['lat_perf']
    style2 = 'b-' 
    alpha2 = 0.8
    lw2 = 2.0

    # Dane do wykresów błędów
    raw_time_1 = df1['timestamp_fix_sec'] + df1['timestamp_fix_nanosec'] * 1e-9
    time_series = raw_time_1 - raw_time_1.iloc[0] 
    
    err_lat_1 = df1['lat_error']
    err_lon_1 = df1['lon_error']
    
    # Zmienne dla drugiego pliku (puste w tym trybie)
    time_series_2 = None
    err_lat_2 = None
    err_lon_2 = None

# ==========================================
#        TRYB 2: PORÓWNANIE DWÓCH PLIKÓW
# ==========================================
else:
    file2_name = sys.argv[2]
    path2 = os.path.join("Sim_output", file2_name)
    
    if not os.path.exists(path2):
        print(f"ERROR: Plik nie istnieje: {path2}")
        sys.exit(1)
        
    df2 = pd.read_csv(path2)
    print(f"--- Tryb PORÓWNANIA: {file1_name} vs {file2_name} ---")

    series_name_1 = LABEL_1 if LABEL_1 else file1_name
    series_name_2 = LABEL_2 if LABEL_2 else file2_name
    plot_title = CUSTOM_TITLE if CUSTOM_TITLE else f"Porównanie: {series_name_1} vs {series_name_2}"

    # Statystyki dla pliku 1
    print(f"--- {series_name_1} ---")
    # print(f"Śr. błąd Lat: {df1['lat_error'].abs().mean():.2e}, Lon: {df1['lon_error'].abs().mean():.2e}")
    # print(f"Wariancja Lat: {df1['lat_error'].var():.2e}, Lon: {df1['lon_error'].var():.2e}")
    print_stats(series_name_1, df1)
    
    # Statystyki dla pliku 2
    print(f"--- {series_name_2} ---")
    # print(f"Śr. błąd Lat: {df2['lat_error'].abs().mean():.2e}, Lon: {df2['lon_error'].abs().mean():.2e}")
    # print(f"Wariancja Lat: {df2['lat_error'].var():.2e}, Lon: {df2['lon_error'].var():.2e}")
    print_stats(series_name_2, df2)

    # Trajektoria (Perfect vs Perfect)
    x1, y1 = df1['lon_perf'], df1['lat_perf']
    style1 = 'b-'
    alpha1 = 0.7
    lw1 = 3.0
    
    x2, y2 = df2['lon_perf'], df2['lat_perf']
    style2 = 'r-'
    alpha2 = 0.7
    lw2 = 3.0

    # Dane do wykresów błędów
    raw_time_1 = df1['timestamp_fix_sec'] + df1['timestamp_fix_nanosec'] * 1e-9
    time_series = raw_time_1 - raw_time_1.iloc[0]

    raw_time_2 = df2['timestamp_fix_sec'] + df2['timestamp_fix_nanosec'] * 1e-9
    time_series_2 = raw_time_2 - raw_time_2.iloc[0]
    
    err_lat_1 = df1['lat_error']
    err_lon_1 = df1['lon_error']
    err_lat_2 = df2['lat_error']
    err_lon_2 = df2['lon_error']


# ==========================================
#              RYSOWANIE WYKRESÓW
# ==========================================

# --- Wykres 1: Trajektoria (Wspólny dla obu trybów) ---

plt.figure(figsize=(10, 8))

# Rysowanie tras
plt.plot(x1, y1, style1, alpha=alpha1, linewidth=lw1, label=series_name_1)
plt.plot(x2, y2, style2, alpha=alpha2, linewidth=lw2, label=series_name_2)

# ---------------------------------------------------------
# === DODAWANIE PUNKTÓW (WAYPOINTS) ===
# ---------------------------------------------------------

# 1. Punkt startowy łodzi (W0) - pobrany z pierwszego pomiaru w pliku
start_lon = df1['lon_fix'].iloc[0]
start_lat = df1['lat_fix'].iloc[0]

plt.plot(start_lon, start_lat, 'k*', markersize=14, markeredgecolor='white', markeredgewidth=1, zorder=5)
plt.text(start_lon, start_lat, '  W0', fontsize=12, fontweight='bold', color='black', ha='left', va='bottom')

# 2. Checkpointy z KML (W1, W2, W3)
# Dane przepisane z Twojego KML: <coordinates>lon,lat</coordinates>
waypoints_kml = [
    (150.674264, -33.721192, "W1"),  # First
    (150.675368, -33.721365, "W2"),  # Second
    (150.675245, -33.722538, "W3")   # Third
    # Fourth to to samo co First, więc nie rysujemy osobno
]

for wx, wy, wlabel in waypoints_kml:
    # Rysujemy czarną gwiazdkę z białą obwódką dla lepszej widoczności
    plt.plot(wx, wy, 'k*', markersize=14, markeredgecolor='white', markeredgewidth=1, zorder=5)
    plt.text(wx, wy, f'  {wlabel}', fontsize=12, fontweight='bold', color='black', ha='left', va='center')

# ---------------------------------------------------------

plt.xlabel("Długość geograficzna")
plt.ylabel("Szerokość geograficzna")
plt.title(plot_title)
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

# --- Wykresy Błędów (Zależne od trybu) ---

if mode == "COMPARE":
    # ---------------------------------------------
    # Wykres 2: Porównanie Błędu Szerokości (Lat)
    # ---------------------------------------------
    
    plt.figure(figsize=(12, 6))
    plt.plot(time_series, err_lat_1, color='blue', linestyle="None", marker='.', alpha=0.7, label=f'{series_name_1}')
    plt.plot(time_series_2, err_lat_2, color='red', linestyle="None", marker='.', alpha=0.7, label=f'{series_name_2}')
    
    plt.xlabel("Czas trwania eksperymentu [s]")
    plt.ylabel("Błąd Latitude [deg]")
    plt.title(f"Porównanie błędu: Szerokość Geograficzna (Latitude)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # ---------------------------------------------
    # Wykres 3: Porównanie Błędu Długości (Lon)
    # ---------------------------------------------
    
    plt.figure(figsize=(12, 6))
    plt.plot(time_series, err_lon_1, color='blue', linestyle="None", marker='.', alpha=0.7, label=f'{series_name_1}')
    plt.plot(time_series_2, err_lon_2, color='red', linestyle="None", marker='.', alpha=0.7, label=f'{series_name_2}')
    
    plt.xlabel("Czas trwania eksperymentu [s]")
    plt.ylabel("Błąd Longitude [deg]")
    plt.title(f"Porównanie błędu: Długość Geograficzna (Longitude)")
    plt.legend()
    plt.grid(True)
    plt.show()

else:
    # ---------------------------------------------
    # Tryb SINGLE: Jeden wykres ze wszystkim
    # ---------------------------------------------
    
    plt.figure(figsize=(12, 6))
    plt.plot(time_series, err_lat_1, color='blue', linestyle='-', alpha=0.6, label='Lat Error')
    plt.plot(time_series, err_lon_1, color='green', linestyle='-', alpha=0.6, label='Lon Error')
    
    plt.xlabel("Czas trwania eksperymentu [s]")
    plt.ylabel("Błąd [deg]")
    plt.title(f"Analiza błędów w czasie: {series_name_1}")
    plt.legend()
    plt.grid(True)
    plt.show()

