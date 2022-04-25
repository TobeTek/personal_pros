import os 
import shutil
import sys

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from collections import defaultdict



targets = defaultdict(list)
targets = {'TT-Docs':["docx", "txt", "doc"],'TT-Music':["m4a","mp3","wav"],'TT-Apps':["exe",'msi'], 'TT-Video':["mp4","ts","mpg","3gp"], 'TT-PyWheels':["whl"],'TT-Images':["png","jpeg","jpg"], 'TT-Books':["pdf","epub"]}


if __name__ == '__main__':
	print('\r\nWelcome to TT-Util | Made by TobeTek')
	print('')
	
	loc =sys.argv[1] if len(sys.argv) > 1 else input('Enter the folder path : ')
	custom = int(input('Would you like the program to create custom folders\nfor unknown file types?     (Yes = 1 , No = 0)\n :'))	
	
	
	
	try:
		for folder in list(targets.keys()):
			os.chdir(os.path.join(loc,folder))
			os.chdir('..')

		print("\n Done checking directories\n Transfering files now...")
	
	except IOError:
		print(" Did not find directories. Making directories.\n")
		try:
			for folder in list(targets.keys()):
				os.mkdir(os.path.join(loc,folder))

		except FileExistsError:
			print(" Unable to complete process due to abnormalities. Try changing target folder names or contact us for help. ")
			sys.exit()


	class  MyHandler(FileSystemEventHandler):

		# def on_moved(self,event):
		# 	print(f'{event.src_path} has been moved from{event.dest_path}')
		# def on_created(self,event):
		# 	print(f'{event.src_path} has been created.')

		def on_modified(self,event):
			time.sleep(10)
			
			head , tail = os.path.split(event.src_path)
			
			extension = tail.split('.')[-1]
	
			success = False
			if (os.path.isfile(event.src_path)):
				print(f'{tail} has been modified and being moved...')

				for folder in targets:
					if (extension.lower() in targets[folder]):
						init = os.path.join(loc, tail)
						final = os.path.join(loc,folder ,tail)
						try:
							shutil.move(init, final)
						except FileNotFoundError:
							print('This program is is still buggy, pls ignore.')
						except PermissionError:
							print('Make sure your system is not using the file and try again.')

						success = True

						
				if success == False and custom:
					try:
						os.mkdir(os.path.join(loc,extension.upper()))
						targets[extension.upper()] = [extension]
						init = os.path.join(loc, tail)
						print(init)
						final = os.path.join(loc,extension.upper() ,tail)
						print(final)		
						shutil.move(init,final)
					
					except FileExistsError:
						print('Unable to handle extension {} .'.format(extension)) 
		


	event_handler = MyHandler()
	observer = Observer()
	observer.schedule(event_handler,loc,recursive = True)
	observer.start()
	
	try:
		while True:
			
			time.sleep(5)
			
	except KeyboardInterrupt:
		observer.stop()

	observer.join()
	
	print(" Your folder has been arranged.\n Thank You for using TT-Util ...")