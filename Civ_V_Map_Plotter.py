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
parser.add_argument('-m', '--method',
                    help='The capture method use.  Allowable options are: \'sc3\': \
                        OSX\'s Shift-Cmd-3 to capture the full screen; \'sc4sb\': \
                        OSX\'s Shift-Cmd-4, Spacebar to capture the window with a \
                        shadow,\n',
                    type=str)
parser.add_argument('-nc', '--nocrop',
                    help='Do not crop the image specified.',
                    action='store_true')
parser.add_argument('-p', '--pdf',
                    help='Create PDF instead of PNG.',
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

if(args.method):
    method = args.method.lower()
    if(method not in ['sc3', 'sc4sb']):
        raise RuntimeError('Improper screen capture method specified.  Valid \
options are: sc3 and sc4sb.')
else:
    method = 'sc3'

if(args.verbosity):
    print("Enabling verbose output, degree " + str(args.verbosity) + ".")
    verbosity = args.verbosity
else:
    verbosity = 0

if(verbosity >= 1):
    print("Processing raw screenshot file " + args.infilename + \
            " as a " + args.mapsize.lower() + " map.")

# Unless the user specified not to crop, do it.
img_manip = Civ_V_Image_Manip(  args.infilename,
                                args.mapsize.lower(),
                                method,
                                verbosity,
                                args.diagnostic,
                                args.pdf)

# Crop and reset infilename to the cropped image.
if(not args.nocrop):
    args.infilename = img_manip.Crop()
    img_manip = Civ_V_Image_Manip(  args.infilename,
                                    args.mapsize.lower(),
                                    method,
                                    verbosity,
                                    args.diagnostic,
                                    args.pdf)

# Finally, we make the image that we are interested in.
img_manip.Create_Map_Image()
