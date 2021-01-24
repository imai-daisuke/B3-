from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *

def light(level,x,y,z):
    for i in range(y,y+9):
        setBlock(level,x,i,z,42,0)
    for j in range(1,3):
        setBlock(level,x+j,i,z-j,45,0)
        setBlock(level,x-j,i,z+j,45,0)
        setBlock(level,x+j,i,z+j,45,0)
        setBlock(level,x-j,i,z-j,45,0)
    for l in range(1,3):
        setBlock(level,x+j,i-l,z-j,113,0)
        setBlock(level,x-j,i-l,z+j,113,0)
        setBlock(level,x+j,i-l,z+j,113,0)
        setBlock(level,x-j,i-l,z-j,113,0)
    setBlock(level,x+j,i-l-1,z-j,169,0)
    setBlock(level,x-j,i-l-1,z+j,169,0)
    setBlock(level,x+j,i-l-1,z+j,169,0)
    setBlock(level,x-j,i-l-1,z-j,169,0)
    setBlock(level,x,i+1,z,89,0)