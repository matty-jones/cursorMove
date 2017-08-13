import pynput as inp
import _thread
import time as T

mouseController = inp.mouse.Controller()

shortcut = ['ctrl', 'shift', '?']
currentlyPressedKeys = []


def on_press(key):
    global currentlyPressedKeys
    if key not in currentlyPressedKeys:
        currentlyPressedKeys.append(key)
        print("Key", key, "pressed")
        print(currentlyPressedKeys)


def on_release(key):
    global currentlyPressedKeys
    currentlyPressedKeys[:] = [pressedKey for pressedKey in\
            currentlyPressedKeys if pressedKey != key]
    print("Key", key, "released")
    print(currentlyPressedKeys)


def checkForCombo():
    while True:
        keyValues = []
        for key in currentlyPressedKeys:
            try:
                keyValues.append(key.name)
            except:
                keyValues.append(key.char)
        print(set(keyValues), set(shortcut), set(keyValues) == set(shortcut))
        if set(keyValues) == set(shortcut):
            print("MOVING MOUSE")
            moveMouse()
        T.sleep(0.1)


def moveMouse():
    mouseController.position = (10,10)


if __name__ == "__main__":
    with inp.keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        _thread.start_new_thread(checkForCombo, ())
        listener.join()
