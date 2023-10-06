import random
import numpy as np
from scipy.io import wavfile
from scipy.signal import resample
import subprocess
import argparse
import threading
import time

def read_wav(file_path):
    rate, data = wavfile.read(file_path)
    return rate, data

def play_audio(file_path):
    subprocess.run(["aplay", "-r", "44100", "-f", "S16_LE", "-c", "2", "--buffer-size=400000", file_path])

def generate_glitch_music(input_data):
    fragments_per_second = 14  # Numero di frammenti al secondo
    pitch_shift = 0.5  # Fattore di cambio di tonalità
    duration = 20  # Durata del file di output in secondi per ciascun loop
    loop_duration = 5  # Durata totale del loop in secondi

    input_data_length = len(input_data)
    frame_size = input_data_length // fragments_per_second

    iteration = 1

    while True:
        channel1_fragments = []
        channel2_fragments = []

        for _ in range(fragments_per_second * duration):
            start = random.randint(0, input_data_length - frame_size)
            end = start + frame_size
            fragment = input_data[start:end]

            # Effetto pitch shift
            if pitch_shift != 1.0:
                fragment = resample(fragment, int(len(fragment) * pitch_shift))

            # Divide il frammento in chunk di lunghezze diverse
            num_chunks = random.randint(1, 5)  # Numero casuale di chunks
            chunk_lengths = np.linspace(0, len(fragment), num_chunks + 1, dtype=int)
            chunks = [fragment[chunk_lengths[i]:chunk_lengths[i + 1]] for i in range(num_chunks)]

            # Ricombina casualmente i chunks
            random.shuffle(chunks)

            # Aggiungi i chunks ai canali stereo
            channel1_fragments.extend(chunks[random.randint(0, num_chunks - 1)])
            channel2_fragments.extend(chunks[random.randint(0, num_chunks - 1)])

        # Crea il file stereo .wav in memoria
        stereo_data = np.array(list(zip(channel1_fragments, channel2_fragments)), dtype=np.int16)
        output_file = f"{iteration}.wav"
        wavfile.write(output_file, input_data_length, stereo_data)

        # Avvia i processi "aplay" in thread separati
        threading.Thread(target=play_audio, args=(output_file,)).start()

        # Aggiorna input_data con il nuovo stereo_data per il prossimo ciclo
        input_data = stereo_data

        # Aspetta metà della durata del file audio prima di passare al successivo
        time.sleep(duration / 2)

        # Incrementa il contatore per il nome del file di output
        iteration += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Genera un nuovo file stereo .wav con effetto di time splicing, pitch shift e ritmi glitchy.')
    parser.add_argument('input_file', help='Il file .wav di input')
    args = parser.parse_args()

    # Leggi il file di input una sola volta e conserva i dati audio in memoria
    _, input_data = read_wav(args.input_file)

    # Avvia il processo di generazione glitch music utilizzando l'input e il nome del file di output numerato
    generate_glitch_music(input_data)
