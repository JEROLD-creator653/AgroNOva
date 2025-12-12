# 🌾 AgroNova
### Offline Voice-Enabled AI Assistant for Farmers

AgroNova is a fully offline conversational assistant designed to support farmers with hands-free interactions. It uses **Vosk** for offline speech-to-text, **FLAN-T5** for offline text generation, and **pyttsx3** for offline text-to-speech — ensuring zero internet dependency and high reliability in rural environments.

---

## 🚀 Features
- 🎙️ Offline Voice Recognition using Vosk  
- 🤖 AI Responses powered by FLAN-T5-Small  
- 🔊 Offline Text-to-Speech via pyttsx3  
- 🎤 Automatic Microphone Detection  
- 🛜 100% Offline Operation  

---

## 📂 Project Structure
```

AgroNova/
└── AgroNova.py

````

---

## 🧠 Tech Stack
| Component | Technology |
|----------|------------|
| Speech-to-Text | Vosk (vosk-model-small-en-us-0.15) |
| Text Generation | Google FLAN-T5 Small |
| Text-to-Speech | pyttsx3 |
| Audio Input | PyAudio |
| AI Pipeline | HuggingFace Transformers |

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/JEROLD-creator653/AgroNova
cd AgroNova
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Vosk Offline Model

Download the STT model from:
[https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)

Recommended:

```
vosk-model-small-en-us-0.15
```

Extract it and update the path inside `AgroNova.py`:

```python
model_path = r"PATH_TO_DOWNLOADED_VOSK_MODEL"
```

---

## ▶️ How to Use AgroNova

Run the assistant:

```bash
python AgroNova.py
```

You will see:

```
=== AgroNova is now online ===
Say 'exit' or 'quit' to stop.
```

Then simply **speak**.
AgroNova will:

1. Listen to your microphone input
2. Convert your speech → text
3. Generate an AI response
4. Speak it aloud through TTS

---

## 📌 Example Interaction

```
🎙️ Speak now...
👨‍🌾 Farmer: what crops grow best in winter?
🤖 AgroNova: Cool-season crops like spinach, peas, and cabbage thrive well in winter.
```

---

## 🔧 How It Works Internally

### 1. Voice Recognition

PyAudio streams microphone audio → Vosk model → recognized text.

### 2. AI Text Generation

The FLAN-T5 model generates a response:

```python
reply = chatbot(query, max_length=60, do_sample=True)
```

### 3. Text-to-Speech

pyttsx3 speaks the generated response back to the user.

---

## ❗ Limitations

* FLAN-T5-Small is lightweight; complex agricultural advice may require model fine-tuning
* Auto microphone selection may not work perfectly on all systems

---

## 🤝 Contributing

Pull requests and suggestions are welcome!

---
