import time
from basicfunc import takecommand, speak
from datetime import datetime
from playsound import playsound
from keyboard import press

def alarm(query):
    term = str(query)
    term = term.replace("ok", "")
    term = term.replace("jarvis", "")
    term = term.replace("set", "")
    term = term.replace("the", "")
    term = term.replace("alarm", "")
    term = term.replace("for", "")
    term = term.replace("and", "")
    term = term.replace("hours", ":")
    term = term.replace("minutes", "")
    term = term.replace(" ", "")
    term = term.replace("p.m.", "")
    term = term.replace("a.m.", "")
    speak(f"The alarm is set for {term}")
        
    while True:
        if datetime.now().strftime("%H:%M")==term:
            print(f"{term} alarm ran out.")
            playsound("F:\\Python\\02_myprojects\\voiceassistant\\Database\\Sound\\alarm.mp3")            
            break
        else:
            continue

alarm("set the alarm for 13 hours and 43 minutes")