#include <iostream>
#include <conio.h>

using namespace std;

char test[256] = "Sample text for reading...";

int main()
{
	cout << "Addr: " << &test << endl;
	getch();
	return 0;
}
