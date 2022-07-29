# import the opencv library
import cv2
from cv2 import WND_PROP_TOPMOST

# define a video capture object
vid = cv2.VideoCapture(0)

print(cv2.data.haarcascades)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while(True):
  # Capture the video frame
  # by frame
  ret, frame = vid.read()

  #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  faces = faceCascade.detectMultiScale(frame, 1.3, 5)

  for (x, y, w, h) in faces:
    frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 3)

  frame = cv2.flip(frame, 1)

  # Display the resulting frame
  cv2.imshow('frame', frame)

  cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)

  # the 'q' button is set as the
  # quitting button you may use any
  # desired button of your choice
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
