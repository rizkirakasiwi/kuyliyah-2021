import cv2, numpy as np, face_recognition, os
from webservice_manager import get_name, do_attendance


class VideoCamera(object):
        
    def __init__(self):
        self.path = r'C:\xampp\htdocs\foe_attendance\foe_web\images'
        self.imageList = os.listdir(self.path)

        self.known_images = []
        self.known_email = []
        self.known_encode = []

        for cl in self.imageList:
            img = cv2.imread(f'{self.path}/{cl}')
            self.known_images.append(img)
            self.known_email.append(os.path.splitext(cl)[0])
            
        for img in self.known_images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            self.known_encode.append(encode)
        self.video_capture = cv2.VideoCapture(0)
        
        
    def __del__(self):
        self.video_capture.release()
        
    def get_frame(self):
        ret, frame = self.video_capture.read()
        name = "[Unknown]"
        email = ""
        attendance = ""
        
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
            matches = face_recognition.compare_faces(self.known_encode, current_face_encoding)
            
            face_distances = face_recognition.face_distance(self.known_encode, current_face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                email = self.known_email[best_match_index]
                
            # get name by email using api request
            name = get_name(email)
            # do attendance
            attendance = do_attendance(email)
               

        if len(detect_current_face) > 0:
            current_face = detect_current_face[0]
            cv2.putText(frame, name, (current_face[3]+6, current_face[0]-6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 255, 0), 1)
            cv2.putText(frame, attendance, (50,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0, 255, 0), 1)
        
        ret, jpeg = cv2.imencode('.jpg',frame)
        return jpeg.tobytes()
    
    
    def get_camera(self):
        ret, frame = self.video_capture.read()
        frame = cv2.flip(frame, 1)
            # read frame
        ret, jpeg = cv2.imencode('.jpg',frame)
        return jpeg.tobytes()