import random
import particle

def setup():
    global Pieces
    Pieces = []
    for i in range (10): 
        Piece = particle.Particle()
        Pieces.append(Piece)
   
    size(450,450)
    background(0)


def draw():
    background(0)
    stroke(255) 
    global Pieces
    for i in range(len(Pieces)):
        Piece = Pieces[i]
        Piece.draw()
        Piece.move()
