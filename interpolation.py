# Function to perform linear interpolation between two values
def interpolate(value1, value2):
    return (value1 + value2) / 2.0

# Leggi i valori dal file .txt in una lista
with open('input.txt', 'r') as file:
    values = [float(line.strip()) for line in file]

# Interpolate values between each pair of consecutive points
interpolated_values = []
for i in range(len(values) - 1):
    interpolated_values.append(values[i])
    interpolated_values.append(interpolate(values[i], values[i + 1]))
interpolated_values.append(values[-1])  # Aggiungi l'ultimo valore

# Scrivi la nuova lista interpolata in un file .txt
with open('interpolated_output.txt', 'w') as file:
    for value in interpolated_values:
        file.write(f'{value:.8f}\n')
print("File interpolato di output creato con successo!")