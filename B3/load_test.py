from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
from functions import *
import load as L
import light
import car
import skyscraper as s
import park as p
displayName = "OIKORA"


def perform(level, box, options):
    (width, height, depth)=getBoxSize(box)
    #L.load_builder(level,box.minx,box.miny,box.minz,32,32)
    #s.skyscraper(level,box.minx,box.minz,box.miny)
    p.make_park(level,box.minx,box.miny,box.minz,16,16)