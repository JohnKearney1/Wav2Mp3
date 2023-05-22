import os
from pydub import AudioSegment

# Directory paths
input_dir = 'files'
output_dir = 'converted'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Convert each WAV file to MP3
for file_name in os.listdir(input_dir):
    if file_name.endswith('.wav'):
        # Load WAV file
        wav_path = os.path.join(input_dir, file_name)
        audio = AudioSegment.from_wav(wav_path)

        # Construct output file path
        mp3_file_name = os.path.splitext(file_name)[0] + '.mp3'
        mp3_path = os.path.join(output_dir, mp3_file_name)

        # Export as MP3
        audio.export(mp3_path, format='mp3')

        print(f"Converted '{file_name}' to '{mp3_file_name}'")

print("Conversion complete!")
