import numpy as np
import cv2

# Define the codec and create VideoWriter object
frameSize = (640,480)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, frameSize, isColor=False)

frame = np.zeros(frameSize, dtype = np.uint8)
frame[300:400, 200:300] = 255

while True:
    # Create random data
#     data = np.random.uniform(0, 255, frameSize[0] * frameSize[1])
#     frame = data.reshape(frameSize).astype(np.uint8)
    frame = cv2.blur(frame, (7,7))

    # write data to the frame
    out.write(frame.transpose())  # OPENCV is col-major :(

    cv2.imshow('frame',frame.transpose())    # OPENCV is col-major :(
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()