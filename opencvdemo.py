import cv2

# read an image:

image = cv2.imread("example.jpg")

# some basic cv2 functions:
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) -- Convert to black and white
image = cv2.bitwise_not(image) #-- inversion


cv2.imshow("This is an example.",image) # Show the image in a window called 'This is an example'
cv2.waitKey(0)
cv2.destroyAllWindows()
