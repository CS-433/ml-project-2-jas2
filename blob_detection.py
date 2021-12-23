import cv2
import numpy as np;
from multiprocessing import Pool


def clear_image(name, src, dst, merge_image):

    # Load image from file
    image = cv2.imread(src + "/" + name)

    # Define parameters and create detector
    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 100
    params.maxThreshold = 200
    params.thresholdStep = 50
    params.minDistBetweenBlobs = 1

    params.filterByArea = True
    params.minArea = 0
    params.maxArea = 20

    params.filterByCircularity = False
    params.filterByConvexity = False
    params.filterByInertia = False

    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs (computationally heavy)
    keypoints = detector.detect(image)

    # Clear blobs
    (height, width) = image.shape[:2]
    for k in keypoints:
        (x, y) = k.pt
        x = int(x)
        y = int(y)
        s = int(k.size)
        s2 = s*s+1
        for i in range(-s,s+1):
            for j in range(-s,s+1):
                if (i*i + j*j <= s2) and (y+j >= 0) and (x+i >= 0) and (y+j < height) and (x+i < width):
                    if(merge_image):
                        (b, g, r) = image[y+j,x+i]
                        image[y+j,x+i] = (128+b/2,128+g/2,128+r/2)
                    else:
                        image[y+j,x+i] = (255,255,255)
    #save image
    cv2.imwrite(dst + '/' + name, image)
    return

def detect_text(name, path="./data"):

    # Load image from file
    image = cv2.imread(path+"/"+name)

    # Define parameters and create detector
    params = cv2.SimpleBlobDetector_Params()

    params.minThreshold = 100
    params.maxThreshold = 200
    params.thresholdStep = 50
    params.minDistBetweenBlobs = 1

    params.filterByArea = True
    params.minArea = 5
    params.maxArea = 600

    params.filterByCircularity = False
    params.filterByConvexity = False
    params.filterByInertia = False

    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs (computationally heavy)
    keypoints = detector.detect(image)

    # Clear blobs
    (height, width) = image.shape[:2]
    for k in keypoints:
        (x, y) = k.pt
        x = int(x)
        y = int(y)
        s = 6
        s2 = s*s+1
        for i in range(-s,s+1):
            for j in range(-s,s+1):
                if (i*i + j*j <= s2) and (y+j >= 0) and (x+i >= 0) and (y+j < height) and (x+i < width):
                    image[y+j,x+i] = (0,0,0)

    #save image
    cv2.imwrite(path + "/detected-"+ name, image)
    return


def loop(raw_folder):
    """
    To call only from clean_data().
    Unfortunately can't pickle inner functions
    """
    # go through all images inside these folders
    src = sample + '/' + raw_folder
    dst = clean + '/' + raw_folder
    print(src, dst)
    if not os.path.exists(dst):
        os.mkdir(dst)

    for image in os.listdir(src):
        if "xml" not in image: # sample contains xml files
            # in case of unexpected interruption
            if not os.path.exists(dst + '/' + image):
                bd.clear_image(image, src, dst)

def clean_data():
    # parllelize !
    pool = Pool(3)
    results = pool.map(loop, os.listdir(di_raw))
