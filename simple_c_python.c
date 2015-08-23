#include </usr/include/python2.7/Python.h>

int
main() {
	printf("\nThis is a simple program where C embeds python.\n");

	char filename[] = "MyPyFile.py";
	FILE *fp = fopen(filename, "r");

	//Initialize the python interpreter
	Py_Initialize();
	PyRun_SimpleFile(fp, filename);
	
	Py_Finalize();
	return 0;
}
