from Hexagon_Grid_Generator import *
import numpy as np
from PIL import Image, ImageDraw
from pyx import *
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

        bbox_coords = [minx, miny, maxx, miny, maxx, maxy, minx, maxy]

        # Calculate polygon center.
        midx = (minx + maxx) / 2.0
        midy = (miny + maxy) / 2.0

        coords[::2]  = [(self.scale * (x - midx)) + midx for x in coords[::2]]
        coords[1::2] = [(self.scale * (y - midy)) + midy for y in coords[1::2]]

        subhex_coords = list(zip(coords[::2], coords[1::2]))

        subhex_hull = MultiPoint(subhex_coords).convex_hull

        # Flatten subhex list of tuples to conventional list for plotting.
        subhex_coords = list(sum(subhex_coords, ()))

        for x in range(int(math.floor(minx)), int(math.ceil(maxx))):
            for y in range(int(math.floor(miny)), int(math.ceil(maxy))):
                mypt = Point(x, y)
                if(subhex_hull.contains(mypt)):
                    r, g, b = im.getpixel(tuple([x, y]))
                    rgb[0] += r
                    rgb[1] += g
                    rgb[2] += b
                    count  += 1

        rgb[0] = rgb[0] / count
        rgb[1] = rgb[1] / count
        rgb[2] = rgb[2] / count

        rgb_color = tuple([int(i) for i in rgb])

        return bbox_coords, subhex_coords, rgb_color

    def Create_Map_Image(self):
        im = Image.open(self.infilename)
        im = im.convert('RGB')

        if(self.diagnostic and not self.makepdf):
            outfilename = re.sub(r'\.png', '_diagnostic.png', self.infilename)
            f = open('rgb.dat', 'w+')
            imout = Image.open(self.infilename)
            imout = im.convert('RGB')
            draw = ImageDraw.Draw(imout)
        elif(not self.diagnostic and not self.makepdf):
            outfilename = re.sub(r'\.png', '_processed.png', self.infilename)
            imout = Image.open(self.infilename)
            imout = im.convert('RGB')
            draw = ImageDraw.Draw(imout)
            draw.rectangle((0, 0, im.size[0], im.size[1]), fill=(0, 0, 0))
        elif(self.diagnostic and self.makepdf):
            outfilename = re.sub(r'\.png', '_diagnostic.pdf', self.infilename)
            f = open('rgb.dat', 'w+')
            pdf_pages = []
            pdf_c = canvas.canvas()
            pdf_c.fill(path.rect(   (-self.border)*self.PSF, 
                                    (self.border)*self.PSF, 
                                    (im.size[0]+2*self.border)*self.PSF, 
                                    (-im.size[1]-2*self.border)*self.PSF),
                                    [color.rgb.black])
        elif(not self.diagnostic and self.makepdf):
            outfilename = re.sub(r'\.png', '_processed.pdf', self.infilename)
            pdf_pages = []
            pdf_c = canvas.canvas()
            pdf_c.fill(path.rect(   (-self.border)*self.PSF, 
                                    (self.border)*self.PSF, 
                                    (im.size[0]+2*self.border)*self.PSF, 
                                    (-im.size[1]-2*self.border)*self.PSF),
                                    [color.rgb.black])

        # Initialize hexagon grid. 
        hexagon_generator = Hexagon_Grid_Generator(edge_length = self.edgelength,
                                                   hex_orient = "TipUp",
                                                   xshift = self.xshift,
                                                   yshift = self.yshift)

        if(self.verbosity >= 1):
            if(self.diagnostic):
                print('Creating diagnostic image.')
            if(self.makepdf):
                print('Creating PDF image (' + outfilename + ').')
            else:
                print('Creating PNG image (' + outfilename + ').') 

        # Loop over each hexagon and process/draw it.
        for row in range(self.rmin, self.rmax):
          for col in range(self.cmin, self.cmax):
            hexagon = hexagon_generator(row, col)
            hex_coords = list(hexagon)

            # Diagnostic output.
# This was commented out because of the move from Python 3.4 to Python 2.7 because
# there is no pyx package in Fink on Mac OSX for Python 3.4.  Hopefully, some day 
# that will be resolved and this diagnostic output can be re-included.
#           if(self.verbosity >= 2):
#               [print("{:9.2f}".format(i), end="") for i in hex_coords]; print("")

            bbox_coords, subhex_coords, rgb_color = \
                self.Find_Average_Hexagon_Color(tuple(hex_coords), im)

            # Diagnostic PNG
            if(self.diagnostic and not self.makepdf):

                # Draw diagnostic polygon bounding box.
                draw.polygon(bbox_coords, outline=(0, 0, 255))

                # Draw diagnostic polygon.
                draw.polygon(hex_coords, outline=(255, 0, 0))

                # Draw diagnostic area of averaging.
                draw.polygon(subhex_coords, outline=(0, 255, 0))
                f.write(str(rgb_color) + '\n')

            # Non-diagnostic PNG
            elif(not self.diagnostic and not self.makepdf):

                # Draw full-scale polygon.
                draw.polygon(hex_coords, outline=rgb_color, fill=rgb_color)

            # Diagnostic PDF
            elif(self.diagnostic and self.makepdf):

                # Create diagnostic polygon bounding box.
                box_path = path.path(   path.moveto(bbox_coords[ 0]*self.PSF, -bbox_coords[ 1]*self.PSF),
                                        path.lineto(bbox_coords[ 2]*self.PSF, -bbox_coords[ 3]*self.PSF),
                                        path.lineto(bbox_coords[ 4]*self.PSF, -bbox_coords[ 5]*self.PSF),
                                        path.lineto(bbox_coords[ 6]*self.PSF, -bbox_coords[ 7]*self.PSF),
                                        path.closepath()) 

                # Create full-scale polygon.
                subhex_path = path.path(   path.moveto(subhex_coords[ 0]*self.PSF, -subhex_coords[ 1]*self.PSF),
                                           path.lineto(subhex_coords[ 2]*self.PSF, -subhex_coords[ 3]*self.PSF),
                                           path.lineto(subhex_coords[ 4]*self.PSF, -subhex_coords[ 5]*self.PSF),
                                           path.lineto(subhex_coords[ 6]*self.PSF, -subhex_coords[ 7]*self.PSF),
                                           path.lineto(subhex_coords[ 8]*self.PSF, -subhex_coords[ 9]*self.PSF),
                                           path.lineto(subhex_coords[10]*self.PSF, -subhex_coords[11]*self.PSF),
                                           path.closepath())

                # Create full-scale polygon.
                hex_path = path.path(   path.moveto(hex_coords[ 0]*self.PSF, -hex_coords[ 1]*self.PSF),
                                        path.lineto(hex_coords[ 2]*self.PSF, -hex_coords[ 3]*self.PSF),
                                        path.lineto(hex_coords[ 4]*self.PSF, -hex_coords[ 5]*self.PSF),
                                        path.lineto(hex_coords[ 6]*self.PSF, -hex_coords[ 7]*self.PSF),
                                        path.lineto(hex_coords[ 8]*self.PSF, -hex_coords[ 9]*self.PSF),
                                        path.lineto(hex_coords[10]*self.PSF, -hex_coords[11]*self.PSF),
                                        path.closepath())

                # Draw shapes on canvase.
                pdf_c.stroke(box_path, [color.rgb.blue])
                pdf_c.stroke(hex_path, [color.rgb.red])
                pdf_c.stroke(subhex_path, [color.rgb.red])

            # Non-Diagnostic PDF
            elif(not self.diagnostic and self.makepdf):

                # Create full-scale polygon.
                hex_path = path.path(   path.moveto(hex_coords[ 0]*self.PSF, -hex_coords[ 1]*self.PSF),
                                        path.lineto(hex_coords[ 2]*self.PSF, -hex_coords[ 3]*self.PSF),
                                        path.lineto(hex_coords[ 4]*self.PSF, -hex_coords[ 5]*self.PSF),
                                        path.lineto(hex_coords[ 6]*self.PSF, -hex_coords[ 7]*self.PSF),
                                        path.lineto(hex_coords[ 8]*self.PSF, -hex_coords[ 9]*self.PSF),
                                        path.lineto(hex_coords[10]*self.PSF, -hex_coords[11]*self.PSF),
                                        path.closepath())

                # Draw polygon and border together, note that non-uniform border
                # colors will give the appearance of minor overlaps at corners.
                pdf_c.stroke(hex_path, [             color.rgb( rgb_color[0]/255.,
                                                                rgb_color[1]/255.,
                                                                rgb_color[2]/255.),  
                                        deco.filled([color.rgb( rgb_color[0]/255.,
                                                                rgb_color[1]/255.,
                                                                rgb_color[2]/255.)])
                                       ])

                # Draw polygon and border separately; another method to accomplish
                # the same thing as above.
#               pdf_c.fill(hex_path, [color.rgb( rgb_color[0]/255.,
#                                                rgb_color[1]/255.,
#                                                rgb_color[2]/255.)])
#
#               pdf_c.stroke(hex_path, [color.rgb.black, style.linewidth(0.0)])

        if(not self.makepdf):
            imout.save(outfilename, "PNG")
        else:
            pdf_c.writePDFfile(outfilename)

        if(self.diagnostic):
            f.close()

        return

    # The cropboxes assigned here assume the use of OSX's built-in screenshot
    # utility applied to a full screen (Shift-Command-4, Spacebar, Left-click)
    # capture of a full screen Civ V summary map screen.
    def __init__(   self, infilename, mapsize, method,
                    verbosity=0, diagnostic=False, makepdf=True, border=0):

        # Create nested dictionary to contain magic numbers for image manipulations.
        image_dims = {}
        image_dims['sc3'] = {}
        image_dims['sc4sb'] = {}

        # Spacings calculated in Mathematica with commands:
        # N[{1817, 1701, 1718, 1682, 1776, 1750}/(({40,56,66,80,104,128}*2+1)*Cos[30\[Degree]])]
        # %*Cos[30\[Degree]]
    
        image_dims['sc3']['duel']       = [[771, 564, 1817, 946], 25.9024, 22.4321, 0.0, 0.75, 0,  2, 0, 2], # 24,  40 
        image_dims['sc3']['tiny']       = [[829, 564, 1701, 946], 17.3818, 15.0531, 0.0, 0.65, 0,  2, 0, 2], # 36,  56 
        image_dims['sc3']['small']      = [[821, 564, 1718, 946], 14.9156, 12.9173, 0.0, 0.65, 0,  2, 0, 2], # 42,  66 
        image_dims['sc3']['standard']   = [[839, 564, 1682, 946], 12.0634, 10.4472, 0.0, 0.65, 0,  2, 0, 2], # 52,  80 
        image_dims['sc3']['large']      = [[792, 564, 1776, 946],  9.8122,  8.4976, 0.0, 0.65, 0,  2, 0, 2], # 64, 104 
        image_dims['sc3']['huge']       = [[805, 564, 1750, 946],  7.8628,  6.8093, 0.0, 0.50, 0,  2, 0, 2], # 80, 128 
    
        image_dims['sc4sb']['duel']     = [[886, 678, 1817, 946], 25.9024, 22.4321, 0.0, 0.75, 0,  2, 0, 2], # 24,  40 
        image_dims['sc4sb']['tiny']     = [[944, 678, 1701, 946], 17.3818, 15.0531, 0.0, 0.65, 0,  2, 0, 2], # 36,  56 
        image_dims['sc4sb']['small']    = [[935, 678, 1718, 946], 14.9156, 12.9173, 0.0, 0.65, 0,  2, 0, 2], # 42,  66 
        image_dims['sc4sb']['standard'] = [[953, 678, 1682, 946], 12.0634, 10.4472, 0.0, 0.65, 0,  2, 0, 2], # 52,  80 
        image_dims['sc4sb']['large']    = [[906, 678, 1776, 946],  9.8122,  8.4976, 0.0, 0.65, 0,  2, 0, 2], # 64, 104 
        image_dims['sc4sb']['huge']     = [[919, 678, 1750, 946],  7.8628,  6.8093, 0.0, 0.50, 0,  2, 0, 2], # 80, 128 

        self.infilename  = infilename
        self.verbosity   = verbosity
        self.diagnostic  = diagnostic
        self.makepdf     = makepdf
        if(self.makepdf):
            self.border  = border
            self.PSF     = 0.025 # Page scaling factor so PDFs aren't huge.

        self.cropbox    = image_dims[method][mapsize][0][0]
        self.edgelength = image_dims[method][mapsize][0][1]
        self.xshift     = image_dims[method][mapsize][0][2] 
        self.yshift     = image_dims[method][mapsize][0][3] 
        self.scale      = image_dims[method][mapsize][0][4]
        self.rmin       = image_dims[method][mapsize][0][5]
        self.rmax       = image_dims[method][mapsize][0][6]
        self.cmin       = image_dims[method][mapsize][0][7]
        self.cmax       = image_dims[method][mapsize][0][8]

        self.cropbox = (self.cropbox[0],                   # Distance from left to start.
                        self.cropbox[1],                   # Distance from top to start.
                        self.cropbox[0] + self.cropbox[2], # Distance from left to end.
                        self.cropbox[1] + self.cropbox[3]) # Distance from top to end.

