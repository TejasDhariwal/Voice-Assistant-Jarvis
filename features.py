# Here we will add various feature to our jarvis and make him more responsible.
from basicfunc import speak

def googleSearch(term):
    """ 
    This function will perform google search """
    import wikipedia
    from pywikihow import search_wikihow
    import pywhatkit
    query = str(term)
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

def youtubeSearch(term):
    """ 
    This function will perform youtube search and will also play the latest video. """
    import webbrowser
    import pywhatkit
    path = "https://www.youtube.com/results?search_query=" + term
    webbrowser.open(path)
    speak("This is what I found for your search.")

    pywhatkit.playonyt(term)
    speak("This may also help you sir.")

def telljokes():
    """ 
    This function will tell us jokes """
    from pyjokes import get_joke
    joke = get_joke(language="en", category="neutral")
    speak(joke)

def temperature(term):
    import requests
    from bs4 import BeautifulSoup
    
    ''' This function will tell the current temperature. '''
    url = f"http://www.google.com/search?q={term}" #searching weather
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
    return time

def Weather_Report():
    ''' This function will tell the weather report of the current location. ''' 
    import pywhatkit
    speak("showing weather reports")
    pywhatkit.search("weather")
