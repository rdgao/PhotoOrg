import os, sys, PhotoOrg

if __name__=="__main__":

	print '+'*40,'\n', 'PhotoOrg','\n','+'*40
	if len(sys.argv)==1:
		mydir = '.'
	else:
		mydir = sys.argv[1]

	PhotoOrg.renameAll(mydir)
	PhotoOrg.getStats(mydir)
