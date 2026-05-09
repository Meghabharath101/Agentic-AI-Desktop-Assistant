import os
import subprocess
import platform as py_platform
import datetime
import requests
import webbrowser
import urllib.parse
import pywhatkit
import pyautogui
import time


# =========================================================
# SEARCH WEB USING CHROME
# =========================================================

def search_web(query):

    try:

        encoded_query = urllib.parse.quote(query)

        url = f"https://www.google.com/search?q={encoded_query}"

        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ]

        for chrome in chrome_paths:

            try:

                subprocess.Popen([chrome, url])

                return f"Searched Google for: {query}"

            except:
                continue

        return "Chrome not found."

    except Exception as e:

        return f"Search Error: {str(e)}"


# =========================================================
# SEND WHATSAPP MESSAGE
# =========================================================

def send_whatsapp_message(contact, message):

    try:

        # Auto add +91
        if not contact.startswith("+"):
            contact = "+91" + contact

        pywhatkit.sendwhatmsg_instantly(
            phone_no=contact,
            message=message,
            wait_time=30,
            tab_close=False
        )

        # Wait for WhatsApp to load
        time.sleep(8)

        # Press Enter to send
        pyautogui.press("enter")

        return f"WhatsApp message sent to {contact}"

    except Exception as e:

        return f"WhatsApp Error: {str(e)}"


# =========================================================
# SEND WHATSAPP GROUP MESSAGE
# =========================================================

def send_whatsapp_group_message(group_name, message):

    try:

        import webbrowser
        import pyautogui
        import time

        # Open WhatsApp Web
        webbrowser.open("https://web.whatsapp.com")

        # Wait for WhatsApp to fully load
        time.sleep(15)

        # CLICK WHATSAPP SEARCH BOX
        pyautogui.click(x=250, y=175)

        time.sleep(1)

        # Type group name
        pyautogui.write(group_name, interval=0.05)

        time.sleep(3)

        # Open chat
        pyautogui.press("enter")

        time.sleep(2)

        # Type message
        pyautogui.write(message, interval=0.03)

        time.sleep(1)

        # Send message
        pyautogui.press("enter")

        return (
            f"Sent WhatsApp group message to {group_name}"
        )

    except Exception as e:

        return f"WhatsApp Group Error: {str(e)}"

# =========================================================
# DETECT OPERATING SYSTEM
# =========================================================

def get_os():
    return py_platform.system().lower()


# =========================================================
# OPEN FILE
# =========================================================

def open_file(path):

    try:

        full_path = os.path.expanduser(path)

        os_type = get_os()

        if os_type == "darwin":
            subprocess.run(["open", full_path])

        elif os_type == "windows":
            os.startfile(full_path)

        elif os_type == "linux":
            subprocess.run(["xdg-open", full_path])

        return f"Opened: {full_path}"

    except Exception as e:

        return str(e)


# =========================================================
# OPEN APPLICATION
# =========================================================

def open_app(app_name):

    try:

        os_type = get_os()

        # WhatsApp
        if "whatsapp" in app_name.lower():

            webbrowser.open("https://web.whatsapp.com")

            return "Opened WhatsApp Web"

        # Chrome
        if "chrome" in app_name.lower():

            chrome_paths = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            ]

            for chrome in chrome_paths:

                if os.path.exists(chrome):

                    subprocess.Popen([chrome])

                    return "Opened Chrome"

            return "Chrome not found."

        # Normal opening
        if os_type == "darwin":

            subprocess.run([
                "open",
                "-a",
                app_name
            ])

        elif os_type == "windows":

            subprocess.run(
                f'start {app_name}',
                shell=True
            )

        elif os_type == "linux":

            subprocess.run([app_name])

        return f"Opened app: {app_name}"

    except Exception as e:

        return str(e)


# =========================================================
# CLOSE APPLICATION
# =========================================================

def close_app(app_name):

    try:

        os_type = get_os()

        variations = [
            app_name,
            app_name.title(),
            app_name.capitalize(),
            app_name.replace(" ", ""),
            app_name.title().replace(" ", "")
        ]

        if os_type == "windows":

            for name in variations:

                exe = (
                    name
                    if name.endswith(".exe")
                    else name + ".exe"
                )

                result = subprocess.run(
                    f'taskkill /F /IM "{exe}"',
                    shell=True,
                    capture_output=True,
                    text=True,
                    encoding="utf-8"
                )

                if result.returncode == 0:
                    return f"Closed: {app_name}"

            return (
                f"Could not close '{app_name}'. "
                "Make sure it is running."
            )

        return f"Close not supported on {os_type}"

    except Exception as e:

        return str(e)


# =========================================================
# LIST FILES
# =========================================================

def list_files(path="."):

    try:

        full_path = os.path.expanduser(path)

        return os.listdir(full_path)

    except Exception as e:

        return str(e)


# =========================================================
# RUN TERMINAL COMMAND
# =========================================================

def run_command(command):

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=5,
            encoding="utf-8"
        )

        return (
            result.stdout
            if result.stdout
            else result.stderr
        )

    except Exception as e:

        return str(e)


# =========================================================
# GET CURRENT TIME
# =========================================================

def get_time():

    return datetime.datetime.now().strftime(
        "%I:%M %p"
    )


# =========================================================
# GET CURRENT DATE
# =========================================================

def get_date():

    return datetime.date.today().strftime(
        "%B %d, %Y"
    )


# =========================================================
# GET WEATHER
# =========================================================

def get_weather(city="Kochi"):

    try:

        response = requests.get(
            f"https://wttr.in/{city}?format=3",
            timeout=5
        )

        if response.status_code == 200:
            return response.text.strip()

        return "Weather unavailable."

    except Exception as e:

        return f"Weather Error: {str(e)}"