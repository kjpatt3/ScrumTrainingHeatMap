import matplotlib.pyplot as plt
from Point import Point
from xAxis import Axis

#Gather User Input
def userInput():
    j=0
    points = []
    while(j < 2):
        xVal = input("Enter X Value: ")
        yVal = input("Enter Y Value: ")
        label = raw_input("Enter Label: ")
        p = Point()
        p.initialize(xVal, yVal, label)
        points.append(p)
        j+=1
    return points


def plotPoint(x,y,clr,questionID):
    plt.scatter(x,y,label = "dots", color = clr,marker = "o", s = 30)
    plt.annotate(questionID,(x,y))


# Points for Focus Triangle
x1 = [2,6,6,2] 
y1 = [5,2,5,5] 
# # plotting the Focus Triange
plt.plot(x1, y1, label = "Focus Triangle")

#X axis customization
xAxis = Axis()
xAxis.init()

plt.plot(xAxis.greenX, xAxis.greenY, color = "green")
plt.axvspan(0, 1, alpha=0.5, ymax = 0.06, color='green')
plt.plot(xAxis.yellowX, xAxis.yellowY, color  = "yellow")
plt.axvspan(1, 2, alpha=0.5, ymax = 0.06, color='yellow')
plt.plot(xAxis.orangeX, xAxis.orangeY, color  = "orange")
plt.axvspan(2, 3, alpha=0.5, ymax = 0.06, color='orange')
plt.plot(xAxis.orangeX2, xAxis.orangeY2, color = "orange")
plt.axvspan(3, 4, alpha=0.5, ymax = 0.06, color='orange')
plt.plot(xAxis.orangeX3, xAxis.orangeY3, color = "orange")
plt.axvspan(4, 5, alpha=0.5, ymax = 0.06, color='orange')
plt.plot(xAxis.redX, xAxis.redY, color = "red")
plt.axvspan(5, 6, alpha=0.5, ymax = 0.06, color='red')


# Get User Input
listOfPoints = userInput()


# plotting the points from User Input
i = 0
while(i < len(listOfPoints)):
    if(listOfPoints[i].xCoordinate > 0 and listOfPoints[i].xCoordinate < 1):
        plotPoint(listOfPoints[i].xCoordinate,listOfPoints[i].yCoordinate, "green", listOfPoints[i].label)
        i += 1
    elif(listOfPoints[i].xCoordinate > 1 and listOfPoints[i].xCoordinate < 2):
        plotPoint(listOfPoints[i].xCoordinate,listOfPoints[i].yCoordinate, "yellow", listOfPoints[i].label)
        i += 1
    elif(listOfPoints[i].xCoordinate > 2 and listOfPoints[i].xCoordinate < 3):
        plotPoint(listOfPoints[i].xCoordinate,listOfPoints[i].yCoordinate, "orange", listOfPoints[i].label)
        i += 1
    elif(listOfPoints[i].xCoordinate > 3 and listOfPoints[i].xCoordinate < 4):
        plotPoint(listOfPoints[i].xCoordinate,listOfPoints[i].yCoordinate, "orange", listOfPoints[i].label)
        i += 1
    elif(listOfPoints[i].xCoordinate > 4 and listOfPoints[i].xCoordinate < 5):
        plotPoint(listOfPoints[i].xCoordinate,listOfPoints[i].yCoordinate, "orange", listOfPoints[i].label)
        i += 1
    elif(listOfPoints[i].xCoordinate > 5 and listOfPoints[i].xCoordinate < 6):
        plotPoint(listOfPoints[i].xCoordinate,listOfPoints[i].yCoordinate, "red", listOfPoints[i].label)
        i += 1



#setting the values on the axis.
plt.xlim(0,6)
plt.ylim(0,5)
# naming the x axis
plt.xlabel("How We feel We're Doing")
# naming the y axis
plt.ylabel("Importance")

# giving a title to my graph
plt.title('309 Scrum Status')

# function to show the plot
plt.show()
# Press the green button in the gutter to run the script.

