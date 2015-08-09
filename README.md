Civ_V_Map_Plotter
-----------------

This application is inteded to process the map produced at the end of each game
into a more aesthetically-pleasing rendition.

It does this by overlaying a hexagonal grid atop the PNG file read in, and then
sampling/averaging the color of subhexagonal regions in each hex.

See the example directory for before/after images from screen captures.

Note that the test case directory does not include results to avoid the
inclusion of copious, unnecessary, binary files.

Required Packages
-----------------

* Numpy
* PIL
* Pyx

Optional Software
-----------------

* ImageMagick (for `convert` and/or `mogrify` for post-processing)

Execution Instructions
----------------------

From the command line, put the image (e.g., `image.png`) in the directory with
the `.py` files and run

`python Civ_V_Map_Plotter.py image.png large --pdf`

where `large` is the size of the Civilization V map (i.e., duel, tiny, small,
standard, large, huge).

One might then choose to use `convert` to convert the generated PDF to a hi-res
PNG as:

`convert -density 200 -resize 50% image_cropped_processed.pdf image_final_map.png`
