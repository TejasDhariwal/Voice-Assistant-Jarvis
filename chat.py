# In this file we will make our jarvis chat with us in order to interact in a better manner

from basicfunc import speak

user_chats = ['how are you doing', 'whatsapp', 'thank you', 'i am feeling a bit low', 'good morning', 'good afternoon', 'good evening']

jarvis_replies = ['I am fine sir. What about you ?', 'fine sir', "It's my pleasure sir.", 'may i play some music for you ?', 'good morning sir !', 'good afternoon sir !', 'good evening sir !']

def chat(user_text):
    """ this function will make jarvis chat with us """
    
    for user_chat in user_chats:
        if user_text.lower() == user_chat.lower():
            i = user_chats.index(user_chat)
            jarvis_reply = jarvis_replies[i]

        else:
            jarvis_reply = "Sir I didn't understood."
    
    speak(jarvis_reply)
