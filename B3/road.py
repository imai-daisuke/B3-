from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *
import light as li
import car as c
import random as random

def road_builder(level,start_x,start_y,start_z,area_size_x,area_size_z,n_direction,e_direction,s_direction,w_direction):
    s_x=start_x
    s_z=start_z
    s_y=start_y
    areasize=[area_size_x,area_size_z]
    level=level
    road_area=[[1]*area_size_x for i in range(area_size_z)]
    if area_size_x>=area_size_z:
        walking_space=area_size_z//5
    else:
        walking_space=area_size_x//5
    for i in range(walking_space,areasize[0]-walking_space):
        for j in range(walking_space,areasize[1]-walking_space):
            road_area[j][i]=0
    road(level,s_x,s_y,s_z,areasize,road_area,walking_space,n_direction,e_direction,s_direction,w_direction)
#center_line=2,road=0,walk=1

def road(level,s_x,s_y,s_z,areasize,road_area,walking_space,n_direction,e_direction,s_direction,w_direction):
    # 0:road 1:other
    count=n_direction+s_direction+w_direction+e_direction
    if n_direction==0:
        for j in range(walking_space):
            for i in range(walking_space,areasize[0]-walking_space):
                road_area[j][i]=0
    if s_direction==0:
        for j in range(areasize[1]-walking_space,areasize[1]):
            for i in range(walking_space,areasize[0]-walking_space):
                road_area[j][i]=0
    if e_direction==0:
        for i in range(areasize[0]-walking_space,areasize[0]):
            for j in range(walking_space,areasize[1]-walking_space):
                road_area[j][i]=0
    if w_direction==0:
        for i in range(walking_space):
            for j in range(walking_space,areasize[1]-walking_space):
                road_area[j][i]=0
    
    if areasize[0] >= 13 and areasize[1] >=13:
        for i in range(areasize[0]):#center_line
            for j in range(areasize[1]):
                if areasize[0]%2==0:
                    if (i==areasize[0]/2) or (i==areasize[0]/2-1): 
                        road_area[j][i]=2
                else:
                    if i==-(-areasize[0]//2)-1: 
                        road_area[j][i]=2
                if areasize[1]%2==0:
                    if (j==areasize[1]/2) or (j==areasize[1]/2-1): 
                        road_area[j][i]=2
                else:
                    if j==-(-areasize[1]//2)-1: 
                        road_area[j][i]=2

    if count<2:
        for i in range(walking_space,areasize[0]-walking_space):
            for j in range(walking_space,areasize[1]-walking_space):
                road_area[j][i]=0
    else:
        if n_direction==1:
            if areasize[1]%2==0:
                for j in range(walking_space,areasize[1]/2-1):
                    if areasize[0]%2==0:
                        road_area[j][areasize[0]/2]=0
                        road_area[j][areasize[0]/2-1]=0
                    else:
                        road_area[j][-(-areasize[0]//2)-1]=0
            else:
                for j in range(walking_space,-(-areasize[1]//2)-1):
                    if areasize[0]%2==0:
                        road_area[j][areasize[0]/2]=0
                        road_area[j][areasize[0]/2-1]=0
                    else:
                        road_area[j][-(-areasize[0]//2)-1]=0
        
        if s_direction==1:
            if areasize[1]%2==0:
                for j in range(areasize[1]/2+1,areasize[1]-walking_space):
                    if areasize[0]%2==0:
                        road_area[j][areasize[0]/2]=0
                        road_area[j][areasize[0]/2-1]=0
                    else:
                        road_area[j][-(-areasize[0]//2)-1]=0
            else:
                for j in range(-(-areasize[1]//2),areasize[1]-walking_space):
                    if areasize[0]%2==0:
                        road_area[j][areasize[0]/2]=0
                        road_area[j][areasize[0]/2-1]=0
                    else:
                        road_area[j][-(-areasize[0]//2)-1]=0
        
        if w_direction==1:
            if areasize[0]%2==0:
                for i in range(walking_space,areasize[0]/2-1):
                    if areasize[1]%2==0:
                        road_area[areasize[1]/2][i]=0
                        road_area[areasize[1]/2-1][i]=0
                    else:
                        road_area[-(-areasize[1]//2)-1][i]=0
            else:
                for i in range(walking_space,-(-areasize[0]//2)-1):
                    if areasize[1]%2==0:
                        road_area[areasize[1]/2][i]=0
                        road_area[areasize[1]/2-1][i]=0
                    else:
                        road_area[-(-areasize[1]//2)-1][i]=0
        
        if e_direction==1:
            if areasize[0]%2==0:
                for i in range(areasize[0]/2+1,areasize[0]-walking_space):
                    if areasize[1]%2==0:
                        road_area[areasize[1]/2][i]=0
                        road_area[areasize[1]/2-1][i]=0
                    else:
                        road_area[-(-areasize[1]//2)-1][i]=0
            else:
                for i in range(-(-areasize[0]//2),areasize[0]-walking_space):
                    if areasize[1]%2==0:
                        road_area[areasize[1]/2][i]=0
                        road_area[areasize[1]/2-1][i]=0
                    else:
                        road_area[-(-areasize[1]//2)-1][i]=0
        
    lights_x=areasize[0]/15
    lights__z=areasize[1]/15

    if n_direction==1:
        for i in range(lights_x):
            road_area[walking_space-1][i*15]=3#3 light
    if s_direction==1:
        for i in range(lights_x):
            road_area[-walking_space][i*15]=3
    if e_direction==1:
        for i in range(lights__z):
            road_area[i*15][-walking_space]=3
    if w_direction==1:
        for i in range(lights__z):
            road_area[i*15][walking_space-1]=3
    if n_direction==1 or s_direction==1:
        car_x=areasize[0]-10
        car_max=areasize[0]/10
        pi=random.randint(0,2)
        for i in range(car_max):
            car_p_x=random.randint(0,car_x)
            check=0
            pi=random.randint(1,2)
            for k in range(9):
                for j in range(4):
                    if i % 2==0:
                        check=check+road_area[walking_space+pi+j][car_p_x+k]
                    else:
                        check=check+road_area[-walking_space-4-pi+areasize[1]+j][car_p_x+k]
            if check==0:
                for k in range(9):
                    for j in range(4):
                        if i % 2==0:
                            road_area[walking_space+pi+j][car_p_x+k]=6# 6 car
                        else:
                            road_area[-walking_space-4-pi+areasize[1]+j][car_p_x+k]=6                        
                if i % 2==0:
                    c.car(level,car_p_x+s_x,s_y,walking_space+pi+s_z,1)
                else:
                    c.car(level,car_p_x+s_x,s_y,-walking_space-4-pi+s_z+areasize[1],1)
    
    if e_direction==1 or w_direction==1:
        car_z=areasize[1]-10
        car_max=areasize[1]/10
        pi=random.randint(0,2)
        for i in range(car_max):
            car_p_z=random.randint(0,car_z)
            check=0
            pi=random.randint(1,2)
            for k in range(0,9):
                for j in range(0,4):
                    if i % 2==0:
                        check=check+road_area[car_p_z+k][walking_space+pi+j]
                    else:
                        check=check+road_area[car_p_z+k][-walking_space-4-pi+areasize[0]+j]
            if check==0:
                for k in range(9):
                    for j in range(4):
                        if i % 2==0:
                            road_area[car_p_z+k][walking_space+pi+j]=6# 6 car
                        else:
                            road_area[car_p_z+k][-walking_space-4-pi+areasize[0]+j]=6                        
                if i % 2==0:
                    c.car(level,walking_space+pi+s_x,s_y,car_p_z+s_z,0)
                else:
                    c.car(level,-walking_space-4-pi+areasize[0]+s_x,s_y,car_p_z+s_z,0)


        
        #1=walking 2=center_line 0=road
    for i in range(areasize[0]):
        for j in range(areasize[1]):
            if road_area[j][i]==0 or road_area[j][i]==6:
                setBlock(level,s_x+i,s_y,s_z+j,1,0)
            elif road_area[j][i]==1 or road_area[j][i]==2:
                setBlock(level,s_x+i,s_y,s_z+j,1,4)
            elif road_area[j][i]==3:
                li.light(level,s_x+i,s_y,s_z+j)


#def road_normal(:
    #for i in range(s_x,s_x+areasize[0]):
        #for j in range(s_z,s_z+areasize[1]):
            #setBlock(level,i,s_y,j,1,0)
            #if (i==s_x+road_end or i+1==s_x+areasize[0]) and (j==s_z+road_end or j+1==s_z+areasize[1]):
                #if i==s_x+road_end:
                    #a=0
                #else:
                    #a=1
                #if j==s_z+road_end:
                    #b=0
                #else:
                    #b=1
                #for k in range(i-road_end+a,i+a):
                    #for m in range(j-road_end+b,j+b):
                        #setBlock(level,k,s_y,m,1,4)
    
#def road_x(:
    #road_end=6
    #for i in range(s_x,s_x+areasize[0]):
        #for j in range(s_z,s_z+areasize[1]):
            #setBlock(level,i,s_y,j,1,0)
            #setBlock(level,(s_x*2+areasize[0])/2,s_y,j,1,4)
            #setBlock(level,(s_x*2+areasize[0])/2-1,s_y,j,1,4)
            #if (i==s_x+road_end or i+1==s_x+areasize[0]):
                #if i==s_x+road_end:
                    #a=0
                #else:
                    #a=1
                #for k in range(i-road_end+a,i+a):
                        #setBlock(level,k,s_y,j,1,4)
        
                
