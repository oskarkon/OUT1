import pandas as pd
import requests
from io import StringIO

# URL do strony z danymi
url = "https://stooq.pl/q/o/?s=wig20&v=2&i=1"

# Wysłanie żądania GET i pobranie zawartości strony
response = requests.get(url)

# Sprawdzenie, czy żądanie zakończyło się sukcesem (kod 200)
if response.status_code == 200:
    # Przetworzenie danych do formatu DataFrame
    data = pd.read_csv(StringIO(response.text), sep=",")

    # Wyświetlenie kilku pierwszych wierszy DataFrame
    print(data.head())
else:
    print("Nie udało się pobrać danych. Kod odpowiedzi:", response.status_code)
data