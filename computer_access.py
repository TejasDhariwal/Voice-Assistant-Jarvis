""" In this file we will give our jarvis the access to our whole computer. """
import os
from keyboard import press, press_and_release
from basicfunc import speak, takecommand

def restart():
    os.system("shutdown /r /t 1")# restart the computer.

def restart_time():
    os.system("shutdown /r /t 20")# shut down the computer after 20 seconds.

def logout():
    os.system("shutdown -1")# logout from the computer

def shutdown():
    os.system("shutdown /s /t 1")# shutdown the computer

def windows_automate(command):
    """ This function will automate various things of the windows. """
    query = str(command)
    if "close" in query:
        press_and_release("Alt+F4")
    
    elif "switch window" in query:
        press_and_release("Alt+Tab")
    
    elif "open the settings" in query:
        press_and_release("Windows + i")
    
    elif "make a new folder" in query:
        name = query.replace("make", "")
        name = name.replace("a", "")
        name = name.replace("new", "")
        name = name.replace("folder", "")
        name = name.replace("and", "")
        name = name.replace("name", "")
        name = name.replace("it", "")
        name = name.replace(" ", "")

        os.makedirs(name)
        speak(f"New folder name {name} is being made successfully")


a = takecommand().lower()
windows_automate(a)