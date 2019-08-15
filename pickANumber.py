#for pythonista

import random
import ui

def rank(sender):

	def closeme(sender):
		v_results.close()

	minNum = int(v_main['minNum'].text)
	maxNum = int(v_main['maxNum'].text)
	randPick = random.randint(minNum,maxNum)
	valDict={}

	for i in range(6):
		iName='name_'+str(i)
		iNum='num_'+str(i)
		if v_main[iNum].text:
			valDict[v_main[iName].text]=int(v_main[iNum].text)

	diffNamesDict={}
	for nameVal in valDict:
		valDiff = abs(valDict[nameVal]-randPick)
		diffNamesDict[nameVal]=valDiff

	v_results=ui.load_view('pANpopout')
	v_results.present('poppver')	
	resultViewBox = v_results['results']
	
	resultViewBox.text=f"The random number is {randPick}"
	for key,value in sorted(diffNamesDict.items(),key=lambda x:x[1]):
		nameResult = f"{key}: \u0394{value}"
		resultViewBox.text+=f"\n{nameResult}"
	
v_main=ui.load_view('pickANumber')
v_main.present('fullscreen')
