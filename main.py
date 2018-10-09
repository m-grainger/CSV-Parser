import glob

def concat(indir="<directory goes here!>\\"):
	os.chdir(indir) # set current dir to working dir
	fileList = glob.glob("*.csv")
	master_list = []
	for fn in fileList:
		colnames = ['Column1','Column2']
		data = pandas.read_csv(f'<insert directory here>\\{fn}', names=colnames, header = None)
		c1 = data.Column1.tolist()
		c1.pop(0)
		c2 = data.Column2.tolist()
		c2.pop(0)
		master_list.append(c2)
	print(master_list)	
  
concat()
