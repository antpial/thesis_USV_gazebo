import rclpy
from rclpy.serialization import deserialize_message
# ZMIANA 1: Dodano import StorageFilter
from rosbag2_py import SequentialReader, StorageOptions, ConverterOptions, StorageFilter
from msg_interfaces.msg import InternalState
import matplotlib.pyplot as plt
import sys
import os

def get_data_from_bag(bag_path, topic_name):
    print(f"--- Analiza baga: {bag_path} ---")
    
    # Sprawdzenie czy ścieżka istnieje (prosta walidacja)
    if not os.path.exists(bag_path):
        # Sprawdzamy, czy może użytkownik podał ścieżkę względną, a bag jest obok
        if os.path.exists(os.path.join(os.getcwd(), bag_path)):
            bag_path = os.path.join(os.getcwd(), bag_path)
        else:
            print(f"BŁĄD: Nie znaleziono ścieżki: {bag_path}")
            return [], []

    data_t = []
    data_val = []

    # Wykrywanie formatu (mcap/sqlite3)
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
        return [], []

    # Sprawdzenie tematów
    topics = [t.name for t in reader.get_all_topics_and_types()]
    if topic_name not in topics:
        print(f"BŁĄD: Temat '{topic_name}' nie istnieje. Dostępne: {topics}")
        return [], []

    # ZMIANA 2: Użycie obiektu StorageFilter zamiast słownika/listy
    storage_filter = StorageFilter(topics=[topic_name])
    reader.set_filter(storage_filter)

    start_time = None
    msg_count = 0

    while reader.has_next():
        (topic, data, t_stamp) = reader.read_next()
        msg_count += 1
        
        try:
            msg = deserialize_message(data, InternalState)
            
            # Pobieramy float z pola 'e'
            val = msg.e 
            
            if start_time is None:
                start_time = t_stamp
            
            rel_time = (t_stamp - start_time) / 1e9 

            data_t.append(rel_time)
            data_val.append(val)

        except Exception as e:
            print(f"Błąd deserializacji w wiadomości #{msg_count}: {e}")
            break

    print(f"Pobrano {len(data_val)} próbek.")
    return data_t, data_val

def plot_comparison(bag_files, topic_name):
    plt.figure(figsize=(12, 6))
    
    has_data = False
    for bag in bag_files:
        t, y = get_data_from_bag(bag, topic_name)
        
        if len(t) > 0:
            plt.plot(t, y, label=f'{bag}', linewidth=2)
            has_data = True
        else:
            print(f"OSTRZEŻENIE: Pusty zbiór danych dla {bag}")

    if has_data:
        plt.title(f"Porównanie wartości nastaw członu P regulatora wewnętrzego")
        plt.xlabel("Czas od startu nagrania [s]")
        plt.ylabel("Wartość błędu w stopniach")
        plt.legend()
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
        plt.show()
        plt.minorticks_on()
    else:
        print("Nie udało się wygenerować wykresu (brak danych).")

def main():
    # Upewnij się, że ścieżki do bagów są poprawne względem miejsca uruchomienia (~)
    bags = [
        # "rosbag_los_p_07", 
        # "rosbag_los_p_06",
        # "rosbag_los_p_05",
        # "rosbag_los_p_04",
        # "rosbag_los_p_03",
        # "los_p_02",
        "rosbag_los_p_20",
        "rosbag_los_p_10",
        "rosbag_los_p_5",
        "rosbag_los_p_1",

    ]
    
    topic = "/usv/stan" 

    plot_comparison(bags, topic)

if __name__ == "__main__":
    main()