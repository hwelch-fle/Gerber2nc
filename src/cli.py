from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def add_args(parser: ArgumentParser) -> None:
    parser.formatter_class = ArgumentDefaultsHelpFormatter
    # Required Positional
    parser.add_argument(
        'project',
        help='Filepath of the KiCAD project to convert e.g. **/myproject.kicad_pro'
    )
    parser.add_argument(
        'outfile',
        help='Target for the generated numerical control (.nc) file [optional]'
    )
    
    # Optional output configurations
    parser.add_argument(
        '-f', '--front',
        help='Generate Frontside code',
        action='store_true',
        default=True,
    )
    parser.add_argument(
        '-b', '--back',
        help='Generate Backside code',
        action='store_true',
        default=False,
    )

    # Optional Configuration Parameters
    config = parser.add_argument_group(title='Configuration')
    config.add_argument(
        '-s', '--spindle-speed',
        help='Spindle speed in RPM',
        type=int,
        default=12000,
        metavar='',
    )
    config.add_argument(
        '-c', '--cut-depth',
        help='Cut depth for outlining traces (mm)',
        type=float,
        default=-0.1,
        metavar='',
    )
    config.add_argument(
        '-e', '--edge-depth',
        help='Edge cut depth for PCB outline (mm)',
        type=float,
        default=-0.2,
        metavar='',
    )
    config.add_argument(
        '-g', '--safe-height',
        help='Safe height above workpiece (mm)',
        type=float,
        default=3.0,
        metavar='',
    )
    config.add_argument(
        '-p', '--z-feed-rate',
        help='Feedrate along Z axis (mm/min)',
        type=int,
        default=200,
        metavar='',
    )
    config.add_argument(
        '-r', '--feed-rate',
        help='Feedrate along X/Y (mm/min)',
        type=int,
        default=450,
        metavar='',
    )
    config.add_argument(
        '-t', '--hole-start',
        help='Depth to start slow drilling holes (mm)',
        type=float,
        default=0.1,
        metavar='',
    )
    config.add_argument(
        '-d', '--hole-depth',
        help='Depth at which a hole is complete likely workpiece thickness (mm)',
        type=float,
        default=-1.8,
        metavar='',
    )
    

def run():
    parser = ArgumentParser(prog='gerber2nc')
    add_args(parser)
    parser.parse_args()
    pass

if __name__ == '__main__':
    run()

## For calculating extents of the board
#x_min:float = 1000000.0
#x_max:float = -1000000.0
#y_min:float = 1000000.0
#y_max:float = -1000000.0
#
## Use KiCad's naming convention to  get the copper front layer, ege cuts, and drill files.
#gerber_traces = Gerber_Traces_Parser(base_name+"-F_Cu.gbr")
#gerber_edgecuts = Gerber_EdgeCuts_Parser(base_name+"-Edge_cuts.gbr")
#drilldata = Drillfile_Parser(base_name+"-PTH.drl")
#
## Offset all the coordinates so that the origin is on the bottom left.
## Set the CNC origin to the botom left corner of where your PCB should be milled.
#gerber_traces.shift(x_min, y_min)
#gerber_edgecuts.shift(x_min, y_min)
#drilldata.shift(x_min, y_min)
#
## Now compute the outlines to use for tool paths.
## Parameters for outlne milling the traces
#offset_distance = 0.22 # Offset of initial path from trace or pad edge
#num_passes = 3         # Number of passes to take around traces
#path_spacing = 0.2     # Additional offset per pass
#sh_base = Shapely_bases(gerber_traces)
#trace_mill_geometry = sh_base.compute_trace_toolpaths(offset_distance, num_passes, path_spacing)
#
## Now visualize it, then wait for window to be closed before proceeding.
#visualizer = Output_visualizer()
#visualizer.load_trace_geometries(gerber_traces)
#visualizer.load_trace_mill_geometry(trace_mill_geometry)
#visualizer.load_edge_cut_geometry(gerber_edgecuts.outline)
#visualizer.load_holes(drilldata.holes)
#visualizer.create_tkinter_visualization();
#
## After window is closed, generate the G-code
#if len(sys.argv) > 2:  outname = sys.argv[2]+".nc"
#gcode = Gcode_Generator()
#gcode.OutputGcode(outname, gerber_edgecuts.outline, trace_mill_geometry, drilldata.holes)