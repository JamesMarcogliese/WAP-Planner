#!/usr/bin/python

"""Main script.

"""

import math
from graphics import *

def main():
	"""Main loop for the program."""
	
	# Declare global variables --------------------
	
	frequencyBand = None
	dataRateRequirements = None
	frequencyBand = None
	maxExpectedClients = None
	roomLength = None
	roomWidth = None
	pointList = []
	chanTouch = []
	rectDict = dict()
	circDict = dict()
	chanDict = dict()
	guiDict = dict()
	chanIdx = 0
	padding = 50

	#Input GUI --------------------
	
	win = GraphWin('WAP-Planner', 400, 400) # create window

	titleText = Text(Point(200, 50), "WAP-Planner")	# create text objects
	titleText.setStyle("bold")
	lengthText = Text(Point(105, 100), "Room Length (meters): ")
	widthText = Text(Point(102, 150), "Room Width (meters): ")
	clientsText = Text(Point(122, 200), "Maximum Expected Clients: ")
	bandText = Text(Point(85, 250), "Frequency Band: ")
	rateText = Text(Point(114, 300), "Data Rate Requirements: ")
	
	lengthInputBox = Entry(Point(325, 100), 4) # create input box objects
	widthInputBox = Entry(Point(325, 150), 4)
	clientsInputBox = Entry(Point(325, 200), 4)
	
	twoFourRectangle = Rectangle(Point(265, 240), Point(324, 260)) # create rectangle buttons
	fiveRectangle = Rectangle(Point(325, 240), Point(385, 260))
	lowRectangle = Rectangle(Point(265, 290), Point(304, 310))
	medRectangle = Rectangle(Point(305, 290), Point(344, 310))
	highRectangle = Rectangle(Point(345, 290), Point(385, 310))
	submitRectangle = Rectangle(Point(150, 350), Point(250, 380))
	guiDict[0] = twoFourRectangle
	guiDict[1] = fiveRectangle
	guiDict[2] = lowRectangle
	guiDict[3] = medRectangle
	guiDict[4] = highRectangle
	guiDict[5] = submitRectangle
	
	lowRectangleText = Text(lowRectangle.getCenter(), "Low") # creat text for buttons
	medRectangleText = Text(medRectangle.getCenter(), "Med")
	highRectangleText = Text(highRectangle.getCenter(), "High")
	twoFourRectangleText = Text(twoFourRectangle.getCenter(), "2.4 GHz")
	fiveRectangleText = Text(fiveRectangle.getCenter(), "5 GHz")
	submitRectangleText = Text(submitRectangle.getCenter(), "Generate")
	lowRectangleText.setSize(10)
	medRectangleText.setSize(10)
	highRectangleText.setSize(10)
	twoFourRectangleText.setSize(10)
	fiveRectangleText.setSize(10)
	
	titleText.draw(win)	# draw all objects onto window
	lengthText.draw(win)
	widthText.draw(win)
	clientsText.draw(win)
	bandText.draw(win)
	rateText.draw(win)
	lengthInputBox.draw(win)
	widthInputBox.draw(win)	
	clientsInputBox.draw(win)
	lowRectangle.draw(win)
	medRectangle.draw(win)
	highRectangle.draw(win)
	lowRectangleText.draw(win)
	medRectangleText.draw(win)
	highRectangleText.draw(win)
	twoFourRectangle.draw(win)
	fiveRectangle.draw(win)
	twoFourRectangleText.draw(win)
	fiveRectangleText.draw(win)
	submitRectangle.draw(win)
	submitRectangleText.draw(win)
	
	def contains(rectangle, point):	# function to check if coordinate of click is within a button area
		return (rectangle.getP1().getX() <= point.getX() <= rectangle.getP2().getX() and
			rectangle.getP1().getY() <= point.getY() <= rectangle.getP2().getY())
	
	loop = True # loop that will check if user clicks on a button 
	while (loop):
		clickPoint = win.getMouse() # get click point
		for i in range (6):
			if (contains(guiDict[i],clickPoint)): # if within a button area...
				guiDict[i].setOutline("red") # set button to red...
				if (i == 0): # change other option back to black and save selection
					guiDict[1].setOutline("black")
					frequencyBand = 1
				elif (i == 1):
					guiDict[0].setOutline("black")
					frequencyBand = 2
				elif (i == 2):
					guiDict[3].setOutline("black")
					guiDict[4].setOutline("black")
					dataRateRequirements = "low"
				elif (i == 3):
					guiDict[2].setOutline("black")
					guiDict[4].setOutline("black")
					dataRateRequirements = "med"
				elif (i == 4):
					guiDict[2].setOutline("black")
					guiDict[3].setOutline("black")
					dataRateRequirements = "high"
				elif (i == 5): # check if all data is supplied, if so, advance to solution and close window
					if (lengthInputBox.getText() and widthInputBox.getText() and 
						clientsInputBox.getText() and frequencyBand and dataRateRequirements):
						roomLength = math.fabs(float(lengthInputBox.getText()))
						roomWidth =  math.fabs(float(widthInputBox.getText()))
						maxExpectedClients =  math.fabs(int(clientsInputBox.getText()))
						win.close()
						loop = False
	
	#Scaler --------------------
	
	originalRoomLength = roomLength
	originalRoomWidth = roomWidth
	
	if (roomLength > 500 or roomWidth > 500): # scales supplied dimensions of room to available window space
		if (roomLength >= roomWidth):
			scale = roomLength - 500
		elif (roomLength < roomWidth):
			scale = roomWidth - 500
		roomLength -= scale
		roomWidth -= scale
	elif (roomLength < 500 or roomWidth < 500):
		if (roomLength >= roomWidth):
			scale = 500 - roomLength
		elif (roomLength < roomWidth):
			scale = 500 - roomWidth
		roomLength += scale
		roomWidth += scale
		
	#Solution Generator --------------------
	
	if (frequencyBand == 1): # selects appropriate channel list
		channels = [["1","blue"], ["6","red"], ["11","green"]]
	elif (frequencyBand == 2):
		channels = [
			["36","blue"], ["40","red"], ["44","green"], ["48","aqua"], ["52","brown"], 
			["56","crimson"], ["60","cyan"], ["64","fuchsia"], ["100","gold"], ["104","gray"], 
			["108","dark green"], ["112","indigo"], ["116","lime"], ["120","maroon"], ["124","olive"], 
			["128","orange"], ["132","orchid"], ["136","peru"], ["140","pink"], ["149","purple"], 
			["153","silver"], ["157","teal"], ["161","tomato"]
			]
	
	if (dataRateRequirements == 'high'): # calc minimum required APs based on data rate requirements
		minNumWap = math.ceil(float(maxExpectedClients) / 20.0) # 20 clients per AP  
	elif (dataRateRequirements == 'med'): 
		minNumWap = math.ceil(float(maxExpectedClients) / 25.0) # 25 clients per AP
	elif (dataRateRequirements == 'low'): 
		minNumWap = math.ceil(float(maxExpectedClients) / 30.0) # 30 clients per AP

	win = GraphWin('WAP-Planner', 1000, 700) # create a window
	
	room = Rectangle(Point(padding, padding), Point(roomWidth + padding, roomLength + padding)) # create a rectangle to represent dimentions of room
	room.draw(win)
	
	numColumns = math.ceil(math.sqrt(minNumWap)) # determine smallest num of columns
	numRows = math.ceil(float(minNumWap) / float(numColumns)) # determine smallest num of rows per num of columns
	
	#print numColumns
	#print numRows
	#print roomLength, roomWidth, maxExpectedClients
	
	widthOfSubRect = roomWidth / numColumns # width of sub spaces within room
	lengthOfSubRect = roomLength / numRows # length of sub spaces within room
	
	for i in range(0, int(numColumns)): # generate list of coordinates for sub spaces within room
		for j in range(0, int(numRows)):
			pointList.append([[(i * widthOfSubRect) + padding, (j * lengthOfSubRect) + padding],[((i + 1) * widthOfSubRect) + padding,((j + 1) * lengthOfSubRect) + padding]])
	
	for i in range(0,len(pointList)): # create circles using coordinates of sub spaces (rectangles created first for testing)
		rectDict[i] = Rectangle(Point(pointList[i][0][0],pointList[i][0][1]), Point(pointList[i][1][0],pointList[i][1][1]))
		circDict[i] = Circle(rectDict[i].getCenter(),(math.hypot(widthOfSubRect,lengthOfSubRect) / 2))
		
		if (frequencyBand == 1): # fill circles with chosen channel and color accordingly
			chanTouch.append(chanDict.get((i - numRows), Text(Point(0, 0), "0")).getText()) # check below of space to see what channel was used
			chanTouch.append(chanDict.get((i - numRows), Text(Point(0, 0), "0")).getText()) # since they overlap, have a weight of three
			chanTouch.append(chanDict.get((i - numRows), Text(Point(0, 0), "0")).getText())
			if (i % numRows != 0): # check if channel is not touching a wall, if so, check to the left and diagonal left and right below
				chanTouch.append(chanDict.get((i - 1), Text(Point(0, 0), "0")).getText()) # check to the left
				chanTouch.append(chanDict.get((i - 1), Text(Point(0, 0), "0")).getText()) # since range overlaps, have a weight of three
				chanTouch.append(chanDict.get((i - 1), Text(Point(0, 0), "0")).getText())
				chanTouch.append(chanDict.get((i - numRows - 1), Text(Point(0, 0), "0")).getText()) # left diagonal
				chanTouch.append(chanDict.get((i - numRows + 1), Text(Point(0, 0), "0")).getText()) # right diagonal
			elif (i % (numRows - 1 + numRows) == 0): # if deciding for AP on right side
				chanTouch.append(chanDict.get((i - numRows - 1), Text(Point(0, 0), "0")).getText()) # left diagonal
				chanTouch.append(chanDict.get((i - 1), Text(Point(0, 0), "0")).getText()) # check to the left
				chanTouch.append(chanDict.get((i - 1), Text(Point(0, 0), "0")).getText()) # since range overlaps, have a weight of three
				chanTouch.append(chanDict.get((i - 1), Text(Point(0, 0), "0")).getText())
			elif (i % numRows == 0): # if deciding for AP on left side
				chanTouch.append(chanDict.get((i - numRows + 1), Text(Point(0, 0), "0")).getText()) # right diagonal
			freq1 = chanTouch.count(channels[0][0])
			freq6 = chanTouch.count(channels[1][0])
			freq11 = chanTouch.count(channels[2][0])
			#print freq1, freq6, freq11
			
			if (freq1 <= freq6 and freq1 < freq11): # select the channel least used 
				chanIdx = 0
			elif (freq6 < freq1 and freq6 < freq11):
				chanIdx = 1
			else:
				chanIdx = 2
				
			circDict[i].setOutline(channels[chanIdx][1]) # change color and set to chosen channel
			chanDict[i] = Text(rectDict[i].getCenter(), channels[chanIdx][0])	
			chanDict[i].setTextColor(channels[chanIdx][1])
			del chanTouch[:]
		else:
			circDict[i].setOutline(channels[chanIdx][1])
			chanDict[i] = Text(rectDict[i].getCenter(), channels[chanIdx][0]) # if 5Ghz, simply place one after another
			chanDict[i].setTextColor(channels[chanIdx][1])
			chanIdx += 1
		
		circDict[i].draw(win)
		chanDict[i].draw(win)
		
	#Graphical additions --------------------
	originalLengthStr = str(originalRoomLength) + " m"
	originalWidthStr = str(originalRoomWidth) + " m"
	apStr = str(len(circDict)) + " WAPs required to support " + str(int(maxExpectedClients)) + " " + dataRateRequirements + " data-rate clients" 
	apStr2 = "in a " + str(roomLength) + "m x " + str(roomWidth) + "m room." 
	
	
	lengthText = Text(Point((roomWidth + padding + 40), (roomLength / 2 + padding)), originalLengthStr)
	widthText = Text(Point((roomWidth / 2 + padding), (roomLength + padding + 30)), originalWidthStr)
	apText = Text(Point((roomWidth + padding + 250), (padding + 50)), apStr)
	apText2 = Text(Point((roomWidth + padding + 250), (padding + 70)), apStr2)
	
	
	lengthText.draw(win)
	widthText.draw(win)
	apText.draw(win)
	apText2.draw(win)
		
	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()