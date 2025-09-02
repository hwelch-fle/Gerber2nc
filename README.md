# Gerber2nc
<h1>G-code from Gerber files for PCBs</h1>
A Python script to make g-code toolpaths from gerber files for milling out simple PCBs

<img src="example_pcb.png">

A relatively simple script to calculate CNC toolpaths for milling out traces for a 
simple single sided PCB designed with KiCad (not tested with anything else).
<br>
It pops up a picture of the traces and toolpaths
for review before generating the g-code.
<p>
No "configuration" -- the parameters are all in the code.  The code IS the configuration
file, just search for "parameters" in the code if you want to change them.
<p>
The nice thing about this is that you can just run the script to get the gcode files.

