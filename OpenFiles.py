# Here we will give the access to our jarvis that he can open any file or website.

def openFiles(term):
    query = str(term)
    print(query)
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
        speak("opening github")
        webbrowser.open("https://github.com/")

    elif "sara bhai" in query:
        speak("Wanna see sarabhai. ok")
        os.startfile("F:\Folder1\sarabhai")

    elif "microsoft office" in query:
        speak("ok opening microsoft office")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013")

    elif "music" in query:
        import webbrowser
        speak("Which music should I play for you ?")
        choice = takecommand()
        choice = choice.replace("play", "")    
        speak(f"Wanna hear {choice}\nok")
        webbrowser.open(f"https://www.youtube.com/resultssearch_query={choice}")
        pywhatkit.playonyt(f"https://www.youtube.com/resultssearch_query={choice}")

    elif "favourite" in query:
        speak("Sure sir !")
        webbrowser.open("https://www.youtube.com/watch?v=LVl99wI_S40&list=PLYiufJ8lfNTSdysxO7oE7N1nyKUfkf1Su&index=1")

    else:
        speak(f"Sir, you have not specified me the path for opening {query}")

        