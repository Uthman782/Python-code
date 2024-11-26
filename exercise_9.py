def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    print(str)
    speak.Speak(str)

if __name__ == '__main__':
    speak("Hello How are you Usman Khan.")
