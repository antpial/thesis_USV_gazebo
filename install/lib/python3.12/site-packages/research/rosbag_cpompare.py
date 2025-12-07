import rclpy
from rclpy.serialization import deserialize_message
from rosbag2_py import SequentialReader, StorageOptions, ConverterOptions
from msg_interfaces.msg import InternalState
import matplotlib.pyplot as plt
import sys

def get_data_from_bag(bag_path, topic_name):
    """
    Czyta baga i zwraca listy: czas_relatywny, x, y.
    Czas jest liczony od 0.0 (pierwsza wiadomość = 0s).
    """
    data_t = []
    data_x = []
    data_y = []

    storage_options = StorageOptions(uri=bag_path, storage_id='mcap') # lub 'sqlite3'
    converter_options = ConverterOptions('', '')
    reader = SequentialReader()
    reader.open(storage_options, converter_options)

    storage_filter = [topic_name]
    reader.set_filter(topics=storage_filter)

    start_time = None
    start_pos_x = None
    start_pos_y = None

    while reader.has_next():
        (topic, data, t_stamp) = reader.read_next()
        
        # Deserializacja (tutaj Odometria - kluczowe dla USV)
        msg = deserialize_message(data, InternalState)
        msg = msg.e

        # 1. Normalizacja Czasu (Start = 0.0s)
        if start_time is None:
            start_time = t_stamp
        
        rel_time = (t_stamp - start_time) / 1e9  # Konwersja nanosekund na sekundy

        # Pobranie danych (np. pozycja)
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        # 2. Opcjonalnie: Normalizacja Pozycji (Start = 0,0)
        # Jeśli chcesz porównać kształt trasy, a nie bezwzględne GPS
        if start_pos_x is None:
            start_pos_x = x
            start_pos_y = y
        
        # Odejmujemy pozycję startową (odkomentuj jeśli potrzebujesz absolutnych danych)
        x -= start_pos_x 
        y -= start_pos_y

        data_t.append(rel_time)
        data_x.append(x)
        data_y.append(y)

    return data_t, data_x, data_y

def plot_comparison(bag_files, topic_name):
    plt.figure(figsize=(10, 6))
    
    # Dla każdego baga w liście
    for bag in bag_files:
        try:
            print(f"Przetwarzanie: {bag}...")
            t, x, y = get_data_from_bag(bag, topic_name)
            
            # WYKRES 1: Trajektoria XY (Świetne do Path Following)
            plt.plot(x, y, label=f'Trajektoria: {bag}', linewidth=2)
            
            # ALTERNATYWA: Jeśli wolisz wykres wartości od czasu (np. Błąd X od czasu)
            # plt.plot(t, y, label=f'Błąd Y: {bag}') 
            
        except Exception as e:
            print(f"Błąd przy czytaniu {bag}: {e}")

    plt.title(f"Porównanie danych z tematu: {topic_name}")
    plt.xlabel("Pozycja X (znormalizowana) [m]")
    plt.ylabel("Pozycja Y (znormalizowana) [m]")
    # plt.xlabel("Czas od startu [s]") # Dla wykresu czasowego
    plt.legend()
    plt.grid(True)
    plt.axis('equal') # Ważne dla map! Żeby skala X i Y była taka sama
    plt.show()

if __name__ == "__main__":
    # KONFIGURACJA
    # 1. Lista folderów z bagami do porównania
    bags = [
        "rosbag_los_p_07",       # Ścieżka do baga 1
        "rosbag_los_p_06"    # Ścieżka do baga 2
    ]
    
    # 2. Temat do analizy (musi być typu Odometry, chyba że zmienisz importy)
    topic = "/usv/stan" 

    plot_comparison(bags, topic)