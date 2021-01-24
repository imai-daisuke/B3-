from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *

def load_builder(level,start_x,start_y,start_z,area_size_x,area_size_z):
    s_x=start_x
    s_z=start_z
    s_y=start_y
    areasize=[area_size_x,area_size_z]
    level=level
    load_area=[[1]*area_size_x for i in range(area_size_z)]
    if area_size_x>=area_size_z:
        walking_space=area_size_z//5
    else:
        walking_space=area_size_x//5
    for i in range(walking_space,areasize[0]-walking_space):
        for j in range(walking_space,areasize[1]-walking_space):
            load_area[j][i]=0
    load(level,s_x,s_y,s_z,areasize,load_area,walking_space)
#center_line=2,load=0,walk=1

def load(level,s_x,s_y,s_z,areasize,load_area,walking_space):
    n_direction=1# 0:load 1:other
    s_direction=0
    e_direction=1
    w_direction=0
    count=n_direction+s_direction+w_direction+e_direction
    if n_direction==0:
        for j in range(walking_space):
            for i in range(walking_space,areasize[0]-walking_space):
                load_area[j][i]=0
    if s_direction==0:
        for j in range(areasize[1]-walking_space,areasize[1]):
            for i in range(walking_space,areasize[0]-walking_space):
                load_area[j][i]=0
    if e_direction==0:
        for i in range(areasize[0]-walking_space,areasize[0]):
            for j in range(walking_space,areasize[1]-walking_space):
                load_area[j][i]=0
    if w_direction==0:
        for i in range(walking_space):
            for j in range(walking_space,areasize[1]-walking_space):
                load_area[j][i]=0
    
    for i in range(areasize[0]):#center_line
        for j in range(areasize[1]):
            if areasize[0]%2==0:
                if (i==areasize[0]/2) or (i==areasize[0]/2-1): 
                    load_area[j][i]=2
            else:
                if i==-(-areasize[0]//2)-1: 
                    load_area[j][i]=2
            if areasize[1]%2==0:
                if (j==areasize[1]/2) or (j==areasize[1]/2-1): 
                    load_area[j][i]=2
            else:
                if j==-(-areasize[1]//2)-1: 
                    load_area[j][i]=2
    
    if count<2:
        for i in range(walking_space,areasize[0]-walking_space):
            for j in range(walking_space,areasize[1]-walking_space):
                load_area[j][i]=0
    else:
        if n_direction==1:
            if areasize[1]%2==0:
                for j in range(walking_space,areasize[1]/2-1):
                    if areasize[0]%2==0:
                        load_area[j][areasize[0]/2]=0
                        load_area[j][areasize[0]/2-1]=0
                    else:
                        load_area[j][-(-areasize[0]//2)-1]=0
            else:
                for j in range(walking_space,-(-areasize[1]//2)-1):
                    if areasize[0]%2==0:
                        load_area[j][areasize[0]/2]=0
                        load_area[j][areasize[0]/2-1]=0
                    else:
                        load_area[j][-(-areasize[0]//2)-1]=0
        
        if s_direction==1:
            if areasize[1]%2==0:
                for j in range(areasize[1]/2+1,areasize[1]-walking_space):
                    if areasize[0]%2==0:
                        load_area[j][areasize[0]/2]=0
                        load_area[j][areasize[0]/2-1]=0
                    else:
                        load_area[j][-(-areasize[0]//2)-1]=0
            else:
                for j in range(-(-areasize[1]//2),areasize[1]-walking_space):
                    if areasize[0]%2==0:
                        load_area[j][areasize[0]/2]=0
                        load_area[j][areasize[0]/2-1]=0
                    else:
                        load_area[j][-(-areasize[0]//2)-1]=0
        
        if w_direction==1:
            if areasize[0]%2==0:
                for i in range(walking_space,areasize[0]/2-1):
                    if areasize[1]%2==0:
                        load_area[areasize[1]/2][i]=0
                        load_area[areasize[1]/2-1][i]=0
                    else:
                        load_area[-(-areasize[1]//2)-1][i]=0
            else:
                for i in range(walking_space,-(-areasize[0]//2)-1):
                    if areasize[1]%2==0:
                        load_area[areasize[1]/2][i]=0
                        load_area[areasize[1]/2-1][i]=0
                    else:
                        load_area[-(-areasize[1]//2)-1][i]=0
        
        if e_direction==1:
            if areasize[0]%2==0:
                for i in range(areasize[0]/2+1,areasize[0]-walking_space):
                    if areasize[1]%2==0:
                        load_area[areasize[1]/2][i]=0
                        load_area[areasize[1]/2-1][i]=0
                    else:
                        load_area[-(-areasize[1]//2)-1][i]=0
            else:
                for i in range(-(-areasize[0]//2),areasize[0]-walking_space):
                    if areasize[1]%2==0:
                        load_area[areasize[1]/2][i]=0
                        load_area[areasize[1]/2-1][i]=0
                    else:
                        load_area[-(-areasize[1]//2)-1][i]=0
        
        #1=walking 2=center_line 0=load
    for i in range(areasize[0]):
        for j in range(areasize[1]):
            if load_area[j][i]==0:
                setBlock(level,s_x+i,s_y,s_z+j,1,0)
            elif load_area[j][i]==1 or load_area[j][i]==2:
                setBlock(level,s_x+i,s_y,s_z+j,1,4)

#def load_normal(:
    #for i in range(s_x,s_x+areasize[0]):
        #for j in range(s_z,s_z+areasize[1]):
            #setBlock(level,i,s_y,j,1,0)
            #if (i==s_x+load_end or i+1==s_x+areasize[0]) and (j==s_z+load_end or j+1==s_z+areasize[1]):
                #if i==s_x+load_end:
                    #a=0
                #else:
                    #a=1
                #if j==s_z+load_end:
                    #b=0
                #else:
                    #b=1
                #for k in range(i-load_end+a,i+a):
                    #for m in range(j-load_end+b,j+b):
                        #setBlock(level,k,s_y,m,1,4)
    
#def load_x(:
    #load_end=6
    #for i in range(s_x,s_x+areasize[0]):
        #for j in range(s_z,s_z+areasize[1]):
            #setBlock(level,i,s_y,j,1,0)
            #setBlock(level,(s_x*2+areasize[0])/2,s_y,j,1,4)
            #setBlock(level,(s_x*2+areasize[0])/2-1,s_y,j,1,4)
            #if (i==s_x+load_end or i+1==s_x+areasize[0]):
                #if i==s_x+load_end:
                    #a=0
                #else:
                    #a=1
                #for k in range(i-load_end+a,i+a):
                        #setBlock(level,k,s_y,j,1,4)
        
                
