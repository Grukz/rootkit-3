#include <iostream>
#include <windows.h>
#include <TlHelp32.h>

using namespace std;
DWORD ADDR = 0x476004;
DWORD PID;

int main()
{
	HWND Window = FindWindow(0, "target");
	cout << "HWDN:" << Window << endl;
	GetWindowThreadProcessId(Window, &PID);
	cout << "PID:"<< PID << endl;
	HANDLE Process = OpenProcess(PROCESS_ALL_ACCESS, FALSE, PID);
	char Buffer[256];
	ReadProcessMemory(Process, (LPCVOID)ADDR, &Buffer, sizeof(Buffer), 0);
	cout << "Address contains:" << Buffer << endl;
}
