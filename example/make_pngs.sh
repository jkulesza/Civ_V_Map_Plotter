#!/bin/bash

/sw/bin/python2.7 Civ_V_Map_Plotter.py assalted_01_early_game.png large --pdf
/sw/bin/python2.7 Civ_V_Map_Plotter.py assalted_02_mid_game.png large --pdf
/sw/bin/python2.7 Civ_V_Map_Plotter.py assalted_03_late_game.png large --pdf

convert -density 200 -resize 50% assalted_01_early_game_cropped_processed.pdf assalted_01_early_game_final_map.png
convert -density 200 -resize 50% assalted_02_mid_game_cropped_processed.pdf   assalted_02_mid_game_final_map.png
convert -density 200 -resize 50% assalted_03_late_game_cropped_processed.pdf  assalted_03_late_game_final_map.png

rm *cropped*
