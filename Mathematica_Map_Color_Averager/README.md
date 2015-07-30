This utility was created to parse a map processed by the Python routine that
provides non-uniform tile colors.  That is, tile colors for features such as
ice, deep water, grasslands, will vary somewhat in hue when processed within
Python.  This utility parses those colors, to find tiles close in color, and
then provides the average color value (in RGB) to be used for calculating
distances for other tiles.

This is useful if, instead of various colors, the user wants tiles that are all
a consistent color by landscape type.

An example of the *Manipulate* driven interface is shown below.

![Image](./Color_Averager_Interface.png?raw=true)
