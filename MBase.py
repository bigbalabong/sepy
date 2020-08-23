'''
Tier: Base
'''

import string                   # https://docs.python.org/2/library/string.html

import sys                      # https://docs.python.org/2/library/sys.html
import platform                 # https://docs.python.org/2/library/platform.html
import socket                   # https://docs.python.org/2/library/socket.html
import uuid                     # https://docs.python.org/2.7/library/uuid.html

import os                       # https://docs.python.org/2/library/os.html
import shutil                   # https://docs.python.org/2/library/shutil.html
import glob                     # https://docs.python.org/2/library/glob.html

import logging                  # https://docs.python.org/2/library/logging.html

import random                   # https://docs.python.org/2/library/random.html
import math                     # https://docs.python.org/2/library/math.html

import re

import itertools
import functools                # https://docs.python.org/2/library/functools.html
import inspect                  # https://docs.python.org/2/library/inspect.html

import ctypes                   # https://docs.python.org/2/library/ctypes.html

import subprocess               # https://docs.python.org/2/library/subprocess.html

from contextlib import contextmanager

import collections

'''
Built-in Functions      https://docs.python.org/2/library/functions.html
'''




###########################################################################
############################ Naming Conventions ###########################
###########################################################################

'''
Global Variable Name        capitalize with underscore
        e.g. App_Ver

Local Variable Name         lowercase with underscore
        e.g. app_ver

Class Attribute Name        capitalize
        e.g. Name / Id / Points / 

Function Name               camel case
        e.g. getName

Arugment Name               lowercase with underscore
        e.g. name_of_point
'''









###########################################################################
################################### APP ###################################
###########################################################################












###########################################################################
################################# Python 3 ################################
###########################################################################

def p( *args, **kwargs ):
    strings = [ str(i) for i in args ]

    if 'sep' in kwargs:
        sep = ' {} '.format(kwargs['sep'])
    else:
        sep = ' '

    info = sep.join( strings )
    info += '\n'
        
    sys.stdout.write( info )











###########################################################################
############################# Global Variables ############################
###########################################################################

"""
Examples:
    string.ascii_lowercase
    # Returns: 'abcdefghijklmnopqrstuvwxyz'
"""
A_Z = string.ascii_lowercase


"""
Examples:
    os.environ['USERNAME']  
    # Returns: 'SEAN'
"""
User_Name = os.environ['USERNAME']

"""
Examples:
    os.path.expanduser('~')
    # Returns: 'C:\\Users\\SEAN'

    os.path.join( os.path.expanduser('~'), '.nuke', 'meta.json' )
    # Returns: 'C:\\Users\\SEAN\\.nuke\\meta.json'
"""
User_Path = os.path.expanduser('~')



# system = os.name                                          # nt
# system = sys.platform                                     # win32 / linux2
System_Info = platform.system()                             # Windows / Linux
System_Info_Details = platform.platform()                   # Windows-10-xx.x.xxxx


Processor = platform.processor()                            # Intel64 Family 6 Model xxxxxxx


Hostname = socket.gethostname()                             # DESKTOP-xxxxxxx
IP = socket.gethostbyname( Hostname )                       # 192.168.xxx.xxx
IP_list = socket.gethostbyname_ex( Hostname )               # ('DESKTOP-xxxxx', [], ['192.168.xxx.xxx', '192.168.xxx.xxx'])


Anaconda2 = r"C:\ProgramData\Anaconda2\python.exe"          # Anaconda2


isPy3 = sys.version_info > (3,)




# ~~~~~~~~~~~~~~~ >>>>>>>>> ~~~~~~~~~~~~~~~ #
# Temp Folder

Temp_Folderpath = os.environ['TMP']                             # e.g. 'C:\\Users\\SEAN\\AppData\\Local\\Temp'

def openTempFolder():
    os.startfile( Temp_Folderpath )

def openTempBakFolder():
    temp_bak_folder = os.path.join( Temp_Folderpath, '_bak' )
    if not os.path.exists( temp_bak_folder ):
        os.mkdir( temp_bak_folder )
    os.startfile( temp_bak_folder )
# ~~~~~~~~~~~~~~~ <<<<<<<<<< ~~~~~~~~~~~~~~ #




def getWinEnv( var ):
    r'''
    ARGUMENTS:

    var
            example: 'path'

    os.environ
            some testing                    return
            os.environ['OS']                Windows_NT
            os.environ['USERDOMAIN']        DESKTOP-xxxxx
            os.environ['SYSTEMROOT']        C:\WINDOWS
            os.environ['WINDIR']            C:\WINDOWS
            os.environ['HOMEPATH']          \Users\SEAN
            os.environ['USERPROFILE']       C:\Users\SEAN
            os.environ['USERNAME']          SEAN
            os.environ['PYTHONPATH']        
    '''
    # get windows environment variables
    value = os.getenv( var )
    # os.environ['PATH']


    # processing info
    if value.__class__.__name__ == 'str':
        if ';' in value:
            value = [ i for i in value.split(';') if i ]


    if value.__class__.__name__ == 'list':
        for i in value:
            p( i )

    return value



def setWinEnv( var, 
                value, normpath=True, sep=';',
                permanent=True, for_all_users=True,
                mode='add' ):
    """
    Reference:
        https://www.shellhacks.com/windows-set-environment-variable-cmd-powershell/
        # Get system environment variable.
        os.system( 'echo %VAR_NAME%' )

        # Set an environment variable for the current terminal session:
        os.system( 'set VAR_NAME="VALUE"' )

        # Permanently set an environment variable for the current user.
        os.system( 'setx VAR_NAME "VALUE"' )

        # Permanently set an environment variable for all users.
        os.system( 'setx /M VAR_NAME "VALUE"' )

    Args:
        var (str): Environment variable name.

        value (str): Environment variable value.
        normpath (bool, optional): Defaults to True.
        sep (str, optional): Defaults to ';'.

        permanent (bool, optional): If ture, set the environment variable permanently. Otherwise, set it just for current session. 
                                    Attention: you need administrator permission to execute this.
                                    Defaults to False.
        for_all_users (bool, optional): [description]. Defaults to False.
        
        mode (str, optional): Defaults to 'add'.
    """
    # get new value
    if normpath:
        value = os.path.normpath( value )

    old_value = os.getenv( var )
    if not old_value:
        old_value = ''


    # check existence
    if value in old_value:
        print( 'This value has already been contained in environment variable. Execution stopped.' )
        return


    if mode == 'add':
        new_value = '{}{}{}'.format( old_value, value, sep )
    else: # mode == 'set'
        new_value = '{}{}'.format( value, sep )


    # set environment variable
    if not permanent:
        os.system( 'set {}="{}"'.format( var, new_value ) )

    else:
        if not for_all_users:
            os.system( 'setx {} "{}"'.format( var, new_value ) )
        else:
            os.system( 'setx /M {} "{}"'.format( var, new_value ) )



def getDocPath( sw=None, open=False ):
    '''
    'maya' : '/maya',
    'sd' : '/Allegorithmic/Substance Designer',
    'sp' : '/Allegorithmic/Substance Painter',
    'houdini17.5' : '/houdini17.5',
    '''

    # user document path
    doc_path = os.path.expanduser('~/Documents').replace('\\','/')



    # software path
    sw_path_dict = { 'maya' : '/maya',
                     'sd' : '/Allegorithmic/Substance Designer',
                     'sp' : '/Allegorithmic/Substance Painter',
                     'houdini17.5' : '/houdini17.5',
                     }

    if sw and sw.lower() in sw_path_dict.keys() :
        doc_path += sw_path_dict[ sw.lower() ]



    # open windows file explorer
    if open:
        os.startfile( doc_path )


    return doc_path

    







###########################################################################
############################### Easy-to-use ###############################
###########################################################################

def pause( exit=False ):
    p( '\n'*2 )
    os.system("pause")

    # terminate python execution
    if exit:
        sys.exit()


def clear():
    p( '\n'*15 )


def builtinKeywords():
    # https://docs.python.org/2/library/__builtin__.html
    import __builtin__              

    builtin_keywords = __builtin__.__dict__.keys()
    # builtin_keywords.sort()

    return builtin_keywords


def rawInputConfirm( prompt='Continue ??', affirmative='enter' ):

    prompt = '\n\n {}  Yes. (press {}) / No. (anything else) \n\t'.format( prompt, affirmative.upper() )
    user_input = raw_input( prompt )
    user_input = user_input.lower()

    affirmative = affirmative.lower()
    if affirmative == 'enter':
        affirmative = ''

    return True if user_input == affirmative else False


def getPyFilepath():
    '''
    RETURN:
            File path of current .py file.
    '''
    try:
        this_py_filepath = __file__

    except:
        this_py_filepath = inspect.getfile( lambda: None )
        this_py_filepath = os.path.normpath( this_py_filepath ).replace('\\','/')

    return this_py_filepath


def currentFolderPath():
    return os.path.abspath( '.' )


def ch( folder_path ):

    if os.path.isdir( folder_path ):
        os.chdir( folder_path )


def desktopPath():
    '''
    e.g. 'C:\\Users\\SEAN/Desktop'
    '''
    return os.path.expanduser("~/Desktop")


def printVar( **kwargs ):
    for name, value in kwargs.items():
        p( ' {}  >> '.format(name), value )


        

def type_( object_ ):
    '''
    EXAMPLES:
            type_('pCube1')
                RETURNS: <class 'pymel.core.nodetypes.Transform'>
            type_('lambert1')
                RETURNS: <class 'pymel.core.nodetypes.Lambert'>
    '''
    if not object_:
        return None

    if L_(object_).isList:
        object_ = object_[0]

    return type( object_ )


def normpath( path_a, path_b='', check=True ):
    """
    Convert relative path to absolute path.

    Args:
        path_a (str): Base path.
        path_b (str): Relative path.
        check (bool, optional): If true, check path validation. Defaults to True.

    Returns:
        [str]: jointed path based on relative path.

    References:
        Absolute vs Relative Imports in Python              https://realpython.com/absolute-vs-relative-python-imports/
        The Definitive Guide to Python import Statements    https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
        Reading and Writing Files                           https://automatetheboringstuff.com/chapter8/
    """
    full_path = os.path.join( path_a, path_b )
    real_path = os.path.normpath( full_path )
    real_path = real_path.replace( '\\', '/' )

    if check:
        if not os.path.exists( real_path ):
            p( 'Missing Path: ', real_path )
            raise Exception( 'Final path does not exist.' )
            
    return real_path


def openPath( path_a, path_b=None ):
    """
    Open path_a. If failed, open path_b.

    Args:
        path_a (str): Try to open this path firstly.
        path_b (str, optional): If failed to open path_a, try this one. Defaults to None.
    """
    if os.path.exists( path_a ):
        path = path_a
    
    else:
        if path_b:
            if os.path.exists( path_b ):
                path = path_b
            else:
                raise Exception( 'Both paths do not exist.' )

        else:
            raise Exception( 'The path does not exist.' )

    os.startfile( path )



def isSequence( var ):
    """
    Check if the input variable is a sequence data type. (aka. list, tuple, etc.)

    Args:
        var ([type]): [description]

    Returns:
        [bool]: [description]
    """
    return isinstance( var, collections.Sequence )







###########################################################################
################################# Operator ################################
###########################################################################
'''
Operator        https://docs.python.org/2/library/operator.html


Comparisons
__lt__        <
__le__        <=
__eq__        ==
__ne__        !=
__ge__        >=
__gt__        >


Math
__add__       +
__iadd__      +=
__sub__       -
__isub__      -=
__mul__       *
__imul__      *=
__pow__       **  
__ipow__      **=
__div__       /
__idiv__      /=
__floordiv__  //
__ifloordiv__ //=
__mod__       %
__imod__      %=
__pos__       +obj    Return obj positive (+obj).
__neg__       -obj    Return obj negated (-obj).


Bitwise 
__and__       &
__or__        |
__xor__       ^       Return the bitwise exclusive or of a and b.
__ixor__      ^=
__lshift__    <<      a shifted left by b.
__ilshift__   <<=
__rshift__    >>      a shifted right by b.
__irshift__   >>=



__contains__  in


__matmul__    @
'''










###########################################################################
############################### Flow Control ##############################
###########################################################################

@contextmanager
def except_handler( exc_handler ):
    '''
    Raising errors without traceback        https://stackoverflow.com/questions/38598740/raising-errors-without-traceback/38598793#38598793
    Sets a custom exception handler for the scope of a 'with' block.
    '''
    sys.excepthook = exc_handler
    yield
    p( '~~~~~~~~~restore sys.excepthook~~~~~~~' )
    sys.excepthook = sys.__excepthook__

def excepthook( type, value, traceback ):
    logging.error( value )


def ifInvalid( bool_, prompt_info='Hello world ~~', parent=None ):
    '''
    Print an error message without printing a traceback and close the program when a condition is not met
    https://stackoverflow.com/questions/17784849/print-an-error-message-without-printing-a-traceback-and-close-the-program-when-a
    '''
    if not bool_:
        # with except_handler( excepthook ):
        raise Exception( prompt_info ) 

def ifValid( bool_, prompt_info='Hello world ~~', parent=None ):
    if bool_:
        # with except_handler( excepthook ):
        raise Exception( prompt_info ) 









###########################################################################
################################# Function ################################
###########################################################################

'''
# terminate tool execution
# codes....
sys.exit()
# codes....
'''


class Func( object ):

    def __init__( self ):
        pass


    @staticmethod
    def defaultValue( func, argv ):
        '''
        PARMS:
                func  -  function
                argv  -  str
        '''
        # info = inspect.getargspec( func )
        # args_with_default_value = dict(zip( info.args[ -len(info.defaults): ], info.defaults ))
        # return args_with_default_value[ argv ]
        return Func.defaultValuesDict( func )[ argv ]
        

    @staticmethod
    def defaultValuesDict( func ):
        '''
        PARMS:
                func  -  function
                argv  -  str
        '''
        info = inspect.getargspec( func )
        args_with_default_value = dict(zip( info.args[ -len(info.defaults): ], info.defaults ))
        return args_with_default_value


    # ~~~~~~~~~~~~~~ >>>>>>>>>>>> ~~~~~~~~~~~~~ #
    # List Related

    @staticmethod
    def _1stArgv_beList( func ):

        def wrapper( *args, **kwargs ):

            # pre-processing the first argument
            # if not isinstance( args[0], list ) and not isinstance( args[0], tuple ):
            if type(args[0]) not in [list, tuple]:
                args = list(args)
                args[0] = [ args[0] ]


            # execute func
            result = func( *args, **kwargs )


            return result
        
        return wrapper

    @staticmethod
    def _2ndArgv_beList( func ):

        def wrapper( *args, **kwargs ):

            # pre-processing the first argument
            if not isinstance( args[1], list ) and not isinstance( args[1], tuple ):
                args = list(args)
                args[1] = [ args[1] ]


            # execute func
            result = func( *args, **kwargs )


            return result
        
        return wrapper


    @staticmethod
    def _1stArgvList_KeepIntact( func ):

        def wrapper( *args, **kwargs ):

            # keep list intact by duplicate the original
            args[0] = list( args[0] )


            # execute func with the duplicated list
            result = func( *args, **kwargs )


            return result

        return wrapper
    # ~~~~~~~~~~~~~~ <<<<<<<<<<<< ~~~~~~~~~~~~~ #


    # ~~~~~~~~~~~~~~ >>>>>>>>>>> ~~~~~~~~~~~~~~ #
    # Path Related
    @staticmethod
    def _1stArgvPath_Validation(func):

        def wrapper( *args, **kwargs ):

            if not os.path.exists( args[0] ):
                logging.error( "File dosen't exist !!    Maybe because there's UTF-8 character in file's name." )
                return

            else:
                result = func( *args, **kwargs )
                return result

        return wrapper
    # ~~~~~~~~~~~~~~~ <<<<<<<<<< ~~~~~~~~~~~~~~ #














###########################################################################
###########################################################################
###########################################################################
# Class, Module
# Class, Module
# Class, Module
# Class, Module
# Class, Module

'''
New-style Class                 https://docs.python.org/2/glossary.html#term-new-style-class
        Any class which inherits from object. 
        This includes all built-in types like list and dict. 
        Only new-style classes can use Python's newer, versatile features like __slots__, descriptors, properties, and __getattribute__().
New-style and Classic Classes   https://docs.python.org/2/reference/datamodel.html#newstyle
        

super                           https://docs.python.org/2/library/functions.html#super

Multiple Inheritance            https://docs.python.org/2/tutorial/classes.html#multiple-inheritance

Python super() arguments: why not super(obj)?           https://stackoverflow.com/questions/17509846/python-super-arguments-why-not-superobj
        The two-argument form is only needed in Python 2. 
        The reason is that self.__class__ always refers to the "leaf" class in the inheritance tree -- that is, the most specific class of the object -- 
        but when you call super you need to tell it which implementation is currently being invoked, so it can invoke the next one in the inheritance tree.
'''


'''
ERROR: __init__() should return None, not 'str'.
https://www.reddit.com/r/learnpython/comments/scwwc/can_you_help_me_to_understand_what_i_made_wrong/
the __init__ method isn't supposed to return a value at all. 
That's what the error is telling you: should return None. 
Whereas you are trying to return a value (a) from it.
'''


'''
Class Attribute vs. Instance Attribute      https://dzone.com/articles/python-class-attributes-vs-instance-attributes
    ....
    Class Attributes Mutate to Be Instance Attributes
    ....
    The affectation added a new instance attribute to the object foo and only to that object 
    which is why in the previous example the object bar kept printing the class attribute.

    With immutable objects, this behavior is always the same. 
    However, with mutable objects like lists, for example, it is not always the case, 
    depending on how you modify your class attribute.
    ....
    When a mutable class attribute is modified by an object, 
    it does not mutateto turn into an instance attribute for that object. 
    It stays shared between all the objects of the class with the new elements appended to it.
    
    However, if you attach a new list to that attribute ( foo.class_attr = list("foo")) 
    you will get the same behavior as the immutable objects. 

Python Class Attributes: An Overly Thorough Guide       https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
'''


'''
Descriptor HowTo Guide      https://docs.python.org/2/howto/descriptor.html
property                    https://docs.python.org/2/library/functions.html#property
'''


def isClass( object ):
    """
    Args:
        object ([type]): Test object.

    Returns:
        [bool]: If object is a class.

    Another way:
        type( object ) is type
    """
    return inspect.isclass( object )


def moduleSymbolTable( mod ):
    '''
    https://docs.python.org/2/library/stdtypes.html?highlight=__dict__#modules
    '''

    return mod.__dict__


def getClassName( cls_inst ):
    """
    Args:
        cls_inst (class instance): Any class instance.

    Returns:
        [str]: the class name of class instance.
    """    
    return cls_inst.__class__.__name__


def baseClasses( cls_inst ):
    '''
    EXAMPLES:

            str.__bases__
            >>> (<type 'basestring'>,)    
    '''

    return cls_inst.__class__.__bases__


def rootClasses( cls ):
    '''
    HOT TO USE:
            inspect.getmro(ass.ls()[0].__class__)
                RETURNS: (<type 'Material'>, <type 'MaterialInterface'>, <type 'Object'>, <type '_ObjectBase'>, <type '_WrapperBase'>, <type 'object'>)
    '''
    if not isClass( cls ):
        cls = cls.__class__

    class_hierachy = inspect.getmro(cls)
    class_hierachy_name = [ i.__name__ for i in class_hierachy ]

    return class_hierachy_name


'''
def collectClassInst( dictionary, class_name, alias=False ):
    
    # list of matched class instance 
    collection = [ dictionary[i] for i in dictionary.keys() if dictionary[i].__class__.__name__ == class_name ]



    # list for dictionary
    list_for_dict = [ (i.name.lower(), i) for i in collection ]

    if alias:
        for i in collection:
            if i.alias:
                for j in i.alias:
                    list_for_dict.append( (j.lower(), i) )



    # build dictionary
    collection = dict( list_for_dict ) 


    return collection
'''


'''
# Check if a class is a dataclass in Python 3
import dataclasses
dataclasses.is_dataclass( something )
'''

'''
# Get attribute (variable) of module.
getattr( kwargs['node'].hm(), 'Node_Block_Codes' )
'''

def setAttr( cls, attr_name, attr_value, 
                replace = False, terminate = False,
                name_prefix = '', name_suffix = '',
                ):
    """
    Args:
        cls (Class / Class Inst): [description]
        attr_value (str): name of attribute / property / static method / class method
        replace (bool, optional): [description]. Defaults to False.
    """
    if name_prefix:
        attr_name = name_prefix + attr_name
    if name_suffix:
        attr_name = attr_name + name_suffix

    if not replace and attr_name in dir(cls):
        msg = '{}.{} exists.'.format( cls, attr_name )
        if terminate:
            raise Exception( msg )
        else:
            # print( msg )
            return
        
    setattr( cls, attr_name, attr_value )
    '''
    # another way
    target_cls_inst.__dict__[target_name] = value
    target_cls_inst.__dict__.setdefault( target_name, value )
    '''

def copyAttr( target_cls_inst, target_name,
                source_cls_inst, source_name,
                replace=False ):
    if not replace:
        if target_name in dir(target_cls_inst):
            return

    value = getattr( source_cls_inst, source_name )

    target_cls_inst.__dict__[target_name] = value

def hasAttr( cls_inst, name, exception=True ):
    exist = name in dir(cls_inst)
    
    if exception:
        if not exist:
            raise Exception( 'Attribute "{}" does not exist.'.format(name) )

    return exist






###########################################################################
################################# Session #################################
###########################################################################

def declareMainVar( variable_name, variable_value ):
    sys.modules['__main__'].__dict__[ variable_name ] = variable_value

    '''
    # anothery way
    import __main__
    __main__.nodes = hou.selectedItems()
    __main__.node = __main__.nodes[0]
    '''


def evalMainVar( variable_name ):
    if variable_name in sys.modules['__main__'].__dict__.keys():
        return sys.modules['__main__'].__dict__[ variable_name ]
    else:
        return None


def importIntoMainSession( py_script_path, sys_argv=None ):

    # you could use these sys.argv in your python script file
    if sys_argv:
        sys.argv = sys_argv

    # import python script file into __main__ session
    with open( py_script_path ) as src:
        imp.load_module( '__main__', src, py_script_path, (".py", "r", imp.PY_SOURCE) )


def execute( code=None, pyfile=None ):

    if code:
        # if isPy3:
        #     exec( code )
        # else:
        #     exec code
        pass

    elif pyfile:
        execfile( pyfile )

    else:
        p("No execution.")
















###########################################################################
################################## STDOUT #################################
###########################################################################

def stdout( object_='', info='', step='', start=False, end=False ):
    if object_:
        object_ = '({}) '.format(object_)

    if info:
        info += ' >> '
    
    if start:
        step = 'Start'
    elif end:
        step = 'Finished'
    else:
        pass
        
    p( '{}{}{}\n'.format(object_, info, step) )
    sys.stdout.flush()










###########################################################################
################################### Enum ##################################
###########################################################################
'''
type(name, bases, dict)     https://docs.python.org/2/library/functions.html#type

def enum( *enumerated ):
    enums = dict( zip( enumerated, range( len( enumerated ) ) ) )
    enums[ 'names' ] = enumerated
    new_type = type( 'enum', (), enums )
    return new_type

test = enum( 'ZERO', 'ONE', 'TWO', 'THREE' )
print test.ZERO, test.ONE, test.TWO, test.THREE
# >> 0 1 2 3
print test.names[ test.ZERO ], test.names[ test.ONE ], test.names[ test.TWO ], test.names[ test.THREE ]
# >> ZERO ONE TWO THREE
'''









###########################################################################
################################ Clipboard ################################
###########################################################################

def copy2Clipboard( info ):
    command = 'echo '+ info.strip() + '|clip'
    subprocess.check_call( command, shell=True )







