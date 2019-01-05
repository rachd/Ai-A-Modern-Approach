WIDTH = 2
HEIGHT = 1

# 0 = clean; 1 = dirty
dirt = [[0, 0]]
loc = [0, 0]
score = 0

def performance(dirt):
    score = 0
    for row in dirt:
        for col in row:
            if col  == 0:
                score = score + 1
    return score

def vacuum():
    locState = dirt[loc[0]][loc[1]]
    if locState == 1:
        suck()
    else:
        move()

def suck():
    global dirt
    dirt[loc[0]][loc[1]] = 0

def move():
    global loc
    global score
    if loc[1] == 0:
        loc = [loc[0], 1]
    else:
        loc = [loc[0], 0]
    score = score - 1

def run(idirt, iloc):
    global dirt
    global loc
    global score
    dirt = idirt
    loc = iloc
    score = 0
    for i in range(0, 1000):
        vacuum()
        score = score + performance(dirt)
    return score

score1 = run([[0, 0]], [0, 0])
score2 = run([[0, 0]], [0, 1])
score3 = run([[0, 1]], [0, 0])
score4 = run([[0, 1]], [0, 1])
score5 = run([[1, 0]], [0, 0])
score6 = run([[1, 0]], [0, 1])
score7 = run([[1, 1]], [0, 0])
score8 = run([[1, 1]], [0, 1])

average = (score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8) / 8
print("1: " + str(score1) + "\n2: " + str(score2) + "\n3: " + str(score3) + "\n4: " + str(score4) + "\n5: " + str(score5) + "\n6: " + str(score6) + "\n7: " + str(score7) + "\n8: " + str(score8))
print("average: " + str(average))
