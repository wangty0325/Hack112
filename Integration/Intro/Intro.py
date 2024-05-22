from cmu_graphics import *
# import playsound

def onAppStart(app):
     app.counter = 0
     app.stepsPerSecond = 1
     app.startGame = False
     app.rightClick = False

def redrawAll(app): 
    if 1 > app.counter:
        drawSceneOne(app)
    elif 0.5 < app.counter < 3:
        drawSceneTwo(app)
    elif 2.5 < app.counter < 5:
        drawSceneThree(app)
    elif  4.5 < app.counter and app.rightClick == False:
        drawSceneFour(app)
    elif 4.5 < app.counter and app.rightClick == True:
        drawSceneOne(app)
    drawConversation(app)
    drawButton(app)
    drawScreen(app)

# first graph is scene 1
def drawSceneOne(app):
    imageWidth, imageHeight = 400, 400
    drawImage('scene1.jpeg', app.width/2, app.height/2, width = imageWidth, height = imageHeight, align = 'center')

# second scene
def drawSceneTwo(app):
    imageWidth, imageHeight = 400, 400
    drawImage('scene2.jpeg', app.width/2, app.height/2, width = imageWidth, height = imageHeight, align = 'center')


# third scene
def drawSceneThree(app):
    imageWidth, imageHeight = 400, 400
    drawImage('scene3.jpeg', app.width/2, app.height/2, width = imageWidth, height = imageHeight, align = 'center')

# forth scene
def drawSceneFour(app):
    imageWidth, imageHeight = 400, 400
    drawImage('scene4.jpeg', app.width/2, app.height/2, width = imageWidth, height = imageHeight, align = 'center')

# draw the witch conversation
def drawConversation(app):
    if 0.5 < app.counter < 3:
        #drawRect(10, 320, 250, 50, fill = 'cornSilk', border = 'white', borderWidth = 2)
        drawLabel('Me:', 180, 310, fill = 'black', size = 15, bold = True, align = 'left')
        drawLabel('Wow an old house...', 180, 325, fill = 'black', size = 15, bold = True, align = 'left')
        drawLabel('Never came here before!', 180, 340, fill = 'black', size = 15, bold = True, align = 'left')
    elif 2.5 < app.counter < 5:
        #drawRect(10, 320, 250, 50, fill = 'cornSilk', border = 'white', borderWidth = 2)
        drawLabel('Troy:', 50, 310, fill = 'black', size = 15, bold = True, align = 'left')
        drawLabel('Lets prank them!', 50, 325, fill = 'black', size = 15, bold = True, align = 'left')
    elif  4.5 < app.counter:
        if app.rightClick == False:
            #drawRect(10, 320, 250, 50, fill = 'cornSilk', border = 'white', borderWidth = 2)
            drawLabel('Me:', 180, 310, fill = 'black', size = 15, bold = True, align = 'left')
            drawLabel('Aight lets go...', 180, 325, fill = 'black', size = 15, bold = True, align = 'left')
            drawLabel('Click -right- to end conversation', 180, 340, fill = 'red', size = 10, bold = True, align = 'left')

# draw the button for the whole scarry house
def drawButton(app):
    if app.rightClick == True:
        drawRect(200, 200, 400, 400, fill = 'cornSilk', border = 'white', borderWidth = 2, align = 'center', opacity = 0)

# draw the temporay black screen
def drawScreen(app):
    if app.startGame == True:
        drawRect(200, 200, 400, 400, fill = 'black', align = 'center')

# Check if you are cliking on any buttons
def onMousePress(app, mouseX, mouseY):
    if (0 < mouseX < 400) and (0 < mouseY < 400) and (app.rightClick == True):
        app.startGame = True

# checking key press for texting
def onKeyPress(app, key):
    if key == 'right' and app.counter > 6:
        app.rightClick = True

def onStep(app):
    app.counter += 1
    # print(app.counter)

def main():
  runApp()

main()