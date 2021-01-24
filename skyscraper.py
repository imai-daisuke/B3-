from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *
import random

def skyscraper(level,start_x,start_z,start_y):
    y=0
    glass1=random.randint(0,15)
    glass2=random.randint(0,15)
    wool1=random.randint(0,15)
    wool2=random.randint(0,15)
    materials=[glass1,glass2,wool1,wool2]
    materials_copy=materials
    if glass1==glass2 or wool2==wool1 or glass1==wool1 or glass1==wool2 or glass2==wool1 or glass2==wool2:
        glass1=random.randint(0,15)
        glass2=random.randint(0,15)
        wool1=random.randint(0,15)
        wool2=random.randint(0,15)
    floor_count=random.randint(9,16)
    set_furniture(level,start_x,start_y,start_z,y)
    y=first_floor(level,start_x,start_z,start_y,y,glass1,glass2,wool1,wool2)
    for i in range(floor_count):
        set_furniture(level,start_x,start_y,start_z,y)
        y=floor(level,start_x,start_z,start_y,y,glass1,glass2,wool1,wool2)
    set_furniture(level,start_x,start_y,start_z,y)
    y=final_floor(level,start_x,start_z,start_y,y,glass1,glass2,wool1,wool2)
    for height in range(1,y+1):
        if height%2!=0:
            for i in range(15,17):
                for j in range(15,17):
                    setBlock(level,start_x+i,start_y+height,start_z+j,68,0)
        else:
            for i in range(15,17):
                for j in range(15,17):
                    setBlock(level,start_x+i,start_y+height,start_z+j,9,0)


def first_floor(level,s_x,s_z,s_y,y,glass1,glass2,wool1,wool2):
    for i in range(s_x,s_x+32):
        for j in range(s_z,s_z+32):
            setBlock(level,i,s_y+y,j,35,wool1)
    for i in range(s_x+3,s_x+29):
        for j in range(s_z+3,s_z+29):
            setBlock(level,i,s_y+y,j,5,0)
    for m in range(3):
        setBlock(level,s_x+14,s_y+y,s_z+m,35,wool2)
        setBlock(level,s_x+17,s_y+y,s_z+m,35,wool2)
        setBlock(level,s_x+14,s_y+y,s_z+31-m,35,wool2)
        setBlock(level,s_x+17,s_y+y,s_z+31-m,35,wool2)
        setBlock(level,s_x+m,s_y+y,s_z+14,35,wool2)
        setBlock(level,s_x+m,s_y+y,s_z+17,35,wool2)
        setBlock(level,s_x+31-m,s_y+y,s_z+14,35,wool2)
        setBlock(level,s_x+31-m,s_y+y,s_z+17,35,wool2)

    y=y+1
    for n in range(4):    
        for i in range(s_x+1,s_x+31):
            if i==s_x+15 or i==s_x+16:
                continue
            setBlock(level,i,s_y+y,s_z+1,95,glass1)
            setBlock(level,i,s_y+y,s_z+30,95,glass1)
        for j in range(s_z+1,s_z+31):
            if j==s_z+15 or j==s_z+16:
                continue
            setBlock(level,s_x+1,s_y+y,j,95,glass1)#glass1
            setBlock(level,s_x+30,s_y+y,j,95,glass1)
        for i in range(14,18):
            setBlock(level,s_x+i,s_y+y,s_z+14,169,0)
            setBlock(level,s_x+i,s_y+y,s_z+17,169,0)
            setBlock(level,s_x+14,s_y+y,s_z+i,169,0)
            setBlock(level,s_x+17,s_y+y,s_z+i,169,0)
        for m in range(3):
            setBlock(level,s_x+14,s_y+y,s_z+m,35,wool2)#wool2
            setBlock(level,s_x+17,s_y+y,s_z+m,35,wool2)
            setBlock(level,s_x+14,s_y+y,s_z+31-m,35,wool2)
            setBlock(level,s_x+17,s_y+y,s_z+31-m,35,wool2)
            setBlock(level,s_x+m,s_y+y,s_z+14,35,wool2)
            setBlock(level,s_x+m,s_y+y,s_z+17,35,wool2)
            setBlock(level,s_x+31-m,s_y+y,s_z+14,35,wool2)
            setBlock(level,s_x+31-m,s_y+y,s_z+17,35,wool2)
        for _ in range(3):
            setBlock(level,s_x+4,s_y+y,s_z+_,35,wool1)#wool1
            setBlock(level,s_x+4,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+9,s_y+y,s_z+_,35,wool1)
            setBlock(level,s_x+9,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+27,s_y+y,s_z+_,35,wool1)
            setBlock(level,s_x+27,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+22,s_y+y,s_z+_,35,wool1)
            setBlock(level,s_x+22,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+4,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+4,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+9,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+9,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+27,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+27,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+22,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+22,35,wool1)
        y=y+1
    for k in range(3,5):
        for _ in range(15,17):
            setBlock(level,s_x+_,s_y+k,s_z,169,0)
            setBlock(level,s_x+_,s_y+k,s_z+31,169,0)
            setBlock(level,s_x+_,s_y+k,s_z+1,169,0)
            setBlock(level,s_x+_,s_y+k,s_z+30,169,0)
            setBlock(level,s_x+_,s_y+k,s_z+2,169,0)
            setBlock(level,s_x+_,s_y+k,s_z+29,169,0)
            setBlock(level,s_x,s_y+k,s_z+_,169,0)
            setBlock(level,s_x+31,s_y+k,s_z+_,169,0)
            setBlock(level,s_x+1,s_y+k,s_z+_,169,0)
            setBlock(level,s_x+30,s_y+k,s_z+_,169,0)
            setBlock(level,s_x+2,s_y+k,s_z+_,169,0)
            setBlock(level,s_x+29,s_y+k,s_z+_,169,0)
    setBlock(level,s_x+15,s_y+1,s_z+1,71,1)
    setBlock(level,s_x+15,s_y+2,s_z+1,71,8)

    setBlock(level,s_x+15,s_y+1,s_z+30,71,3)
    setBlock(level,s_x+15,s_y+2,s_z+30,71,12)

    setBlock(level,s_x+1,s_y+1,s_z+15,71,0)
    setBlock(level,s_x+1,s_y+2,s_z+15,71,8)

    setBlock(level,s_x+30,s_y+1,s_z+15,71,5)
    setBlock(level,s_x+30,s_y+2,s_z+15,71,12)

    setBlock(level,s_x+16,s_y+1,s_z+1,71,1)
    setBlock(level,s_x+16,s_y+2,s_z+1,71,12)

    setBlock(level,s_x+16,s_y+1,s_z+30,71,3)
    setBlock(level,s_x+16,s_y+2,s_z+30,71,8)

    setBlock(level,s_x+1,s_y+1,s_z+16,71,7)
    setBlock(level,s_x+1,s_y+2,s_z+16,71,12)

    setBlock(level,s_x+30,s_y+1,s_z+16,71,2)
    setBlock(level,s_x+30,s_y+2,s_z+16,71,8)
    for h in range(15,17):
        setBlock(level,s_x+h,s_y+1,s_z,70,0)
        setBlock(level,s_x+h,s_y+1,s_z+31,70,0)
        setBlock(level,s_x,s_y+1,s_z+h,70,0)
        setBlock(level,s_x+31,s_y+1,s_z+h,70,0)
        setBlock(level,s_x+h,s_y+1,s_z+2,70,0)
        setBlock(level,s_x+h,s_y+1,s_z+29,70,0)
        setBlock(level,s_x+2,s_y+1,s_z+h,70,0)
        setBlock(level,s_x+29,s_y+1,s_z+h,70,0)

    setBlock(level,s_x+14,s_y+1,s_z+15,193,0)
    setBlock(level,s_x+14,s_y+2,s_z+15,193,8)

    setBlock(level,s_x+17,s_y+1,s_z+15,193,5)
    setBlock(level,s_x+17,s_y+2,s_z+15,193,12)

    setBlock(level,s_x+14,s_y+1,s_z+16,193,7)
    setBlock(level,s_x+14,s_y+2,s_z+16,193,12)

    setBlock(level,s_x+17,s_y+1,s_z+16,193,2)
    setBlock(level,s_x+17,s_y+2,s_z+16,193,8)
    return y

def floor(level,s_x,s_z,s_y,y,glass1,glass2,wool1,wool2):
    y_given=y
    for i in range(s_x,s_x+32):
        for j in range(s_z,s_z+32):
            if (i==s_x+15 or i==s_x+16 or j==s_z+15 or j==s_z+16) and (j==s_z or j==s_z+31 or i==s_x or i==s_x+31):
                continue
            setBlock(level,i,s_y+y,j,35,wool1)
    for i in range(s_x+3,s_x+29):
        for j in range(s_z+3,s_z+29):
            setBlock(level,i,s_y+y,j,5,0)
    setBlock(level,s_x+15,s_y+y,s_z+1,95,glass2)#if first __ delete
    setBlock(level,s_x+16,s_y+y,s_z+1,95,glass2)
    setBlock(level,s_x+15,s_y+y,s_z+30,95,glass2)
    setBlock(level,s_x+16,s_y+y,s_z+30,95,glass2)
    setBlock(level,s_x+1,s_y+y,s_z+15,95,glass2)
    setBlock(level,s_x+1,s_y+y,s_z+16,95,glass2)
    setBlock(level,s_x+30,s_y+y,s_z+15,95,glass2)
    setBlock(level,s_x+30,s_y+y,s_z+16,95,glass2)
    setBlock(level,s_x+15,s_y+y,s_z+2,35,wool2)#if first __ delete
    setBlock(level,s_x+16,s_y+y,s_z+2,35,wool2)
    setBlock(level,s_x+15,s_y+y,s_z+29,35,wool2)
    setBlock(level,s_x+16,s_y+y,s_z+29,35,wool2)
    setBlock(level,s_x+2,s_y+y,s_z+15,35,wool2)
    setBlock(level,s_x+2,s_y+y,s_z+16,35,wool2)
    setBlock(level,s_x+29,s_y+y,s_z+15,35,wool2)
    setBlock(level,s_x+29,s_y+y,s_z+16,35,wool2)
    for m in range(3):
        setBlock(level,s_x+14,s_y+y,s_z+m,35,wool2)
        setBlock(level,s_x+17,s_y+y,s_z+m,35,wool2)
        setBlock(level,s_x+14,s_y+y,s_z+31-m,35,wool2)
        setBlock(level,s_x+17,s_y+y,s_z+31-m,35,wool2)
        setBlock(level,s_x+m,s_y+y,s_z+14,35,wool2)
        setBlock(level,s_x+m,s_y+y,s_z+17,35,wool2)
        setBlock(level,s_x+31-m,s_y+y,s_z+14,35,wool2)
        setBlock(level,s_x+31-m,s_y+y,s_z+17,35,wool2)

    y=y+1
    for n in range(4):    
        for i in range(s_x+1,s_x+31):
            setBlock(level,i,s_y+y,s_z+1,95,glass1)
            setBlock(level,i,s_y+y,s_z+30,95,glass1)
        for j in range(s_z+1,s_z+31):
            setBlock(level,s_x+1,s_y+y,j,95,glass1)#glass1
            setBlock(level,s_x+30,s_y+y,j,95,glass1)
        for i in range(14,18):
            setBlock(level,s_x+i,s_y+y,s_z+14,169,0)
            setBlock(level,s_x+i,s_y+y,s_z+17,169,0)
            setBlock(level,s_x+14,s_y+y,s_z+i,169,0)
            setBlock(level,s_x+17,s_y+y,s_z+i,169,0)
        setBlock(level,s_x+15,s_y+y,s_z+1,95,glass2)#glass2
        setBlock(level,s_x+16,s_y+y,s_z+1,95,glass2)
        setBlock(level,s_x+15,s_y+y,s_z+30,95,glass2)
        setBlock(level,s_x+16,s_y+y,s_z+30,95,glass2)
        setBlock(level,s_x+1,s_y+y,s_z+15,95,glass2)
        setBlock(level,s_x+1,s_y+y,s_z+16,95,glass2)
        setBlock(level,s_x+30,s_y+y,s_z+15,95,glass2)
        setBlock(level,s_x+30,s_y+y,s_z+16,95,glass2)
        setBlock(level,s_x+15,s_y+y,s_z+2,35,wool2)#if first __ delete
        setBlock(level,s_x+16,s_y+y,s_z+2,35,wool2)
        setBlock(level,s_x+15,s_y+y,s_z+29,35,wool2)
        setBlock(level,s_x+16,s_y+y,s_z+29,35,wool2)
        setBlock(level,s_x+2,s_y+y,s_z+15,35,wool2)
        setBlock(level,s_x+2,s_y+y,s_z+16,35,wool2)
        setBlock(level,s_x+29,s_y+y,s_z+15,35,wool2)
        setBlock(level,s_x+29,s_y+y,s_z+16,35,wool2)
        for m in range(3):
            setBlock(level,s_x+14,s_y+y,s_z+m,35,wool2)#wool2
            setBlock(level,s_x+17,s_y+y,s_z+m,35,wool2)
            setBlock(level,s_x+14,s_y+y,s_z+31-m,35,wool2)
            setBlock(level,s_x+17,s_y+y,s_z+31-m,35,wool2)
            setBlock(level,s_x+m,s_y+y,s_z+14,35,wool2)
            setBlock(level,s_x+m,s_y+y,s_z+17,35,wool2)
            setBlock(level,s_x+31-m,s_y+y,s_z+14,35,wool2)
            setBlock(level,s_x+31-m,s_y+y,s_z+17,35,wool2)
            setBlock(level,s_x+4,s_y+y,s_z+1,35,wool1)
        for _ in range(3):
            setBlock(level,s_x+4,s_y+y,s_z+_,35,wool1)#wool1
            setBlock(level,s_x+4,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+9,s_y+y,s_z+_,35,wool1)
            setBlock(level,s_x+9,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+27,s_y+y,s_z+_,35,wool1)
            setBlock(level,s_x+27,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+22,s_y+y,s_z+_,35,wool1)
            setBlock(level,s_x+22,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+4,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+4,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+9,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+9,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+27,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+27,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+22,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+22,35,wool1)
        y=y+1

    setBlock(level,s_x+14,s_y+y_given+1,s_z+15,193,0)
    setBlock(level,s_x+14,s_y+y_given+2,s_z+15,193,8)

    setBlock(level,s_x+17,s_y+y_given+1,s_z+15,193,5)
    setBlock(level,s_x+17,s_y+y_given+2,s_z+15,193,12)

    setBlock(level,s_x+14,s_y+y_given+1,s_z+16,193,7)
    setBlock(level,s_x+14,s_y+y_given+2,s_z+16,193,12)

    setBlock(level,s_x+17,s_y+y_given+1,s_z+16,193,2)
    setBlock(level,s_x+17,s_y+y_given+2,s_z+16,193,8)
    return y

def final_floor(level,s_x,s_z,s_y,y,glass1,glass2,wool1,wool2):
    y_given=y
    for i in range(s_x,s_x+32):
        for j in range(s_z,s_z+32):
            if (i==s_x+15 or i==s_x+16 or j==s_z+15 or j==s_z+16) and (j==s_z or j==s_z+31 or i==s_x or i==s_x+31):
                continue
            setBlock(level,i,s_y+y,j,35,wool1)
    for i in range(s_x+3,s_x+29):
        for j in range(s_z+3,s_z+29):
            setBlock(level,i,s_y+y,j,5,0)
    setBlock(level,s_x+15,s_y+y,s_z+1,95,glass2)#if first __ delete
    setBlock(level,s_x+16,s_y+y,s_z+1,95,glass2)
    setBlock(level,s_x+15,s_y+y,s_z+30,95,glass2)
    setBlock(level,s_x+16,s_y+y,s_z+30,95,glass2)
    setBlock(level,s_x+1,s_y+y,s_z+15,95,glass2)
    setBlock(level,s_x+1,s_y+y,s_z+16,95,glass2)
    setBlock(level,s_x+30,s_y+y,s_z+15,95,glass2)
    setBlock(level,s_x+30,s_y+y,s_z+16,95,glass2)
    setBlock(level,s_x+15,s_y+y,s_z+2,35,wool2)#if first __ delete
    setBlock(level,s_x+16,s_y+y,s_z+2,35,wool2)
    setBlock(level,s_x+15,s_y+y,s_z+29,35,wool2)
    setBlock(level,s_x+16,s_y+y,s_z+29,35,wool2)
    setBlock(level,s_x+2,s_y+y,s_z+15,35,wool2)
    setBlock(level,s_x+2,s_y+y,s_z+16,35,wool2)
    setBlock(level,s_x+29,s_y+y,s_z+15,35,wool2)
    setBlock(level,s_x+29,s_y+y,s_z+16,35,wool2)
    for m in range(3):
        setBlock(level,s_x+14,s_y+y,s_z+m,35,wool2)
        setBlock(level,s_x+17,s_y+y,s_z+m,35,wool2)
        setBlock(level,s_x+14,s_y+y,s_z+31-m,35,wool2)
        setBlock(level,s_x+17,s_y+y,s_z+31-m,35,wool2)
        setBlock(level,s_x+m,s_y+y,s_z+14,35,wool2)
        setBlock(level,s_x+m,s_y+y,s_z+17,35,wool2)
        setBlock(level,s_x+31-m,s_y+y,s_z+14,35,wool2)
        setBlock(level,s_x+31-m,s_y+y,s_z+17,35,wool2)

    y=y+1
    for n in range(4):    
        for i in range(s_x+1,s_x+31):
            setBlock(level,i,s_y+y,s_z+1,95,glass1)
            setBlock(level,i,s_y+y,s_z+30,95,glass1)
        for j in range(s_z+1,s_z+31):
            setBlock(level,s_x+1,s_y+y,j,95,glass1)#glass1
            setBlock(level,s_x+30,s_y+y,j,95,glass1)
        for i in range(14,18):
            setBlock(level,s_x+i,s_y+y,s_z+14,169,0)
            setBlock(level,s_x+i,s_y+y,s_z+17,169,0)
            setBlock(level,s_x+14,s_y+y,s_z+i,169,0)
            setBlock(level,s_x+17,s_y+y,s_z+i,169,0)
        setBlock(level,s_x+15,s_y+y,s_z+1,95,glass2)#glass2
        setBlock(level,s_x+16,s_y+y,s_z+1,95,glass2)
        setBlock(level,s_x+15,s_y+y,s_z+30,95,glass2)
        setBlock(level,s_x+16,s_y+y,s_z+30,95,glass2)
        setBlock(level,s_x+1,s_y+y,s_z+15,95,glass2)
        setBlock(level,s_x+1,s_y+y,s_z+16,95,glass2)
        setBlock(level,s_x+30,s_y+y,s_z+15,95,glass2)
        setBlock(level,s_x+30,s_y+y,s_z+16,95,glass2)
        setBlock(level,s_x+15,s_y+y,s_z+2,35,wool2)#if first __ delete
        setBlock(level,s_x+16,s_y+y,s_z+2,35,wool2)
        setBlock(level,s_x+15,s_y+y,s_z+29,35,wool2)
        setBlock(level,s_x+16,s_y+y,s_z+29,35,wool2)
        setBlock(level,s_x+2,s_y+y,s_z+15,35,wool2)
        setBlock(level,s_x+2,s_y+y,s_z+16,35,wool2)
        setBlock(level,s_x+29,s_y+y,s_z+15,35,wool2)
        setBlock(level,s_x+29,s_y+y,s_z+16,35,wool2)
        for m in range(3):
            setBlock(level,s_x+14,s_y+y,s_z+m,35,wool2)#wool2
            setBlock(level,s_x+17,s_y+y,s_z+m,35,wool2)
            setBlock(level,s_x+14,s_y+y,s_z+31-m,35,wool2)
            setBlock(level,s_x+17,s_y+y,s_z+31-m,35,wool2)
            setBlock(level,s_x+m,s_y+y,s_z+14,35,wool2)
            setBlock(level,s_x+m,s_y+y,s_z+17,35,wool2)
            setBlock(level,s_x+31-m,s_y+y,s_z+14,35,wool2)
            setBlock(level,s_x+31-m,s_y+y,s_z+17,35,wool2)
            setBlock(level,s_x+4,s_y+y,s_z+1,35,wool1)
        for _ in range(3):
            setBlock(level,s_x+4,s_y+y,s_z+_,35,wool1)#wool1
            setBlock(level,s_x+4,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+9,s_y+y,s_z+_,35,wool1)
            setBlock(level,s_x+9,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+27,s_y+y,s_z+_,35,wool1)
            setBlock(level,s_x+27,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+22,s_y+y,s_z+_,35,wool1)
            setBlock(level,s_x+22,s_y+y,s_z+31-_,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+4,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+4,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+9,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+9,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+27,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+27,35,wool1)
            setBlock(level,s_x+_,s_y+y,s_z+22,35,wool1)
            setBlock(level,s_x+31-_,s_y+y,s_z+22,35,wool1)
        y=y+1
    for i in range(s_x,s_x+32):
        for j in range(s_z,s_z+32):
            setBlock(level,i,s_y+y+1,j,171,wool2)
            if (i==s_x+15 or i==s_x+16 or j==s_z+15 or j==s_z+16) and (j==s_z+1 or j==s_z+30 or i==s_x+1 or i==s_x+30):
                setBlock(level,i,s_y+y,j,95,glass2)
                continue
            setBlock(level,i,s_y+y,j,35,wool1)
    setBlock(level,s_x+14,s_y+y_given+1,s_z+15,193,0)
    setBlock(level,s_x+14,s_y+y_given+2,s_z+15,193,8)

    setBlock(level,s_x+17,s_y+y_given+1,s_z+15,193,5)
    setBlock(level,s_x+17,s_y+y_given+2,s_z+15,193,12)

    setBlock(level,s_x+14,s_y+y_given+1,s_z+16,193,7)
    setBlock(level,s_x+14,s_y+y_given+2,s_z+16,193,12)

    setBlock(level,s_x+17,s_y+y_given+1,s_z+16,193,2)
    setBlock(level,s_x+17,s_y+y_given+2,s_z+16,193,8)
    return y

def set_furniture(level,s_x,s_y,s_z,y):
    area=[[0]*26 for i in range(26)]
    bed_color=random.randint(0,15)
    book_height=random.randint(2,4)
    furnitures=[[58,0],[47,0],[89,0]]
    for i in range(26):
        if  11<=i<=14:
            area[i][0]=9#9=can't use
            area[i][25]=9
            area[0][i]=9
            area[25][i]=9
            continue
        area[i][0]=1#1=bookself
        area[i][25]=1
        area[0][i]=1#1=bookself
        area[25][i]=1
    for i in range(9,17):
        for j in range(9,17):
            area[i][j]=9
    if random.random() <= 0.6:
        for i in range(2,6):
            for j in range(11,15):
                area[i][j]=2#carpet
        for i in range(3,5):
            for j in range(12,14):
                area[i][j]=3#carpet
    
    if random.random() <= 0.6:
        for i in range(2,6):
            for j in range(11,15):
                area[j][i]=2#carpet
        for i in range(3,5):
            for j in range(12,14):
                area[j][i]=3#table
        
    if random.random() <= 0.6:
        for i in range(20,24):
            for j in range(11,15):
                area[i][j]=2#carpet
        for i in range(21,23):
            for j in range(12,14):
                area[i][j]=3#table

    if random.random() <= 0.6:
        for i in range(20,24):
            for j in range(11,15):
                area[j][i]=2#carpet
        for i in range(21,23):
            for j in range(12,14):
                area[j][i]=3#table
    for count1,j in enumerate(area):
        for count2,i in enumerate(j):
            if i==0:
                if random.random() <= 0.3:
                    if area[count1-1][count2]!=0 or area[count1+1][count2]!=0 or area[count1][count2-1]!=0 or area[count1][count2+1]!=0:
                        area[count1][count2]=4#furniture

    for count1,j in enumerate(area):
        for count2,i in enumerate(j):
            if i==1:
                for h in range(1,book_height):
                    setBlock(level,s_x+3+count2,s_y+y+h,s_z+3+count1,47,0)
            if i==2:
                setBlock(level,s_x+3+count2,s_y+y+1,s_z+3+count1,171,bed_color)
            if i==3:
                setBlock(level,s_x+3+count2,s_y+y+1,s_z+3+count1,85,0)
                setBlock(level,s_x+3+count2,s_y+y+2,s_z+3+count1,171,bed_color)
            if i==4:
                furniture=random.choice(furnitures)
                id1=furniture[0]
                id2=furniture[1]
                setBlock(level,s_x+3+count2,s_y+y+1,s_z+3+count1,id1,id2)