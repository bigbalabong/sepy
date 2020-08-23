'''
Tier: Base
'''

from .MBase import *



###########################################################################
################################# Integer #################################
###########################################################################

class Integer( object ):
    
    def __init__( self, integer_ ):
        # super( Integer, self ).__init__()

        self.integer_ = integer_


    def clamp( self, min_=0, max_=1 ):
        value = self.integer_
        return min( max(value, min_), max_ )



    # ======================================================== #
    # ====================== Conversion ====================== #
    # ======================================================== #
    def hex( self ):
        '''
        hex     https://docs.python.org/2.7/library/functions.html#hex
        '''
        return hex( self.integer_ )



    # ======================================================== #
    # ======================== Random ======================== #
    # ======================================================== #
    @staticmethod
    def rand( a=0, b=10 ):
        '''
        RETURNS:
                a random integer N such that a <= N <= b.
        '''
        return random.randint( a, b )

I_ = Integer







###########################################################################
################################## Float ##################################
###########################################################################
'''
Scientific Notation Converter       https://www.calculatorsoup.com/calculators/math/scientific-notation-converter.php
'''

class Float( object ):
    
    def __init__( self, float_ ):
        # super( Float, self ).__init__()

        self.float_ = float_


    def round( self, digits_num=4 ):
        return round( self.float_, digits_num )


    def fit01( self, new_min=0.0, new_max=1.0 ):
        return new_min * (1-self.float_) + new_max * value


    def clamp( self, min_=0.0, max_=1.0 ):
        return min( max(self.float_, min_), max_ )



    # ~~~~~~~~~~~~~~~ >>>>>>>>> ~~~~~~~~~~~~~~~ #
    # Random

    @staticmethod
    def rand():
        return random.random()
    
    @staticmethod
    def rand2( multiplier=1 ):
        return ( random.random() * multiplier, random.random() * multiplier )
    
    @staticmethod
    def rand3( multiplier=1 ):
        return ( random.random() * multiplier, random.random() * multiplier, random.random() * multiplier )
    
    @staticmethod
    def rand4( multiplier=1 ):
        return ( random.random() * multiplier, random.random() * multiplier, random.random() * multiplier, random.random() * multiplier )
    # ~~~~~~~~~~~~~~~~ <<<<<<<< ~~~~~~~~~~~~~~~ #

F_ = Float




class Vec3( object ):

    def __init__( self, float_list ):
        # super( Vec3, self ).__init__()

        self.vec3_ = float_list


    def __mul__( self, multiplier ):
        if isinstance( multiplier, float ):
            multiplier = [multiplier] * 3

        v1, v2, v3 = self.vec3_
        m1, m2, m3 = multiplier

        return ( v1*m1, v2*m2, v3*m3 )


    @classmethod
    def rand( cls, normalize=False ):
        x_ = random.random()
        y_ = random.random()
        z_ = random.random()

        new_vector = cls( (x_, y_, z_) )

        if normalize:
            new_vector.normalize()

        return new_vector.vec3_


    @property
    def Length( self ):
        x_, y_, z_ = self.vec3_
        return math.sqrt( (x_*x_) + (y_*y_) + (z_*z_) )


    @property
    def Length2( self ):
        x_, y_, z_ = self.vec3_
        return (x_*x_) + (y_*y_) + (z_*z_)


    def normalize( self ):
        ratio = 1 / self.Length

        self.vec3_ = self.__mul__( ratio )

        return self.vec3_










###########################################################################
################################## String #################################
###########################################################################

class String( object ):
    '''
    DOCS:
            String Methods      https://docs.python.org/2/library/stdtypes.html#string-methods
            string              https://docs.python.org/2/library/string.html
    
    Character                   https://en.wikipedia.org/wiki/Character_(computing)
            Examples of characters include letters, numerical digits, common punctuation marks (such as "." or "-"), and whitespace.
    '''

    seperator = '\n\n' + '>'*60


    def __init__( self, string ):
        self.string_ = string


    def __str__( self ):
        return self.string_


    def __and__( self, another_string, match_case=False ):
        '''
        Find the same part.

        if you want to turn on 'match_case', you could do like this.
        String( 'some strings' ).__and__( 'another string', True )
        '''

        # pre-processing arguments
        str1_raw = self.string_
        str2_raw = another_string.string if another_string.__class__.__name__ == 'String' else another_string

        substring = ""
        match = ""


        # find common substring
        # compare two strings in both direction
        for str1, len1, str2, len2 in ( ( str1_raw, len(str1_raw), str2_raw, len(str2_raw) ),
                                        ( str2_raw, len(str2_raw), str1_raw, len(str1_raw) ) ):
            for i in range( len1 ):
                for j in range( len2 ):

                    if match_case and i + j < len1 and str1[i + j] == str2[j] :
                        match += str2[j]
                    elif not match_case and i + j < len1 and str1[i + j].lower() == str2[j].lower() :
                        match += str2[j]
                    else:
                        if match.__len__() > substring.__len__() : 
                            substring = match
                        match = ""


        return substring


    def isString( self ):
        '''
        For Python 2, check if the type is "str" or "unicode".
        '''
        if isPy3:
            return isinstance( self.string_, str )
        else:
            return type( self.string_ ) in (str, unicode)



    def split( self, string, num=None, rsplit=False ):
        raw = self.string_
        raw_lowercase = self.string_.lower()

        splitter = string
        splitter_lowercase = splitter.lower()



        # split
        if not num:
            if not rsplit:
                raw_lowercase_splitted = raw_lowercase.split( splitter_lowercase )
            else:
                raw_lowercase_splitted = raw_lowercase.rsplit( splitter_lowercase )
        else:
            if not rsplit:
                raw_lowercase_splitted = raw_lowercase.split( splitter_lowercase, num )
            else:
                raw_lowercase_splitted = raw_lowercase.rsplit( splitter_lowercase, num )



        raw_lowercase_splitted_length = [ len(i) for i in raw_lowercase_splitted ]

        raw_lowercase_splitted_indexs = [ 0 ]
        for i, length in enumerate( raw_lowercase_splitted_length[1:] ):
            i += 1
            raw_lowercase_splitted_indexs.append( sum(raw_lowercase_splitted_length[:i]) + i * len(splitter) )



        raw_splitted = []
        for i, index in enumerate( raw_lowercase_splitted_indexs ):
            slice_start = index
            slice_end = index + raw_lowercase_splitted_length[i]
            raw_splitted.append( raw[ slice_start : slice_end ] )

        return raw_splitted

    def rsplit( self, string, num=None ):
        return self.split( string=string, num=num, rsplit=True )


    def mjust( self, length, pad=' ' ):
        string = self.string_

        string = string.rjust( ( length + len(string) )/2, pad )
        string = string.ljust( length, pad )

        return string




    # ~~~~~~~~~~~~~~~ >>>>>>>>>> ~~~~~~~~~~~~~~ #
    # File Name & Extension

    @property
    def Filename( self ):
        '''
        RETURN:
                Non-extension part.
        '''
        return os.path.splitext( self.string_ )[0]

    @property
    def Ext( self ):
        '''
        RETURN:
                Extension name.
        '''
        return os.path.splitext( self.string_ )[1]
    # ~~~~~~~~~~~~~~ <<<<<<<<<<< ~~~~~~~~~~~~~~ #



    def digitalize( self ):
        '''
        RETURNS:
                all digits part in string as a list.
        '''
        string = self.string_
        digits_list = []
        digits_str = digits = None

        # do loop
        while True:

            # . in regex is a metacharacter, it is used to match any character. 
            # To match a literal dot, you need to escape it, so use \.
            digits_str = re.search( r'[0-9\.]+', string )
            
            if digits_str:
                # get string
                digits_str = digits_str.group()

                # digitalize
                if '.' not in digits_str:
                    digits = int( digits_str )
                else:
                    digits = float( digits_str )

                # add to list
                digits_list.append( digits )    

                # get rest string
                string = string.split( digits_str, 1 )[1]


            else:
                break


        return digits_list


    def hash():
        return hash( self.string_ )


    def encode():
        '''
        WIP
        '''
        import hashlib                  # https://docs.python.org/2/library/hashlib.html
        return int( hashlib.md5(string).hexdigest()[:8], 16 )

        '''
        # another way
        int_list = [ str(ord(i)) for i in string ]
        return ''.join( int_list )
        '''


    @property
    def Index( self ):
        return self.search2('digits suffix num')
        '''
        # another way
        return int( self.string_.rsplit('[',1)[1].rsplit(']',1)[0])
        '''



    # ~~~~~~~~~~~~~~~ >>>>>>>>>> ~~~~~~~~~~~~~~ #
    # OS

    @property
    def isDir( self ):
        return os.path.isdir( self.string_ )

    @property
    def isFile( self ):
        return os.path.isfile( self.string_ )
    
    
    def normpath( self, validation=False, is_dir=False, is_file=False ):

        # signle path
        if '"' not in self.string_ and '\n' not in self.string_:
            path = os.path.normpath( self.string_ ).replace('\\','/')

            if validation:
                ifInvalid( os.path.exists( path ), "The file path dosn't exist." )
                
            if is_dir:
                ifInvalid( os.path.isdir( path ), "The path is not a folder." )

            if is_file:
                ifInvalid( os.path.isdir( path ), "The path is not a file." )

            return path


        # multiple-lines paths
        else: 
            if '"' in self.string_:
                self.string_ = self.string_.replace('"', '')

            paths = [ i.strip() for i in self.string_.split('\n') ]
            paths = [ i for i in paths if i ]
            paths = [ self.__class__(i).normpath() for i in paths ]

            if validation:
                for path in paths:
                    ifInvalid( os.path.exists( path ), "The file path dosn't exist." )
                
            if is_dir:
                for path in paths:
                    ifInvalid( os.path.isdir( path ), "The path is not a folder." )

            if is_file:
                for path in paths:
                    ifInvalid( os.path.isdir( path ), "The path is not a file." )

            return paths
    
    def relativePathTo( self, path, replace='..' ):
        if self.string_.startswith( path ):
            new_string = self.string_.replace( path, replace )
            return new_string
        
        else:
            return self.string_

    def cd( self ):
        '''
        WIP:
                return parent folder path / child folder path / relative folder path
        '''
        pass
    # ~~~~~~~~~~~~~~~ <<<<<<<<< ~~~~~~~~~~~~~~~ #





    # ======================================================== #
    # ======================= Normalize ====================== #
    # ======================================================== #
    def normTime( self ):
        '''
        Examples:
                S_('72:43').normtime()
                    RETURNS: 01:12:43
        '''

        # '70:20'
        raw_time = self.string_

        # [0, 70, 20]
        h_m_s = [ int(i) for i in raw_time.split(':') ]
        if len(h_m_s) < 3:
            h_m_s = [0] * (3-len(h_m_s)) + h_m_s
        
        # [1, 10, 20
        for i,j in enumerate(h_m_s[1:]):
            i += 1
            h_m_s[i] = j%60
            h_m_s[i-1] += j/60

        # 01:10:20
        for i,j in enumerate(h_m_s):
            h_m_s[i] = str(j).rjust(2,'0')
        h_m_s = ':'.join(h_m_s)

        return h_m_s

    @staticmethod
    def normalizeTime():
        from others import copy as copyToClipboard
        from others import paste as pasteFromClipboard
        
        raw_time = pasteFromClipboard()

        time_normalized = S_(raw_time).normTime()

        copyToClipboard( time_normalized )
    
    
    @staticmethod
    def normalizeFilename():
        from others import copy as copyToClipboard
        from others import paste as pasteFromClipboard

        raw_filename = pasteFromClipboard()

        raw_filename = [ i.strip() for i in raw_filename.split('\n') ]
        raw_filename = '__'.join([ raw_filename[0], raw_filename[-1] ])
        raw_filename = raw_filename.replace('/', '-')

        copyToClipboard( raw_filename )




    # ======================================================== #
    # ====================== Re / Search ===================== #
    # ======================================================== #
    '''
    re      https://docs.python.org/2/library/re.html
            https://docs.python.org/2/library/re.html#regular-expression-syntax
            \A  Matches only at the start of the string.
            \Z  Matches only at the end of the string.

            \d  Matches any decimal digit. This is equivalent to the set [0-9].
            \D  Matches any non-digit character. This is equivalent to the set [^0-9].

            \w  Matches any alphanumeric character and the underscore. This is equivalent to the set [a-zA-Z0-9_].
            \W  Matches any non-alphanumeric character. This is equivalent to the set [^a-zA-Z0-9_].

            \s  Matches any whitespace character. This is equivalent to the set [\t\n\r\f\v].
            \S  Matches any non-whitespace character. This is equivalent to the set [^\t\n\r\f\v].

            \b  Matches the empty string, but only at the beginning or end of a word.
            \B  Matches the empty string, but only when it is not at the beginning or end of a word.

            *   Matches 0 or more repetitions.
            +   Matches 1 or more repetitions.
    '''
    def prune( self, chars ):
        new_string = self.string_

        for i in chars:
            new_string = new_string.replace( i, '' )

        new_string = new_string.strip()
        
        return new_string


    @property
    def SuffixDigitsStr( self ):
        result = re.search( r'[\d]*[.]*\d+\Z', self.string_ )
        if result:
            return result.group()

    @property
    def SuffixDigits( self ):
        digits = self.SuffixDigitsStr

        if digits:
            digits = int(digits)
            return digits



    def search( self, regex, from_start=False, from_end=False, find_all=False ):
        if find_all:
            return re.findall( regex, self.string_ )

        else:
            # pre-processing regex
            if from_start:
                regex = r'\A' + regex
            if from_end:
                regex = regex + r'\Z'

            # search
            result = re.search( regex, self.string_ )
            if result:
                return result.group()
    

    def search2( self, preset=None, inverse=False ):
        '''
        Search using preset regex.
        Args
                inverse (bool_)  -  e.g. If inverse is true, select digits suffix part.
                                         If inverse is false, select non digits suffix part.
        '''
        preset = preset.lower()

        if not preset:
            return

        elif preset in ('letters digits prefix', 'ldp') and not inverse:
            return self.search( r'[a-zA-Z]+\d+', from_start=True )
        elif preset in ('letters digits prefix', 'ldp') and inverse:
            letters_digits_prefix = self.search2( 'letters digits prefix' )
            return self.string_.rsplit(letters_digits_prefix, 1)[0]

        elif preset in ('digits suffix', 'ds') and not inverse:
            # e.g. digits suffix.                   123 / 4.22
            digits_suffix = self.search( r'[\d]*[.]*\d+', from_end=True )
            if digits_suffix:
                return digits_suffix
            
            # e.g. round brackets digits suffix.    (123) / (4.22)
            digits_suffix = self.search( r'\([\d]*[.]*\d+\)', from_end=True )
            if digits_suffix:
                return digits_suffix

            # e.g. square brackets digits suffix.   [123] / [4.22]
            digits_suffix = self.search( r'\[[\d]*[.]*\d+\]', from_end=True )
            if digits_suffix:
                return digits_suffix

            # e.g. curly brackets digits suffix.    {123} / {4.22}
            digits_suffix = self.search( r'{[\d]*[.]*\d+}', from_end=True )
            if digits_suffix:
                return digits_suffix

            # e.g. angle brackets digits suffix.    <123> / <4.22>
            digits_suffix = self.search( r'<[\d]*[.]*\d+>', from_end=True )
            if digits_suffix:
                return digits_suffix
        elif preset in ('digits suffix', 'ds') and inverse:
            digits_suffix = self.search2( 'digits suffix' )
            return self.string_.rsplit(digits_suffix, 1)[0]
        elif preset in ('digits suffix number', 'digits suffix num', 'dsn'):
            # e.g. digits suffix.                   123 / 4.22
            if not self.string_[-1].isdigit():
                self.string_ = self.string_[:-1]

            digits_suffix = self.search( r'[\d]*[.]*\d+', from_end=True )
            if digits_suffix:
                if '.' in digits_suffix:
                    return float(digits_suffix)
                else:
                    return int(digits_suffix)

        elif preset in ('underscore suffix', 'us'):
            # e.g. _file / __Mesh
            return self.search( r'_+[a-zA-Z0-9]+', from_end=True )

        elif preset in ('bak suffix', 'bs'):
            return self.search( r'bak\d*', from_end=True )

        elif preset in ('ext',): 
            return self.search( r'.[a-zA-Z0-9]+', from_end=True )

        elif preset in ('author', 'au'): 
            author_list = self.search( r'__[a-zA-Z0-9\s]+', from_end=True )
            if author_list:
                return author_list.rsplit('__', 1)[1].strip()

            author_list = self.search( r' by [a-zA-Z0-9\s]+', find_all=True )
            if author_list:
                return author_list[-1].rsplit(' by ', 1)[1].strip()

        else:
            ifInvalid( False, "There's no matched preset." )


    def searchAll( self, regex, index_pairs=False, inverse=False ):
        '''
        Examples:
                S_('test_12_Mesh2__23').searchAll( r'\d+' )
                    RETURN: ['12', '2', '23']
                S_('test_12_Mesh2__23').searchAll( r'\d+', index_pairs=True )
                    RETURN: [(5, 7), (12, 13), (15, 17)]
                S_('test_12_Mesh2__23').searchAll( r'\d+', inverse=True )
                    RETURN: ['test_', '_Mesh', '__']
        '''
        # return list of strings part which matching regex
        if not index_pairs and not inverse:
            return re.findall( regex, self.string_ )


        # get index pairs pointing at strings part which matching regex
        indexes = [ (i.start(), i.end()) for i in re.finditer( regex, self.string_ ) ]


        # return index pairs
        if index_pairs and not inverse:
            return indexes


        # return list of string which not matching regex
        strings = self.extractFromIndexPairs( index_pairs, True )
        return strings


    def extractFromIndexPairs( self, index_pairs, inverse=False ):
        '''
        Examples:
                S_('0123456789').extractFromIndexPairs( [(2,3), (6,9)] )
                    RETURN: ['2', '678']
                S_('0123456789').extractFromIndexPairs( [(2,3), (6,9)], True )
                    RETURN: ['01', '345', '9']
        '''
        if not inverse:
            strings = [ self.string_[i[0]:i[1]] for i in index_pairs ]
            
        else:
            index_pairs.reverse()
            strings = [ self.string_ ]
            for indexes in index_pairs:
                i,j = indexes
                strings = strings[0].rsplit( self.string_[i:j], 1 ) + strings[1:]

            strings = [ i for i in strings if i ]
            
        return strings


    # ======================================================== #
    # ========================= HTML ========================= #
    # ======================================================== #
    def addTag( self, tag ):
        '''
        TAGs:
                <h1> to <h6>    define HTML headings.
                <ul>    defines an unordered (bulleted) list.

        Args
                tag (str)  -  ul
        '''
        tag_start = '<{}>'.format(tag)
        tag_end = '</{}>'.format(tag)
        return tag_start + self.string_ + tag_end

S_ = String









###########################################################################
################################### List ##################################
###########################################################################

class List( object ):
    '''
    Mutable Sequence Types      https://docs.python.org/2/library/stdtypes.html#mutable-sequence-types

    Tips about list:
            avoid list indexing error: IndexError: list index out of range
            test = []
            test[0]     return:  IndexError: list index out of range
            test[:1]    return:  []
    '''

    def __init__( self, list_=[] ):
        self.raw_list = list_

        if list_ is None:
            self.list_ = None
        
        elif type( list_ ) is list:
            self.list_ = list_

        elif type( list_ ) is tuple:
            self.list_ = list(list_)
        
        elif S_(list_).isString():
            self.list_ = [ list_ ]
        
        elif '__len__' in dir(list_):
            '''
            e.g.
                pm.dt.Vector(1,2,3)
                    RETURN: dt.Vector([1.0, 2.0, 3.0])
                L_( pm.dt.Vector(1,2,3) ).list_
                    RETURN: [1.0, 2.0, 3.0]
            '''
            self.list_ = list(list_)
        
        else:
            self.list_ = [ list_ ]


    def __len__( self ):
        return self.list_.__len__()


    def isList( self ):
        '''
        Check if the type is list or tuple.
        '''
        return type( self.raw_list ) in (list, tuple)


    def get( self, index ):
        '''
        When get item of list like this
            the_list[0]
        if the index is out of range, it would be error.
        So, you could use this function to get item of list.
        If the index is invalid, return None rather than error.
        '''
        if not self.list_:
            return
            
        the_list = self.list_[ index, index + 1 ]
        if the_list:
            return the_list[ 0 ]


    def append( self, value ):
        '''
        The build-in "append" function of "list" return nothing.
        So, if you need the result of "append", please use this shortcut.
        '''
        self.list_.append( value )
        return self.list_


    # ~~~~~~~~~~~~~ >>>>>>>>>>>>> ~~~~~~~~~~~~~ #
    # Index
    def prev( self, item ):
        '''
        Examples:
                List([1,2,3,4,5]).prev(3)
                    RETURNS: 2
                List([1,2,3,4,5]).prev(1)
                    RETURNS: None
        '''
        index = self.list_.index( item )

        if index == 0:
            return None
        else:
            return self.list_[ index-1 ]

    def next( self, item ):
        '''
        Examples:
                List([1,2,3,4,5]).next(3)
                    RETURNS: 4
                List([1,2,3,4,5]).next(5)
                    RETURNS: None
        '''
        index = self.list_.index( item )

        if index == len(self.list_)-1:
            return None
        else:
            return self.list_[ index+1 ]
    

    def sortRandom( self, percent=None ):
        # list_ = list(self.list_)
        list_ = self.list_


        # sort randomly
        random.shuffle( list_ )


        # filter percent
        if percent:
            return list_[ : int(math.ceil( len(list_) * percent )) ]


        return list_

    def sortBy( self, orders, as_string=False ):
        '''
        Args
                orders (list)
        Examples:
                L_( list('abcde') ).sortBy( [5,2,4,3,1] )
                        RETURNS: ['e', 'b', 'd', 'c', 'a']
        '''
        if len(orders) < len(self.list_):
            raise Exception( 'The length of order list is too short.' ) 

        sorted_list = zip( self.list_, orders )
        sorted_list.sort( key=lambda x: x[1] )
        sorted_list = [ i[0] for i in sorted_list ]

        if as_string:
            return ''.join( sorted_list )
        else:
            return sorted_list


    def group( self, group_members_num, remain_incomplete_group=True ):
        '''
        Examples:
                groupList( [0,1,2,3,4,5,6,7,8,9,10,11,12], 2 )
                    RETURNS: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), [12]]
                groupList( [0,1,2,3,4,5,6,7,8,9,10,11,12], 3 )
                    RETURNS: [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), [12]]
                groupList( [0,1,2,3,4,5,6,7,8,9,10,11,12], 4 )
                    RETURNS: [(0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), [12]]
                groupList( [0,1,2,3,4,5,6,7,8,9,10,11,12], 2, remain_incomplete_group=False )
                    RETURNS: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
        '''
        list_ = self.list_


        unzipped_list = []
        for i in range( group_members_num ):
            unzipped_list.append( list_[i::group_members_num] )


        zipped_list = zip( *unzipped_list )


        if remain_incomplete_group:
            all_members_num = len(zipped_list) * group_members_num
            if all_members_num < len(list_):
                zipped_list.append( list_[ all_members_num: ] )


        return zipped_list
    # ~~~~~~~~~~~~~~ <<<<<<<<<<< ~~~~~~~~~~~~~~ #



    # ~~~~~~~~~~~~~~~~ >>>>>>>> ~~~~~~~~~~~~~~~ #
    # Calculate
    def sum( self, setized=False ):
        """
        Args:
            setized (bool, optional): Convert result list to set, then convert it back to list. 
                                        Defaults to False.

        Returns:
            [empty list]: [description]
            [list]:     if type of element in input list is sequence (list, set).
            [dict]:     if type of element in input list is dictionary.
            [int]:      if type of element in input list is integer.
            [float]:    if type of element in input list is float.

        Examples:
            L_( ['a','_b', '_c'] ).sum()
                # ['a', '_', 'b', '_', 'c']
                # If you want to combine strings, you should use ''.join( list of str )
            L_([ ['a'], ['_b'], ['_c'] ]).sum()
                # ['a', '_b', '_c']
            L_( [ (1,2,3), (4,5,6), (7,8,9) ] ).sum()
                # [1, 2, 3, 4, 5, 6, 7, 8, 9]
            L_( [ {1:2}, {2:3, 4:5}, {1:-1} ] ).sum()
                # {1: -1, 2: 3, 4: 5}
                # NOTE: For duplicated items, the last will replace the former.
        """
        list_ = self.list_

        if not list_:
            return []


        if isSequence( list_[0] ):
            new_list = list( itertools.chain.from_iterable( list_ ) )

            if setized:
                new_list = list(set( new_list ))

            return new_list


        elif type(list_[0]) is dict:
            sum_items = List([ i.items() for i in list_ ]).sum()
            return dict( sum_items )


        elif type(list_[0]) is int:
            return sum( list_ )


        elif type(list_[0]) is float:
            return sum( list_ )

        '''
        # another way
        reduce( lambda x,y: x+y, list_ )
        '''


    def round( self, digits_num, as_tuple=False ):
        '''
        Examples:
                List([ 1.42371522398, 2.4232157841, 3.1471214895, 4.157495157432 ]).round()
                    RETURNS: [1.42372, 2.42322, 3.14712, 4.1575]
        '''
        rounded_list = map( lambda x : round(x, digits_num), self.list_ )
        if as_tuple:
            return tuple( rounded_list )
        else:
            return rounded_list 
    # ~~~~~~~~~~~~~~ <<<<<<<<<<<< ~~~~~~~~~~~~~ #



    # ~~~~~~~~~~~~~ >>>>>>>>>>>>> ~~~~~~~~~~~~~ #
    # Padding
    def _just( self, num, var, direction ):
        list_ = list(self.list_)

        complement_list = [var] * max( num - len(list_), 0 )

        if direction == 'right':
            return complement_list + list_
        else: # direction == 'left'
            return list_ + complement_list


    def rjust( self, num, var ):
        return self._just( num, var, 'right' )


    def ljust( self, num, var ):
        return self._just( num, var, 'left' )
    # ~~~~~~~~~~~~~~ <<<<<<<<<<<< ~~~~~~~~~~~~~ #



    # ~~~~~~~~~~~~~~~~ >>>>>>> ~~~~~~~~~~~~~~~~ #
    # Set : Combinations, Permutations
    def combinations( self, num ):
        return [ i for i in itertools.combinations( self.list_, num ) ]

    def permutations( self, num ):
        return [ i for i in itertools.permutations( self.list_, num ) ]
    # ~~~~~~~~~~~~~~ <<<<<<<<<<<< ~~~~~~~~~~~~~ #


    def inStr( self, string ):

        check_list = self.list_

        check_list_1_char =         [ i for i in check_list if i.__len__() == 1 ]
        check_list_multi_chars =    [ i for i in check_list if i.__len__() > 1 ]

        string_list = list( string )


        # in string ?
        check_list_1_char = tuple( set(check_list_1_char) & set(string_list) )
        check_list_multi_chars = tuple([ i for i in check_list_multi_chars if i in string ])


        return check_list_1_char + check_list_multi_chars


    def setized( self ):
        hashized_list = []
        for i in self.list_:

            if isinstance( i, list ):
                i = tuple(i)

            hashized_list.append( i )

        return list(set( hashized_list ))


    def pruneNull( self ):
        return [ i for i in self.list_ if i ]
    strip = pruneNull


    def filter( keywords=None ):
        the_list = self.list_

        # pre-processing keywords
        keywords = [ i.lower() for i in keywords ]


        # initialize filtered list
        list_filtered = the_list


        # filtering
        if keywords:

            temp_list = []

            for each in list_filtered:
                if [ i for i in keywords if i in each.lower() ]:
                    temp_list.append( each )

            list_filtered = temp_list


        # excluded list
        list_excluded = [ i for i in the_list if i not in list_filtered ]


        return list_filtered, list_excluded



    # ~~~~~~~~~~~~~~~ >>>>>>>>> ~~~~~~~~~~~~~~~ #
    # Easy-to-use

    @staticmethod
    def inList( self, list_ ):
        '''
        Examples:
            from sepy.base import L
            hou.Node.inList = L.inList
        '''
        list_.append( self )
        return list_
    # ~~~~~~~~~~~~~~~~ <<<<<<< ~~~~~~~~~~~~~~~~ #

L_ = List









###########################################################################
################################### Dict ##################################
###########################################################################
'''
Mapping Types       https://docs.python.org/2/library/stdtypes.html#mapping-types-dict
    .clear()        # Remove all items from the dictionary.
'''

class Dict( object ):

    def __init__( self, dict_ ):
        if dict_ is None:
            self.dict_ = {}
        else:
            self.dict_ = dict_


    # get     https://docs.python.org/2/library/stdtypes.html#dict.get
    # def get( self, key ):
    #     if key not in self.dict_.keys():
    #         return None
    #     else:
    #         return self.dict_[key]

    def sat( self, key, value ):
        self.dict_[key] = value
        return self.dict_


    def itemsUnzipped( self ):
        '''
        Examples:
                D_({ 1: [2, 3], 2: [7, 10] }).itemsUnzipped()
                    RETURNS: [(1, 2), (1, 3), (2, 7), (2, 10)]
        '''
        pairs = []
        for key, value in self.dict_.items():
            if isSequence(value):
                pairs += zip( [key]*len(value), value )
            else:
                pairs.append( (key, value) )

        return pairs

    def itemsUnzippedReversed( self ):
        '''
        Examples:
                D_({ 1: [2, 3], 2: [7, 10] }).itemsUnzippedReversed()
                    RETURNS: [(2, 1), (3, 1), (7, 2), (10, 2)]
        '''
        pairs = self.itemsUnzipped()
        pairs_reversed = []
        for a, b in pairs:
            pairs_reversed.append( (b, a) )

        return pairs_reversed


    @staticmethod
    def fromZipped( list_ ):
        '''
        Examples:
                Dict.fromZipped( [ (1,2), (1,3), (2,7), (2,10) ] )
                    RETURNS: { 1: [2, 3], 2: [7, 10] }
        '''

        # Unlike in Python 2, the zip function in Python 3 returns an iterator.
        # Iterators can only be exhausted (by something like making a list out of them) once. 
        # The purpose of this is to save memory by only generating the elements of the iterator as you need them, 
        # rather than putting it all into memory at once.
        # If you want to reuse your zipped object, just create a list out of it.
        if not list_:
            return
        
        keys, values = list(zip( *list_ ))
        keys = set( keys )

        # initialize the dictionary with empty list
        dict_ = dict( [ (i,[]) for i in keys ] )
        # fill in the dictionary
        for i,j in list_:
            dict_[i].append(j)

        return dict_


    def reverse( self ):
        sample_value = self.dict_[ self.dict_.keys()[0] ]

        if isSequence(sample_value):
            '''
            e.g.    D_({1:['a','b'], 2:['b','c']}).reverse()
                        RETURN: {'a': 1, 'c': 2, 'b': 2}        # repeated value will be override
            '''
            return dict([ (i[1], i[0]) for i in self.itemsUnzipped() ])
        
        else: # value is not a list.
            '''
            e.g.    D_({1:'a', 2:'b', 3:'a'}).reverse()
                        RETURN: {'a': 3, 'b': 2}        # repeated value will be override
            '''
            return { j:i for i,j in self.dict_.items() }


    def pruneNull( self ):
        '''
        Delete empty keys.

        Examples:
                test = { 'a':'aaa', 'b':None, 'c':'ccc' }
                Dict( test ).pruneNull()
                test
                        RETURNS: {'a': 'aaa', 'c': 'ccc'}
        '''
        nulls = [ i[0] for i in self.dict_.items() if not i[1] ]
        for key in nulls:
            del self.dict_[key]

        return self.dict_
    strip = pruneNull


    def rebuildKeysAsIndex( self ):
        '''
        Examples:
                Dict( { 'a':'aaa', 'b':'bbb', 'c':'ccc' } ).rebuildKeysAsIndex()
                    RETURNS: {0: 'aaa', 1: 'bbb', 2: 'ccc'}
        '''
        items = self.dict_.items()
        items.sort( key=lambda x: x[0] )
        items = [ (i[0], i[1][1]) for i in enumerate( items ) ]
        return dict( items )


    def flatten( self ):
        '''
        Examples:
                Dict({1:'a', 2:'b', 3:'c'}).flatten()
                    RETURN: ['a', 'b', 'c']
        '''
        return self.dict_.values()

D_ = Dict









