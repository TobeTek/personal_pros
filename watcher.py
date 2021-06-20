from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
import shutil
import os
if __name__ == '__main__':
	patterns = ['*']
	ignore_patterns = None
	ingnore_directories = False
	case_sensitive = True
	path = r'C:\Users\Pc\Test'
	def on_created(event):
		print(f"Hey ,{event.src_path} has been created!")
		init = os.path.join(path, event.src_path)
		print(init)
		print(event.src_path)
		a = (event.src_path).split(r"\\")
		print(a[-1])
		final = os.path.join(r'C:\Users\Pc\Testy', a[-1])
		print(final)
		shutil.move(event.src_path, final )


	def on_deleted(event):
		print(f"Somebody deleted {event.src_path}!")

	def on_modified(event):
		print(f"Hey {event.src_path} has been modified.")

	def on_moved(event):
		print(f"Hey {event.src_path} has been moved to {event.dest_path}")

	my_event_handler = PatternMatchingEventHandler(patterns,ignore_patterns,ingnore_directories,case_sensitive)
	my_event_handler.on_moved = on_moved
	my_event_handler.on_created = on_created
	my_event_handler.on_deleted = on_deleted
	my_event_handler.on_modified= on_modified



	go_recursively = True

	my_observer = Observer()

	my_observer.schedule(my_event_handler, path, recursive = True)

	my_observer.start()

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		my_observer.stop()
		my_observer.join()