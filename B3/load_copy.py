from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *

    def __init__(self,level,start_x,start_y,start_z,area_size_x,area_size_z):
        self.s_x=start_x
        self.s_z=start_z
        self.s_y=start_y
        self.areasize=[area_size_x,area_size_z]
        self.level=level
        self.load_area=[[1]*area_size_x for i in range(area_size_z)]
        if area_size_x>=area_size_z:
            self.walking_space=area_size_z//5
        else:
            self.walking_space=area_size_x//5
        for i in range(self.walking_space,self.areasize[0]-self.walking_space):
            for j in range(self.walking_space,self.areasize[1]-self.walking_space):
                self.load_area[j][i]=0
    #center_line=2,load=0,walk=1
    
    def load(self):
        n_direction=1# 0:load 1:other
        s_direction=0
        e_direction=1
        w_direction=0
        count=n_direction+s_direction+w_direction+e_direction
        if n_direction==0:
            for j in range(self.walking_space):
                for i in range(self.walking_space,self.areasize[0]-self.walking_space):
                    self.load_area[j][i]=0
        if s_direction==0:
            for j in range(self.areasize[1]-self.walking_space,self.areasize[1]):
                for i in range(self.walking_space,self.areasize[0]-self.walking_space):
                    self.load_area[j][i]=0
        if e_direction==0:
            for i in range(self.areasize[0]-self.walking_space,self.areasize[0]):
                for j in range(self.walking_space,self.areasize[1]-self.walking_space):
                    self.load_area[j][i]=0
        if w_direction==0:
            for i in range(self.walking_space):
                for j in range(self.walking_space,self.areasize[1]-self.walking_space):
                    self.load_area[j][i]=0
        
        for i in range(self.areasize[0]):#center_line
            for j in range(self.areasize[1]):
                if self.areasize[0]%2==0:
                    if (i==self.areasize[0]/2) or (i==self.areasize[0]/2-1): 
                        self.load_area[j][i]=2
                else:
                    if i==-(-self.areasize[0]//2)-1: 
                        self.load_area[j][i]=2
                if self.areasize[1]%2==0:
                    if (j==self.areasize[1]/2) or (j==self.areasize[1]/2-1): 
                        self.load_area[j][i]=2
                else:
                    if j==-(-self.areasize[1]//2)-1: 
                        self.load_area[j][i]=2
        
        if count<2:
            for i in range(self.walking_space,self.areasize[0]-self.walking_space):
                for j in range(self.walking_space,self.areasize[1]-self.walking_space):
                    self.load_area[j][i]=0
        else:
            if n_direction==1:
                if self.areasize[1]%2==0:
                    for j in range(self.walking_space,self.areasize[1]/2-1):
                        if self.areasize[0]%2==0:
                            self.load_area[j][self.areasize[0]/2]=0
                            self.load_area[j][self.areasize[0]/2-1]=0
                        else:
                            self.load_area[j][-(-self.areasize[0]//2)-1]=0
                else:
                    for j in range(self.walking_space,-(-self.areasize[1]//2)-1):
                        if self.areasize[0]%2==0:
                            self.load_area[j][self.areasize[0]/2]=0
                            self.load_area[j][self.areasize[0]/2-1]=0
                        else:
                            self.load_area[j][-(-self.areasize[0]//2)-1]=0
            
            if s_direction==1:
                if self.areasize[1]%2==0:
                    for j in range(self.areasize[1]/2+1,self.areasize[1]-self.walking_space):
                        if self.areasize[0]%2==0:
                            self.load_area[j][self.areasize[0]/2]=0
                            self.load_area[j][self.areasize[0]/2-1]=0
                        else:
                            self.load_area[j][-(-self.areasize[0]//2)-1]=0
                else:
                    for j in range(-(-self.areasize[1]//2),self.areasize[1]-self.walking_space):
                        if self.areasize[0]%2==0:
                            self.load_area[j][self.areasize[0]/2]=0
                            self.load_area[j][self.areasize[0]/2-1]=0
                        else:
                            self.load_area[j][-(-self.areasize[0]//2)-1]=0
            
            if w_direction==1:
                if self.areasize[0]%2==0:
                    for i in range(self.walking_space,self.areasize[0]/2-1):
                        if self.areasize[1]%2==0:
                            self.load_area[self.areasize[1]/2][i]=0
                            self.load_area[self.areasize[1]/2-1][i]=0
                        else:
                            self.load_area[-(-self.areasize[1]//2)-1][i]=0
                else:
                    for i in range(self.walking_space,-(-self.areasize[0]//2)-1):
                        if self.areasize[1]%2==0:
                            self.load_area[self.areasize[1]/2][i]=0
                            self.load_area[self.areasize[1]/2-1][i]=0
                        else:
                            self.load_area[-(-self.areasize[1]//2)-1][i]=0
            
            if e_direction==1:
                if self.areasize[0]%2==0:
                    for i in range(self.areasize[0]/2+1,self.areasize[0]-self.walking_space):
                        if self.areasize[1]%2==0:
                            self.load_area[self.areasize[1]/2][i]=0
                            self.load_area[self.areasize[1]/2-1][i]=0
                        else:
                            self.load_area[-(-self.areasize[1]//2)-1][i]=0
                else:
                    for i in range(-(-self.areasize[0]//2),self.areasize[0]-self.walking_space):
                        if self.areasize[1]%2==0:
                            self.load_area[self.areasize[1]/2][i]=0
                            self.load_area[self.areasize[1]/2-1][i]=0
                        else:
                            self.load_area[-(-self.areasize[1]//2)-1][i]=0
            
            #1=walking 2=center_line 0=load
        for i in range(self.areasize[0]):
            for j in range(self.areasize[1]):
                if self.load_area[j][i]==0:
                    setBlock(self.level,self.s_x+i,self.s_y,self.s_z+j,1,0)
                elif self.load_area[j][i]==1 or self.load_area[j][i]==2:
                    setBlock(self.level,self.s_x+i,self.s_y,self.s_z+j,1,4)
