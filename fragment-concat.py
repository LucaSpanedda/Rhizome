import random

# Leggi i valori dal file .txt in una lista
with open('input.txt', 'r') as file:
    values = [float(line.strip()) for line in file]

# Specifica il numero di frammenti desiderato
num_fragments = 20

# Calcola la dimensione di ciascun frammento
fragment_size = len(values) // num_fragments

# Dividi la lista in frammenti di uguale dimensione
fragments = [values[i:i + fragment_size] for i in range(0, len(values), fragment_size)]

# Mescola casualmente i frammenti
random.shuffle(fragments)

# Concatena i frammenti mescolati
new_values = [value for fragment in fragments for value in fragment]

# Scrivi la nuova lista in un file .txt
with open('output.txt', 'w') as file:
    for value in new_values:
        file.write(f'{value:.8f}\n')
print("File di output creato con successo!")