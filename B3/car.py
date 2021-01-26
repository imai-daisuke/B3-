from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *
import random

def car(level,x,y,z,direction):
    car_depth=9
    car_width=4
    material=random.randint(0,15)
    if direction==0:
        for i in range(x,x+car_width):
            for j in range(z,z+car_depth):
                setBlock(level,i,y+2,j,35,material)
                setBlock(level,i,y+3,j,35,material)
        for i in range(x,x+car_width):
            for j in range(z+2,z+car_depth-2):
                setBlock(level,i,y+4,j,35,material)
                setBlock(level,i,y+5,j,35,material)
        for k in range(y+1,y+3):
            setBlock(level,x,k,z+2,42,0)
            setBlock(level,x,k,z+1,42,0)
            setBlock(level,x,k,z+car_depth-2,42,0)
            setBlock(level,x,k,z+car_depth-3,42,0)
            setBlock(level,i,k,z+2,42,0)
            setBlock(level,i,k,z+1,42,0)
            setBlock(level,i,k,z+car_depth-2,42,0)
            setBlock(level,i,k,z+car_depth-3,42,0)
    else:
        for i in range(x,x+car_depth):
            for j in range(z,z+car_width):
                setBlock(level,i,y+2,j,35,material)
                setBlock(level,i,y+3,j,35,material)
        for i in range(x+2,x+car_depth-2):
            for j in range(z,z+car_width):
                setBlock(level,i,y+4,j,35,material)
                setBlock(level,i,y+5,j,35,material)
        for k in range(y+1,y+3):
            setBlock(level,x+2,k,z,42,0)
            setBlock(level,x+1,k,z,42,0)
            setBlock(level,x+car_depth-2,k,z,42,0)
            setBlock(level,x+car_depth-3,k,z,42,0)
            setBlock(level,x+2,k,j,42,0)
            setBlock(level,x+1,k,j,42,0)
            setBlock(level,x+car_depth-2,k,j,42,0)
            setBlock(level,x+car_depth-3,k,j,42,0)