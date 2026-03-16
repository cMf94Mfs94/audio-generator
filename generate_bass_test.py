import numpy as np
from pydub import AudioSegment
import pyttsx3
import os

sample_rate = 44100
frequencies = list(range(40, 101, 5))  # 40, 45, ..., 100

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume

full_audio = AudioSegment.empty()

for freq in frequencies:
    # Announcement
    text = f"{freq} Hertz"
    temp_wav = f"temp_{freq}.wav"
    engine.save_to_file(text, temp_wav)
    engine.runAndWait()
    
    ann_audio = AudioSegment.from_wav(temp_wav)
    
    # Sine wave for 7 seconds
    duration = 7
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    sine_wave = 0.5 * np.sin(2 * np.pi * freq * t)  # 0.5 to avoid clipping
    sine_wave = (sine_wave * 32767).astype(np.int16)
    
    sin_audio = AudioSegment(
        sine_wave.tobytes(),
        frame_rate=sample_rate,
        sample_width=2,
        channels=1
    )
    
    # Concatenate announcement and sine wave
    segment = ann_audio + sin_audio
    full_audio += segment
    
    # Clean up temp file
    os.remove(temp_wav)

# Export the full audio
full_audio.export('bass_test.wav', format='wav')

print("bass_test.wav generated successfully!")