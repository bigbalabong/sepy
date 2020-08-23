'''
Tier: Base
'''

from .MBase import *
from .MData import *


'''
os - Files and Directories                  https://docs.python.org/2/library/os.html#files-and-directories
shutil - Directory and files operations     https://docs.python.org/2/library/shutil.html#directory-and-files-operations
'''




class File( object ):

    Temp_Folders = ( 
                        '_bak', '_reg', '_test',
                        '.vscode', '__pycache__', 
                        '.mayaswatches', 
                    )

    Code_Hints = {
                    'VEX' : {
                            'start_hints': ( 
                                    'void',
                                    'int',      'float',    'vector',   'string',
                                    'int[]',    'float[]',  'vector[]', 'string[]',
                                    'matrix',   'matrix3',
                                ),
                            'end_hints': (
                                '){\n',
                                )
                        }
                }



    # ======================================================== #
    # ====================== Initialize ====================== #
    # ======================================================== #
    def __init__(self, filepath, size_unit='MB', new_file=False ):
        
        # if not exist, create new file
        if new_file and not os.path.exists( filepath ):
            with open( filepath, 'w' ) as f:
                f.write('')

        # ifInvalid( os.path.exists( filepath ), "The file path dosn't exist." )

        filepath = S_(filepath).normpath()

        self.Path = filepath

        self.getFilepathInfo()

        self.getFilenameInfo()

        self.Valid = os.path.exists( filepath )

        if self.Valid:
            self.getFilesize( size_unit )
    

    def getFilepathInfo( self ):
        '''
        self.IsFile (bool)
        self.IsDir (bool)

        self.Bak (str)
        self.IsBak (bool)

        self.Root (str)
        self.Folder (str)
        self.Basename (str)
        self.Filename (str)
        self.Ext (str)
        '''
        filepath = self.Path

        self.IsFile = os.path.isfile( filepath )
        self.IsDir = os.path.isdir( filepath )           

        self.Bak = S_(filepath).search2( 'bak suffix' )
        self.IsBak = bool(self.Bak)


        if self.IsBak:
            filepath = filepath.rsplit('.',1)[0]


        if self.IsFile or self.IsDir:                           
            self.Root = os.path.dirname( filepath )             
            self.Folder = os.path.basename( self.Root )         
            self.Basename = os.path.basename( filepath )        

            if self.IsFile:
                self.Filename, ext = [ os.path.basename( i ) for i in os.path.splitext( filepath ) ]    
                self.Ext = ext.lower()
            else: # self.IsDir:
                self.Filename = self.Basename
                self.Ext = None

        else:              
            self.Root = self.Folder = self.Ext = None
            self.Basename = self.Filename = filepath


    def getFilenameInfo( self ):
        filename = self.Filename

        self.Author = S_(filename).search2( 'author' )


        midfix, suffix = self._getSuffix( filename )
        prefix, midfix = self._getPrefix( midfix )

        self.Prefix = prefix
        self.Midfix = midfix
        self.Suffix = suffix

    def _getPrefix( self, string ):
        prefix_list = []


        # letters + digits
        prefix = S_(string).search2( 'letters digits prefix' )
        if prefix and prefix != string:
            prefix_list.append( prefix )
            string = string.split(prefix, 1)[1]         


        return prefix_list, string

    def _getMidfix( self, midfix, anyfix ):
        # seps = ( '_', '-' )

        # if midfix.startswith( anyfix ):
        #     midfix = midfix.split( anyfix, 1 )[1].strip()

        #     if midfix[0] in seps:
        #         midfix = midfix[1:].strip()

        # if midfix.endswith( anyfix ):
        #     midfix = midfix.rsplit( anyfix, 1 )[0].strip()

        #     if midfix[-1] in seps:
        #         midfix = midfix[:-1].strip()

        # return midfix
        pass

    def _getSuffix( self, string ):
        self.DigitsSuffix = None
        suffix_list = []


        # _files
        _files = S_(string).search( '_files', from_end=True )
        if _files:
            suffix_list.append( _files )
            string = string.rsplit(_files, 1)[0]


        # underscore
        underscore = S_(string).search2( 'underscore suffix' )
        if underscore:
            suffix_list.append( underscore )
            string = string.rsplit(underscore, 1)[0]


        # digits
        digits = S_(string).search2( 'digits suffix' )
        if digits:
            self.DigitsSuffix = S_(digits).search2( 'digits suffix number' )
            suffix_list.append( digits )
            string = string.rsplit(digits, 1)[0]


        suffix_list.reverse()
        return string, suffix_list


    def getFilesize( self, size_unit='GB' ):
        '''
        PARMS:
                unit (str)  -  'KB' / 'MB' / 'GB'
        '''
        self.Size = self.SizeStr = size = None
        self.SizeUnit = size_unit.upper()


        if self.IsFile:
            size = os.path.getsize( self.Path )

        elif self.IsDir:
            file_list = File.allFiles( self.Path, subfolder=True )
            size = sum( [ os.path.getsize( i ) for i in file_list ] )

        if size is not None:
            exp = {'KB': 1, 'MB': 2, 'GB': 3}[ self.SizeUnit ]
            size = float(size) / pow(1024, exp)
            size = round( size, 3 )
            self.Size = size
            self.SizeStr = '{} {}'.format( self.Size, self.SizeUnit )



    @property
    def Name( self ):
        return self.Filename

    @Name.setter
    def Name( self, new_name ):
        self.rename( new_name )
        return new_name





    # ======================================================== #
    # ====================== List Files ====================== #
    # ======================================================== #
    @staticmethod
    def allFiles( folderpath, subfolder=False, 
                    include_files=None, exclude_files=None,
                    include_folders=None, exclude_folders=None,
                    include_ext=None, exclude_ext=None,
                    as_dict=False, caseSensitve=False ):
        """
        List all files.

        Args:
            folderpath (str): Single folder path or multiple folder paths.
            subfolder (bool, optional): Recursively list all files. Defaults to False.

            include_ext (list of str, optional): These types of files will be included. 
                                                    Defaults to None.
                                                    e.g. [ '.fbx', '.tga', '.py' ]
            exclude_ext (list of str, optional): These types of files will be excluded. 
                                                    Defaults to None.
                                                     e.g. [ '.html', '.exe', '.7z' ]

            as_dict (bool, optional): Return dictionary of files. Basename as key. Filepath as value. Defaults to False.
            caseSensitve (bool, optional): [description]. Defaults to False.

        Returns:
            [type]: [description]

        Author: Sean
        """
        # get list of folder paths
        folderpaths = S_(folderpath).normpath( validation=True, is_dir=True )
        folderpaths = L_(folderpaths).list_


        # ~~~~~~~~~~~~~~~ list files ~~~~~~~~~~~~~~ #
        all_files = []

        for folderpath in folderpaths:
            # Recursively list all files.
            if subfolder:
                for root, dirs, files in os.walk( folderpath ):
                    all_files += [ S_(os.path.join( root, i )).normpath() for i in files ]

            # just files in input folder paths.
            else:
                files = [ S_(os.path.join( folderpath, i )).normpath() for i in os.listdir( folderpath ) ]
                files = [ i for i in files if os.path.isfile(i) ]
                files.sort()
                all_files += files


        if include_folders:
            include_folders = [ '/{}/'.format( i.lower() ) for i in include_folders ]

            included_files = []
            for filepath in all_files:
                for include_folder in include_folders:
                    if include_folder in filepath.lower():
                        included_files.append( filepath )

            all_files = list(set(included_files))


        if exclude_folders:
            exclude_folders = [ '/{}/'.format( i.lower() ) for i in exclude_folders ]

            excluded_files = []
            for filepath in all_files:
                for exclude_folder in exclude_folders:
                    if exclude_folder in filepath.lower():
                        excluded_files.append( filepath )

            all_files = [ i for i in all_files if i not in excluded_files ]
            

        if include_files:
            include_files = [ i.lower() for i in include_files ]
            all_files = [ i for i in all_files if os.path.basename(i).lower() in include_files ]

        if exclude_files:
            exclude_files = [ i.lower() for i in exclude_files ]
            all_files = [ i for i in all_files if os.path.basename(i).lower() not in exclude_files ]


        if include_ext:
            include_ext = [ i.lower() for i in include_ext ]
            all_files = [ i for i in all_files if os.path.splitext(i)[1].lower() in include_ext ]

        if exclude_ext:
            exclude_ext = [ i.lower() for i in exclude_ext ]
            all_files = [ i for i in all_files if os.path.splitext(i)[1].lower() not in exclude_ext ]


        if not as_dict:
            return all_files


        # The returned files dictionary could be used to find same files in different folders.
        if not caseSensitve:
            all_files = [ i.lower() for i in all_files ]            


        # build dictionary
        all_files = D_.fromZipped([ (os.path.basename(i), i) for i in all_files ])

        return all_files


    @staticmethod
    def allFolders( folderpath, subfolder=False ):
        # pre-processing arguments
        folderpaths = S_(folderpath).normpath( validation=True, is_dir=True )
        folderpaths = L_(folderpaths).list_


        # list folders
        folder_list = []

        for folderpath in folderpaths:
            if subfolder:
                for root, dirs, files in os.walk( folderpath ):
                    folder_list += [ S_(os.path.join( root, i )).normpath() for i in dirs ]

            else:
                folders = [ os.path.join( folderpath, i ) for i in os.listdir( folderpath ) ]
                folders = [ i for i in folders if os.path.isdir(i) ]
                folders.sort()
                folder_list += folders


        return folder_list







    # ======================================================== #
    # ================= Basic File Operations ================ #
    # ======================================================== #
    @staticmethod
    def newFolder( folderpath ):
        try:
            os.makedirs( folderpath )
        except:
            pass

        ifInvalid( os.path.exists( folderpath ), 'Folder creation failed.' )

        return folderpath


    def delete( self, force=False ):
        if self.IsFile:
            os.remove( self.Path )

        elif self.IsDir:
            files = File.allFiles( self.Path, subfolder=True )

            ifValid( files and not force, 'This folder is not empty.' )

            shutil.rmtree( self.Path )


    def move( self, dst, replace=False,  ):
        src = self.Path
        dst = os.path.abspath( dst )


        if not os.path.exists( dst ):
            os.makedirs( dst )


        if not os.path.isdir( dst ):
            logging.error( 'Destination path is invalid.' )
            return


        if os.path.normpath( self.Root ) == os.path.normpath( dst ):
            p('\n Source path is same with destination path.')
            return


        dst = os.path.join( dst, self.Basename )

        if os.path.exists( dst ) and not replace:
            p('\n File already exits. Stop moving.\t{}'.format( self.Basename ))
            return

        shutil.move( src, dst )
    

    def copy( self, dst, new_name=None, force=True ):
        """[summary]

        Args:
            dst (str): Destination folder.
            
            new_name (str, optional): Copy file with a new name. Defaults to None.
            
            force (bool, optional): 
                    If source is a file and force is true, destination file would be replaced if it exists. 
                    Otherwise raise exception.
                    If source is a folder and force is true, destination folder would be pre-delete if it exists.
                    Otherwise copy operation would be failed.
                    Defaults to True.

        Returns:
            [str]: Copied file path.
        """
        if new_name:
            fullpath = os.path.join( dst, new_name )
        else:
            fullpath = os.path.join( dst, self.Basename )


        # copy operation
        if self.IsFile:
            '''
            shutil.copy         https://docs.python.org/2/library/shutil.html#shutil.copy
                    Copy the file src to the file or directory dst. 
                    If dst is a directory, a file with the same basename as src is created (or overwritten) in the directory specified.
            shutil.copy2        https://docs.python.org/2/library/shutil.html#shutil.copy2
                    Identical to copy() except that copy2() also attempts to preserve file metadata.
            shutil.copyfile     https://docs.python.org/2/library/shutil.html#shutil.copyfile
                    Copy the contents (no metadata) of the file named src to a file named dst. 
                    dst must be the complete target file name; 
                    look at shutil.copy() for a copy that accepts a target directory path.
            '''
            if not force:
                if os.path.exists( fullpath ):
                    raise Exception( 'Destination path already exists.' )


            # create folder if necessary
            if not os.path.exists( dst ):
                os.makedirs( dst )


            # copy file. and if destination path exists, replace it.
            shutil.copyfile( self.Path, fullpath )

        else: # self.IsDir
            '''
            shutil.copytree     https://docs.python.org/2/library/shutil.html#shutil.copytree
                    Recursively copy an entire directory tree rooted at src. 
                    The destination directory, named by dst, must not already exist; 
                    it will be created as well as missing parent directories.
            shutil.rmtree       https://docs.python.org/2/library/shutil.html#shutil.rmtree
            '''
            # destination path can't exist. otherwise, it would fail.

            if force and os.path.exists( fullpath ):
                # delete destination folder
                shutil.rmtree( fullpath )

            # copy folder
            shutil.copytree( src=self.Path, dst=fullpath )


        return fullpath


    def rename( self, new_name, correct_terms=False ):
        '''
        os.rename       https://docs.python.org/2/library/os.html?highlight=os#os.rename
        os.renames      https://docs.python.org/2/library/os.html?highlight=os#os.renames
        '''
        new_name = self._correctTerms( new_name ) if correct_terms else new_name

        src = self.Path
        dst = os.path.join( self.Root, new_name )

        if self.IsFile:
            dst += self.Ext

            try:
                os.rename( src, dst )
                self.Path = dst
            except:
                p( ' Rename failed. New name file exists. \t >> \t', self.Basename )

        elif self.IsDir:
            if not os.path.exists( dst ):
                shutil.move( src, dst )

            else:
                files = [ os.path.join( src, i ) for i in os.listdir( src ) ]
                for i in files:
                    try:
                        shutil.move( i, dst )
                    except:
                        continue

            self.Path = dst

        else:
            self.Basename = new_name

        return dst


    def renameTemp( self ):
        temp_name = '__temp_{}'.format( I_.rand(b=100000) )
        return self.rename( temp_name )


    def _correctTerms( self, string ):

        string_list = string.split()

        string_lower = string.lower()
        string_lower_list = string_lower.split()
        
        terms = term_dict.keys()
        keys.reverse()
        for key in keys:
            if key in name_low:
                slice_start = name_low.index( key )
                slice_end = slice_start + key.__len__()

                part0 = name[:slice_start]
                part1 = name[slice_end:]
                name = part0 + abbrBase[key] + part1        # replace with abbreviation
                
                name_low = name.lower()             # update




    # ======================================================== #
    # ======================== Backup ======================== #
    # ======================================================== #
    def backup( self, temp_folder=False ):
        if not self.IsFile:
            return

        # backup folder path
        if temp_folder:
            bak_root = os.path.join( os.environ['TMP'], '_bak' )
        else:
            bak_root = os.path.join( self.Root, '_bak' )

        # create backup folder if necessary
        if not os.path.exists( bak_root ):
            os.mkdir( bak_root )

        existing_bak_files = [ i for i in os.listdir( bak_root ) if '.bak' in i ]
        existing_bak_files = [ i for i in existing_bak_files if self.Basename == i.rsplit('.bak')[0] ]
        existing_bak_files = [ i for i in existing_bak_files if i.rsplit('.bak')[1].isdigit() ]

        if existing_bak_files:
            # e.g. re.search( r'\d+\Z', 'cube__QA.mb.bak14' ).group()   # RETURNS: '14'
            bak_index = max( [ int(re.search( r'\d+\Z', i ).group()) for i in existing_bak_files ] ) + 1
        else:
            bak_index = 1


        # backup file
        bak_path = self.copy( bak_root, '{}.bak{}'.format( self.Basename, bak_index ) )

        return bak_path
    
    def latestBak( self, temp_folder=False ):

        if not self.IsFile:
            return


        # backup folder path
        if temp_folder:
            bak_root = os.path.join( os.environ['TMP'], '_bak' )
        else:
            bak_root = os.path.join( self.Root, '_bak' )


        if not os.path.exists( bak_root ):
            return


        # get all bak files
        existing_bak_files = [ i for i in os.listdir( bak_root ) if i.rsplit('.bak')[0] == self.Basename ]


        if not existing_bak_files:
            return


        # get latest bak file
        existing_bak_files.sort( key=lambda x: int(re.search( r'\d+\Z', x ).group()) )
        latest_bak_file = existing_bak_files[-1]


        return os.path.join( bak_root, latest_bak_file )

    def restore( self ):
        pass





    # ======================================================== #
    # ======================= Contents ======================= #
    # ======================================================== #
    @property
    def Data( self ):
        return FileData( self.Path )

    @property
    def data( self ):
        return self.Data.data




    # ======================================================== #
    # ======================== Search ======================== #
    # ======================================================== #
    @staticmethod
    def search( folderpath, keywords ):
        path = '{}\{}'.format( folderpath, keywords )

        results = glob.glob( path )
        results = [ os.path.join( folderpath, i ).replace('\\','/') for i in results ]
        results.sort( key = lambda x: ( os.path.isfile(x), x.lower() ) )

        return results
    

    def findSame( self, folderpath ):
        filename = self.Basename

        folderpaths = S_(folderpath).normpath( validation=True, is_dir=True )
        folderpaths = L_(folderpaths).list_

        search_results = []
        for folderpath in folderpaths:
            search_path = '{}\*\{}'.format( folderpath, filename )
            search_result = glob.glob( search_path ) 
            search_results += search_result

        return search_results




class FileData( object ):

    def __init__( self, filepath ):
        self.Path = filepath

    @property
    def Data( self ):
        """
        'r'     read only (default)
        'w'     write only
        'a'     append
        'r+'    read and write

        (On Windows, 'b' appended to the mode opens the file in binary mode.)
        'rb'
        'wb'
        'r+b'

        References:
            https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
        """
        with open( self.Path, 'r' ) as f:
            data = f.read()
        
        return data        

    @Data.setter
    def Data( self, data ):
        with open( self.Path, 'w' ) as f:
            f.write( data )


    def append( self, datas ):
        datas = L_(datas).list_

        new_data = self.Data
        for data in datas:
            new_data += data

        self.Data = new_data


    def insert( self, anchor_string, datas, end_of_line=False ):
        '''
        PARMS:
                anchor_string  -  the string which the data will be inserted after
        '''
        datas = L_(datas).list_
        new_data = ''
        for data in datas:
            new_data += data


        if end_of_line:
            with open( self.Path ) as f:
                line = ''
                while not line.startswith( anchor_string ):
                    line = f.readline()

            old_line = line.strip()
            new_line = old_line + new_data
            self.replace( old_line, new_line )


        else:
            old_data = self.Data
            part1, part2 = old_data.split( anchor_string, 1 )
            new_data = part1 + anchor_string + new_data + part2

            self.Data = new_data


    def replace( self, anchor_string, data ):
        old_data = self.Data
        part1, part2 = old_data.split( anchor_string, 1 )
        new_data = part1 + data + part2

        self.Data = new_data

    def replaceAll( self, anchor_string, data ):
        old_data = self.Data
        old_data_list = old_data.split( anchor_string )
        new_data = data.join( old_data_list )

        self.Data = new_data

    def replaceBlock( self, anchor_string_start, anchor_string_end, data ):
        old_data = self.Data
        part1, part2 = old_data.split( anchor_string_start, 1 )
        useless, part2 = part2.split( anchor_string_end, 1 )
        new_data = part1 + data + part2

        self.Data = new_data


    ###########################################################################
    ############################## Parsing Codes ##############################
    ###########################################################################

    # ~~~~~~~~~~~~~~~~~~ VEX ~~~~~~~~~~~~~~~~~~ #
    def parseVexLib( self ):
        start_hints =   self.Code_Hints['VEX']['start_hints']
        end_hints =     self.Code_Hints['VEX']['end_hints']
        
        with open( self.Path ) as f:
            line = 'hello world ~'

            funcs = []
            docs = []

            check_doc_exists = False
            record_doc = False
            doc = ''

            while line:
                line = f.readline()
                
                if check_doc_exists:

                    if line.startswith( '    /*' ):
                        record_doc = True

                        doc = ''
                        # doc += line

                    else:
                        docs.append( "No doc string." )

                    check_doc_exists = False

                elif record_doc:

                    if line.startswith( '    */' ):
                        # doc += line
                        docs.append( doc )
                        doc = ''

                        record_doc = False

                    else:
                        doc += line

                else:
                    func_start = [ i for i in start_hints if line.startswith( i ) ]
                    func_end = [ i for i in end_hints if line.endswith( i ) ]
                    
                    if func_start and func_end:
                        func = line.split(' ', 1)[1]
                        func = func.split('(', 1)[0]

                        if func not in funcs:
                            funcs.append( func )

                            check_doc_exists = True


        

        funcs = zip( funcs, docs )
        funcs = dict( funcs )
        
        return funcs




    ###########################################################################
    ################################ Temp Funcs ###############################
    ###########################################################################
    def update_setAttr( self ):
        lines = self.Data.split('\n')
            
        new_data = []
        for line in lines:
            if not line.startswith( '#' ) and '=' in line:
                if 'property(' in line or 'staticmethod(' in line or 'classmethod(' in line:
                    name, value = [ i.strip() for i in line.split('=', 1) ]
                    name1, name2 = name.rsplit('.',1)
                    new_line = 'setAttr( {}, "{}", {} )'.format( name1, name2, value )
                    
                    print( '\n', line )
                    print( new_line )
                    new_data.append( new_line )

        new_data = '\n'.join( new_data )

        new_pyfile = File( r"D:\new_temp.py" )
        new_pyfile.Data.Data = new_data

        print( '\n   Processing Finished.' )








