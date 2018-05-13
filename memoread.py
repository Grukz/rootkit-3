from win32process import GetWindowThreadProcessId
from win32api import OpenProcess
from win32gui import FindWindow
import ctypes

ADDR = 0x476020

def memoread(NAME, ADDR):

	ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory
	PROCESS_ALL_ACCESS = 0x1F0FFF

	while 1:

		HWND = FindWindow(None, NAME)
		if HWND == 0:
			continue
		else:
			break

	print("%s HWND: %i" % (NAME, HWND))
	PID = GetWindowThreadProcessId(HWND)[1]
	print("%s PID: %i" % (NAME, PID))

	try:
		HANDLE = OpenProcess(PROCESS_ALL_ACCESS, 0, PID)
	except Exception as error:
		print("OpenProcess error:", error)
		exit(0)

	print("%s HANDLE: %i" % (NAME, HANDLE.handle))
	buffer_size = 256
	buffer = ctypes.create_string_buffer(buffer_size)

	ReadProcessMemory(HANDLE.handle, ADDR, buffer, buffer_size, 0)

	return buffer.raw