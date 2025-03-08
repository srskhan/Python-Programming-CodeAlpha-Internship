import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()


# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[2].id)  

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            print("Say something...")
            voice = listener.listen(source)
            print("Processing your command...")
            command = listener.recognize_google(voice, language="en-US")
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '').strip()
                print("Command:", command)
            else:
                command = "" 
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Sorry, my speech service is down.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return command

def run_alexa():
    while True:
        command = take_command()
        print("Command received:", command)
        if not command:
            continue 

        if 'play' in command:
            song = command.replace('play', '').strip()
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command or 'who the heck is' in command:
            person = command.replace('who is', '').replace('who the heck is', '').strip()
            try:
                info = wikipedia.summary(person, sentences=2)
                print(info)
                talk(info)
            except wikipedia.exceptions.DisambiguationError as e:
                talk("There are multiple matches. Please be more specific.")
            except wikipedia.exceptions.PageError:
                talk("Sorry, I could not find any information about that.")
        elif 'date' in command:
            talk('Sorry, I have a headache.')
        elif 'are you single' in command:
            talk('I am in a relationship with Wi-Fi.')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'stop' in command:
            talk('Goodbye!')
            break  
        else:
            talk('Please say the command again.')


run_alexa()