import numpy as np
import sounddevice as sd

def play_tone(frequency, duration=1, sample_rate=44100):
    # Generate an array of time values
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # Generate the audio signal (sine wave)
    tone = np.sin(2 * np.pi * frequency * t)
    # Play the audio signal
    sd.play(tone, sample_rate)
    sd.wait()  # Wait until the sound has finished playing

if __name__ == "__main__":
    for i in range(2200):
        play_tone(i)
