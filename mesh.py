import cv2 
import mediapipe as mp

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh()

cap =  cv2.VideoCapture(0)

while True:
    _ , frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_h , frame_w, _ = frame.shape
    result = face_mesh.process(frame)
    try:
        for facial_marks in result.multi_face_landmarks:
            for i in range(0,468):
                landmark = facial_marks.landmark[i]
                loc_x = int(landmark.x * frame_w)
                loc_y = int(landmark.y * frame_h)
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                cv2.circle(frame,(loc_x,loc_y),1,(0,200,0),0)
                cv2.imshow('Hacker', frame)
    except:
        cv2.imshow('Hacker', frame)           
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()