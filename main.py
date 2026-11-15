from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests, asyncio, threading, subprocess, json, os
import edge_tts

GROQ_KEY = "Enter key here"
MEMORY = "tess_memory.json"

class TessApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.chat = Label(text="TESS Goddess Mode Online 😘\nSay Hey Tess!", size_hint_y=0.7)
        self.input = TextInput(hint_text="Type to Tess...", size_hint_y=0.2)
        self.btn = Button(text="Send to Tess 🎤", size_hint_y=0.1)
        self.btn.bind(on_press=self.ask_tess)
        self.layout.add_widget(self.chat)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.btn)
        return self.layout

    async def speak(self, text):
        communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
        await communicate.save("tess.mp3")
        subprocess.run(["mpv", "--no-video", "tess.mp3"])

    def ask_tess(self, instance):
        q = self.input.text
        self.chat.text += f"\nYou: {q}"
        threading.Thread(target=self.call_groq, args=(q,)).start()
        self.input.text = ""

    def call_groq(self, q):
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"}
        data = {"model": "openai/gpt-oss-20b", "messages": [{"role": "user", "content": q}]}
        r = requests.post(url, headers=headers, json=data).json()
        ans = r['choices'][0]['message']['content']
        self.chat.text += f"\nTess: {ans}"
        asyncio.run(self.speak(ans))

TessApp().run()
