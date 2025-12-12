import pyttsx3
from transformers import pipeline
from vosk import Model, KaldiRecognizer
import pyaudio
import json
import time

# Load offline AI model
chatbot = pipeline("text2text-generation", model="google/flan-t5-small", local_files_only=True)

# Load Vosk model
model_path = r"D:\AgroNova\vosk-model-small-en-us-0.15"
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

# Offline TTS engine
engine = pyttsx3.init()

def select_microphone():
    p = pyaudio.PyAudio()
    print("Available microphones:")
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(i, info['name'], "Max Input Channels:", info['maxInputChannels'])
        if info['maxInputChannels'] >= 1:
            print(f"-> Selecting microphone: {info['name']} (Index {i})")
            p.terminate()
            return i
    p.terminate()
    raise Exception("No suitable microphone found!")

MIC_INDEX = select_microphone()

def listen(timeout=15):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    input_device_index=MIC_INDEX,
                    frames_per_buffer=8000)
    stream.start_stream()

    print("🎙️ Speak now...")
    text = ""
    start_time = time.time()

    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "")
            break
        else:
            partial = json.loads(recognizer.PartialResult())
            # optional: print partial recognition
            # print("Partial:", partial.get("partial", ""))

        if time.time() - start_time > timeout:
            break

    stream.stop_stream()
    stream.close()
    p.terminate()
    return text.strip()

def respond(query):
    print(f"👨‍🌾 Farmer: {query}")
    if query == "":
        reply = "I could not understand."
    else:
        reply = chatbot(query, max_length=60, do_sample=True)[0]['generated_text']
    print(f"🤖 AgroNova: {reply}")
    engine.say(reply)
    engine.runAndWait()

print("=== AgroNova is now online ===")
print("Say 'exit' or 'quit' to stop.")

while True:
    query = listen(timeout=15)
    if query.lower() in ["exit", "quit"]:
        print("Shutting Down AgroNova...... Goodbye!")
        break
    respond(query)
