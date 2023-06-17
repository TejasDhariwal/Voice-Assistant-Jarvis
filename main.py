""" This is the main part of our jarvis where the work is being assigned to it for different things. """


def jarvis():
    # Brain of jarvis 

    from basicfunc import WishMe, takecommand, speak 
    WishMe()
    
    from OpenFiles import openFiles
    from features import searchWikipedia, googleSearch, youtubeSearch, temperature, present_time, Weather_Report, alarm, justWait, sleepJarvis, time_table
    from computer_access import shutdown, restart, restart_time, logout
    from datetime import date
    from chat import chat

    system = True

    while system:
        Query = takecommand().lower()                    
        if "wikipedia" in Query:
            # searching for wikipedia 
            searchWikipedia(Query)

        elif "google search" in Query:
            # searching on google 
            googleSearch(Query)

        elif "youtube search" in Query:
            # making youtube search 
            youtubeSearch(Query)

        elif "open" in Query:
            # will open any file in the computer or even a website 
            openFiles(Query)
        
        elif "music" in Query:
            # will play any music or song from youtube as specified by the user 
            openFiles(Query)

        elif "favourite" in Query:
            # will play my favourite playlist on youtube 
            openFiles(Query)
        
        elif "see" in Query:
            openFiles(Query)
        
        elif "time" in Query:
            # will tell the present time 
            present_time()
            
        elif "date" in Query:
            # will tell the present date 
            present_date = date.today()
            speak(f"Today's date is {present_date}")
        
        elif "temperature" in Query:
            # will tell the current temperature
            temperature(Query)

        elif "weather report" in Query:
            # will tell the weather report 
            Weather_Report()

        elif "alarm" in Query: 
            # will set the alarm 
            alarm(Query)
 
        elif "your full form" in Query:
            # will tell the full form of jarvis 
            speak("That is\nJust A Really Very Intelligent System.")

        elif "shutdown" in Query:
            # will shutdown the computer on the spot or after some time 

            speak("Sir ! Do you really want me to shutdown the computer ?")
            a = takecommand()
            if "yes" in a:
                speak("ok sir! Have a nice day ahead!")
                shutdown()
            else:
                speak("ok sir!")
            
        elif "restart" in Query:
            # will restart the computer 
            speak("Should I restart now or after some time ?")
            option = takecommand()

            if "time" in option:
                speak("ok sir!")
                restart_time()
            else:
                speak("ok sir!")
                restart()

        elif "logout" in Query:
            # will logout from the pc 
            try: 
                speak("ok sir !")
                logout()
            except Exception as er:
                print(er)
                speak("Sir, you have not login into the computer yet.")
        
        elif "go to sleep" in Query:
            # will switch off the jarvis 
            sleepJarvis()

        elif "just wait" in Query:
            # will wait for the time specified by the user 
            justWait()  

        elif "schedule" in Query:
            # will make a file where user can make the time table for the next day.
            time_table()


        else:
            # if user's input doesn't matches any of the case, then we will use the chat function to proceed with it.
            
            chat(Query)
        
