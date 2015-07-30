from Hexagon_Grid_Generator import *
import numpy as np
from PIL import Image, ImageDraw
import re

class Civ_V_Image_Manip():

    # This function crops a given PNG file according to a cropbox defined
    # according to the size map played.
    def Crop(self):
        outfilename = re.sub(r'\.png', '_cropped.png', self.infilename)
        if(self.verbosity >= 1):
            print("Cropping Image to " + outfilename + ".")
        try:        
            im = Image.open(self.infilename)
        except IOError as e:
            print("Unable to open file.") 

        im = im.crop(self.cropbox)
        im.save(outfilename) 
        return outfilename

    # Find the difference between two colors.
    def Diff_Colors(color1, color2):
        difference = 0
        difference += abs(testColor[0] - otherColor[0])
        difference += abs(testColor[1] - otherColor[1])
        difference += abs(testColor[2] - otherColor[2])
        return difference

    # Find the average color within a hexagon, scaled down by a certain amount.
    # Note that we must play tuple/list games to keep argument immutable.
    def Find_Average_Hexagon_Color(self, hex_coords, im):    
        from shapely.geometry import Point, MultiPoint
    
        coords = list(hex_coords)
    
        # Default RGB values to black opaque and pixel counter to zero.
        rgb = [0, 0, 0]
        count = 0
    
        # Calculate hexagon bounding box.    
        minx = min(coords[::2])
        maxx = max(coords[::2])
        miny = min(coords[1::2])
        maxy = max(coords[1::2])
    
        # Calculate polygon center.
        midx = (minx + maxx) / 2.0
        midy = (miny + maxy) / 2.0
    
        coords[::2]  = [(self.scale * (x - midx)) + midx for x in coords[::2]]
        coords[1::2] = [(self.scale * (y - midy)) + midy for y in coords[1::2]]
        
        hex_hull = MultiPoint(list(zip(coords[::2], coords[1::2]))).convex_hull
    
        int_pt_coords = []
        for x in range(math.floor(minx), math.ceil(maxx)):
            for y in range(math.floor(miny), math.ceil(maxy)):
                mypt = Point(x, y)
                if(hex_hull.contains(mypt)):
                    int_pt_coords.append([x, y])
                    r, g, b = im.getpixel(tuple([x, y]))
                    rgb[0] += r
                    rgb[1] += g
                    rgb[2] += b
                    count  += 1
    
        rgb[0] = rgb[0] / count
        rgb[1] = rgb[1] / count
        rgb[2] = rgb[2] / count

        rgb_color = tuple([int(i) for i in rgb])
        
    #   crgb = min(colors, key=partial(colorDifference, rgb))
    #   hex_color = '#%02x%02x%02x' % (crgb[0], crgb[1], crgb[2])
    
        return int_pt_coords, rgb_color

    def Create_Map_Image(self, diagnostic=False):

        im = Image.open(self.infilename)
        im = im.convert('RGB')
        imout = Image.open(self.infilename)
        imout = im.convert('RGB')

        draw = ImageDraw.Draw(imout)

        if(diagnostic):
            outfilename = re.sub(r'\.png', '_diagnostic.png', self.infilename)
            f = open('rgb.dat', 'w+')
        else:
            outfilename = re.sub(r'\.png', '_processed.png', self.infilename)
            draw.rectangle((0, 0, im.size[0], im.size[1]), fill=(0, 0, 0))
  
        hexagon_generator = Hexagon_Grid_Generator(edge_length = self.edgelength, 
                                                   hex_orient = "TipUp",
                                                   xshift = self.xshift,
                                                   yshift = self.yshift)

        for row in range(self.rmin, self.rmax):
          for col in range(self.cmin, self.cmax):
            hexagon = hexagon_generator(row, col)
            hex_coords = list(hexagon)
        
            # Diagnostic output.
            if(self.verbosity >= 2):
                [print("{:9.2f}".format(i), end="") for i in hex_coords]; print("")
        
            subhex_coords, rgb_color = self.Find_Average_Hexagon_Color(tuple(hex_coords), im)   

            if(diagnostic):            
                # Draw diagnostic polygon.
                draw.polygon(hex_coords, outline=(255, 0, 0))
                # Draw diagnostic area of averaging.
                [draw.point(p, fill=(0, 255, 0)) for p in subhex_coords]
                f.write(str(rgb_color) + '\n')
            else:
                # Draw full-scale polygon.
                draw.polygon(hex_coords, outline=rgb_color, fill=rgb_color)

        imout.save(outfilename, "PNG")

        if(diagnostic):
            f.close()

        return
 
    # The cropboxes assigned here assume the use of OSX's built-in screenshot
    # utility applied to a full screen (Shift-Command-4, Spacebar, Left-click)
    # capture of a full screen Civ V summary map screen.
    def __init__(self, infilename, mapsize, verbosity):

        self.infilename  = infilename
        self.mapsize     = mapsize
        self.verbosity   = verbosity

        if(mapsize == "duel"):
            self.cropbox = [886, 678, 1817, 946] 
            self.edgelength = 25.9
            self.xshift = 21.0
            self.yshift =  1.0
            self.scale = 0.75
            self.rmin = 0
            self.rmax = 24
            self.cmin = 0
            self.cmax = 40
        elif(mapsize == "tiny"):
            self.cropbox = [944, 678, 1701, 946]
            self.edgelength = 17.35
            self.xshift = 15.6
            self.yshift =  1.0
            self.scale = 0.65
            self.rmin = 0
            self.rmax = 36
            self.cmin = 0
            self.cmax = 56
        elif(mapsize == "small"):
            self.cropbox = [935, 678, 1718, 946]
            self.edgelength = 14.89
            self.xshift = 14.25
            self.yshift =  1.0
            self.scale = 0.65
            self.rmin = 0
            self.rmax = 42
            self.cmin = 0
            self.cmax = 66
        elif(mapsize == "standard"):
            self.cropbox = [953, 678, 1682, 946]
            self.edgelength = 12.05
            self.xshift = 11.0  
            self.yshift =  1.0
            self.scale = 0.65
            self.rmin = 0
            self.rmax = 52
            self.cmin = 0
            self.cmax = 80
        elif(mapsize == "large"):
            self.cropbox = [906, 678, 1776, 946]
            self.edgelength = 9.805
            self.xshift = 9.0  
            self.yshift =  0.0
            self.scale = 0.65
            self.rmin = 0
            self.rmax = 64
            self.cmin = 0
            self.cmax = 104
        elif(mapsize == "huge"):
            self.cropbox = [919, 678, 1750, 946]
            self.edgelength = 7.855
            self.xshift = 8.0  
            self.yshift =  0.0
            self.scale = 0.50
            self.rmin = 0
            self.rmax = 80
            self.cmin = 0
            self.cmax = 128

        self.cropbox = (self.cropbox[0],                   # Distance from left to start.
                        self.cropbox[1],                   # Distance from top to start.
                        self.cropbox[0] + self.cropbox[2], # Distance from left to end. 
                        self.cropbox[1] + self.cropbox[3]) # Distance from top to end.  
