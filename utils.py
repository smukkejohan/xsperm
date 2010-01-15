from settings import BADWORDS
import re
 
def ireplace(self,old,new,count=0):
	''' Behaves like string.replace(), but does so in a case-insensitive
	fashion. '''
	pattern = re.compile(re.escape(old),re.I)
	return re.sub(pattern,new,self,count)
 
def filterBadWords(string):
	for w in BADWORDS:
		string = string.ireplace(w, "")
 
	return string
