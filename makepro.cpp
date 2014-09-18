/*makepro is designed to simplify and automate makeing a new project
  argument[1] is the project folder name
  argument[2...n] are the files to be opened*/

#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main(int argc, char *argv[])
{
	//first create the project's directory
	FILE *f;
	char scriptName[40];
	sprintf(scriptName, ".mpScript.sh");
	f = fopen(scriptName, "w");
	fprintf(f, "mkdir %s\n", argv[1]);

	FILE *k;
	char readerName[40];
	sprintf(readerName, "files.txt");
	k = fopen(readerName, "w");
	fprintf(k, "%s\n", argv[1]);

	for(int i = 2; i <= (argc - 1); i++)
	{
		fprintf(k, "%s\n", argv[i]);
	}

	fclose(f);
	fclose(k);

	system("chmod +x ./.mpScript.sh");
	system("./.mpScript.sh");
	system("python ~/.makepro/makepro.py");
	system("rm .mpScript.sh");
	system("rm files.txt");
}	