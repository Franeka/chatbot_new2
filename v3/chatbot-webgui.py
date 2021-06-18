#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from flask import Flask, render_template, request, flash
from chatbot_ai import chatbot_ai
from pathlib import Path


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Pa$$w0rd'


@app.route('/', methods=('GET', 'POST'))
def index():
    logging.basicConfig(filename="webgui-dev.log", level=logging.DEBUG)
    chatbot_label = "Hallo, worüber wollen Sie sprechen?"

    # Logik
    if request.method == 'POST':
        chatbot_input = request.form['chatbot_input']
        if not chatbot_input:
            flash("Ohne Frage kann ich nicht antworten")
        else:
            bot = chatbot_ai("v3/intents.json")
            bot.set_Message(chatbot_input)
            chatbot_label = bot.get_Response()
    p = Path(__file__).parent / 'templates'
    template = str(p.joinpath("/chatbot.html"))
    return render_template(template, chatbot_label=chatbot_label)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
