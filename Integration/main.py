from cmu_graphics import *

def onAppStart(app):
    #room1
    app.x1, app.y1 = 100, 100
    app.size = app.width/2
    app.blockSize = app.size//3
    app.blocks = [[3, 4, 6], [0, 1, 2], [5, 8, 7]]
    app.zeroIndex = (1,0)
    app.highlight = (0,0)
    app.prevBox = None
    app.boxPressed = False
    app.room1 = True
    app.puzzle1 = False
    app.page = 1
    #room2
    app.hints = ['use arrows to scroll through hints', 'your friend is a carnivore', 
                 'the hot dog lover is surrounded by 2 Japanese food fans', 
                 'the ramen loving witch is always first', 
                 'snakes are lactose intolerant']
    app.hintNum = 0
    app.start = False
    app.room2 = False
    app.success2 = None
    app.puzzle2 = app.buttons2 = False
    app.buttonWidth = app.width/5
    app.diameter = app.buttonWidth * 8/9
    app.x2Centers = set()
    app.oCenters = set()
    app.circleCenters = createCircleList(app)
    app.circleAnswer = 2
    app.x2 = app.width/2
    app.y = app.height/2
    app.stepsPerSecond = 4
    app.counter = 0
    app.successText = "...i’m so hungry...so hungry...so hungry...what do i do? i’m scared they are going to eat me...i think i saw a kitchen on the map"
    
def createCircleList(app):
    z = app.diameter*2/7
    result = []
    for i in range(5):
        xCoor = app.width/2 + z/2 - 2*app.diameter - 2*z + i*(app.diameter + z)
        yCoor = app.height*2/7
        result.append((xCoor,yCoor))
    return result

def onStep(app):
    app.counter += 1

def redrawAll(app):
    if app.room2:
        drawRoom2(app)
    elif app.room1:
        drawRoom1(app)

def onKeyPress(app, key):
    if key == 'space' and not app.puzzle1 and not app.puzzle2:
        if app.page == 4:
            app.room1 = False
            app.room2 = True
        else:
            app.counter = 0
        app.page += 1
    if app.puzzle1 and app.highlight!=None:
        x, y = app.highlight
        x0, y0 = app.zeroIndex
        if key == 'enter':
            print(checkSolution(app))
        elif key == 'down' and x-x0==-1 and y==y0:
            if x + 1 < 3:
                app.blocks[x][y], app.blocks[x+1][y] = app.blocks[x+1][y], app.blocks[x][y]
                app.zeroIndex = (x, y)
        elif key == 'up' and x-x0==1 and y==y0:
            if x - 1 >= 0:
                app.blocks[x][y], app.blocks[x-1][y] = app.blocks[x-1][y], app.blocks[x][y]
                app.zeroIndex = (x, y)
        elif key == 'left' and x==x0 and y-y0==1:
            if y - 1 >= 0:
                app.blocks[x][y], app.blocks[x][y-1] = app.blocks[x][y-1], app.blocks[x][y]
                app.zeroIndex = (x, y)
        elif key == 'right' and x==x0 and y-y0==-1:
            if y + 1 < 3:
                app.blocks[x][y], app.blocks[x][y+1] = app.blocks[x][y+1], app.blocks[x][y]
                app.zeroIndex = (x, y)
        if checkSolution(app):
            app.puzzle1 = False

    elif app.puzzle2:
        if key == 'right':
            app.hintNum = (app.hintNum + 1)%5
        elif key == 'left' and app.hintNum > 1:
            app.hintNum = (app.hintNum - 1)%4

def onMouseMove(app, mouseX, mouseY):
    if app.puzzle1:
        app.prevBox = app.highlight
        app.highlight = getCurrentBox(app, mouseX, mouseY)
        if app.prevBox != app.highlight:
            app.boxPressed = False

def onMousePress(app, mouseX, mouseY):
    if app.room1:
        if ((app.x1+3*app.blockSize <= mouseX <= app.x1+4*app.blockSize) and 
            (app.y1+3/2*app.blockSize <= mouseY <= app.y1+3*app.blockSize)):
            app.puzzle1 = True
        elif app.puzzle1:
            if app.highlight != None:
                app.boxPressed = True
    elif app.room2:
        if ((app.width/2 <= mouseX <= app.width/2 + app.buttonWidth)
            and (app.height*9/10 <= mouseY <= app.height*9/10 + app.buttonWidth/2)):
            app.puzzle2 = True
        elif app.puzzle2:
            if (app.buttonWidth*7/2 <= mouseX <= app.buttonWidth*7/2 + app.buttonWidth*3/5):
                x = app.width/20
                if (app.buttonWidth*11/12 <= mouseY <= app.buttonWidth*11/12 + x):
                    app.puzzle2 = False
                    app.buttons2 = True
                elif (app.buttonWidth*27/8 <= mouseY <= app.buttonWidth*27/8 + x*3/2):
                    app.x2Centers = set()
                    app.oCenters = set()
            else:
                newCenterPoint = (mouseX, mouseY)
                if newCenterPoint in app.x2Centers:
                    app.oCenters.add(newCenterPoint)
                    app.x2Centers.remove(newCenterPoint)
                elif newCenterPoint in app.oCenters:
                    app.x2Centers.add(newCenterPoint)
                    app.oCenters.remove(newCenterPoint)
                else:
                    app.x2Centers.add(newCenterPoint)
        elif app.buttons2:
            for i in range(len(app.circleCenters)):
                cX, cY = app.circleCenters[i]
                if abs(mouseX - cX) <= app.diameter/2 and abs(mouseY - cY) <= app.diameter/2:
                    if i == app.circleAnswer - 1:
                        app.success2 = True
                    else:
                        app.success2 = False
                    app.buttons2 = False

def drawRoom1(app):
    if app.puzzle1:
        drawImage('room1-2-1.jpg', 0, 0)
        for row in range(3):
            for col in range(3):
                label = app.blocks[row][col]
                if app.blocks[row][col] == 0:
                    box = 'lightGray'
                    label = ''
                elif (row, col) == app.highlight:
                    if app.boxPressed:
                        box = 'darkGray'
                    else:
                        box = 'darkGray'
                else:
                    box = 'silver'
                drawRect(app.x1+col*app.blockSize, app.y1+row*app.blockSize, app.blockSize, app.blockSize, fill = box, border = 'gainsboro')
                drawLabel(f'{label}', app.x1+col*app.blockSize + app.blockSize/2, app.y1+row*app.blockSize + app.blockSize/2, size = 30, font = 'monospace', bold = True)
    else:
        start = max(0, app.counter-25)
        if app.page == 1:
            drawImage('room1-1.jpeg', 0, 0)
            text = "Oh no! My friends are locked in cages! What should I do?"
            drawLabel(f'{text[start:app.counter+1]}', app.width*2/3, app.width*3/4 + app.width/10, font = 'monospace', size = 13)
        elif app.page == 2:
            drawImage('room1-2.jpeg', 0, 0)
            text = "Look! There's a padlock! Maybe I should try unlocking it."
            drawLabel(f'{text[start:app.counter+1]}', app.width*2/3, app.width*3/4 + app.width/10, font = 'monospace', size = 13)
        elif app.page == 3:
            drawImage('room1-2-1.jpg', 0, 0)
        elif app.page == 4:
            drawImage('room1-3.jpeg', 0, 0)
            text = "I made it in! Now let's go find my friend!"
            drawLabel(f'{text[start:app.counter+1]}', app.width*2/3, app.width*3/4 + app.width/10, font = 'monospace', size = 13)

def getCurrentBox(app, x, y):
    for row in range(3):
        for col in range(3):
            if (abs(x - (app.x1+col*app.blockSize + app.blockSize/2)) <= app.blockSize/2 and 
                abs(y - (app.y1+row*app.blockSize + app.blockSize/2)) <= app.blockSize/2):
                return row, col
    return None

def checkSolution(app):
    prevNum = -1
    for row in range(3):
        for col in range(3):
            num = app.blocks[row][col]
            if num < prevNum and num != 0:
                return False
            elif num != 0:
                prevNum = num
    return True

def drawRoom2(app):
    x = app.width/20
    start = max(0, app.counter-25)
    if app.success2 != None:
        if app.success2:
            drawImage('room2-5.jpeg', 0, 0)
            drawRect(x, app.width*3/4, app.width-2*x, 4*x, fill = 'gainsboro', opacity = 5)
            drawLabel(f"{app.successText[start:app.counter+1]}", app.width*2/3, app.width*3/4 + app.width/10, font = 'monospace', size = 13)
        else:
            drawImage('room2-6.jpeg', 0, 0)
    elif app.buttons2:
        drawImage('room2-3.jpeg', 0, 0)
        for i in range(5):
            cX, cY = app.circleCenters[i]
            drawCircle(cX, cY, app.diameter/2, fill = 'grey', opacity = 50)
    elif not app.puzzle2:
        if app.page == 5:
            drawImage('room2-1.jpeg', 0, 0)
            text = "wow, there are so many cages..."
            drawLabel(f'{text[start:app.counter+1]}', app.width*2/3, app.width*3/4 + app.width/10, font = 'monospace', size = 13)
        elif app.page == 6:
            drawImage('room2-2.jpeg', 0, 0)
            text = "Hello there. You seem a bit lost. If you solve the puzzle on the table, you might just find what you're looking for."
            drawLabel(f'{text[start:app.counter+1]}', app.width*2/3, app.width*3/4+ app.width/20, font = 'monospace', size = 13)
        elif app.page == 7:
            drawImage('room2-3.jpeg', 0, 0)
    else:
        drawImage('room2-4.jpeg', 0, 0)
        drawLabel("HINTS:", app.buttonWidth, app.buttonWidth, align = 'left', font='monospace')
        drawLabel(app.hints[app.hintNum], app.width/2, app.buttonWidth*4/3, font='monospace', align = 'center', size = 8)
        for i in range(4):
            fillCircle = None
            if i == app.hintNum-1:
                fillCircle = 'lightSteelBlue'
            drawCircle(app.buttonWidth*4/3, app.buttonWidth*13/7 + i*45, 17, fill = fillCircle, border = 'black', opacity = 80)
            drawLabel(f'{i+1}', app.buttonWidth*4/3, app.buttonWidth*13/7 + i*45)
        drawRect(app.buttonWidth*7/2, app.buttonWidth*11/12, app.buttonWidth*3/5, x, fill = None)
        
        for cx, cy in app.x2Centers:
            drawLabel('X', cx, cy)
        for cx, cy in app.oCenters:
            drawLabel('O', cx, cy)

def main():
    runApp()

main()