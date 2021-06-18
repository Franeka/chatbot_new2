#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from chatbot_ai import chatbot_ai


def main():
    # Ausgabe Begrüßung
    print("Willkommen beim Chatbot (v3)")
    print("Zum Beenden geben Sie bye ein...")
    print("Worüber wollen Sie sprechen?")
    print("")

    # Chatbot-Objekt
    bot = chatbot_ai("v3/intents.json")

    # Logik
    nutzereingabe = ""
    while nutzereingabe != "bye":
        nutzereingabe = ""
        while nutzereingabe == "":
            nutzereingabe = input("Ihre Frage oder Antwort: ")
        if nutzereingabe == "bye":
            break
        bot.set_Message(nutzereingabe)
        print(bot.get_Response())

    # Ausgabe Verabschiedung
    print("Bis zum nächsten Mal.")


main()
