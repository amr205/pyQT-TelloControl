import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

def decodeQR(im) : 
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im, symbols=[pyzbar.ZBarSymbol.QRCODE, pyzbar.ZBarSymbol.EAN13])
    
  return decodedObjects


# Display barcode and QR code location  
def showQrImage(im, decodedObjects):

  # Loop over all decoded objects
  for decodedObject in decodedObjects: 
    points = decodedObject.polygon

    # If the points do not form a quad, find convex hull
    if len(points) > 4 : 
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else : 
      hull = points
    
    # Number of points in the convex hull
    n = len(hull)

    # Draw the convext hull
    color = (0,0,255)
    if decodedObject.type == 'QRCODE':
        color = (255,0,0)
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], color, 3)

    #Show text
    cv2.putText(im, str(decodedObject.data), (decodedObject.rect.left,decodedObject.rect.top-20), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

  return im

  
# Main 
if __name__ == '__main__':
  # Read image
  im = cv2.imread('helpers\zbar-test.jpg')
  decodedObjects = decodeQR(im)
  finalImg = showQrImage(im, decodedObjects)

  # Display results 
  cv2.imshow("Results", finalImg)
  cv2.waitKey(0)
