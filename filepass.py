import os
import shutil

# Directorio de origen, directorio de destino, año mínimo y año máximo
path = "C:/Users/ASUS/OneDrive/Escritorio/prueba/"
moveTo = "C:/Users/ASUS/OneDrive/Escritorio/FilePass/new_data/"
minYear = 2021
maxYear = 2024

# Crear directorios de destino
for year in range(minYear, maxYear+1):
    for month in range(1, 13):
        os.makedirs(os.path.join(moveTo, str(year), str(month)), exist_ok=True)

# Listar archivos en el directorio de origen
files = os.listdir(path)

# Mover archivos al directorio de destino
for file_name in files:

    if file_name.startswith('IMG') or file_name.startswith('VID'):
        data = file_name.split('_')
        year = int(data[1][0:4])
        month = int(data[1][4:6])
        print(f'{year} - {month}')
        destination_dir = os.path.join(moveTo, str(year), str(month))
        destination_path = os.path.join(destination_dir, file_name)

        print("Moving file:", file_name)
        print("From:", os.path.join(path, file_name))
        print("To:", destination_path)
        print('\n\n\n')

        shutil.move(os.path.join(path, file_name), destination_path)