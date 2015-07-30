import math

# Returns a hexagon coordinate generator.
#
#   The hexagons generated a assigned:
#   - edge_length, to govern the ... edge length.
#   - hex_orientation, to govern the orientation of the hexagon, currently only
#       "TipUp" (with a tip facing North" or "FlatUp" with the northern flat
#       running East/West.
#   - xshift, amount by which to shift the grid horizontally.
#   - yshift, amount by which to shift the grid vertically
#
#   Ultimately, the generator returns the x-y vertex coordinates for a hexagon
#   at a given position in a hexagonal lattice.
#

class Hexagon_Grid_Generator(object):
    def __init__(self, edge_length = 50, hex_orient = "TipUp", 
                       xshift = 0, yshift = 0):
        self.edge_length = edge_length
        self.hex_orient = hex_orient
        self.xshift = xshift
        self.yshift = yshift
  
    @property
    def col_width(self):
        if(self.hex_orient == "FlatUp"):
            return 2.0 * self.edge_length
        elif(self.hex_orient == "TipUp"):
            return 2.0 * self.edge_length * math.cos(math.pi / 6.0) 
        else:
            raise NameError('Error: Hexagon orientation not recognized, \
                             must be "Flatup" or "TipUp".')
  
    @property
    def row_height(self):
        if(self.hex_orient == "FlatUp"):
            return math.sin(math.pi / 3.0) * self.edge_length
        elif(self.hex_orient == "TipUp"):
            return 1.5 * self.edge_length
        else:
            raise NameError('Error: Hexagon orientation not recognized, \
                             must be "Flatup" or "TipUp".')
   
    def __call__(self, row, col):
        x = (col + 0.5 * ((row + 1) % 2)) * self.col_width + self.xshift
        y = row * self.row_height + self.yshift

        if(self.hex_orient == "FlatUp"):
            lang = 0
            uang = 360
        else:
            lang = 30
            uang = 390
        for angle in range(lang, uang, 60):
            x += math.cos(math.radians(angle)) * self.edge_length
            y += math.sin(math.radians(angle)) * self.edge_length

            # Ensure positivity.
            if(x < 0): x = 0
            if(y < 0): y = 0

            yield x
            yield y
