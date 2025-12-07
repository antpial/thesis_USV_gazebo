std_msgs/Header header

int32 id

# --- Sterowanie ---
float32 v           # przepustnica
float32 d           # kierownica (ster)

# --- Błędy sterowania ---
float32 e           # blad kursu (heading error)
float32 de          # cross track error (odleglosc od linii)

# --- Nawigacja GPS (Musi byc float64!) ---
float64 given_position_lat    # cel lodzi lat
float64 given_position_lon    # cel lodzi lon
float64 starting_position_lat # start lodzi lat
float64 starting_position_lon # start lodzi lon

# --- Wyjścia silników ---
float32 left_thrust   # ciag na lewym silniku
float32 right_thrust  # ciag na prawym silniku

# --- Stan ---
float32 given_azimuth    # azymut do ktorego zmierza lodka
float32 current_azimuth  # chwilowy azymut lodzi
float32 distance         # dystans do punku docelowego

# --- Diagnostyka PID/LOS ---
float32 p_los      # wartość wyjściowa członu P
float32 i_los      # wartosc wyjsciowa czlonu I
float32 kp_los     # nastawa Kp
float32 ki_los     # nastawa Ki