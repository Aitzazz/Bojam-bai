import pyttsx3 #pyttsx is a text-to-speech library in Python; it is completely offline

if __name__ == "__main__":
    engine = pyttsx3.init()
    print("Welcome to the ROBOSPEAKER 1.1 by Aiti_Khan")
    while True:
        X = input("What do you want me to say? ")
        if X == "E":
            engine.say("bye bye friend")
            engine.runAndWait()
            break
        engine.say(X)   
        engine.runAndWait() 