# Team for this assignement consists of
# Ali Waleed 34-673 T-07
# Alaa Hatem 34-878 T-11

import numpy as np
import cv2

def Q1():
    img = cv2.imread('./images/Q1I1.png')
    brightness = 5
    contrast = 6
    # loop on every pixel in the image and adjust contrast/brightness by multiplying/adding a constant
    # if an overflow occurs the pixel is saturated into 255 else if negative value saturated to 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for channel in range(img.shape[2]):
                img[i,j,channel] = np.clip( contrast * img[i,j,channel] + brightness, 0, 255)
            # fading contrast
            contrast -= 0.005352364
        contrast = 6
    cv2.imwrite('./images/test2.png',img)

    batman = cv2.imread('./images/Q1I2.jpg')
    # resize batman image to be equal martha's
    batman = cv2.resize( batman ,(img.shape[1], img.shape[0]))
    # reflecting batman's image
    batman = cv2.flip(batman, 1)
    translationMatrix = np.float32([[1,0,150],[0,1,0]])
    transformedBatman = cv2.warpAffine(batman, translationMatrix , (batman.shape[1],batman.shape[0]))
    # bleding 0.7:0.3 ratio between martha and transformed batman
    output = cv2.addWeighted(img,0.7,transformedBatman,0.3,0)

    cv2.imwrite('./images/flipped.png',output)
def Q2V1():
    sherlock = cv2.imread('./images/Q2I1.jpg')
    frame = cv2.imread('./images/Q2I2.jpg')
    # obtaining three corners of sherlock using an image editor, in the frame image we also obtained the 4 corners to be
    # used later for drawing a black polygon.
    sherlockCorners = np.float32([[0,0],[500,0],[500,685]])
    frameCorners = np.float32([[1218,1333-955],[1218+90,1333-955],[1218+90,1333-955+139]])
    frameAllCorners = np.array([[1218,1333-955],[1218+90,1333-955],[1218+90,1333-955+139],[1218,1333-955+139]])

    affineMatrix = cv2.getAffineTransform(sherlockCorners, frameCorners)
    # scaling and translating sherlock to frame image
    sherlockTransformed = cv2.warpAffine( sherlock, affineMatrix,(frame.shape[1],frame.shape[0]))

    # filling black polygon in the frame image to add it on sherlockTransformed
    cv2.fillConvexPoly(frame, frameAllCorners.astype(int), 0, 16)
    output = frame + sherlockTransformed
    cv2.imwrite('./images/output2.png',output)
def Q2V2():
    sherlock = cv2.imread('./images/Q2I1.jpg')
    frame = cv2.imread('./images/Q2I3.jpg')

    
    sherlockCorners = np.float32([[0,0],[0,685],[500,685]])
    frameCorners = np.float32([[1024-653,678-588],[1024-701,678-148],[1024-360,678-118]])
    frameAllCorners = np.array([[1024-653,678-588],[1024-324,678-547],[1024-360,678-118],[1024-701,678-148]])

    # scaling/translating/rotating sherlock to frame image
    affineMatrix = cv2.getAffineTransform(sherlockCorners, frameCorners)
    sherlockTransformed = cv2.warpAffine(sherlock, affineMatrix, (frame.shape[1],frame.shape[0]))

    # filling black polygon in the frame image to add it on sherlockTransformed
    cv2.fillConvexPoly(frame, frameAllCorners.astype(int), 0, 16)
    output = frame + sherlockTransformed
    cv2.imwrite('./images/output3.png',output)
def Q3():
    sherlock = cv2.imread('./images/Q2I1.jpg')
    frame = cv2.imread('./images/Q3I1.jpg')

    sherlockCorners = np.float32([[0,0],[500,0],[500,685],[0,685]])
    frameAllCorners = np.float32([[612-449,406-369],[612-144,406-335],[612-150,406-54],[612-455,406-19]])

    # Using perspective matrix rather than affine matrix as the perspective isnt the same anymore
    perspectiveMatrix = cv2.getPerspectiveTransform(sherlockCorners, frameAllCorners)
    sherlockTransformed = cv2.warpPerspective(sherlock, perspectiveMatrix, (frame.shape[1], frame.shape[0]))

    # filling black polygon in the frame image to add it on sherlockTransformed
    cv2.fillConvexPoly(frame, frameAllCorners.astype(int), 0, 16)
    output = frame + sherlockTransformed
    cv2.imwrite('./images/output4.png',output)

Q1()
# Q2V1()
# Q2V2()
# Q3()
# reference https://docs.opencv.org/3.1.0/d4/d61/tutorial_warp_affine.html





