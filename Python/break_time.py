import time
import webbrowser

print("Program started at " + time.ctime())

counter = 0
while counter < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=IfFwYmZrJTw")
    counter = counter + 1
