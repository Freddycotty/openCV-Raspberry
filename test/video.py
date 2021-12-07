import cv2

capture = cv2.VideoCapture('files/Peakyblinders.mp4')
salida = cv2.VideoWriter('files/Peakyblinders2.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640,480))
while (capture.isOpened()):
  value, video = capture.read()
  if value == True:
    cv2.imshow('Peaky Blinders', video)
    salida.write(video)
    if cv2.waitKey(1) & 0xff == ord('q'):
      break
  else:
    break

  
capture.releases()
salida.release()
capture.destrouAllWindows()