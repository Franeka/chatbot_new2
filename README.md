# chatbot_new

### Beschreibung
Ein Chatbot mit verschiedenen Oberflächen. Beispiel für objektorientierte Programmierung und die Verwendung von Frameworks.

Zusätzlich: Verwendung von Docker und CI/CD für Test und Verteilung.

### Versionen
1. v2: einfacher Chatbot mit vorgegebenen Fragen und Antworten
2. v3: Chatbot mit künstlicher Intelligenz

### Installation
```bash
git clone https://github.com/JoergEF/chatbot_new
cd chatbot_new
mkdir v3/model
```

### Benutzung
- v2:
```python
	from chatbot import Chatbot
	bot = Chatbot(reaktionen, zufallsantworten)
	bot.set_Message(eingabe)
	ausgabe = bot.get_Response()
```

- v3:
```python
	from chatbot_ai import chatbot_ai
	bot = chatbot_ai(jsonfile)
	bot.set_Message(eingabe)
	ausgabe = bot.get_Response()
```

