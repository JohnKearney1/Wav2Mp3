import os
from pydub import AudioSegment
from tqdm import tqdm  # Import tqdm for the loading bar

# Directory paths
input_dir = 'files'
output_dir = 'converted'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get the number of WAV files
wav_files = [file_name for file_name in os.listdir(input_dir) if file_name.endswith('.wav')]
num_files = len(wav_files)

# Convert each WAV file to MP3 with a loading bar
converted_files = 0
for file_name in tqdm(wav_files, desc="Converting files", unit="file"):
    # Load WAV file
    wav_path = os.path.join(input_dir, file_name)
    audio = AudioSegment.from_wav(wav_path)

    # Construct output file path
    mp3_file_name = os.path.splitext(file_name)[0] + '.mp3'
    mp3_path = os.path.join(output_dir, mp3_file_name)

    # Export as MP3
    audio.export(mp3_path, format='mp3')

    # Get file sizes
    before_size = os.path.getsize(wav_path) / (1024 * 1024)  # Convert to MB
    after_size = os.path.getsize(mp3_path) / (1024 * 1024)  # Convert to MB

    print(f"Converted '{file_name}' to '{mp3_file_name} [{before_size:.2f}MB] -> [{after_size:.2f}MB]'")

    converted_files += 1

print(f"Conversion complete: {converted_files} file(s) converted.")
