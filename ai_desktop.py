import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia  
import webbrowser
import os
import smtplib




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning alpha!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon alpha!")   

    else:
        speak("Good Evening alpha!")  

    speak("I am alpha Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif " your name" in query:
            name = "my name is alpha"
            speak(name)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            
            
        elif "open facebook" in query:
            webbrowser.open("http://facebook.com")
        
        elif "open instgram" in query:
            webbrowser.open("http://instgram.com")
        
        elif "open linkedin" in query:
            webbrowser.open("http://linkedin.com")
        
        elif "open telegram" in query:
            webbrowser.open("http://telegram.com")
        
        
        elif "open chatgtp" in query:
            webbrowser.open("http://chatgtp.com")
        
     
        
        elif "open flipcart" in query:
            webbrowser.open("http://flipcart.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs [0]))
           

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ra600\\AppData\\Local\\Programs\\Microsoft VS Code"
            os.startfile(codePath)
            
        elif  "ashish"   in query:
            speak("ashish is good boy")  
            
        elif "vegamovies" in query:
            webbrowser.open("https://vegamovies.lt/")

        
        elif "vlog" in query:
            webbrowser.open ("https://www.youtube.com/watch?v=0AAYVCVuh1o")
            
        elif "image" in query:
            webbrowser.open ("https://www.bing.com/search?pglt=41&q=images&cvid=efb974f5b9e74352850fb5bd8759c08f&gs_lcrp=EgZjaHJvbWUqBggAEAAYQDIGCAAQABhAMgYIARBFGDkyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEAAYQDIGCAYQABhAMgYIBxAAGEAyBggIEAAYQNIBCDQxMTBqMGoxqAIIsAIB&FORM=ANSPA1&PC=U531")
            
        elif "python" in query:
            webbrowser.open ("https://www.bing.com/search?q=python+download&qs=SS&pq=python+d&sc=10-8&cvid=4E86EE1EEB21491796B5286811575520&FORM=QBRE&sp=1&ghc=1&lq=0")
            
            
        elif "ashu" in query:
            webbrowser.open ("https://www.instagram.com/techcodeashu/")
            
            
        elif "gmail" in query:
            webbrowser.open ("https://mail.google.com/mail/u/0/#inbox")
            
        elif "ekalyan" in query:
            webbrowser.open ("https://ekalyan.cgg.gov.in/Login.do")
            
        elif "news" in query:
            webbrowser.open ("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en")
            
        elif "maps" in query:
            webbrowser.open ("https://www.google.com/maps")
            
            
        elif "translate" in query:
            webbrowser.open ("https://translate.google.com/?sl=auto&tl=en&op=translate")
            
        elif "amazon" in query:
            webbrowser.open ("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=674842289437&hvpos=&hvnetw=g&hvrand=15402962084727183169&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9302445&hvtargid=kwd-10573980&hydadcr=14453_2316415&gad_source=1")
            
        elif "icfai" in query:
            webbrowser.open ("https://www.iujharkhand.edu.in/login_stufee.html?msg=Session%20Timed%20Out.%20Please%20login")
            
            
        elif "hospital" in query:
            webbrowser.open ("https://peoplecarehospital.com/")
            
        elif "swadhyay" in query:
            webbrowser.open ("https://www.iujharkhand.edu.in/swaadhyay.html")