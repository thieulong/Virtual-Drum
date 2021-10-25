import cv2
import mediapipe
from pygame import mixer

mixer.init()

drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands
 
capture = cv2.VideoCapture(1)
 
frameWidth = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
 
with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:
 
    while True:
 
        ret, frame = capture.read()

        frame = cv2.flip(frame, 1)
 
        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        cv2.rectangle(frame, (0,100), (100,300), (0,0,255),2)

        cv2.rectangle(frame, (540,100), (640,300), (0,0,255),2)

        cv2.rectangle(frame, (150,0), (300,150), (255,0,0),2)

        cv2.rectangle(frame, (340,0), (490,150), (255,0,0),2)

        cv2.rectangle(frame, (100,350), (250,475), (0,255,0),2)

        cv2.rectangle(frame, (390,350), (540,475), (0,255,0),2)

        cv2.putText(frame, 'Snare', (5,200), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)

        cv2.putText(frame, 'Snare', (545,200), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)

        cv2.putText(frame, 'Splash', (175,85), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)

        cv2.putText(frame, 'Hi-Hat', (365,85), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)

        cv2.putText(frame, 'Bass', (140,430), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)

        cv2.putText(frame, 'Tom-Drum', (375,430), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
 
        if results.multi_hand_landmarks != None:

            for handLandmarks in results.multi_hand_landmarks:

                fingertip = 8
                fingertip_normalizedLandmark = handLandmarks.landmark[fingertip]
                fingertip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(fingertip_normalizedLandmark.x, fingertip_normalizedLandmark.y, frameWidth, frameHeight)
                cv2.circle(frame, fingertip_pixelCoordinatesLandmark, 5, (255, 0, 255), -1)

                if fingertip_pixelCoordinatesLandmark[0]<100:
                    if fingertip_pixelCoordinatesLandmark[1]<300 and fingertip_pixelCoordinatesLandmark[1]>100:
                        mixer.music.load('sound/snare.wav')
                        mixer.music.play()

                elif fingertip_pixelCoordinatesLandmark[0]>540:
                    if fingertip_pixelCoordinatesLandmark[1]<300 and fingertip_pixelCoordinatesLandmark[1]>100:
                        mixer.music.load('sound/snare2.wav')
                        mixer.music.play()

                elif fingertip_pixelCoordinatesLandmark[1]<150:
                    if fingertip_pixelCoordinatesLandmark[0]>150 and fingertip_pixelCoordinatesLandmark[0]<300:
                        mixer.music.load('sound/splash.wav')
                        mixer.music.play()
                    if fingertip_pixelCoordinatesLandmark[0]>340 and fingertip_pixelCoordinatesLandmark[0]<490:
                        mixer.music.load('sound/hi-hat.wav')
                        mixer.music.play()
                        
                elif fingertip_pixelCoordinatesLandmark[1]>350:
                    if fingertip_pixelCoordinatesLandmark[0]>100 and fingertip_pixelCoordinatesLandmark[0]<250:
                        mixer.music.load('sound/bass.wav')
                        mixer.music.play()
                    if fingertip_pixelCoordinatesLandmark[0]>390 and fingertip_pixelCoordinatesLandmark[0]<540:
                        mixer.music.load('sound/tom-drum.wav')
                        mixer.music.play()
 
        cv2.imshow('Test hand', frame)
 
        if cv2.waitKey(0) == 27:
            break
 
cv2.destroyAllWindows()
capture.release()