
# 🤖 RoboSpeaker 1.1.0

**RoboSpeaker** is a simple Python-based text-to-speech (TTS) tool using the `pyttsx3` library. Just type anything and hear your computer speak it back!

---

## 🎯 Features

* Converts text input to speech using your system's default voice
* Lightweight and easy to use
* Works offline
* Great for basic TTS projects or voice-based experiments

---

## 🔧 Requirements

* Python 3.x
* `pyttsx3` library

You can install the required package using pip:

```bash
pip install pyttsx3
```

---

## 🚀 Getting Started

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/robospeaker.git
cd robospeaker
```

### 2. Run the script:

```bash
python robospeaker.py
```

### 3. Type your message:

```text
Enter your text here: Hello, world!
```

The program will speak your message aloud.

---

## 🧠 How It Works

Here's a simplified version of the core code:

```python
import pyttsx3

tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id)

print("Welcome to RoboSpeaker 1.1.0")
tts.say("Welcome to RoboSpeaker 1.1.0, I am an artificial voice, and say whatever you type!")
tts.runAndWait()

text = input("Enter your text here: ")
tts.say(text)
tts.runAndWait()
```

---

## 🛠️ Customization

You can change the voice (e.g., to a female voice) by modifying the index in:

```python
tts.setProperty('voice', voices[1].id)
```

You can also adjust speech rate and volume:

```python
tts.setProperty('rate', 150)  # Default is 200
tts.setProperty('volume', 0.9)  # Volume: 0.0 to 1.0
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📣 Acknowledgements

Built using the awesome [pyttsx3](https://github.com/nateshmbhat/pyttsx3) text-to-speech library.


