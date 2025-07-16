<strong>Jerrry's Cheese Chase</strong><br>
A 3D web-based game where Jerry chases the cheese while avoiding Tom and the poisonous walls of the rattrap.<br>
You are Jerry. Get to the Daddy Cheese in less than 30 seconds to win the game, but beware of the poisonous walls, rattraps and Tom waiting for you near the Daddy Cheese.<br>
<br>
<strong> Demo Video</strong><br>
https://www.youtube.com/watch?v=iIDA102VYcM<br>
<br>
<strong> Installation</strong><br>
1. Python extension in Visual Studio Code/Python IDLE<br>
2. Ursina Engine <a href=https://www.ursinaengine.org/installation.html>(installation guide)</a><br>
<br>
<strong>Gameplay-Controls</strong><br>
Up, Down. Left, Right keys for moving throught the maze<br>
1. If you hit a trap, you lose a point<br>
2. If you pass through a cheese, you gain a point<br>
3. If you meet Tom, you lose the game<br>
4. If you are not able to reach the Daddy Cheese in not more than 30 seconds, you lose the game <br>
5. If you lose all your lives and are left with 0 lives, you lose the game<br>
6. You win the game when you reach the Daddy Cheese<br>
<br>
<strong>Project Structure</strong><br>
<pre>
├── main.py                           # Python source code
├── index.html                        # HTML Code
├── server.py                         # Python Flask code
├── style.css                         # CSS code
├── mazefinal.glb                     # 3D maze made in TinkerCAD
├── assets                            # Assets folder
│   ├── textures.. (.jpg)             # JPG images (Tom and Jerry picture, cheese background)
│   └── sounds..   (.mp3)             # WAV files (game win, lose; live gain,lost)
│   └── 3D models..(.obj,.mtl)        # STL files (Tom, Jerry, trap, cheeses)
└── README.md                         # This file
</pre><br>
<strong>Tech Stack used- </strong><br>
1. Ursina Engine (of Python)<br>
2. Python Flask<br>
3. HTML and CSS<br>
<br>
<strong> Contributing</strong>-<br>
Pull requests are welcome. For major changes, open an issue.<br>
<br>
Made by- <br>
@dishadhikari<br>
@AkshatPorwal123<br>
