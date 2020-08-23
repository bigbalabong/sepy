'''
Tier: Base
'''


from .MBase import *


from . import MVar
reload(MVar)
Apps =          MVar.Apps
Color =         MVar.Color
FrameRatio =    MVar.FrameRatio


from . import MData
reload(MData)
I_ =    MData.Integer
F_ =    MData.Float
Vec3 =  MData.Vec3
S_ =    MData.String
L_ =    MData.List
D_ =    MData.Dict


from . import MFile
reload(MFile)
File = MFile.File


from . import MTime
reload(MTime)
Time =          MTime.Time
Timer =         MTime.Timer
whatsTheDate =  MTime.whatsTheDate
whatsTheTime =  MTime.whatsTheTime


from . import MMath
reload(MMath)





# ======================================================== #
# ======================== Tier: 1 ======================= #
# ======================================================== #

if os.path.exists( os.path.join( __file__, '../MJson' ) ):
    from . import MJson
    reload(MJson)
    Json = MJson.Json


if os.path.exists( os.path.join( __file__, '../MCSV' ) ):
    from . import MCSV
    reload(MCSV)
    CSV = MCSV.CSV


if os.path.exists( os.path.join( __file__, '../MScreen' ) ):
    from . import MScreen
    reload(MScreen)
    Screen = MScreen.Screen






# ======================================================== #
# ======================== Tier: 2 ======================= #
# ======================================================== #

if os.path.exists( os.path.join( __file__, '../MDistribution.py' ) ):
    from . import MDistribution
    reload(MDistribution)
    Pack = MDistribution.Pack


if os.path.exists( os.path.join( __file__, '../MUtils.py' ) ):
    from . import MUtils
    reload(MUtils)
    WindowsUtils =  MUtils.WindowsUtils
    HandBrake =     MUtils.HandBrake
    ExifTool =      MUtils.ExifTool


if os.path.exists( os.path.join( __file__, '../MWeb.py' ) ):
    from . import MWeb
    reload(MWeb)
    WebBrowser = MWeb.WebBrowser








