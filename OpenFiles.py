# Here we will give the access to our jarvis that he can open any file.
def openFiles(term):
    query = str(term)
    import webbrowser
    import os
    import pywhatkit
    from basicfunc import speak, takecommand

    if "youtube" in query:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    
    elif "google" in query:
        speak("opening google")
        webbrowser.open("https://www.google.com/")

    elif "whatsapp" in query:
        speak("opening whatsapp")
        webbrowser.open("https://web.whatsapp.com/")

    elif "github" in query:
        speak("opening whatsapp")
        webbrowser.open("https://github.com/")

    elif "sarabhai" in query:
        speak("Wanna see sarabhai. ok")
        path = "F:\Folder1\sarabhai"
        os.startfile(path)

    elif "microsoft office" in query:
        speak("ok opening microsoft office")
        path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013"
        os.startfile(path)

    elif "music" in query:
        import webbrowser
        speak("Which music should I play for you ?")
        choice = takecommand()
        choice = choice.replace("play", "")    
        path = f"https://www.youtube.com/resultssearch_query={choice}"
        speak(f"Wanna hear {choice}\nok")
        webbrowser.open(path)
        pywhatkit.playonyt(path)

    else:
        print("Path is not specified")
        