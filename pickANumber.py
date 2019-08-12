#for pythonista

import random
import ui
view=ui.load_view('pickANumber')
view.present('fullscreen')

def rank(sender):
	pass

minNum = int(view['minNum'].text)
maxNum = int(view['maxNum'].text)
randPick = random.randint(minNum,maxNum)
print(randPick)

valDict={}
for i in range(6):
	iName='name_'+str(i)
	iNum='num_'+str(i)
	if view[iNum].text:
		valDict[view[iName].text]=int(view[iNum].text)

diffNamesDict={}
for nameVal in valDict:
	valDiff = abs(valDict[nameVal]-randPick)
	diffNamesDict[nameVal]=valDiff

for key,value in sorted(diffNamesDict.items(),key=lambda x:x[1]):
	print(f"{key}: \u0394{value}")


#print(randPick)

