import pyaudio
import json
from vosk import Model, KaldiRecognizer

# Path to your Vosk model
model_path = r"D:\AgroNova\vosk-model-small-en-us-0.15"
model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()

# List all microphones
print("Available microphones:")
for i in range(p.get_device_count()):
    print(i, p.get_device_info_by_index(i))

# Open default mic, change input_device_index if needed
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
                input=True, frames_per_buffer=8000)
stream.start_stream()

print("🎙️ Speak something for 10 seconds...")

for _ in range(50):  # 50*0.25s = ~12 seconds
    data = stream.read(4000, exception_on_overflow=False)
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        print("Recognized:", result.get("text", ""))
    else:
        partial = json.loads(rec.PartialResult())
        print("Partial:", partial.get("partial", ""))

stream.stop_stream()
stream.close()
p.terminate()
