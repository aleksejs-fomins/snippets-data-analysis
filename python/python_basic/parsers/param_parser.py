

## BASIC COLUMN PARAMETER FILE PARSER
## Algorithm:
## 1) Read all lines in the file
## 2) Delete from line all initial and final spaces and tabs
## 3) Find first instance of #, delete everything afterwards
## 4) Find first instance of space/tab in the remainder. Put all before to key, all after to val

def param_parser(filepathname):
  paramdict = {}
  with open(filepathname) as thisfile:
    for line in thisfile:
      # Strip tabs and white space
      lstripped = line.strip()
      
      # Strip comments
      commentidx = lstripped.find('#')
      if commentidx >= 0:
	lstripped = lstripped[:commentidx]
      
      if len(lstripped) > 0:
	spacesplit = lstripped.find(' ')
	tabsplit = lstripped.find('\t')
	
	if (spacesplit < 0) and (tabsplit < 0):
	  raise ValueError('Bad format in line: \n' + line)
	elif spacesplit < 0:
	  thissplit = tabsplit
	elif tabsplit < 0:
	  thissplit = spacesplit
	else:
	  thissplit = min(spacesplit, tabsplit)
	
	thiskey = lstripped[:thissplit].strip()
	thisval = lstripped[thissplit:].strip()
	
	if thiskey in paramdict:
	  print("Warning, duplicate key " + thiskey)
	
	paramdict[thiskey] = thisval
  
  return paramdict