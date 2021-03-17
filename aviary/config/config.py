import json
import os
import sys
import signal

def handler(signum, frame):
     raise IOError
signal.signal(signal.SIGALRM, handler)


"""
Load the reference package. This will fail if the directory doesn't exist.
"""
def get_gtdb_path():
    try:
        GENERIC_PATH = os.environ['GTDBTK_DATA_PATH']
        return GENERIC_PATH
    except KeyError:
        print('\n' + '=' * 80)
        print(' ERROR '.center(80))
        print('_' * 80 + '\n')
        print("The 'GTDBTK_DATA_PATH' environment variable is not defined.".center(80) + '\n')
        print('Please set this variable to your reference data package.'.center(80))
        print('https://github.com/Ecogenomics/GTDBTk#installation'.center(80))
        print('Alternatively, use --gtdb-path flag.'.center(80))    
        print('=' * 80)
        signal.alarm(20)
        os.environ['GTDBTK_DATA_PATH'] = input('Input GTDBTK_DATA_PATH now:')
        signal.alarm(0)


"""
Set the default conda environment path.
"""
def get_conda_path():
    try:
        CONDA_PATH = os.environ['CONDA_ENV_PATH']
        return CONDA_PATH
    except KeyError:
        print('\n' + '=' * 80)
        print(' ERROR '.center(80))
        print('_' * 80 + '\n')
        print("The 'CONDA_ENV_PATH' environment variable is not defined.".center(80) + '\n')
        print('Please set this variable to your default server/home directory conda environment path.'.center(80))
        print('Alternatively, use --conda-prefix flag.'.center(80))    
        print('=' * 80)
        signal.alarm(20)
        os.environ['CONDA_ENV_PATH'] = input('Input CONDA_ENV_PATH now:')
        signal.alarm(0)
