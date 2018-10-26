import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def rgb2gray(f):
    return ((f[:,:,0] + f[:,:,1] + f[:,:,2]) / 3).astype(int)


capture = cv2.VideoCapture("/media/aleksejs/DataHDD/work/data/Pia/omgbestvideva2.avi")
nFrame = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
print(nFrame)

totMovement = np.zeros((nFrame, 2))
# centroidMovement = np.zeros((nFrame, 2))


ret, frame = capture.read()
RGBShape = frame.shape

frameGrayOld = rgb2gray(frame.astype(int))

iFrame = 0
while True:
    ret, frame = capture.read()
    if ret:
        frameGrayNew = rgb2gray(frame.astype(int))

        diff = frameGrayNew - frameGrayOld
        diffPos = np.copy(diff)
        diffNeg = np.copy(diff)
        diffPos[diffPos < 0] = 0
        diffNeg[diffNeg > 0] = 0

        diffRGB = np.zeros(RGBShape, dtype=np.uint8)
        diffRGB[:, :, 0] = diffPos
        diffRGB[:, :, 1] = -diffNeg

        totMovement[iFrame, 0] = np.sum(diffRGB)
        totMovement[iFrame, 1] = np.sum(diffRGB[diffRGB > 20])

        cv2.imshow('frame', diffRGB.astype(np.uint8))
        # cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frameGrayOld = frameGrayNew[:]
        iFrame += 1
    else:
        break

capture.release()
cv2.destroyAllWindows()

totMovement[:, 0] /= np.sum(totMovement[:, 0])
totMovement[:, 1] /= np.sum(totMovement[:, 1])

plt.figure()
plt.plot(totMovement[:, 0])
plt.plot(totMovement[:, 1])
plt.show()