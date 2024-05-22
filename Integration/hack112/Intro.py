from cmu_graphics import *
# import playsound

def onAppStart(app):
    #  url = 'cmu://664646/26106870/creepyMusic.mp3'
     app.counter = 0
     app.stepsPerSecond = 1
     app.startGame = False
     app.rightClick = False
    #  playsound('creepy.mp3')
    #  app.sound = Sound('Creepy.mp3')
    #  app.soundPause = True
    #  checkingSoundPausing(app)
    #  app.sound.play()

def redrawAll(app): 
    drawBackground(app)
    drawConversation(app)
    drawButton(app)
    drawScreen(app)

# Check if you are cliking on any buttons
def onMousePress(app, mouseX, mouseY):
    200, 150, 200, 200
    if (100 < mouseX < 300) and (50 < mouseY < 250):
        app.startGame = True

def drawBackground(app):
    imageWidth, imageHeight = 400, 400
    drawImage('CreepyHouse.jpg', app.width/2, app.height/2, width = imageWidth, height = imageHeight, align='center')

# draw the button for the whole scarry house
def drawButton(app):
    if app.rightClick == True:
        drawRect(200, 150, 200, 200, fill = 'cornSilk', border = 'white', borderWidth = 2, align = 'center', opacity = 0)

# draw the temporay black screen
def drawScreen(app):
    if app.startGame == True:
        drawRect(200, 200, 400, 400, fill = 'black', align = 'center')


def checkingSoundPausing(app):
    if app.soundPause == False:
        app.sound.play(loop=True)

# checking key press for texting
def onKeyPress(app, key):
    if key == 'right' and app.counter > 6:
        app.rightClick = True

# draw the witch conversation
def drawConversation(app):
    if 1 < app.counter < 3:
        drawRect(10, 320, 250, 50, fill = 'cornSilk', border = 'white', borderWidth = 2)
        drawLabel('Me:', 20, 340, fill = 'black', size = 10, bold = True, align = 'left')
        drawLabel('Wow an old house, we never came here before!', 20, 350, fill = 'black', size = 10, bold = True, align = 'left')
    elif 3.5 < app.counter < 5.5:
        drawRect(10, 320, 250, 50, fill = 'cornSilk', border = 'white', borderWidth = 2)
        drawLabel('Troy:', 20, 340, fill = 'black', size = 10, bold = True, align = 'left')
        drawLabel('Lets prank them!', 20, 350, fill = 'black', size = 10, bold = True, align = 'left')
    elif  6 < app.counter:
        if app.rightClick == False:
            drawRect(10, 320, 250, 50, fill = 'cornSilk', border = 'white', borderWidth = 2)
            drawLabel('Me:', 20, 340, fill = 'black', size = 10, bold = True, align = 'left')
            drawLabel('Aight lets go...', 20, 350, fill = 'black', size = 10, bold = True, align = 'left')
            drawLabel('Click -right- to end conversation', 100, 360, fill = 'red', size = 10, bold = True, align = 'left')

def onStep(app):
    app.counter += 1
    # print(app.counter)

def main():
  runApp()

main()