import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import numpy as np

# Initialize Camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Initialize Hand Detector
detector = HandDetector(maxHands=1, detectionCon=0.8)  # Increased confidence

# Game Variables
timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [AI, Player]
imgAI = None
lastMove = None  # Fallback move

while True:
    imgBG = cv2.imread("BG.png")
    success, img = cap.read()
    
    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    # Detect Hands
    hands, img = detector.findHands(imgScaled)

    #START
    if startGame:
        if not stateResult:
            timer = time.time() - initialTime
            #countdowntimer
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 3:
                stateResult = True  # Result phase
                timer = 0

                # AI Random Choice
                randomNumber = random.randint(1, 3)
                imgAI = cv2.imread(f'{randomNumber}.png', cv2.IMREAD_UNCHANGED)

                # Improved Hand Gesture Detection
                playerMove = None
                if hands:
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    bbox = hand['bbox']
                    center = hand['center']

                    # Calculate finger gaps to better detect gestures
                    lmList = hand["lmList"]
                    distances = []
                    for i in range(5):
                        distances.append(np.linalg.norm(np.array(lmList[i * 4]) - np.array(lmList[0])))

                    thumb_distance = distances[0]
                    index_distance = distances[1]
                    middle_distance = distances[2]

                    # Detecting ROCK (Closed fist)
                    if all(f == 0 for f in fingers) or (index_distance < 40 and middle_distance < 40):
                        playerMove = 1  # Rock

                    # Detecting PAPER (Open palm)
                    elif all(f == 1 for f in fingers) or (index_distance > 100 and middle_distance > 100):
                        playerMove = 2  # Paper

                    # Detecting SCISSORS (Two fingers up)
                    elif fingers[:2] == [1, 1] and fingers[2:] == [0, 0, 0]:
                        playerMove = 3  # Scissors

                    lastMove = playerMove if playerMove else lastMove  # Fallback to last move

                if playerMove is None:
                    playerMove = lastMove if lastMove else 2  # Default to Paper

                # Determine Winner
                if (playerMove == 1 and randomNumber == 3) or \
                   (playerMove == 2 and randomNumber == 1) or \
                   (playerMove == 3 and randomNumber == 2):
                    scores[1] += 1  # Player Wins
                elif (playerMove == 3 and randomNumber == 1) or \
                     (playerMove == 1 and randomNumber == 2) or \
                     (playerMove == 2 and randomNumber == 3):
                    scores[0] += 1  # AI Wins

    imgBG[234:654, 795:1195] = imgScaled

    if stateResult and imgAI is not None:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    # Display Scores
    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow("BG", imgBG)

    key = cv2.waitKey(1)

    # Restart Game when 's' is pressed
    if key == ord('s'):  
        scores = [0, 0]  # Reset scores
        startGame = True
        initialTime = time.time()
        stateResult = False

    # Stop the game when 'q' is pressed
    if key == ord('q'):
        print("\n **Final Scores**")
        print(f" AI: {scores[0]}")
        print(f" Player: {scores[1]}")
        if scores[0] > scores[1]:
            print(" AI Wins the Game! ")
        elif scores[0] < scores[1]:
            print(" You Win the Game! ")
        else:
            print(" It's a Tie! ")
        
        break  # Exit loop

    elif stateResult:  # Automatically start a new round after 2 seconds
        time.sleep(2)
        initialTime = time.time()
        stateResult = False

# Release Camera and Close Windows
cap.release()
cv2.destroyAllWindows()