import pandas as pd
import os
from tempfile import NamedTemporaryFile


def open_dataframe_in_excel(dataframe):
    """
    Otwiera DataFrame w Excelu bez zapisywania na dysku, używając pliku tymczasowego.

    :param dataframe: DataFrame do otwarcia w Excelu
    """

    with NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp_file:
        temp_filename = tmp_file.name

        dataframe.to_excel(temp_filename, index=False)

    # Otwórz plik tymczasowy w Excelu
    os.startfile(temp_filename)


# Przykład użycia
data = {'Imię': ['Jan', 'Anna', 'Piotr'], 'Wiek': [28, 24, 35]}
df = pd.DataFrame(data)
open_dataframe_in_excel(df)
