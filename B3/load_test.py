from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *
import road as R
import light
import car
import skyscraper as s
import park as p
displayName = "OIKORA"


def perform(level, box, options):
    (width, height, depth)=getBoxSize(box)
    R.road_builder(level,box.minx,box.miny,box.minz,box.maxx-box.minx,box.maxz-box.minz,1,1,0,0)
    #s.skyscraper(level,box.minx,box.minz,box.miny)
    #p.make_park(level,box.minx,box.miny,box.minz,30,30)