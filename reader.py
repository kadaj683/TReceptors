#!/usr/local/bin/python3
import re
class CDR:
	def __repr__(self):
		return "CDR: %s, V: %s, D: %s, J: %s" % (self.cdr3, self.v, self.d, self.j)



CDRPattern = re.compile('(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.+?[^,])\s+(.+?[^,])\s+((.+?[^,])\s+)?(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s+(.+?)\s*\n')
chainPattern = re.compile('(.+?),.*')
variantPattern = re.compile('(.+?)\s+(.+?)\s+.*')

def readFirst(str):
	match = re.match(chainPattern,str)
	if match:
		return match.group(1)
	else:
		return str


def readCDR(str,vVariants,dVariants,jVariants):
	cdr = CDR()
	match = re.match(CDRPattern,str)
	cdr.cdr3 = match.group(3)
	cdr.vname = readFirst(match.group(5))
	cdr.v = vVariants[cdr.vname]
	cdr.jname = readFirst(match.group(6))
	cdr.j = jVariants[cdr.jname]
	if match.group(8):
		cdr.dname = readFirst(match.group(8))
		cdr.d = dVariants[cdr.dname]
	else:
		cdr.dname = None
		cdr.d = None
	cdr.vlast = int(match.group(9))
	cdr.dfirst = int(match.group(10))
	cdr.dlast = int(match.group(11))
	cdr.jfirst = int(match.group(12))
	cdr.n_vd = int(match.group(13))
	cdr.n_dj = int(match.group(14))
	cdr.total = int(match.group(15))
	print(cdr)
	return cdr

def readVariant(str):
	match = re.match(variantPattern,str)
	key = match.group(1)
	value = match.group(2)
	return (key,value)


def readCDRFile(fileName,vVariants,dVariants,jVariants):
	cdrs = []
	with open(fileName,"r") as file:
		strings = file.readlines()
		for i in range(1,len(strings)):
			print(i)
			print(strings[i])
			cdrs.append(readCDR(strings[i],vVariants,dVariants,jVariants))
	return cdrs

def readVariantsFile(fileName,variantsDict):
	with open(fileName,"r") as file:
		strings = file.readlines()
		for i in range(1,len(strings)):
			#print(i)
			(key,value) = readVariant(strings[i])
			variantsDict[key] = value
	return variantsDict


# vVariants = {}
# dVariants = {}
# jVariants = {}
# readVariantsFile("TRB/trbv.txt",vVariants)
# readVariantsFile("TRB/trbd.txt",dVariants)
# readVariantsFile("TRB/trbj.txt",jVariants)
# cdrs = readCDRFile("TwD2_A.txt",vVariants,dVariants,jVariants)



#for cdr in cdrs:
#	print(cdr)
#for k in jVariants:
#	print("%s %s" % (k,jVariants[k]))







#cdr = CDR();
#cdr.aaa = "bbb";
#print(cdr.aaa)