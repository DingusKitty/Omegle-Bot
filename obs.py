import pywinauto
import pywinauto.keyboard
import pywinauto.mouse
from pywinauto.application import Application
import pywinauto.controls.menuwrapper
import win32gui

# Doesn't work due to OBS limitations not allowing start from nonparent dir
# app = Application().start("C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe")

# Connect to the OBS application using the UI Automation (UIA) backend
app = Application(backend='uia').connect(title_re='OBS 27\.2\.4 \(64-bit, windows\) - Profile: Untitled - Scenes:.*')
obs_app = app.OBS272464BitWindowsProfileUntitledScenesOmegleActivism

# Uncomment to get diag control identifiers for OBS window
# obs_app.print_control_identifiers()

# Set focus to OBS application
window = app.window(title_re='OBS 27\.2\.4 \(64-bit, windows\) - Profile: Untitled - Scenes:.*')

# if not window.is_visible():
#     # Restore the window
#     win32gui.ShowWindow(window.wrapper_object(), 9)  # Restore

# Window Controls
window.set_focus()
# window.maximize()

def toggle_title():
    window.set_focus()
    pywinauto.keyboard.send_keys('%1')

def toggle_gamechangers():
    window.set_focus()
    pywinauto.keyboard.send_keys('^6')

def toggle_food():
    window.set_focus()
    pywinauto.keyboard.send_keys('^2')

def toggle_cam():
    window.set_focus()
    pywinauto.keyboard.send_keys('^3')

def cruelty():
    window.set_focus()
    pywinauto.keyboard.send_keys('^1')

# Possibly Future Implementation
def start_recording():
    window.set_focus()
    try:
        click_start_rec = obs_app.child_window(title="Start Recording", auto_id="OBSBasic.controlsDock.controlsDockContents.recordButton",
                 control_type="CheckBox").click()
    except:
        print("Already Recording")

def stop_recording():
    window.set_focus()
    try:
        click_stop_rec = obs_app.child_window(title="Stop Recording", auto_id="OBSBasic.controlsDock.controlsDockContents.recordButton", control_type="CheckBox").click()
    except:
        print("Already Stopped")

# connect_obs()
# start_recording()
# stop_recording()
# toggle_title()


