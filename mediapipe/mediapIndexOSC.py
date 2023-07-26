# Import Libraries
import cv2
import time
import mediapipe as mp
from pythonosc import osc_message_builder
from pythonosc import udp_client

num12 = 0.0
num8 = 0.0
num5 = 0.0
num0 = 0.0
closed = False

# Set up the OSC client
sender = udp_client.SimpleUDPClient("127.0.0.1", 57120)

# Grabbing the Hand Model from Mediapipe and
# Initializing the Model
mp_hand = mp.solutions.hands
hands = mp_hand.Hands(
	min_detection_confidence=0.2,
	model_complexity=0,
	max_num_hands=1
)

# Initializing the drawing utils for drawing the facial landmarks on image
mp_drawing = mp.solutions.drawing_utils

# (0) in VideoCapture is used to connect to your computer's default camera
capture = cv2.VideoCapture(0)

# Initializing current time and precious time for calculating the FPS
previousTime = 0
currentTime = 0

while capture.isOpened():
	# capture frame by frame
	ret, frame = capture.read()

	# resizing the frame for better view
	frame = cv2.resize(frame, (800, 600))
	frame = cv2.flip(frame,1)

	# Converting the from BGR to RGB
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Making predictions using holistic model
	# To improve performance, optionally mark the image as not writeable to
	# pass by reference.
	image.flags.writeable = False
	results = hands.process(image)
	image.flags.writeable = True

	# Converting back the RGB image to BGR
	image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

	# Drawing Land Marks
	if results.multi_hand_landmarks:
		for hand_landmark in results.multi_hand_landmarks:
			mp_drawing.draw_landmarks(
										image,
										hand_landmark,
										mp_hand.HAND_CONNECTIONS
									)
		for id, landmark in enumerate(hand_landmark.landmark):
			if id==12 :
				num12 = landmark.y
			if id==8 :
				num8 = landmark.y
			if id==5 :
				num5 = landmark.y
			if id==0 :
				num0 = landmark.y
			if num0-num5 > 0.18:		
				if ((num0-num12 < 0.3) and (num0-num8 < 0.3)):
					if closed==False:
						sender.send_message("/estado", int(1))
					closed = True
				else:
					if closed:
						sender.send_message("/estado", int(0))
					closed = False
			else:
				if ((num0-num12 < 0.15) and (num0-num8 < 0.15)):
					if closed==False:
						sender.send_message("/estado", int(1))
					closed = True
				else:
					if closed:
						sender.send_message("/estado", int(0))
					closed = False
			if id==9 :
				num9y = landmark.y
				num9x = landmark.x

				if num9y > 0.8:
					sender.send_message("/estado", int(2))
				elif num9y > 0.6:
					sender.send_message("/estado", int(3))
				elif num9y > 0.4:
					sender.send_message("/estado", int(4))
				elif num9y > 0.2:
					sender.send_message("/estado", int(5))
				else:
					sender.send_message("/estado", int(6))
					
				if num9x > 0.8:
					sender.send_message("/estado", int(7))
				elif num9x > 0.6:
					sender.send_message("/estado", int(8))
				elif num9x > 0.4:
					sender.send_message("/estado", int(9))
				elif num9x > 0.2:
					sender.send_message("/estado", int(10))
				else:
					sender.send_message("/estado", int(11))

	# Calculating the FPS
	currentTime = time.time()
	fps = 1 / (currentTime-previousTime)
	previousTime = currentTime

	# Displaying FPS on the image
	cv2.putText(image, str(int(fps))+" FPS", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)

	# Display the resulting image
	cv2.imshow("Hall Musical", image)

	# Enter key 'q' to break the loop
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break

# When all the process is done
# Release the capture and destroy all windows
capture.release()
cv2.destroyAllWindows()

# Code to access landmarks
for landmark in mp_holistic.HandLandmark:
	print(landmark, landmark.value)

print(mp_holistic.HandLandmark.WRIST.value)
