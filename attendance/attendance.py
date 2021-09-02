import cv2, numpy as np, face_recognition, os
from webservice_manager import name_by_email, do_attendance

path = r'C:\xampp\htdocs\foe_attendance\attendance\images'
imageList = os.listdir(path)

known_images = []
known_email = []
known_encode = []

for cl in imageList:
    img = cv2.imread(f'{path}/{cl}')
    known_images.append(img)
    known_email.append(os.path.splitext(cl)[0])
    
for img in known_images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    known_encode.append(encode)
    
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    
    # read frame
    frame = cv2.flip(frame, 1)
    detect_current_face = face_recognition.face_locations(frame)
    
    if len(detect_current_face) > 0:
        current_face = detect_current_face[0]
        cv2.rectangle(frame, (current_face[3], current_face[0]), (current_face[1], current_face[2]), (0,255,0), 2)    
    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    
    current_face_location = face_recognition.face_locations(small_frame)
    current_face_encodings = face_recognition.face_encodings(small_frame, current_face_location)
    
    for current_face_encoding in current_face_encodings:
        matches = face_recognition.compare_faces(known_encode, current_face_encoding)
        name = "Unknow"
        
        face_distances = face_recognition.face_distance(known_encode, current_face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            email = known_email[best_match_index]
            
            # get name by email using api request
            name = name_by_email(email)
            
            # do attendance
            attendance = do_attendance(email)

            if len(detect_current_face) > 0:
                current_face = detect_current_face[0]
                cv2.putText(frame, name, (current_face[3]+6, current_face[0]-6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 255, 0), 1)
                cv2.putText(frame, attendance, (50,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 255, 0), 1)
            
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()
            
    
    