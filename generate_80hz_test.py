import numpy as np
from pydub import AudioSegment

# Parameters
frequency = 80  # 80 Hz
duration = 30  # 30 seconds
sample_rate = 44100  # Standard sample rate
amplitude = 0.5  # 0.5 to avoid clipping

# Generate sine wave
t = np.linspace(0, duration, int(duration * sample_rate), False)
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)

# Convert to 16-bit PCM
sine_wave = (sine_wave * 32767).astype(np.int16)

# Create AudioSegment
audio = AudioSegment(
    sine_wave.tobytes(),
    frame_rate=sample_rate,
    sample_width=2,
    channels=1
)

# Export to WAV
audio.export('80hz_test.wav', format='wav')

print("80hz_test.wav generated successfully!")