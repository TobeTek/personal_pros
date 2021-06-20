import os 
import shutil
import sys
if __name__ == '__main__':
	if len(sys.argv) > 1 : 
		loc = sys.argv[1] 
	else: 
		loc = input('Enter path to folder to arrange.\n  :')
	targets = {'TT-Docs':["docx", "txt", "doc"],'TT-Music':["m4a","mp3","wav"],'TT-Apps':["exe",'msi'], 'TT-Video':["mp4","ts","mpg","3gp"], 'TT-PyWheels':["whl"],'TT-Images':["png","jpeg","jpg"], 'TT-Books':["pdf","epub"], "TT-Zips":['zip','gz']}
	print('Welcome to TT-Util | Made by TobeTek\r\n')
	for i,e in enumerate(targets):
		try:
			os.chdir(os.path.join(loc, e))
		
		except IOError:
			print(f"Did not find directory [{e}]. Making directories.\n")
			os.mkdir(os.path.join(loc, e))
	print("Done checking directories\nTransfering files now...")
	
	for file in os.listdir(loc):
		if file.endswith(".pdf"):
			init = os.path.join(loc, file)
			final = os.path.join(loc,'TT-Books' ,file)
			shutil.move(init, final)


		if file.endswith((".m4a",".mp3",".wav",".mid")):
			init = os.path.join(loc, file)
			final = os.path.join(loc,'TT-Music', file)
			shutil.move(init, final)

		if file.endswith((".exe",".msi",)):
			init = os.path.join(loc, file)
			final = os.path.join(loc, 'TT-Apps', file)
			shutil.move(init, final)

		if file.endswith((".mp4",".ts",".mpg",".3gp",))  :
			init = os.path.join(loc, file)
			final = os.path.join(loc,'TT-Video', file)
			shutil.move(init, final)

		if file.endswith(".whl") :
			init = os.path.join(loc, file)
			final = os.path.join(loc, "TT-PyWheels", file)
			shutil.move(init, final)


		if file.endswith((".png",".jpeg",".jpg",".JPG",)) :
			try:
				init = os.path.join(loc, file)
				final = os.path.join(loc, "TT-Images", file)
				shutil.move(init, final)
			except Exception as e:
				print(e)
		if file.endswith((".docx",".doc")) :
			init = os.path.join(loc, file)
			final = os.path.join(loc, "TT-Docs", file)
			shutil.move(init, final)

		if file.endswith((".zip",".gz")) :
			init = os.path.join(loc, file)
			final = os.path.join(loc, "TT-Zips", file)
			shutil.move(init, final)

	print("Your folder has been arranged.")