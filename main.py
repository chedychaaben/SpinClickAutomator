import pyautogui, time

#currentMouseX, currentMouseY = pyautogui.position()
#print(currentMouseX, currentMouseY)
searchbar = (392,130)
button = (922 , 124)
firstResultSettingsBar = (1308,235)
addToPlaylist = (1221,357)
SpinningRecordsLocation = (613,442)
#reclickonsearchbar againg
searches = []
for i in range(50):
    id = 428+i
    searches.append(f'Spinnin\' Sessions Radio - Episode #{str(id)}')

for s in searches:
    pyautogui.moveTo(searchbar)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(s)
    pyautogui.moveTo(button)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(firstResultSettingsBar)
    pyautogui.click()
    pyautogui.moveTo(addToPlaylist)
    pyautogui.click()
    pyautogui.moveTo(SpinningRecordsLocation)
    time.sleep(2)
    pyautogui.click()
    pyautogui.moveTo(searchbar)
    pyautogui.click()
    time.sleep(2)