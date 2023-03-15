import customtkinter
from main import jarvis
from PIL import Image 
import webbrowser
import os

# Screen themes
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

class QuickFunc():
    def runJarvis():
        """ This function will start jarvis """
        jarvis()
    
    def openGoogle():
        webbrowser.open("https://www.google.com/")
    
    def openYoutube():
        webbrowser.open("https://www.youtube.com/")
    
    def openWhatsapp():
        webbrowser.open("https://web.whatsapp.com/")
    
    def openGithub():
        webbrowser.open("https://github.com/")
    
    def shutdown():
        os.system("shutdown /s /t 1")# shutdown the computer
    
    def restart():
        os.system("shutdown /r /t 1")# restart the computer.

    def openPortfolio():
        os.startfile(r'G:\\coding\\Web Development\\Projects\\portfolio')

    def openGymsite():
        os.startfile(r'G:\\coding\\Web Development\\Projects\\GymSite')

    def newsite():
        os.chdir('G:\\coding\\Web Development\\Projects')
        os.mkdir('New Website')
        os.chdir('G:\\coding\\Web Development\\Projects\\New Website')
        os.startfile(r'G:\\coding\\Web Development\\Projects\\New Website')

    def openAi():
        os.startfile(r'G:\\coding\\Python\\02_myprojects\\voiceassistant')

    def newProject():
        os.chdir('G:\\coding\\Python\\02_myprojects')    
        os.mkdir('New Project')
        os.chdir('G:\\coding\\Python\\02_myprojects\\New Project')
        os.startfile(r'G:\\coding\\Python\\02_myprojects\\New Project')
    
    def changeAppearance(choice1):
        if choice1=="Dark":
            customtkinter.set_appearance_mode("dark")
        elif choice1=="Light":
            customtkinter.set_appearance_mode("light")
        elif choice1=="System":
            customtkinter.set_appearance_mode("system")
        else:
            pass

    def changeTheme(choice):
        if choice=="Dark-Blue":
            customtkinter.set_default_color_theme("dark-blue")
        elif choice=="Blue":
            customtkinter.set_default_color_theme('blue')    
        elif choice=="Green":
            customtkinter.set_default_color_theme('green')
        else:
            pass

    def openEcommerce():
        os.startfile(r'G:\\coding\\Web Development\\Projects\\Ecommercesite')

# Window settings
root.geometry("850x600")
root.title("Jarvis | Desktop Assistant")

# Tabs
tabview = customtkinter.CTkTabview(root, width = 780, height = 780)
tabview.pack(padx = 10, pady=10, ipadx = 20, ipady = 20)

# adding the tabs
tabview.add("Jarvis")
tabview.add("Quick Functions")
tabview.add("Projects")
tabview.add("Edit")

# setting the current tab
tabview.set("Jarvis")

# Content of Jarvis tab

jarvis_heading = customtkinter.CTkLabel(tabview.tab("Jarvis"), text="Jarvis  |  Your Personel Desktop Assistant", font=('Dosis', 35))
jarvis_heading.pack(side="top", anchor="c", pady=5)

jarvis_intro = customtkinter.CTkLabel(tabview.tab("Jarvis"), text='''
Hello !\n I am an ARTFICIAL INTELLIGENCE that can help you in your stuff 24/7.\n Just click the below button to start me.''', font=('Dosis', 30))
jarvis_intro.pack(side='top', anchor='c')

ai_img = customtkinter.CTkImage(light_image=Image.open("img.jpg"), size=(400, 450))
img = customtkinter.CTkLabel(tabview.tab('Jarvis'), image=ai_img, text="")
img.pack(side = 'left', anchor = 'w', pady = 10, padx=20)

btn = customtkinter.CTkButton(tabview.tab("Jarvis"), text="Start Jarvis", font=('Dosis', 25), command=QuickFunc.runJarvis)
btn.pack(side='right', anchor='e', ipady=10, ipadx=10, padx=30)

# Content of Quick Functions tab

# OPEN SECTION
qlabel1 = customtkinter.CTkLabel(tabview.tab('Quick Functions'), text="Open", font=('Dosis', 25))
qlabel1.place(x=10, y=1)

qbtn1 = customtkinter.CTkButton(tabview.tab('Quick Functions'), text="Google", font=('Dosis', 20), width=100, height=35, command=QuickFunc.openGoogle)
qbtn1.place(x=10, y=50)

qbtn2 = customtkinter.CTkButton(tabview.tab('Quick Functions'), text="Youtube", font=('Dosis', 20), width=100, height=35, command=QuickFunc.openYoutube)
qbtn2.place(x=120, y=50)

qbtn3 = customtkinter.CTkButton(tabview.tab('Quick Functions'), text="Whatsapp", font=('Dosis', 20), width=100, height=35, command=QuickFunc.openWhatsapp)
qbtn3.place(x=10, y=100)

qbtn4 = customtkinter.CTkButton(tabview.tab('Quick Functions'), text="GitHub", font=('Dosis', 20), width=100, height=35, command=QuickFunc.openGithub)
qbtn4.place(x=120, y=100)

# POWER SECTION
qlabel2 = customtkinter.CTkLabel(tabview.tab('Quick Functions'), text="Power", font=('Dosis', 25))
qlabel2.place(x=350, y=1)

qbtn5 = customtkinter.CTkButton(tabview.tab('Quick Functions'), text="Shutdown", font=('Dosis', 20), width=100, height=35, command=QuickFunc.shutdown)
qbtn5.place(x=350, y=50)

qbtn6 = customtkinter.CTkButton(tabview.tab('Quick Functions'), text="Restart", font=('Dosis', 20), width=100, height=35, command=QuickFunc.restart)
qbtn6.place(x=460, y=50)

# Content of Projects tab

plabel1 = customtkinter.CTkLabel(tabview.tab('Projects'), text="Recent Projects", font=('Dosis', 25))
plabel1.place(x=330, y=1)

# Websites
plabel2 = customtkinter.CTkLabel(tabview.tab('Projects'), text="Websites", font=('Dosis', 25))
plabel2.place(x=50, y=80)

pbtn1 = customtkinter.CTkButton(tabview.tab('Projects'), text="Portfolio website", font=('Dosis', 20), command=QuickFunc.openPortfolio)
pbtn1.place(x=20, y=130)

pbtn2 = customtkinter.CTkButton(tabview.tab('Projects'), text="GymSite", font=('Dosis', 20), command=QuickFunc.openGymsite)
pbtn2.place(x=180, y=130)

pbtn3 = customtkinter.CTkButton(tabview.tab('Projects'), text="E-commerce", font=('Dosis', 20), command=QuickFunc.openEcommerce)
pbtn3.place(x=20, y=180)

pbtn4 = customtkinter.CTkButton(tabview.tab('Projects'), text="New", font=('Dosis', 20), command=QuickFunc.newsite)
pbtn4.place(x=180, y=180)

# Other projects
plabel3 = customtkinter.CTkLabel(tabview.tab('Projects'), text="Other Python Projects", font=('Dosis', 25))
plabel3.place(x=450, y=80)

pbtn4 = customtkinter.CTkButton(tabview.tab('Projects'), text="Jarvis", font=('Dosis', 20), command=QuickFunc.openAi)
pbtn4.place(x=450, y=130)

pbtn5 = customtkinter.CTkButton(tabview.tab('Projects'), text="New", font=('Dosis', 20), command=QuickFunc.newProject)
pbtn5.place(x=610, y=130)

# Content of Edit tab

elabel1 = customtkinter.CTkLabel(tabview.tab('Edit'), text="Display", font=('Dosis', 30))
elabel1.place(x=20, y=10)

elabel2 = customtkinter.CTkLabel(tabview.tab('Edit'), text="Appearance Mode :-", font=('Dosis', 25))
elabel2.place(x=20, y=60)

appearance_options = customtkinter.CTkComboBox(tabview.tab('Edit'), values=["Dark", "Light", "System"], font=('Dosis', 20), command=QuickFunc.changeAppearance)
appearance_options.place(x=230, y=64)
appearance_options.set("Dark")

elabel3 = customtkinter.CTkLabel(tabview.tab('Edit'), text="Theme :-", font=('Dosis', 25))
elabel3.place(x=20, y=110)

theme_options = customtkinter.CTkComboBox(tabview.tab('Edit'), values=["Dark-Blue", "Blue", "Green"], font=('Dosis', 20), command=QuickFunc.changeTheme)
theme_options.place(x=230, y=114)
theme_options.set("Dark-Blue")

root.mainloop()