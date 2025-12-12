import rclpy
from rclpy.serialization import deserialize_message
from rosbag2_py import SequentialReader, StorageOptions, ConverterOptions, StorageFilter
from msg_interfaces.msg import InternalState
import matplotlib.pyplot as plt
import sys
import os

def get_data_from_bag(bag_path, topic_name):
    print(f"--- Analiza baga: {bag_path} ---")
    
    if not os.path.exists(bag_path):
        if os.path.exists(os.path.join(os.getcwd(), bag_path)):
            bag_path = os.path.join(os.getcwd(), bag_path)
        else:
            print(f"BŁĄD: Nie znaleziono ścieżki: {bag_path}")
            return [], [], []

    data_t = []
    data_val_e = []
    data_val_d = []

    storage_id = 'mcap'
    if os.path.isdir(bag_path):
        for f in os.listdir(bag_path):
            if f.endswith('.db3'):
                storage_id = 'sqlite3'
                break
    
    try:
        storage_options = StorageOptions(uri=bag_path, storage_id=storage_id)
        converter_options = ConverterOptions('', '')
        reader = SequentialReader()
        reader.open(storage_options, converter_options)
    except Exception as e:
        print(f"BŁĄD otwierania: {e}")
        return [], [], []

    topics = [t.name for t in reader.get_all_topics_and_types()]
    if topic_name not in topics:
        print(f"BŁĄD: Temat '{topic_name}' nie istnieje. Dostępne: {topics}")
        return [], [], []

    storage_filter = StorageFilter(topics=[topic_name])
    reader.set_filter(storage_filter)

    start_time = None
    msg_count = 0
    
    # --- KONFIGURACJA TRIGGERA ---
    TRIGGER_VALUE = -20.0

    while reader.has_next():
        (topic, data, t_stamp) = reader.read_next()
        msg_count += 1
        
        try:
            msg = deserialize_message(data, InternalState)
            
            val_e = msg.de 
            val_d = msg.d

            # --- LOGIKA TRIGGERA ---
            if start_time is None:
                if val_e >= TRIGGER_VALUE and val_e != 0.0 and val_e < 60.0:
                    start_time = t_stamp
                    print(f"  -> Wyzwolono start przy wartości e: {val_e:.4f}")
                else:
                    continue

            rel_time = (t_stamp - start_time) / 1e9 
            
            data_t.append(rel_time)
            data_val_e.append(val_e)
            data_val_d.append(val_d)

        except Exception as e:
            print(f"Błąd deserializacji w wiadomości #{msg_count}: {e}")
            break

    print(f"Pobrano {len(data_val_e)} próbek.")
    return data_t, data_val_e, data_val_d

def plot_comparison(bag_dict, topic_name):
    # Tworzymy 2 wykresy jeden pod drugim
    # fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    fig, ax1 = plt.subplots(1, 1, figsize=(12, 5))
    
    has_data = False
    
    # ZMIANA: Iterujemy po elementach słownika (ścieżka, nazwa_etykiety)
    for bag_path, label_name in bag_dict.items():
        t, y_e, y_d = get_data_from_bag(bag_path, topic_name)
        
        if len(t) > 0:
            # Używamy label_name zamiast nazwy pliku
            ax1.plot(t, y_e, label=label_name, linewidth=2)
            # ax2.plot(t, y_d, label=label_name, linewidth=2)
            has_data = True
        else:
            print(f"OSTRZEŻENIE: Brak danych dla {bag_path}")

    if has_data:
        # --- Konfiguracja WYKRESU GÓRNEGO (msg.e) ---
        ax1.set_title(f"Odpowiedź układu na regulator PID i ILOS")
        ax1.set_ylabel("Błąd [m]")
        ax1.legend(loc='upper right')
        ax1.grid(which='major', linestyle='-', linewidth='0.8', color='black', alpha=0.6)
        ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='gray', alpha=0.5)
        ax1.minorticks_on()
        ax1.axhline(0, color='black', linewidth=1.5, linestyle='--')

        # # --- Konfiguracja WYKRESU DOLNEGO (msg.d) ---
        # ax2.set_title(f"Wartość sterowania (d) dla różnych nastaw.")
        # ax2.set_ylabel("Wartość d")
        # ax2.set_xlabel("Czas od wyzwolenia [s]")
        # ax2.legend(loc='upper right')
        # ax2.grid(which='major', linestyle='-', linewidth='0.8', color='black', alpha=0.6)
        # ax2.grid(which='minor', linestyle=':', linewidth='0.5', color='gray', alpha=0.5)
        # ax2.minorticks_on()
        # ax2.axhline(0, color='black', linewidth=1.0, linestyle='--')

        plt.tight_layout()
        plt.show()
    else:
        print("Nie udało się wygenerować wykresu.")

def main():
    # ZMIANA: Słownik zamiast listy
    # Klucz = Nazwa folderu/baga
    # Wartość = To co ma się wyświetlić w legendzie
    bags_config = {
        # "rosbag_los_p_1": "Kp = 0.10",
        # "rosbag_los_p_07": "Kp = 0.07",
        # "rosbag_los_p_05": "Kp = 0.05",
        # "rosbag_los_p_03": "Kp = 0.030",
        # "rosbag_los_p_025": "Kd = 0.0000",
        # "rosbag_los_p_02": "Kp = 0.020",
        # Możesz tu dodać dowolne inne:
        # "rosbag_los_p_03": "Kp = 0.3",
        # "rosbag_los_Kd_0_0025": "Kd = 0.0025",
        # "rosbag_los_Kd_0_0050": "Kd = 0.0050",
        # "rosbag_los_Kd_0_025": "Kd = 0.025",
        # "rosbag_los_Kd_0_0": "Kd = 0.0",
        # "rosbag_los_Kd_0_5": "Kp_los = 0.0",
        # "rosbag_los_Kd_1_0": "Kd = 1.0",
        # "rosbag_los_Kp_los_10": "Kp = 10.0",
        # "rosbag_los_Kp_los_9_5": "Kp = 9.5",
        # "rosbag_los_Kp_los_9": "Kp = 9.0",
        # "rosbag_los_Kp_los_8": "Kp_los = 8.0",
        # "rosbag_los_ZNv1": "Kp = 4.275, Ki = 0.214 (Z-N)",
        # "rosbag_los_Ki_0_321": "Kp_los = 4.275, Ki_los = 0.321",
        # "rosbag_los_Ki_0_428": "Kp_los = 4.275, Ki_los = 0.428",
        # "rosbag_los_Kd_10": "Kp_los = 4.275, Ki_los = 0.428, Kd_los = 10.0",
        # "rosbag_los_Kd_10_ki_0_856": "Kp_los = 4.275, Ki_los = 0.856, Kd_los = 10.0",
        # "rosbag_los_Kp_8_Ki_214": "Kp_los = 8.0, Ki_los = 0.214, Kd_los = 10.0",
        # "rosbag_los_Kp_8_Ki_428": "Kp_los = 8.0, Ki_los = 0.428, Kd_los = 10.0",
        # "rosbag_los_Kp_8_Ki_856": "Kp_los = 8.0, Ki_los = 0.856, Kd_los = 10.0",
        # "rosbag_los_Kp_8_Ki_856_Kd_20": "Kp_los = 8.0, Ki_los = 0.856, Kd_los = 20.0",
        # "rosbag_los_Kp_8_Ki_856_Kd_30": "Kp_los = 8.0, Ki_los = 0.856, Kd_los = 30.0",
        # "rosbag_los_Kp_8_Ki_1_Kd_20": "Kp_los = 8.0, Ki_los = 1.0, Kd_los = 20.0",
        # "rosbag_los_Kp_9_Ki_856_Kd_20": "Kp = 9.0, Ki = 0.856, Kd = 20.0",
        # "rosbag_los_Kp_4_275_Ki_0_856_Kd_20": "Kp_los = 4.275, Ki_los = 0.856, Kd_los = 20.0",
        "rosbag_los_Kp_9_Ki_0_856_Kd_25": "PID: Kp = 9.0, Ki = 0.856, Kd = 25.0",
        # "rosbag_los_Kp_9_Ki_0_856_Kd_30": "Kp = 9.0, Ki = 0.856, Kd = 30.0",
        # "rosbag_delta_0_4": "Δ = 4.0 m",
        # "rosbag_delta_10": "Δ = 10.0 m",
        # "rosbag_delta_5": "Δ = 5.0 m",
        # "rosbag_delta_6": "Δ = 6.0 m",
        # "rosbag_delta_7": "Δ = 7.0 m",
        # "rosbag_delta_8": "Δ = 8.0 m",
        # "rosbag_delta_9_8": "Δ = 9.8 m (2xL), σ = 0.0",
        # "rosbag_delta_12_25": "Δ = 12.25 m (2.5xL), σ = 0.0",
        # "rosbag_delta_12_25_sigma_0_2": "Δ = 12.25 m, σ = 0.2",
        # "rosbag_delta_12_25_sigma_0_5": "Δ = 12.25 m, σ = 0.5",
        # "rosbag_delta_12_25_sigma_0_7": "Δ = 12.25 m, σ = 0.7",
        "rosbag_delta_12_25_sigma_0_85": "ILOS: Δ = 12.25 m, σ = 0.85",
        # "rosbag_delta_12_25_sigma_1_0": "Δ = 12.25 m, σ = 1.0",
        # "rosbag_delta_14_7": "Δ = 14.7 m (3xL), σ = 0.0",
        # "rosbag_delta_8_sigma_0_2": "Δ = 8.0 m, σ = 0.2",
        # "rosbag_delta_8_sigma_0_3": "Δ = 8.0 m, σ = 0.3",
        # "rosbag_delta_8_sigma_0_4": "Δ = 8.0 m, σ = 0.4",
        # "rosbag_delta_8_sigma_0_5": "Δ = 8.0 m, σ = 0.5",

    }
    
    topic = "/usv/stan" 

    plot_comparison(bags_config, topic)

if __name__ == "__main__":
    main()