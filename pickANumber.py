#for pythonista

import random
import ui

def rank(sender):
	print ('test')

	def closeme(sender):
		v_results.close()
		

	minNum = int(v_main['minNum'].text)
	maxNum = int(v_main['maxNum'].text)
	randPick = random.randint(minNum,maxNum)
	valDict={}
		
	v_results=ui.load_view('pANpopout')
	v_results.present('poppver')
	
	resultViewBox = v_results['results']
	resultViewBox.text=('hi')
	for i in range (3):
		resultViewBox.text+=('jello\n')


v_main=ui.load_view('pickANumber')
v_main.present('fullscreen')


'''


  def rank(sender):
    print ("hello")
    def closeme(sender):
      self.v_results.close()


    for i in range(6):
      iName='name_'+str(i)
      iNum='num_'+str(i)
      if self.v_main[iNum].text:
        valDict[self.v_main[iName].text]=int(self.v_main[iNum].text)

    diffNamesDict={}
    for nameVal in valDict:
      valDiff = abs(valDict[nameVal]-randPick)
      diffNamesDict[nameVal]=valDiff

    resultList = [];

    for key,value in sorted(diffNamesDict.items(),key=lambda x:x[1]):
      nameResult = f"{key}: \u0394{value}"
      resultList.append(nameResult)

    self.v_results = ui.load_view('pANpopout')
    self.v_results.present('popover')
    resultViewBox = self.v_results['results']
    resultViewBox.data_source=resultList

PickANum()
'''
