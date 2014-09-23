#this python script is used to write the makefile and set up the files that the user wants and sets up a git repo

#function for writting c++ files
def writeCpp(fileAndPath):
	writefile = open(fileAndPath, "w")
	writefile.write("#include <iostream>\n#include <stdio.h>\n#include <string.h>\n\nusing namespace std;\n\nint main(int argc, char *argv[])\n{\n\n}")
	writefile.close()
	return

#function for starting python files
def writePy(fileAndPath):
	writefile = open(fileAndPath, "w")
	writefile.write("#makepro started this for you, ain't that cool?\n")
	writefile.close()
	return

#function for writing c# files
def writeCs(fileAndPath):
	writefile = open(fileAndPath, "w")
	writefile.write("using System;\nusing System.Collections.Generic;\nusing System.Linq;\nusing System.Text;\nnamespace DerivativeV2._4\n{\nclass Program\n    {\n        static void Main(string[] args)\n        {\n\n}\n}\n}\n}")
	writefile.close()
	return

#function for making headers
def writeH(fileAndPath):
	writefile = open(fileAndPath, "w")
	writefile.write("//makepro started this header for you, ain't that cool?\n")
	writefile.close()
	return

#function for writing a Makefile
def writeMake(fileAndPath, files):
	writefile = open(fileAndPath, "w")
	writefile.write("CXXFLAGS=-std=gnu++11\n\nall:")
	for nowExe in files:
		new = ' ' + nowExe
		writefile.write(new)
	writefile.write("\n")
	writefile.close()
	return

#function for making unidentified files
def writeOther(fileAndPath):
	writefile = open(fileAndPath, "w")
	writefile.write("Sorry I couldn't recognize this file type,\nemail willnorvelle@gmail.com and let me know how to set it up\nand maybe I can update makepro.\n")
	writefile.close()
	return

def writeTxt(fileAndPath):
	writefile = open(fileAndPath, "w")
	writefile.write("//makepro started this text file for you, ain't that cool?\n")
	writefile.close()
	return

filesfile = open("files.txt", "r")

folder = filesfile.readline()
folder = folder[0 : (len(folder) - 1)]

fileList = filesfile.readlines()

needMake = 0
filesForMake = []

readpath = "./" + folder + "/" + "README.md"
readFile = open(readpath, "w")
readFile.write("This project was set up by makepro\nIt contains:\n")

for filename in fileList:
	extension = filename.split('.')
	extensionTrueish = extension[1]
	extensionLen = len(extension[1]) - 1
	extensionTrue = extensionTrueish.strip()

	suffix = extension[0]

	realFile = filename.strip()
	path = "./" + folder + "/" + realFile
	READrealFile = realFile + "\n"
	readFile.write(READrealFile)

	if(extensionTrue == "cpp"):
		writeCpp(path)
		needMake = 1
		filesForMake.append(suffix)
	elif(extensionTrue == "py"):
		writePy(path)
	elif(extensionTrue == "cs"):
		writeCs(path)
	elif(extensionTrue == "h"):
		writeH(path)
	elif(extensionTrue == "txt"):
		writeTxt(path)
	else:
		writeOther(path)

readFile.close()

makepath = "./" + folder + "/" + "Makefile"
if(needMake == 1):
	writeMake(makepath, filesForMake)

filesfile.close()