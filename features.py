""" The advance features synthesized to give advanced authority to jarvis to perform a variety of tasks. """
from basicfunc import speak
from datetime import date
import os

def searchWikipedia(term):
    """ This function will take the user input and then it will search the input on wikipedia and speak the results. """
    try:
        import wikipedia
        speak("Searching wikipedia")
        term = term.replace("wikipedia", "")
        term = term.replace("search", "")
        results = wikipedia.summary(term, sentences=2)
        speak(f"According to wikipedia \n{results}")
    except Exception as e:
        speak("Sir ! I did not found any page related to your search.")

def googleSearch(input):
    """ 
    This function will perform google search """
    import wikipedia
    from pywikihow import search_wikihow
    import pywhatkit
    
    speak("Searching for your results.")
    
    query = str(input)
    query = query.replace('google', '')
    query = query.replace('search', '')
    pywhatkit.search(query)

    try:
        if "how to" in query:
            how_to_func = search_wikihow(query=query)
            #assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        else:
            search = wikipedia.summary(query, 2)
            speak(f"According to wikipedia : \n{search}")
    except Exception as e:
        print("No pages were found on wikipedia related to your search.")

def youtubeSearch(input):
    """ 
    This function will perform youtube search and will also play the latest video. """
    import webbrowser
    import pywhatkit
    
    speak("Here are the results.")

    input = input.replace('youtube', '')
    input = input.replace('search', '')
    path = "https://www.youtube.com/results?search_query=" + input
    webbrowser.open(path)
    speak("This is what I found for your search.")

    pywhatkit.playonyt(input)
    speak("This may also help you sir.")

def temperature(input):
    ''' This function will tell the current temperature. '''
    import requests
    from bs4 import BeautifulSoup
    
    url = f"http://www.google.com/search?q={input}" #searching weather
    # taking raw data
    r = requests.get(url) 
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div",class_="BNeawe").text
    temp=temp.replace("India ", "")
    temp=temp.replace("Meteorological ", "")
    temp=temp.replace("Department", "")
    speak(f"It's {temp} outside.")

def dateFormateConverter(term):
    '''  This will convert the date format.
    '''
    
    Date = term.replace("and","-")
    Date = term.replace(" and ","-")
    Date = Date.replace(" ","")
    print(str(Date))

def present_time():
    '''This function will convert the national clock time into normal clock time. '''
    from datetime import datetime
    current_hour = datetime.now().strftime("%H")
    current_min = datetime.now().strftime("%M")
    
    new_hour = current_hour.replace("13", "1")
    new_hour = new_hour.replace("14", "2")
    new_hour = new_hour.replace("15", "3")
    new_hour = new_hour.replace("16", "4")
    new_hour = new_hour.replace("17", "5")
    new_hour = new_hour.replace("18", "6")
    new_hour = new_hour.replace("19", "7")
    new_hour = new_hour.replace("20", "8")
    new_hour = new_hour.replace("21", "9")
    new_hour = new_hour.replace("22", "10")
    new_hour = new_hour.replace("23", "11")
    new_hour = new_hour.replace("24", "12")

    c = int(current_hour)
    if c >= 1 and c < 12:
        time = new_hour+":"+current_min+" am"
    else:
        time = new_hour+":"+current_min+" pm"

    speak(f"It's {time}")

def Weather_Report():
    ''' This function will tell the weather report of the current location. ''' 
    import pywhatkit
    speak("showing weather reports")
    pywhatkit.search("weather")

def alarm(user_time):
    """ This function will take the user input in the form of time and then play the alarm on the targeted time. """

    from datetime import datetime
    import os

    # converting the user command to proper time format
    user_time = user_time.replace('hours', '')
    user_time = user_time.replace('and', '')
    user_time = user_time.replace('minutes', '')
    
    splitted_time = user_time.split()
    index = splitted_time.index('for')
    time = splitted_time[index+1::]
    
    alarm_time = ":".join(time)
    speak(f"The alarm is set for {alarm_time}.")
    
    # running the alarm loop
    alarm_system = True
    
    while alarm_system:
        if datetime.now().strftime("%H:%M")[0] == '0':
            present_time = datetime.now().strftime("%H:%M").removeprefix('0')

        else:
            present_time = datetime.now().strftime("%H:%M")

        if present_time==alarm_time:
            print(f"{alarm_time} alarm ran out.")
            os.startfile(r"G:\\coding\\Python\\02_myprojects\\voiceassistant\\Database\\Sound\\alarm.mp3")
            
            alarm_system = False

def justWait(user_time):
    """ This function will allow jarvis to wait for the time specified by the user. """
    
    import time

    waiting_time=user_time.replace("just", "")
    waiting_time=waiting_time.replace("wait", "")
    waiting_time=waiting_time.replace("I", "")
    waiting_time=waiting_time.replace("will", "")
    waiting_time=waiting_time.replace("be", "")
    waiting_time=waiting_time.replace("back", "")
    waiting_time=waiting_time.replace("in", "")
    waiting_time=waiting_time.replace("and", "")
    waiting_time=waiting_time.replace(" ", "")
    waiting_time=waiting_time.replace("i", "")

    if 'minutes'or'minute' in waiting_time:
        wait_time = waiting_time.replace('minutes', '')
        wait_time = waiting_time.replace('minute', '')
        speak('Ok sir.')
        time.sleep(int(wait_time) * 60)

    elif 'seconds' in waiting_time:
        wait_time = waiting_time.replace('seconds', '')
        speak('Ok sir.')
        time.sleep(int(wait_time))

def sleepJarvis():
    """ This function will switch off jarvis. """
    import random
    from datetime import datetime
    now=datetime.now()
    choices = ['Good Bye sir.', 'We shall meet again.', 'Have a nice day ahead sir.']
            
    reply=["Good night sir" if now.hour>=20 else random.choice(choices)]

    speak(reply)
    quit()

def time_table():
    """ this function will make a file where user can make his time table. """

    speak("Sure sir.")


    with open(f"Time Table\\time_table_{date.today()}.txt", "w") as file:
        file.write(f'''Time table for {date.today()}.

             5.00 a.m. -> wake up.
            -5.25 a.m. -> freshen up.
            -5.55 a.m. -> do yoga.
            -6.15 a.m. -> take bath.
            -6.25 a.m. -> get ready.
            -6.50 a.m. -> breakfast.
                   (7.20 a.m. -> take medicine)
                   


                    (6.30 p.m. -> take medicine)
            7.00 - 7.45 p.m. -> dinner
            -8.15 p.m. -> vajarasana
            -8.45 p.m. -> read newspaper
            -9.15 p.m. -> read book
            -9.30 p.m. -> prepare for bed
            -9.35 p.m. -> drink milk
            -10.00 p.m. -> do anything
                   then go to bed.    
        ''')

    open(f"Time Table\\time_table_{date.today()}.txt", "r")
