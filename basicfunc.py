""" The basic functions which will be used at each and every time in our jarvis. """

def speak(text):
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    print(f": {text}")
    engine.runAndWait()

def takecommand():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)    
    try:
        print("Recognizing..")
        q = r.recognize_google(audio, language="en")
        print(f"User Said : {q}\n")            
    except Exception as e:
        print("Say that again please.")
        return "None"
    
    query = q.lower()
    query = query.replace("jarvis", "")
    query = query.replace("ok", "")
    query = query.replace("hey", "")

    return query

def WishMe():
    from datetime import datetime, date
    from features import present_time, temperature
    hour = int(datetime.now().hour)
    present_date = date.today()
    if hour>=0 and hour<12:
        speak("Good Morning Sir") 
    elif hour>=12 and hour<=17:
        speak("Good Afternoon Sir")        
    elif hour>17 and hour<24:
        speak("Good Evening Sir")
    time=present_time()    
    speak(f"Its {time}")
    speak(f"The day is {present_date}")
    temperature("temperature")
    speak("I am Jarvis! How can I help you?")
