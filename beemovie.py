import pyautogui, time
time.sleep(2)  
f = open("beemovie.txt", 'r')
for word in f:
    # you can add a timer there to control timing of the spam. 
    # time.sleep(1)    #will trigger every second 
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    