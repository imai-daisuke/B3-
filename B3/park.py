from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *
import random as rand

def make_park(level,start_x,start_y,start_z,x_size,z_size):
    park=[[1]*x_size for i in range (z_size)]#1 leaves
    entrance_size=5
    for i in range(1,x_size-1):
        for j in range(1,z_size-1):
            park[i][j]=0
    if x_size>7 and z_size>7:
        for i in range(entrance_size):
            if i%2:
                park[x_size/2-2+i][0]=2#2 stone fence
                park[x_size/2-2+i][-1]=2
                park[0][z_size/2-2+i]=2
                park[-1][z_size/2-2+i]=2
            else:
                park[x_size/2-2+i][0]=0#0 none
                park[x_size/2-2+i][-1]=0
                park[0][z_size/2-2+i]=0
                park[-1][z_size/2-2+i]=0
    else:
        park[x_size/2][0]=0#0 none
        park[x_size/2][-1]=0
        park[0][z_size/2]=0
        park[-1][z_size/2]=0

    direction=0
    if x_size >= z_size:
        width_area=(x_size-4)/5
        depth_area=(z_size-4)/3
        swing_x=rand.randint(0,width_area-1)
        swing_z= rand.randint(0,depth_area-1)
        if x_size*z_size>=100:
            sand_x=rand.randint(0,width_area-1)
            sand_z=rand.randint(0,depth_area-1)
            while swing_x==sand_x or swing_z==sand_z:
                sand_x=rand.randint(0,width_area-1)
                sand_z=rand.randint(0,depth_area-1)
        for i in range(5):
            for j in range(3):
                park[swing_x*5+i+2][swing_z*3+j+2]=3#3 swing
                if x_size*z_size>=100:
                    park[sand_x*5+i+2][sand_z*3+j+2]=4#4 sand
    """ else:
        direction=1
        width_area=(z_size-4)/5
        depth_area=(x_size-4)/3
        swing_x=rand.randint(0,depth_area-1)
        swing_z= rand.randint(0,width_area-1)
        if x_size*z_size>=100:
            sand_x=rand.randint(0,depth_area-1)
            sand_z=rand.randint(0,width_area-1)
            while swing_x==sand_x or swing_z==sand_z:
                sand_x=rand.randint(0,depth_area-1)
                sand_z=rand.randint(0,width_area-1)
        for i in range(5):
            for j in range(3):
                park[swing_x*3+j+2][swing_z*5+i+2]=3#3 swing
                if x_size*z_size>=100:
                    park[sand_x*3+j+2][sand_z*5+i+2]=4#4 sand
 """
    lightcount=0
    lightlimit=x_size*z_size/200
    if x_size*z_size<200:
        lightlimit=1
    for i in range(1,x_size-1):
        for j in range(1,z_size-1):
            if park[i][j]==0 and rand.random() <= 0.05:
                park[i][j]=5#5 light
                lightcount=1+lightcount
            if lightcount >= lightlimit:
                break


    swing_count=0        
    for i in range(x_size):
        for j in range(z_size):
            setBlock(level,start_x+i,start_y,start_z+j,208,0)
            if park[i][j]==1:
                setBlock(level,start_x+i,start_y+1,start_z+j,18,0)
            elif park[i][j]==2:
                setBlock(level,start_x+i,start_y+1,start_z+j,139,0)
            elif park[i][j]==5:
                setlight(level,start_x+i,start_y,start_z+j)
            elif park[i][j]==4:
                setBlock(level,start_x+i,start_y,start_z+j,12,0)
            elif park[i][j]==3:
                setBlock(level,start_x+i,start_y,start_z+j,1,0)
            if swing_count>=1:
                continue
            elif park[i][j]==3:
                swing(level,start_x+i,start_y+1,start_z+j,direction)
                swing_count=1+swing_count

def setlight(level,x,y,z):
    for i in range(1,6):
        setBlock(level,x,y+i,z,191,0)
    setBlock(level,x,y+i+1,z,89,0)
    setBlock(level,x+1,y+i+1,z,96,7)
    setBlock(level,x-1,y+i+1,z,96,6)
    setBlock(level,x,y+i+1,z+1,96,5)
    setBlock(level,x,y+i+1,z-1,96,4)
    setBlock(level,x,y+i+2,z,96,0)

def swing(level,start_x,start_y,start_z,direction):
    if direction==0:
        setBlock(level,start_x,start_y,start_z,139,0)
        setBlock(level,start_x,start_y,start_z+2,139,0)
        setBlock(level,start_x+4,start_y,start_z,139,0)
        setBlock(level,start_x+4,start_y,start_z+2,139,0)
        for i in range(3):
            setBlock(level,start_x,start_y+1,start_z+i,85,0)
            setBlock(level,start_x+4,start_y+1,start_z+i,85,0)
            setBlock(level,start_x,start_y+2+i,start_z+1,85,0)
            setBlock(level,start_x+4,start_y+2+i,start_z+1,85,0)
            setBlock(level,start_x+1+i,start_y+4,start_z+1,85,0)
            setBlock(level,start_x+1,start_y+3-i,start_z+1,198,0)
            setBlock(level,start_x+3,start_y+3-i,start_z+1,198,0)
            setBlock(level,start_x+1+i,start_y,start_z+1,44,10)
    else:
        setBlock(level,start_x,start_y,start_z,139,0)
        setBlock(level,start_x+2,start_y,start_z,139,0)
        setBlock(level,start_x,start_y,start_z+4,139,0)
        setBlock(level,start_x+2,start_y,start_z+4,139,0)
        for i in range(3):
            setBlock(level,start_x+i,start_y+1,start_z,85,0)
            setBlock(level,start_x+i,start_y+1,start_z+4,85,0)
            setBlock(level,start_x+1,start_y+2+i,start_z,85,0)
            setBlock(level,start_x+1,start_y+2+i,start_z+4,85,0)
            setBlock(level,start_x+1,start_y+4,start_z+1+i,85,0)
            setBlock(level,start_x+1,start_y+3-i,start_z+1,198,0)
            setBlock(level,start_x+1,start_y+3-i,start_z+3,198,0)
            setBlock(level,start_x+1,start_y,start_z+1+i,44,10)

        
