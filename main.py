def jarvis():
    from basicfunc import WishMe, takecommand, speak
        
    #WishMe()              
    
    while 1:
        Query = takecommand().lower()                    
        if "wikipedia" in Query:
            try:
                import wikipedia
                speak("Searching wikipedia")
                Query = Query.replace("wikipedia", "")
                Query = Query.replace("search", "")
                results = wikipedia.summary(Query, sentences=2)
                speak(f"According to wikipedia \n{results}")
            except Exception as e:
                speak("Sir ! I did not found any page related to your search.")

        elif "google search" in Query:
            speak("Searching for your results.")
            Query = Query.replace("google search","")
            from features import googleSearch
            googleSearch(Query)

        elif "youtube search" in Query:
            speak("Here are the results.")
            Query = Query.replace("youtube search","")
            from features import youtubeSearch
            youtubeSearch(Query)

        elif "open" in Query:
            from OpenFiles import openFiles
            openFiles(Query)
        
        elif "music" in Query:
            from OpenFiles import openFiles
            openFiles(Query)
        
        elif "see" in Query:
            from OpenFiles import openFiles
            openFiles(Query)
        
        elif "play" in Query:
            from OpenFiles import openFiles
            openFiles(Query)

        elif "time" in Query:
            from features import present_time
            time = present_time()
            speak(f"Sir it's {time}")

        elif "date" in Query:
            from datetime import date
            present_date = date.today()
            speak(f"Today's date is {present_date}")
        
        elif "temperature" in Query:
            from features import temperature
            temperature(Query)

        elif "weather report" in Query:
            from features import Weather_Report
            Weather_Report()

        # Need to work on this
        elif "alarm" in Query: 
            # need to work
            import os
            import keyboard
            path="F:\\Python\\02_myprojects\\voiceassistant\\alarming.py"
            os.startfile(path)
            keyboard.send("F3")
 
        elif "your full form" in Query:
            speak("That is\nJust A Really Very Intelligent System.")

        elif "shutdown" in Query:
            from computer_access import shutdown
            speak("Sir ! Do you really want me to shutdown the computer ?")
            a = takecommand()
            if "yes" in a:
                speak("ok sir! Have a nice day ahead!")
                shutdown()
            else:
                speak("ok sir!")
            
        elif "restart" in Query:
            from computer_access import restart, restart_time
            speak("Should I restart now or after some time ?")
            option = takecommand()

            if "time" in option:
                speak("ok sir!")
                restart_time()
            else:
                speak("ok sir!")
                restart()

        elif "logout" in Query:
            try:
                from computer_access import logout
                speak("ok sir !")
                logout()
            except Exception as er:
                print(er)
                speak("Sir, you have not login into the computer yet.")
        
        elif "go to sleep" in Query:
            import random
            from datetime import datetime
            now=datetime.now()
            choices = ['Good Bye sir.', 'We shall meet again.', 'Have a nice day ahead sir.']
            
            reply=["Good night sir" if now.hour>=20 else random.choice(choices)]

            speak(reply)
            quit()

        elif "just wait" in Query:
            import time
            waitingtime=Query.replace("just", "")
            waitingtime=waitingtime.replace("wait", "")
            waitingtime=waitingtime.replace("I", "")
            waitingtime=waitingtime.replace("will", "")
            waitingtime=waitingtime.replace("be", "")
            waitingtime=waitingtime.replace("back", "")
            waitingtime=waitingtime.replace("in", "")
            waitingtime=waitingtime.replace("and", "")
            waitingtime=waitingtime.replace(" ", "")
            waitingtime=waitingtime.replace("i", "")
            
            if "minutes" in waitingtime:
                waitingtime = waitingtime.replace("minutes", "")
                waitime = int(waitingtime)*60
            else:
                waitingtime = waitingtime.replace("seconds", "")
                waitime = int(waitingtime)
                
            speak("ok sir")
            time.sleep(waitime)            

        else:
            print("Please speak again.")

