#Author: Omer213447, github.com/Omer213447
#No License

#Think those as a const definition in c, c++, you can change them to any number you want 
#but dont make them negative, 0 or any float, just use positive integers
xSpaceCount = 3 #spacing between x coordinates 
ySpaceCount = 1 #spacing between y coordinates

#######################
#The form of points used in this work is in the form of (x coordinate, y coordinate).
#The matrix it is using to drawind with is in the form of :     #  |------| i
#                                                               #  |      | 0
                                                                #  |      | 1
                                                                #  |      | 2
                                                                # j|0-1-2-|
#This is 3x3 example. i is the row index and j is the column index of the matrix
#In this work the coordinate (0,0) is placed bottom left corner of the matrix, 
#So j is the x coordinate. But i is not the y coordinate. y coordinate and i are reverse of each other. 
#Thus in this work it reverses the y coordinate whenever it uses the y coordinate on the matrix.
#######################

def drawTheSiluette(matrix):
    """Draws the matris like this: |-    <matris>    -|"""
    for i in range(len(matrix)):
        print("|-    ", end='')
        for j in range(len(matrix[0])):
            print(matrix[i][j], end='')
        print("    -|\n", end='')

def convertCoordinateToIndex(yCoordinate, rowCount):
    """Converts y coordinate to the usable i index for matrix.
       It takes 2 arguments: Count of rows of the matrix and y coordinate of the point
       It returns i index of the y coordinate.""" 
    yCoordinate = rowCount  - yCoordinate - 1
    return yCoordinate

def drawBetweenPoints(firstPoint, secondPoint, matrix):
    """Makes Ascii Draw in given matrix between 2 points that is given as tuples in form of (x coordinate, y coordinate)
       arguments a and b are points, matrix is the matrix the function makes drawing in. For now it works only if
       x coordinate or y coordinate of the points are equal, otherwise it raises ValueError and it draws - between points in matrix."""
    if(firstPoint[0] != secondPoint[0] and firstPoint[1] != secondPoint[1]):
        raise ValueError("x coordinate or y coordinate of points should be equal") 
    yLen = len(matrix) - 1
    yLen = yLen // ySpaceCount;
    yLen += 1
    if(firstPoint[0] == secondPoint[0]): #draw in y direction
        i = max(firstPoint[1], secondPoint[1])
        j = firstPoint[0]
        if(firstPoint[1] > secondPoint[1]):
            minPoint = firstPoint
            maxPoint = secondPoint
        else:
            minPoint = secondPoint
            maxPoint = firstPoint
        minPoint = list(minPoint)
        maxPoint = list(maxPoint)
        i = convertCoordinateToIndex(i, yLen) #koordinates we given and indices in matris differ, 
                             #because of that we change our y koordinate to make it compatible with matris i index
        minPoint[1] = convertCoordinateToIndex(minPoint[1], yLen)
        maxPoint[1] = convertCoordinateToIndex(maxPoint[1], yLen)
        minPoint[0] *= xSpaceCount
        maxPoint[0] *= xSpaceCount
        j *= xSpaceCount
        minPoint[1] *= ySpaceCount
        maxPoint[1] *= ySpaceCount
        i *= ySpaceCount
        while(i <= maxPoint[1]):
            matrix[i][j] = "-"
            i += 1
    else: #draw in x direction
        i = firstPoint[1]
        j = min(firstPoint[0], secondPoint[0])
        if(firstPoint[0] > secondPoint[0]):
            minPoint = secondPoint
            maxPoint = firstPoint
        else:
            minPoint = firstPoint
            maxPoint = secondPoint
        minPoint = list(minPoint)
        maxPoint = list(maxPoint)
        i = convertCoordinateToIndex(i, yLen) #koordinates we given and indices in matris differ, 
                             #because of that we change our y koordinate to make it compatible with matris i index
        minPoint[1] = convertCoordinateToIndex(minPoint[1], yLen) 
        maxPoint[1] = convertCoordinateToIndex(maxPoint[1], yLen)
        minPoint[0] *= xSpaceCount
        maxPoint[0] *= xSpaceCount
        j *= xSpaceCount
        minPoint[1] *= ySpaceCount
        maxPoint[1] *= ySpaceCount
        i *= ySpaceCount 
        while(j <= maxPoint[0]):
            matrix[i][j] = "-"
            j += 1
    return matrix


siluetteArray = [5, 5, 5, 3, 8, 6, 3, 2, 1, 1, 2, 3, 4]
#You can change the siluette array with any number of positive integers, note how result changes!
#siluetteArray = [1, 1, 1, 2, 2, 3] #Array that represents the heigths of flats in a city
coordinatesOfCorners = [(0,0)] #Array that will represent the coordinates of the corner of flats in a city

for index, item in enumerate(siluetteArray): #In this loop we get points of corners of flats
    if(len(siluetteArray) - 1 == index):
        coordinatesOfCorners.append((index, item))
        coordinatesOfCorners.append((index + 1, item))
        coordinatesOfCorners.append((index + 1, 0))
        break
    if(siluetteArray[index + 1] != item):
        coordinatesOfCorners.append((index, item))
        coordinatesOfCorners.append((index+1,item))
    else:
        coordinatesOfCorners.append((index, item))
coordinatesOfCorners = list(dict.fromkeys(coordinatesOfCorners)) #With this method we get rid of duplicates in the points list.
x = []
y = []
for item in coordinatesOfCorners: 
    #with this we get x coordinates and y coordinates seperated. This is useful if you want to plot with matplotlib
    #but we also get the max width and height for drawing the siluette. This is not efficent. You can change for more efficent code.
    x.append(item[0])
    y.append(item[1])
xMax = max(x) #count of columns in the matrix of siluette
yMax = max(y) #count of rows in the matrix of siluette
###############################
asciiArr = []
for i in range(yMax * ySpaceCount + 1):
  row = []
  for j in range(xMax * xSpaceCount + 1):
    row.append(" ")
  asciiArr.append(row)
############################### initilazation of array
for i in range(len(coordinatesOfCorners)): #draw the basic graph
    asciiArr = drawBetweenPoints(coordinatesOfCorners[i], coordinatesOfCorners[i + 1], asciiArr)
    if(i == len(coordinatesOfCorners) - 2):
        break
drawTheSiluette(asciiArr)