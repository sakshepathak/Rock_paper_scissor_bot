# Rock-Paper-Scissors AI Game  

## Overview  
This is a **Rock-Paper-Scissors game with AI-powered gesture recognition** using OpenCV and Mediapipe. The game detects your hand gestures via webcam and plays against an AI opponent.  

## Features  
- **Real-time hand gesture detection** using OpenCV and Mediapipe.  
- **AI opponent** that randomly selects its move.  
- **Automatic score tracking** for both the player and AI.  
- **Intuitive UI** with a countdown timer before each round.  
- **Seamless gameplay** with auto-restart after each round.  

## Installation  
### 1. Clone the Repository  
```
git clone https://github.com/sakshepathak/rock-paper-scissors-ai.git  
cd rock-paper-scissors-ai  
```
### 2. Create a Virtual Environment (Optional but Recommended)  
```
python -m venv venv  
source venv/bin/activate  # On macOS/Linux  
venv\Scripts\activate     # On Windows  
```
### 3. Install Dependencies  
```
pip install -r requirements.txt  
```

## How to Run the Game  
1. **Ensure your webcam is connected**.  
2. Run the game using:  
```
python main.py  
```
3. Show one of the three gestures: **Rock (fist), Paper (open hand), or Scissors (two fingers up)**.  
4. The AI randomly picks a move, and the winner is displayed.  
5. The game **automatically restarts every round**, or you can press `'s'` to restart manually.  
6. Press `'q'` to **exit** the game.  

## Game Controls  
- **'s' Key** → Restart the game.  
- **'q' Key** → Quit the game.  

## Troubleshooting  
- If the **hand is not detected**, ensure you have good lighting and position your hand clearly in front of the webcam.  
- If OpenCV errors occur, update it with:  
```
pip install --upgrade opencv-python  
```
- If dependencies fail, install them manually:  
```
pip install numpy opencv-python cvzone  
```

## License  
This project is licensed under the **MIT License**. See the `LICENSE` file for details.  
