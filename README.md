# Welcome to TimeStepSelector

A plugin for QGIS by Morten Sickel

Still in pre alpha stage - not useable.

* project home and bug tracker: https://github.com/sickel/TimeStepSelector

## What is the goal

The aim of TimeStepSelector is to be able to animate time series stored in netCDF-files. It may later 
be merged into Anita Graser's Time Mangager plugin.

## What TimeStepSelector Manager currently does

Not much - just lists coverages with potentially may be animated.

## How to use it:

For an example, use test_4layers.nc. Add it as a raster file. On Style, select Render type "Singleband gray", 
select any band as the Gray Band. Set Min to 0 and Max to 0.9 and Strech and clip to MinMax. A quasi-random grid 
should show up. By selecting different Gray bands, different time steps are show - ultimately, they should be 
selected using a slider in the pluginwindow. (Band 1 and 3 are equal as are band 2 and 4)

## License

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

## Dependencies


## What are the limitations?


### Other limitations



