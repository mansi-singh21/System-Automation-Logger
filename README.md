# 🛡️ System Automation Tool for Security Logging

A background keylogger designed strictly for controlled security research, ethical hacking labs, and system automation learning.

## 📌 Overview

This tool captures user keystrokes with input debouncing, logs them into a file, and sends the logs automatically via email using a secure SMTP test service (Mailtrap).

> ⚠️ **Disclaimer**: This tool is built **strictly for educational purposes and ethical security research**. It must only be used in sandbox or controlled environments. Do not use on any system without proper authorization.

---

## 🔧 Features

- Captures keystrokes silently in the background using `pynput`
- Input debouncing to avoid repeated logging
- Logs are stored in a file and sent via Mailtrap every 80 seconds
- GUI-less background execution using pure Python
- Automatically clears logs after dispatch

---

## 💡 How It Works

1. `pynput` is used to listen for keypresses.
2. Input is logged to a text file (`loggeddata.txt`).
3. Every 80 seconds or when `Esc` is pressed, the log is:
   - Read and emailed using `smtplib` through Mailtrap.
   - Cleared after sending.

---

## 🧪 Tech Stack

- Python 3
- `pynput`
- `smtplib`, `email.mime`
- Mailtrap (for email testing)

---

## 🔐 Mailtrap Setup

1. Create a [Mailtrap](https://mailtrap.io/) account.
2. Use sandbox credentials (SMTP host, port, username, password).
3. Replace the placeholders in `keylogger.py`:

```python
server.login('your_mailtrap_username', 'your_mailtrap_password')


⚠️ Disclaimer This tool is strictly for educational and ethical use only. Do not use it on systems you do not own or have permission to test. I do not promote illegal activity of any kind.

Mansi Singh, GitHub: https://github.com/mansi-singh21
