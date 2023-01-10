from vosk import Model, KaldiRecognizer
import pyaudio 
modal = Model(r'voskmodal')
recognizer = KaldiRecognizer(modal, 16000)

cap = pyaudio.PyAudio()
stream = cap.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())