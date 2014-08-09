#Richard Gao, 2014
#Library of code for image file manipulation 
#and statistic gathering


from os import listdir, path, rename
from datetime import datetime
import PhotoOrg

def findFiles(dir):
	#get a list of all pictures in the directory
	dir = checkFolder(dir)
	if dir is None: return
	#search for target extensions
	imgExt = ("jpg", "jpeg", "png", "bmp", "mov", "mp4")
	allFiles = []
	for file in listdir(dir):
		#case invariance
		if file.lower().endswith(imgExt):
			allFiles.append(dir+file)
	print len(allFiles), "files found."
	#return a list of all target files		
	return allFiles

def getFileTime(f_name):
	#return the modified time of the file f_name, both in epoch and in regular time
	ts = path.getmtime(f_name)
	tout = (ts, str(datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')))
	return tout

def renameAll(dir):
	#rename all files in a directory based on their date
	#check for invalid directory
	dir = checkFolder(dir)
	if dir is None: return
	#search for all files in a folder
 	allFiles = findFiles(dir)
	numRenamed = 0
	for file in allFiles:		
		#find file extension
		ext = path.splitext(file)[1].lower()
		#get target name from photo date
		nameDate = getFileTime(file)[1]
		#rename with regular time
		newName = dir+ nameDate + ext
		if not file==newName:
			#rename only if file name is not already proper name	
			ctr=0
			while path.exists(newName):
				#if path name already exists and is not itself, get version postfix
				if newName==file:
					break
				else:
					#in case of duplicate file names
					ctr+=1
					newName = dir+nameDate+"_V"+str(ctr)+ext
			if not file==newName:
				rename(file,newName)
				numRenamed+=1
	#report print statistics
	print '%'*25,'\n',numRenamed,'/',len(allFiles), "files renamed in:\n",dir,'\n','%'*25

def getStats(dir):
	#check for invalid directory
	dir = checkFolder(dir)
	if dir is None: return
	#search for all files in a folder
 	allFiles = findFiles(dir)
 	stats=[]
 	for file in allFiles:
 		stats.append(getFileTime(file)[0])

 	print stats


def checkFolder(dir):
	#fix directory if doesn't end with '/'
	if not dir.endswith("/"):
		dir = dir + '/'
	#check for existence of directory
	if path.exists(dir):
		return dir
	else:
		print '%'*25+"\nGiven path does not exist: \n"+dir+'\n'+'%'*25
		return