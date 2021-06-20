# Standard imports
import cv2
import numpy as np;
 
# Read image
image = cv2.imread("images/Sunflowers.jpg")
 
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs.
keypoints = detector.detect(image)
 
# Draw detected blobs as red circles.
blank = np.zeros((1,1)) 
blobs = cv2.drawKeypoints(image, keypoints, blank, (255,0,0),
                                      cv2.DRAW_MATCHES_FLAGS_DEFAULT)
# Show keypoints
cv2.imshow("Blobs", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()