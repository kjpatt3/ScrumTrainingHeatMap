import matplotlib.pyplot as plt
from Point import Point
from xAxis import Axis

p = Point()
p.initialize(1,2,"test")
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



# x axis values 
a = 0.5
b = 1.5
c = 2.5
d = 3.5
e = 4.5
f = 5.5
xCoords = [d,e,f,c,b,f,e] 
# corresponding y axis values 
yCoords = [3,4,3,4.7,2,2.5,4.5] 

# plotting the points  
plt.scatter(xCoords, yCoords, label= "dots", color= "red", marker= "o", s=30) 

#Add Labels to each point
j = 0
for i in xCoords:
    plt.annotate("Question "+str(j), (xCoords[j], yCoords[j]))
    j+=1


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

