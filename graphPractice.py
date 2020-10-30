import matplotlib.pyplot as plt
from Point import Point



# Points for Focus Triangle
x1 = [2,6,6,2] 
y1 = [5,2,5,5] 
# # plotting the Focus Triange
plt.plot(x1, y1, label = "Focus Triangle")

# x axis values 
xCoords = [4,2,3,3,3,4.5,4] 
# corresponding y axis values 
yCoords = [3,4,3,4.7,2,2.5,4] 

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
plt.title('309 Scrum Stratus')

# function to show the plot
plt.show()
# Press the green button in the gutter to run the script.

