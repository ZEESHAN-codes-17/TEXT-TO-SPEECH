import pyttsx3

choice = 0
while choice != 'q' :
    choice = input("Press 'q' to quit or any other key to continue: ")
    if choice == 'q':
        break
    engine = pyttsx3.init()
    print("Hello, this is a text to speech conversion example.")
    engine.say("Hello, this is a text to speech conversion example.")
    engine.runAndWait()


    user = input("Enter your text u want in speech: ")
    engine.say(user)
    engine.runAndWait()
engine.stop()