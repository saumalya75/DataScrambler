from datetime import datetime

CONFIGURATION_SET = [
    {
        'SRC': r'E:\Python\ScramblerOfc\data\file_1_src.dat',
        'SRC_COL_DELIM': '\t',
        'TGT': r'E:\Python\ScramblerOfc\data\file_1_dest.dat',
        'TGT_COL_DELIM': '\t',
        'COLS_IN_SCOPE': ["COL_A", "COL_B", "COL_C", "COL_D"],
        'CHUNK_SIZE': 2
    }
    , {
        'SRC': r'E:\Python\ScramblerOfc\data\file_2_src.dat',
        'SRC_COL_DELIM': ',',
        'TGT': r'E:\Python\ScramblerOfc\data\file_2_dest.dat',
        'TGT_COL_DELIM': '\t',
        'COLS_IN_SCOPE': ["COL_A", "COL_B", "COL_C", "COL_D"]
    }
]
DATE_SCRAMBLE_FLAG = True
RUN_DATE_TIME = datetime.now().strftime('%Y%m%d%H%M%S')
LOG_TYPE = 'CONSOLE'
LOG_DIR = r'E:\Python\ScramblerOfc\log'
LOG_FILE_PREFIX = 'Scrambler_Log'


if __name__ == '__main__':
    print(CONFIGURATION_SET)
