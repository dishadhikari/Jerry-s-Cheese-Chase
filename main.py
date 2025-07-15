from ursina import *
from ursina.shaders import lit_with_shadows_shader
app = Ursina()


EditorCamera()
lives = 5
lives_text = Text(text=f"Lives: {lives}", position=(-0.4, 0.5), scale=2, color=color.yellow)

recently_hit_cheese = False

# Maze
my_model = Entity(model='mazefinal.glb', scale=100,
                  position=(0, 0, 0), rotation=(0, 0, 0),
                  collider='mesh', texture='brick')

# Characters
tom = Entity(model='assets/TOM.PSDout.obj',
             scale=0.1, position=(-1, 1, 7), collider='mesh',rotation=(-25,180,0))

jerry = Entity(model='assets/JERRY.PSDout.obj', scale=0.07,
               position=(-1.7, 1, -7), collider='box', rotation=(0, 0, 0))

# Big cheese (goal)
bigcheese = Entity(model='assets/SubTool-0-12656639.obj', scale=1,
                   color=color.yellow, position=(2, 1, 5), collider='mesh')
bigcheese.double_sided = True

# Hazard cheeses
traps = []
positions = [(9, 1, 2), (7, 1, -3), (8, 1, -8), (1, 1, -6.3), (-1.5, 1, 2),
             (-7, 1, 0.3), (-4, 1, 4), (-8, 1, 6)]

cheeses=[]
positions2=[(-3, 1, 6), (-3.7, 1, -1.7),
             (-3.5, 1, -7), (3, 1, 0)]

for pos2 in positions2:
    cheese = Entity(model='assets/SubTool-0-12656639.obj',
                    position=pos2,
                    color=color.yellow,
                    scale=0.5,
                    collider='box')
    cheeses.append(cheese)

for pos in positions:
    trap = Entity(model='assets/bait.obj',
                    position=pos,
                    color=color.gold,
                    texture='brick',
                    scale=0.005,
                    rotation=(-90, 90, -90),
                    collider='box')
    traps.append(trap)

def reset_hit():
    global recently_hit_cheese
    recently_hit_cheese = False

def show_message(text, color=color.white):
    msg = Text(text=text, scale=2, position=(0, 0.4), color=color)
    invoke(destroy, msg, delay=2)

def game_over():
    global game_finished
    if not game_finished:
        game_finished = True
        Audio('assets/gamelose.mp3')
        msg = Text(text="GAME OVER!", scale=2, position=(0, 0.4), color=color.red)
        invoke(destroy, msg, delay=2)
        invoke(application.quit, delay=2)

def game_win():
    global game_finished
    if not game_finished:
        game_finished = True
        Audio('assets/gamewin.mp3')
        msg2 = Text(text="You reached the DADDY CHEESE! Hooray!", scale=2, position=(-0.1, 0.4), color=color.yellow)
        invoke(destroy, msg2, delay=2)
        invoke(application.quit, delay=2.5)

def time_exceeded():
    global game_finished
    if not game_finished:
        game_finished = True
        Audio('assets/gamelose.mp3')
        msg = Text(text="Oh no! Time exceeded!", scale=2, position=(0,0.3), color=color.red)
        invoke(destroy, msg, delay=4)
        invoke(application.quit, delay=5.5)
game_finished = False
invoke(time_exceeded,delay=30)

def update():
    global lives, recently_hit_cheese

    move = Vec3(0, 0, 0)

    if held_keys['left arrow']:
        move.x -= 5 * time.dt
    if held_keys['right arrow']:
        move.x += 5 * time.dt
    if held_keys['up arrow']:
        move.z += 5 * time.dt
    if held_keys['down arrow']:
        move.z -= 5 * time.dt

    jerry.position += move

    for trap in traps[:7]:
        if jerry.intersects(trap).hit:
            if not recently_hit_cheese:
                lives -= 1
                lives_text.text = f"Lives: {lives}" 
                recently_hit_cheese = True
                if lives < 0:
                    game_over()
                else:
                    Audio('assets/traphit.mp3')
                    show_message("You lost a life!", color.red)
                    invoke(reset_hit, delay=1)
            break
    for cheese in cheeses[:4]:
        if jerry.intersects(cheese).hit:
            if not recently_hit_cheese:
                lives += 1
                lives_text.text = f"Lives: {lives}"
                Audio('assets/cheesehit.mp3')
                show_message("You gained a life!", color.green)
                recently_hit_cheese = True
                invoke(reset_hit, delay=1)
            break
    if jerry.intersects(bigcheese).hit:
        game_win()
    if jerry.intersects(tom).hit:
        game_over()
app.run()
