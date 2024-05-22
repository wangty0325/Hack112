from cmu_graphics import *
import random


def onAppStart(app):
    app.width = 400
    app.height = 400
    app.countForText = 0
    app.doorOne = False
    app.doorTwo = False
    app.doorThree = False
    app.rightArrow = True
    app.doorList = [False, False, False]
    app.aliveOrDearth = [False, True, False]
    app.counter = 0 


def redrawAll(app):
    #drawBackground(app)
    if app.countForText == 0 or app.countForText == 1 or app.countForText == 3 or app.countForText == 4:
        drawS0134(app)
    elif app.countForText == 2 and (checkFalse(app.doorList) == 2):
        drawS2(app)
    elif app.countForText == 2 and (checkFalse(app.doorList) == 3):
        drawDoor(app)
    elif app.countForText == 5 and (checkFalse(app.doorList) == 2):
        if app.doorList[1] == True:
            drawWin(app)
        elif app.doorList[1] == False:
            drawLost(app)
    elif app.countForText == 5 and (checkFalse(app.doorList) == 3):
        drawDoor(app)
    elif app.countForText == 6:
        drawEnd(app)

    drawButton(app)
    drawConversation(app)

# draw all the background

# def drawBackground(app):
#     imageWidth, imageHeight = 400, 400
#     drawImage('background.jpg', app.width/2, app.height/2, align='center')

def drawS0134(app):
    imageWidth, imageHeight = 400, 400
    drawImage('s0134.PNG', app.width/2, app.height/2, align='center')

def drawS2(app):
    imageWidth, imageHeight = 400, 400
    drawImage('s2.PNG', app.width/2, app.height/2, align='center')

def drawWin(app):
    imageWidth, imageHeight = 400, 400
    drawImage('win.PNG', app.width/2, app.height/2, align='center')

def drawLost(app):
    imageWidth, imageHeight = 400, 400
    drawImage('lost.PNG', app.width/2, app.height/2, align='center')

def drawDoor(app):
    imageWidth, imageHeight = 400, 400
    drawImage('door.jpg', app.width/2, app.height/2, align='center')

def drawEnd(app):
    imageWidth, imageHeight = 400, 400
    drawImage('end.PNG', app.width/2, app.height/2, align='center')




# draw the interaction button
def drawButton(app):
    # button one
    drawRect(120, 230, 30, 30, fill = 'black', align = 'center', opacity = 0)
    # button two
    drawRect(210, 230, 30, 30, fill = 'black', align = 'center', opacity = 0)
    # button three
    drawRect(300, 230, 30, 30, fill = 'black', align = 'center', opacity = 0)

# draw the witch conversation
def drawConversation(app):
    # draw the rect for containg the conversation
    if app.countForText == 0:
        #drawRect(160, 250, 230, 100, fill = 'cornSilk', border = 'white', borderWidth = 2)
        drawLabel('Welcome to the room 5 adventurer!', 45, 290, fill = 'black', size = 10, bold = True, align = 'left')
        drawLabel('Now you have to make your decision!', 45, 300, fill = 'black', size = 10, bold = True, align = 'left')
        drawLabel('One door for alive :(', 45, 310, fill = 'green', size = 10, bold = True, align = 'left')
        drawLabel('Two doors for death :)', 45, 320, fill = 'red', size = 10, bold = True, align = 'left')
        drawLabel('<right> to next message', 45, 340, fill = 'black', size = 10, bold = True, align = 'left')
    elif app.countForText == 1:
        #drawRect(160, 250, 230, 100, fill = 'cornSilk', border = 'white', borderWidth = 2)
        drawLabel('Now select the door you want to choose', 45, 290, fill = 'black', size = 10, bold = True, align = 'left')
        drawLabel('By clickng the door handle', 45, 300, fill = 'black', size = 10, bold = True, align = 'left')
        drawLabel('<right> to close conversation', 45, 340, fill = 'black', size = 10, bold = True, align = 'left')
    elif app.countForText == 2 and (app.doorList[0] == True or app.doorList[1] == True or app.doorList[2] == True):
        #drawRect(160, 250, 230, 100, fill = 'cornSilk', border = 'white', borderWidth = 2)
        drawLabel(f'I choose door {[index + 1 for index, value in enumerate(app.doorList) if value][0] if any(app.doorList) else None}', 180, 310, fill = 'black', size = 10, bold = True, align = 'left')
        drawLabel('<right> to next message', 250, 350, fill = 'black', size = 10, bold = True, align = 'left')
    elif app.countForText == 3:
        #drawRect(160, 250, 230, 100, fill = 'cornSilk', border = 'white', borderWidth = 2)
        drawLabel('Let me give you a little hint', 45, 290, fill = 'black', size = 10, bold = True, align = 'left')
        drawLabel(f'Door {hint(app, app.doorList)} is the death road', 45, 300, fill = 'red', size = 10, bold = True, align = 'left')
        drawLabel('<right> to next message', 45, 340, fill = 'black', size = 10, bold = True, align = 'left')
    elif app.countForText == 4:
        #drawRect(160, 250, 230, 100, fill = 'cornSilk', border = 'white', borderWidth = 2)
        drawLabel('You have one chance for switch it', 45, 290, fill = 'black', size = 10, bold = True, align = 'left')
        drawLabel('Do you want to switch it?', 45, 300, fill = 'black', size = 10, bold = True, align = 'left')
        drawLabel('<right> to close conversation', 45, 340, fill = 'black', size = 10, bold = True, align = 'left')
    elif app.countForText == 5 and (checkFalse(app.doorList) == 2):
        if app.doorList[1] == True:
            #drawRect(160, 250, 230, 100, fill = 'cornSilk', border = 'white', borderWidth = 2)
            # drawLabel('Congratulations! You will be alive!', 170, 290, fill = 'green', size = 10, bold = True, align = 'left')
            drawLabel('<right> to exit the game', 250, 340, fill = 'black', size = 10, bold = True, align = 'left')
        elif app.doorList[1] == False:
            #drawRect(160, 250, 230, 100, fill = 'cornSilk', border = 'white', borderWidth = 2)
            # drawLabel('DEAAAAAAAAAATH', 170, 290, fill = 'red', size = 10, bold = True, align = 'left')
            drawLabel('<right> to exit the game', 50, 340, fill = 'black', size = 10, bold = True, align = 'left')
    # elif app.countForText == 6:
    #     drawRect(200, 200, 400, 400, fill = 'cornSilk', border = 'white', borderWidth = 2, align = 'center')
    #     drawLabel('Game Over', 200, 200, fill = 'black', size = 10, bold = True, align = 'center')

# Reshape the list during 5th
def reShapeTheList(app):
        app.doorList = [False, False, False]
        #print(app.doorList)

# give the hint for which is the death door
def hint(app, L):
    if L[0] == True:
        return 3
    elif L[1] == True:
        return random.randint(1, 3)
    elif L[2] == True:
        return 1

# checking key press for texting
def onKeyPress(app, key):
    if key == 'right':
        if app.countForText == 2 and (checkFalse(app.doorList) == 3):
            app.rightArrow = False
        elif app.countForText == 2 and (checkFalse(app.doorList) == 2):
            app.rightArrow = True
        
        if app.countForText == 4:
            reShapeTheList(app)

        if app.countForText == 5 and (checkFalse(app.doorList) == 3):
            app.rightArrow = False
        elif app.countForText == 5 and (checkFalse(app.doorList) == 2):
            app.rightArrow = True 

        if app.countForText < 6 and app.rightArrow == True:
            app.countForText += 1
            #print(app.countForText)

# Helper function to check how many False in app.doorList
def checkFalse(L):
    count = 0
    for item in L:
        if item == False:
            count += 1
    return count

# track the number to control the right value
def trackRight(app):
    if app.countForText == 2 and (app.doorList[0] == False and app.doorList[1] == False and app.doorList[2] == False):
        app.rightArrow = False
    else:
        app.rightArrow = True

# Check if you are cliking on any buttons
def onMousePress(app, mouseX, mouseY):
    if (105 < mouseX < 135) and (215 < mouseY < 245):
        app.doorList[0] = True
        #print(app.doorList)
    elif (195 < mouseX < 225) and (215 < mouseY < 245):
        app.doorList[1] = True
        #print(app.doorList)
    elif (285 < mouseX < 315) and (215 < mouseY < 245):
        app.doorList[2] = True
        #print(app.doorList)




def main():
  runApp()

main()