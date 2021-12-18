import cv2
import numpy as np

def detect_lines(name, path="./data", threshold = 30):

    img = cv2.imread(path+"/"+name)

    invert = cv2.bitwise_not(img)
    gray = cv2.cvtColor(invert,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    lines = cv2.HoughLines(gray,1,np.pi/180,580)

    amount = 0
    
    for l in lines:
        for rho,theta in l:
            if ((theta < np.pi/2+0.1) and (theta> np.pi/2-0.1)): #detect only horizontal lines
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 10000*(-b))
                y1 = int(y0 + 10000*(a))
                x2 = int(x0 - 10000*(-b))
                y2 = int(y0 - 10000*(a))

                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
                amount+=1

    #save image
    cv2.imwrite(path + "/hough-"+ name, img)

    #returns true if there are enough lines for the image to be considered a text
    #todo : ignore lines at the edges of the scan
    return (amount>=threshold)