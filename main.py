import random
import matplotlib.pyplot as plt

def getnum():
  x=random.random()
  y=random.random()
  return([x,y])

def runtest(num):
  global number
  number = num
  innercircle=0
  xList=[]
  yList=[]
  global predictPiList
  predictPiList = []
  total=0
  for i in range(num):
    [x,y] = getnum()
    xList.append(x)
    yList.append(y)
    polardist = ((x**2)+(y**2))**(0.5)
    # print(polardist)
    total+=1
    if polardist<1:
      innercircle+=1
    predictPi=(4*innercircle/total)
    predictPiList.append(predictPi)

  plt.title("Selecting random points in figure")
  plt.ylabel("y-axis")
  plt.xlabel("x-axis")
  plt.scatter(xList, yList)
  plt.plot([i/10000 for i in range(10000)], [(1-((i/10000)**(2)))**(0.5) for i in range(10000)],0.5,color="red")
  plt.legend(["Randomly Picked Points", "Circle with radius 1 inside of 1 x 1 square"], bbox_to_anchor =(1, 1.2), ncol = 2)
  plt.show()


  plt.title("For every points approching 'pi'")
  plt.ylabel("4 x probality for a point fall in area of Quater Circle")
  plt.xlabel("Number of random points")
  plt.plot([i for i in range(num)],predictPiList)
  plt.plot([i for i in range(num)],[3.141592653589793 for x in range(num)], 1)
  plt.legend(["4 x probality for a point fall in area of Square", "Magnitude of pi (π)"], bbox_to_anchor =(1, 1.2), ncol = 2)
  plt.show()
  print(predictPiList[-5:])


points= int(input("Enter the count of points you want to select : "))
runtest(points)

