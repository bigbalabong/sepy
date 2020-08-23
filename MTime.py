'''
Tier: Base
'''

from .MBase import *
from .MData import *

import time                     # https://docs.python.org/2/library/time.html
import datetime

'''
Time            https://docs.python.org/2/library/time.html
        .time()         Return the time in seconds since the epoch as a floating point number.
        .clock()        On Windows, this function returns wall-clock seconds elapsed since the first call to this function, 
                        as a floating point number, based on the Win32 function QueryPerformanceCounter().
'''




class Time( object ):

    def __init__( self ):
        pass


    @staticmethod
    def timer( func ):

        def wrapper( *args, **kwargs ):

            # record time
            time_start = time.clock()


            # execute func
            result = func( *args, **kwargs )


            time_end = time.clock()
            p( '\t {} : {} sec'.format( func.__name__, time_end - time_start ) )

            return result
        
        return wrapper


    @staticmethod
    def hmsToSecs( hms='00:00:00' ):
        hms = hms.split(':')
        hms = [ int(i) for i in hms ]
        smh = hms[::-1]
        smh = enumerate(smh)
        smh = [ i[1] * pow(60, i[0]) for i in smh ]
        secs = sum( smh )
        return secs




class Timer( object ):
    '''
    HOT TO USE:
            timer = Timer( 'state 1' )
            # some codes

            timer.mark( 'stage 2' )
            # some codes

            timer.mark( 'state 3' )
            # some codes

            timer.stop()

                PRINT:
                    0: state 1  -  xx.xx sec
                    1: stage 2  -  xx.xx sec
                    2: state 3  -  xx.xx sec
    '''

    def __init__( self, start_info='' ):
        self.mark_list = []

        start = '0: {}'.format( start_info )
        self.mark_list.append( (start, time.clock()) )

        self.mark_index = 0


    def mark( self, mark_info='' ):
        self.mark_index += 1
        mark = '{}: {}'.format( self.mark_index, mark_info )
        self.mark_list.append( (mark, time.clock()) )


    def stop( self ):
        stop = 'end: '
        self.mark_list.append( (stop, time.clock()) )

        info = ''
        for i, mark in enumerate(self.mark_list[:-1]):
            duration = self.mark_list[i+1][1] - mark[1]
            duration = round( duration, 2 )

            info += '\n{}  -  {} sec'.format( mark[0], duration )

        p( info )


def whatsTheDate( the_day='today' ):  

    today = datetime.date.today()  
    oneday = datetime.timedelta( days=1 )      

    if the_day == 'today':
        return str(today)

    elif the_day == 'yesterday':
        yesterday = today - oneday   
        return str(yesterday)

    elif the_day == 'tomorrow':
        tomorrow = today + oneday   
        return str(tomorrow)

    else:
        pass

def whatsTheTime( date=False, normalize=False, reverse=False ):
    '''
    EXAMPLES:
            whatsTheTime()
                RETURNS: '12:03:33'
            whatsTheTime( True )
                RETURNS: '12:03:36  2020-02-11'
    '''
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%H:%M:%S")

    if normalize:
        current_time = current_time.replace( ':', '_' )


    if date:
        current_date = whatsTheDate()
        
        if reverse:
            return '{}  {}'.format( current_date, current_time )
        else:
            return '{}  {}'.format( current_time, current_date )
    else:
        return current_time






# ~~~~~~~~~~~~~ >>>>>>>>>>>>>> ~~~~~~~~~~~~ #
# Qt
'''
QTime.currentTime()                 https://doc-snapshots.qt.io/qtforpython/PySide2/QtCore/QTime.html#PySide2.QtCore.PySide2.QtCore.QTime.currentTime
        Returns the current time as reported by the system clock.
        Result: PySide2.QtCore.QTime(21, 31, 2, 971)
QDateTime.currentDateTime()         https://doc-snapshots.qt.io/qtforpython/PySide2/QtCore/QDateTime.html#PySide2.QtCore.PySide2.QtCore.QDateTime.currentDateTime
        Returns the current datetime, as reported by the system clock, in the local time zone.
        Result: PySide2.QtCore.QDateTime(2019, 10, 1, 21, 29, 16, 226, 0)
QDateTime.currentDateTimeUtc()      https://doc-snapshots.qt.io/qtforpython/PySide2/QtCore/QDateTime.html#PySide2.QtCore.PySide2.QtCore.QDateTime.currentDateTimeUtc
        Returns the current datetime, as reported by the system clock, in UTC.
        Result: PySide2.QtCore.QDateTime(2019, 10, 1, 13, 29, 48, 130, 1)
'''




