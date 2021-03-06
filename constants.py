"""
Constants that guide the game.

@author: Jeroen Vlek <j.vlek@anchormen.nl>
"""
DT = 1.0 / 60.0
DAMPING = 0.8

MAX_DISTANCE_THRESHOLD = 75
PHYSICS_STEPS_PER_FRAME = 1

PUSH_BODY_FRICTION = 0.9
PUSH_BODY_ELASTICITY = 1.0
PUSH_BODY_RADIUS = 50
PUSH_BODY_MASS = 5
PUSH_BODY_MAX_V = 50

COUNTER_MARGIN = 20
GOAL_FRICTION = 0.9
GOAL_ELASTICITY = 1.0
GOAL_MARGIN = 10
RELATIVE_GOAL_SIZE = 0.3

LOGO_RADIUS = 2
LOGO_MASS = 5
LOGO_FRICTION = 0.95
LOGO_ELASTICITY = 1.0
LOGO_SIZE = (120, 120)

COLLTYPE_MOUSE = 1
COLLTYPE_LOGO = 2
COLLTYPE_GOAL = 3

# Taken from: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md
LEFT_WRIST_IDX = 7
LEFT_ELBOW_IDX = 6
RIGHT_WRIST_IDX = 4
RIGHT_ELBOW_IDX = 3
NECK_IDX = 2

# Lol, this is actually the golden ratio, look it up
HAND_FOREARM_RATIO = (1 + 5 ** 0.5) / 2

FONT_NAME = 'Comic Sans MS'  # Hell yeah
FONT_SIZE = 60
OBJECT_COLOR = (229, 11, 20)