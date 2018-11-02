import cv2

def convert(inPathName, outPathName):
    # Reader
    capture = cv2.VideoCapture(inPathName)
    nFrame = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = capture.get(cv2.CAP_PROP_FPS)
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frameShape = (width, height)

    # Writer
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(outPathName,fourcc, fps, frameShape, isColor=False)

    print("Converting file", inPathName, "to", outPathName)
    print("total frames", nFrame, "shape", frameShape, "fps", fps)

    # Convert
    while True:
        ret, frame = capture.read()
        if ret:
            out.write(frame[:,:,0])
        else:
            break


    # Release everything if job is finished
    out.release()

# Test
inPathName = "/media/aleksejs/DataHDD/work/data/Pia/Tracking20180928/Shaved/2018.09.28_16_05_11.avi"
outPathName = "output.avi"
convert(inPathName, outPathName)