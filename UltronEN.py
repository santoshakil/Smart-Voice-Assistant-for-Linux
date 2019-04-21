import speech_recognition as sr
from lxml import html
import requests
import webbrowser
import os
from pynput.keyboard import Key, Controller
import mouse


mlist = []
loopme = 1
r = sr.Recognizer()
keyboard = Controller()


while(loopme == 1):
    with sr.Microphone() as source:

        print("Please Wait...")
        r.adjust_for_ambient_noise(source)
        print("What can I do for you Sir ?")
        audio = r.listen(source)
        print("Trying to recognize...")

    try:
        t = r.recognize_google(audio).lower()
        print("You just said "+t)

        # Play a video
        if(t.find("play") != -1):

            le = t.find("play")+len("play")+1
            t = t[le:]

            try:

                print("Playing", t)

                q = 'https://www.youtube.com/results?search_query='+t
                page = requests.get(q)
                tree = html.fromstring(page.content)
                buyers = tree.xpath(
                    '//*[@id="results"]/ol[1]/li[1]/ol[1]/li[1]/div[1]')
                a = buyers[0]
                p = a.get("data-context-item-id")
                webbrowser.open("https://www.youtube.com/watch?v="+p)

            except:
                print("Can't Play.")

         # Installing
        elif (t.find("ultron install") != -1):

            le = t.find("ultron install") + len("ultron install") + 1
            t = t[le:]

            try:

                print("Installing> ", t)
                os.system("sudo pacman -S "+t+" --noconfirm")
            except:
                print("Can't Install")

         # unInstalling
        elif (t.find("ultron uninstall") != -1):

            le = t.find("ultron uninstall") + len("ultron uninstall") + 1
            t = t[le:]

            try:

                print("Installing> ", t)
                os.system("sudo pacman -R "+t+" --noconfirm")
            except:
                print("Can't UnInstall")

        # Typing
        elif (t.find("type") != -1):

            le = t.find("type") + len("type") + 1
            t = t[le:]

            try:

                print("Typing> ", t)
                keyboard.type('' + t+".\n")
            except:
                print("Can't Type")

        # Writing
        elif (t.find("write") != -1):

            le = t.find("write") + len("write") + 1
            t = t[le:]

            try:

                print("Writing> ", t)
                keyboard.type('' + t+".\n")
            except:
                print("Can't Write")

         # Open Application
        elif(t.find("open") != -1):

            le = t.find("open")+len("open")+1
            t = t[le:]

            try:
                # Open Conditions
                if(t == "text" or t == "Text"):
                    os.system("kate </dev/null &>/dev/null &")
                    mlist.append("kate")

                if(t == "file" or t == "File"):
                    os.system("dolphin </dev/null &>/dev/null &")
                    mlist.append("dolphin")

                elif(t == "opera" or t == "Opera"):
                    os.system("opera </dev/null &>/dev/null &")
                    mlist.append("opera")

                elif(t == "firefox" or t == "Firefox"):
                    os.system("firefox </dev/null &>/dev/null &")
                    mlist.append("firefox")

                elif((t.find("chrome") != -1) or (t.find("Chrome") != -1)):
                    os.system("google-chrome </dev/null &>/dev/null &")
                    mlist.append("google-chrome")

                elif((t.find("chromium") != -1) or (t.find("Chromium") != -1)):
                    os.system("chromium </dev/null &>/dev/null &")
                    mlist.append("chromium")

                elif(t == "terminal" or t == "Terminal"):
                    os.system("konsole </dev/null &>/dev/null &")
                    mlist.append("konsole")

                elif(t == "tab" or t == "Tab"):
                    os.system("sleep 0.5 && xdotool key 'Control+t'")

                else:
                    os.system(""+t.lower()+" </dev/null &>/dev/null &")
                    mlist.append(""+t.lower())

            except:

                print("Can't open")

         # Close windows application
        elif(t.find("close") != -1):

            le = t.find("close")+len("close")+1
            t = t[le:]

            try:
                 # Close Conditions
                if(t == "text" or t == "Text"):
                    mlist.index("kate")
                    os.system("killall kate")
                    mlist.remove("kate")

                elif(t == "firefox" or t == "Firefox"):
                    mlist.index("firefox")
                    os.system("killall firefox")
                    mlist.remove("firefox")

                elif(t == "chrome" or t == "Chrome"):
                    mlist.index("google-chrome")
                    os.system("killall chrome")
                    mlist.remove("google-chrome")

                elif(t == "chromium" or t == "Chromium"):
                    mlist.index("chromium")
                    os.system("killall chromium")
                    mlist.remove("chromium")

                elif(t == "file" or t == "File"):
                    mlist.index("dolphin")
                    os.system("killall dolphin")
                    mlist.remove("dolphin")

                elif(t == "terminal" or t == "Terminal"):
                    mlist.index("konsole")
                    os.system("killall konsole")
                    mlist.remove("konsole")

                elif(t == "this" or t == "This"):
                    os.system("sleep 0.5 && xdotool key 'Alt+F4'")

                elif(t == "tab" or t == "Tab"):
                    os.system("sleep 0.5 && xdotool key 'Control+w'")

                elif(t == "ultron" or t == "Ultron"):
                    os.system(
                        "pkill -9 -f ~/.ultron/UltronEN.py")

                else:
                    mlist.index(""+t.lower())
                    os.system("killall "+t.lower())
                    mlist.remove(""+t.lower())

            except:
                print("Could not close")

         # Search something
        elif (t.find("Google") != -1):

            le = t.find("google")+len("google")+1
            t = t[le:]

            try:

                webbrowser.open("https://www.google.co.in/search?q=" + t)

            except:
                print("Can't Find")

        elif (t.find("Search") != -1):

            le = t.find("search")+len("search")+1
            t = t[le:]

            try:

                webbrowser.open("https://www.google.co.in/search?q="+t)

            except:
                print("Can't Search")

         # Web Links
        elif (t.find("go to") != -1):
            le = t.find("go to")+len("go to")+1
            t = t[le:]

            try:
                if (t == "facebook" or t == "fb"):
                    webbrowser.open("https://www.facebook.com")

                elif (t == "twitter" or t == "Twitter"):
                    webbrowser.open("https://www.twitter.com")

                elif (t == "github" or t == "Github"):
                    webbrowser.open("https://www.github.com")

                elif (t == "instagram" or t == "Insta"):
                    webbrowser.open("https://www.instagram.com")

                elif (t == "youtube" or t == "yt"):
                    webbrowser.open("https://www.youtube.com")

                else:
                    webbrowser.open(""+t.lower())

            except:

                print("Couldn't do it")

         # Direct Web Links
        elif (t.find("direct open") != -1):

            le = t.find("direct open")+len("direct open")+1
            t = t[le:]

            try:

                webbrowser.open("https://www."+t)

            except:
                print("Can't open")

         # Volume
        elif (t.find("volume") != -1):
            le = t.find("volume")+len("volume")+1
            t = t[le:]

            try:
                 # Up
                if (t == "up" or t == "high"):
                    os.system("amixer set 'Master' 5%+")
                 # Down
                elif (t == "down" or t == "low"):
                    os.system("amixer set 'Master' 5%-")

            except:

                print("Couldn't do it")

         # Brightness
        elif (t.find("brightness") != -1):
            le = t.find("brightness")+len("brightness")+1
            t = t[le:]

            try:
                 # Up
                if (t == "up" or t == "high"):
                    os.system("xbacklight -inc 5")

                 # Down
                elif (t == "down" or t == "low"):
                    os.system("xbacklight -dec 5")

            except:

                print("Couldn't do it")

         # Brightness/Volume Up
        elif (t.find("increase") != -1):
            le = t.find("increase")+len("increase")+1
            t = t[le:]

            try:

                # Brightness
                if (t == "brightness" or t == "light"):
                    os.system("xbacklight -inc 5")

                # Volume
                elif (t == "volume" or t == "sound"):
                    os.system("amixer set 'Master' 5%+")

            except:

                print("Couldn't do it")

         # Brightness/Volume Down
        elif (t.find("decrease") != -1):
            le = t.find("decrease")+len("decrease")+1
            t = t[le:]

            try:

                # Brightness
                if (t == "brightness" or t == "light"):
                    os.system("xbacklight -dec 5")

                # Volume
                elif (t == "volume" or t == "sound"):
                    os.system("amixer set 'Master' 5%-")

            except:

                print("Couldn't do it")

        # Set Volume/Brightness
        elif (t.find("set") != -1):
            le = t.find("set")+len("set")+1
            t = t[le:]

            try:

                if (t == "volume" or t == "sound"):
                    n = int(filter(str.isdigit, t))
                    os.system("amixer set 'Master' " + n + "%")

                if (t == "brightness" or t == "light"):
                    n = int(filter(str.isdigit, t))
                    os.system("xbacklight -set " + n)

            except:

                print("Couldn't set")

         # Page Up Down
        elif (t.find("scroll") != -1):
            le = t.find("scroll")+len("scroll")+1
            t = t[le:]

            try:
                 # Up
                if (t == "up" or t == "high"):
                    os.system("sleep 0.5 && xdotool key 'Prior'")
                 # Down
                elif (t == "down" or t == "low"):
                    os.system("sleep 0.5 && xdotool key 'Next'")

            except:

                print("Couldn't do it")

        elif (t.find("page") != -1):
            le = t.find("page")+len("page")+1
            t = t[le:]

            try:
                 # Up
                if (t == "up" or t == "high"):
                    os.system("sleep 0.5 && xdotool key 'Prior'")
                 # Down
                elif (t == "down" or t == "low"):
                    os.system("sleep 0.5 && xdotool key 'Next'")

            except:

                print("Couldn't do it")

         # Computer Power Management
        elif(t.find("computer") != -1):

            le = t.find("computer")+len("computer")+1
            t = t[le:]

            try:
                if (t == "suspend" or t == "sleep"):
                    os.system("systemctl suspend")

                elif (t == "power off" or t == "shutdown"):
                    os.system("systemctl poweroff")

                elif (t == "reboot" or t == "restart"):
                    os.system("systemctl reboot -i")

            except:

                print("Couldn't do it")

        elif(t.find("reboot") != -1):

            le = t.find("reboot")+len("reboot")+1
            t = t[le:]

            try:
                if (t == "computer" or t == "pc"):
                    os.system("systemctl reboot -i")

            except:

                print("Couldn't do it")

        elif(t.find("restart") != -1):

            le = t.find("restart")+len("restart")+1
            t = t[le:]

            try:
                if (t == "computer" or t == "pc"):
                    os.system("systemctl reboot -i")

            except:

                print("Couldn't do it")

        elif(t.find("suspend") != -1):

            le = t.find("suspend")+len("suspend")+1
            t = t[le:]

            try:
                if (t == "computer" or t == "pc"):
                    os.system("systemctl suspend")

            except:

                print("Couldn't do it")

        elif(t.find("sleep") != -1):

            le = t.find("sleep")+len("sleep")+1
            t = t[le:]

            try:
                if (t == "computer" or t == "pc"):
                    os.system("systemctl suspend")

            except:

                print("Couldn't do it")

        elif(t.find("shutdown") != -1):

            le = t.find("shutdown")+len("shutdown")+1
            t = t[le:]

            try:
                if (t == "computer" or t == "pc"):
                    os.system("systemctl poweroff")

            except:

                print("Couldn't do it")

        elif(t.find("Poewr off") != -1):

            le = t.find("Poewr off")+len("Poewr off")+1
            t = t[le:]

            try:
                if (t == "computer" or t == "pc"):
                    os.system("systemctl poweroff")

            except:

                print("Couldn't do it")

        # Bluetooth/WiFi
        elif(t.find("disable") != -1):

            le = t.find("disable")+len("disable")+1
            t = t[le:]

            try:
                if (t == "bluetooth" or t == "blue tooth"):
                    os.system("rfkill block bluetooth")

                elif (t == "wi-fi" or t == "wireless"):
                    os.system("nmcli radio wifi off")

            except:

                print("Couldn't do it")

        elif(t.find("enable") != -1):

            le = t.find("enable")+len("enable")+1
            t = t[le:]

            try:
                if (t == "bluetooth" or t == "blue tooth"):
                    os.system("rfkill unblock bluetooth")

                elif (t == "wi-fi" or t == "wireless"):
                    os.system("nmcli radio wifi on")

            except:

                print("Couldn't do it")

        # Update OS
        elif(t.find("update") != -1):

            le = t.find("update")+len("update")+1
            t = t[le:]

            try:
                if (t == "computer" or t == "everything"):
                    os.system("sudo pacman -Syu --noconfirm")

            except:

                print("Couldn't Update")

        elif(t.find("upgrade") != -1):

            le = t.find("upgrade")+len("upgrade")+1
            t = t[le:]

            try:
                if (t == "computer" or t == "everything"):
                    os.system("sudo pacman -Syu --noconfirm")

            except:

                print("Couldn't Update")

         # ScreenShot
        elif(t.find("take") != -1):

            le = t.find("take")+len("tske")+1
            t = t[le:]

            try:
                if (t == "screenshot" or t == "a screenshot"):
                    os.system("sleep 0.5 && xdotool key 'Insert'")

            except:

                print("Couldn't do it")

     # Error excetions
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        loopme = 1

    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
        loopme = 1
