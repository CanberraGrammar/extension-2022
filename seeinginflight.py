# import the opencv library
import cv2
from cv2 import WND_PROP_TOPMOST
import time
from pyardrone import ARDrone

drone = ARDrone()
drone.video_ready.wait()

print(cv2.data.haarcascades)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

drone.takeoff()
time.sleep(5)

while(True):
  # Capture the video frame
  # by frame
  frame = drone.frame

  #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  faces = faceCascade.detectMultiScale(frame, 1.3, 5)
  facesInFrame = len(faces)
  frameWidth = len(frame[0])

  print(facesInFrame)

  for (x, y, w, h) in faces:
    frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 3)
    # print(x, y, w, h)

  if (facesInFrame == 0):
    print("Rotate clockwise, waiting for face...")
    drone.move(cw=0.5)
  else:
    # Determine where in the frame the faces are (x, y, w, h)
    faceX = faces[0][0] + (faces[0][2]/2)
    if (faceX > frameWidth / 2):
      print("Clockwise")
      drone.move(cw=0.3)
    elif (faceX < frameWidth / 2):
      print("Counter Clockwise")
      drone.move(ccw=0.3)
    else:
      pass

  # Display the resulting frame
  cv2.imshow('frame', frame)

  cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)

  # the 'q' button is set as the
  # quitting button you may use any
  # desired button of your choice 
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# After the loop release the cap object
drone.land()
time.sleep(5)
drone.close()
# Destroy all the windows
cv2.destroyAllWindows()
