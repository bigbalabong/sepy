'''
Tier: Base
'''

from .MBase import *





###########################################################################
################################## Color ##################################
###########################################################################

class Color( object ):

    # Pure Solid Color
    Color_Palette_1 = (
            ('red',         '#ff0000'),
            ('orange',      '#ff8000'),     # 1, 0.5, 0
            ('yellow',      '#ffff00'),     # 1, 1, 0

            ('green',       '#00FF00'),
            ('cyan',        '#00FFFF'),     # 0, 1, 1
            ('sky_blue',    '#007FFF'),     # 0, 0.5, 1

            ('blue',        '#0000FF'),
            ('purple',      '#8000ff'),     # 0.5, 0, 1
            ('magenta',     '#FF00FF'),     # 1, 0, 1

            ('white',       '#FFFFFF'),     # 1, 1, 1
            ('gray',        '#7F7F7F'),     # 0.5, 0.5, 0.5
            ('dark',        '#000000'),     # 0, 0, 0
        )

    Color_Palette_1_dict = dict( Color_Palette_1 )


    # Color Palette v2 Harmony (Houdini)





###########################################################################
############################### Frame Ratio ###############################
###########################################################################

class FrameRatio( object ):

    Presets = { 
                'Root 1':   1,                  # 1
                'Root Phi': math.sqrt(1.618),   # 1.272
                'Root 2':   math.sqrt(2),       # 1.414
                '1.5':      1.5,                # 1.5
                'Phi':      1.618,              # 1.618
                'Root 3':   math.sqrt(3),       # 1.732
                'Root 4':   math.sqrt(4),       # 2
                'Root 5':   math.sqrt(5),       # 2.236
                'Root 6':   math.sqrt(6),       # 2.449
            }


    @staticmethod
    def matchFrameByRatio( cls, ratio ):
        ratio_diff = [ ( i[0], abs(i[1] - ratio) ) for i in cls.Presets.items() ]
        ratio_diff.sort( key=lambda x: x[1] )
        frame_rect = ratio_diff[0][0]
        return frame_rect






###########################################################################
#################################### App ##################################
###########################################################################

class Apps( object ):

    IrfanView =     r"C:\Program Files\IrfanView\i_view64.exe"

    # 11.9.9
    ExifTool =      normpath( __file__, '../utils/exiftool.exe', check=False )                       

    FFmpeg =        normpath( __file__, '../utils/exiftool.exe', check=False )

    # 1.3.3   
    HandBrake =     normpath( __file__, '../utils/HandBrakeCLI/HandBrakeCLI.exe', check=False )       





# ======================================================== #
# ======================== Gestalt ======================= #
# ======================================================== #
'''
Law of Pragnanz
        We see the simplest forms possible.

Figure-Ground Relationship

Law of Similarity
        We will perceptually group objects together when they are similar, 
        which can be in terms of shape, color, shading or any other quality.

Law of Symmetry
        The mind likes to perceive objects as being symmetrical and formed around a central point, 
        and also likes to divide objects into symmetrical parts.

Law of Proximity
        We group things that are in close proximity and see it as one shape which unifies them.

Law of Closure

Law of Continuity
        A great technique for unity and movement.

Aspective View

Arabesque
'''

















