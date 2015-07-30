import argparse
from Civ_V_Image_Manip import *

# Configure command line arguments.
parser = argparse.ArgumentParser(add_help=False)

# Optional arguments.
parser.add_argument('-d', '--diagnostic',
                    help='Create diagnostic graphic of hexagon operations.',
                    action="store_true") 
parser.add_argument('-h', '--help',
                    help='Show this help screen and exit.',
                    action="help") 
parser.add_argument('-m', '--multiple',
                    help='Flag to enable processing a series of images. \
                        Note that this is not yet enabled, but will be at some \
                        point with the intent of processing a screen recording \
                        of the video progression through the turns from the \
                        end-of-game map.',
                    action='store_true')
parser.add_argument('-nc', '--nocrop',
                    help='Do not crop the image specified.',
                    action='store_true')
parser.add_argument('-s', '--single',
                    help='Flag to enable processing of a single image.',
                    action='store_true')
parser.add_argument('-v', '--verbosity',
                    help='The degree of output (higher gives more).',
                    type=int)

# Required arguments.
parser.add_argument('infilename', 
                    help='The filename for the raw screenshot from Civilization \
                        V.')
parser.add_argument('mapsize',
                    help='The size of the map played.  Valid options are: Duel, \
                        Tiny, Small, Standard, Large, and Huge.')

# Start working by first processing the command line arguments.
args = parser.parse_args()

# Provide error checking of command line arguments.
mapsize = args.mapsize.lower()
if(mapsize not in ['duel', 'tiny', 'small', 'standard', 'large', 'huge']):
    raise RuntimeError('Mapsize specified not recognized.  Valid options \
are: Duel, Tiny, Small, Standard, Large, and Huge.')

if(args.verbosity):
    print("Enabling verbose output, degree " + str(args.verbosity) + ".")
    verbosity = args.verbosity
else:
    verbosity = 0

if(verbosity >= 1):
    print("Processing raw screenshot file " + args.infilename + \
            " as a " + args.mapsize.lower() + " map.")

# Unless the user specified not to crop, do it.
img_manip = Civ_V_Image_Manip(args.infilename, args.mapsize.lower(), verbosity)
if(not args.nocrop):
    args.infilename = img_manip.Crop()
    img_manip = Civ_V_Image_Manip(args.infilename, args.mapsize.lower(), verbosity)


if(args.diagnostic):
    img_manip.Create_Map_Image(diagnostic=True)     
else:
    img_manip.Create_Map_Image(diagnostic=False)     



