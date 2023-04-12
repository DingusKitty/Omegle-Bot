from pywinauto.application import Application

# Start FireFox if needed
# app = Application().start("C:\\Program Files\\Mozilla Firefox\\firefox.exe").connect()

app = Application(backend="uia").connect(title_re=".*Omegle.* — Mozilla Firefox")
omegle = app.OmegleMozillaFirefox

# window_titles = ["Omegle: Talk to strangers! — Mozilla Firefox", "Omegle — Mozilla Firefox", "___Omegle___ — Mozilla Firefox", "¯¯¯Omegle¯¯¯ — Mozilla Firefox", "Omegle - Google Chrome (Incognito)"]
# for title in window_titles:
#     try:
#         app[title].exists()
#         print(f"Window with title '{title}' exists")
#     except Exception as e:
#         print(f"Window with title '{title}' does not exist: {e}")

# Uncomment to get diag control identifiers for Omegle
# omegle.print_control_identifiers()

# Select Omegle Window/Tab
window = app.window(title_re=".*Omegle.* — Mozilla Firefox")
window.set_focus()

if app:
    print("Omegle Window Found")
else:
    print("Omegle Window Not Found")

def stop():
    window.set_focus()
    omegle.child_window(title="Stop Esc", control_type="Button").wrapper_object().click()
    omegle.child_window(title="Really? Esc", control_type="Button").wrapper_object().click()
