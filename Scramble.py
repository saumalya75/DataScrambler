import scrambler.ScramblerUtil as su
from datetime import datetime
from dateutil.relativedelta import relativedelta
from scrambler.ScramblerUtil import Logger
import re
import sys

try:
    logger = Logger()
except Exception as e:
    print('Executor :: INFO :: Unexpected exception occurred. Returned Error: ' + str(e))
    sys.exit(1)


def _date_scramble(val):
    try:
        for dt_format in su.DATE_FOMARTS:
            try:
                if dt_format.get('TYPE', 'D') == 'D':
                    date_val = datetime.strptime(val, dt_format.get('FORMAT', '%d-%m-%Y')).date()
                elif dt_format.get('TYPE', 'D') == 'DT':
                    date_val = datetime.strptime(val, dt_format.get('FORMAT', '%d-%m-%Y'))
                elif dt_format.get('TYPE', 'D') == 'T':
                    date_val = datetime.strptime(val, dt_format.get('FORMAT', '%d-%m-%Y')).time()
                else:
                    raise ValueError

                date_val += relativedelta(days=1)
                date_val += relativedelta(months=1)
                date_val += relativedelta(years=1)
                return datetime.strftime(date_val, dt_format.get('FORMAT', '%d-%m-%Y'))
            except ValueError:
                pass
            except Exception as e:
                print(f"Date conversion failed for {val}. Error returned: " + str(e))
                sys.exit(1)

        return 0
    except Exception as e:
        logger.write_log('scramble.Scramble', 'ERROR', 'Unexpected exception occurred. Returned Error: ' + str(e))
        sys.exit(1)


def _str_scramble(val):
    try:
        if val == 'nan':
            return 'NA'
        else:
            if su.DATE_SCRAMBLE_FLAG and re.match(su.DATE_PATTERNS, val):
                date_val = _date_scramble(val)
                if date_val:
                    return date_val

            lst_char = []
            for char in val:
                if char == '9':
                    lst_char.append('0')
                elif char == 'z':
                    lst_char.append('a')
                elif char == 'Z':
                    lst_char.append('A')
                else:
                    lst_char.append(chr(ord(char) + 1))
            return ''.join(lst_char)
    except Exception as e:
        logger.write_log('scramble.Scramble', 'ERROR', 'Unexpected exception occurred. Returned Error: ' + str(e))
        sys.exit(1)


def _dec_scramble(val):
    try:
        if su.DATE_SCRAMBLE_FLAG and re.match(su.DATE_PATTERNS, val):
            date_val = _date_scramble(val)
            if date_val:
                return date_val
        lst_char = []
        if val[0] == '-' or val[0] == '+':
            char_cnt = -1
        else:
            char_cnt = 0

        for char in val:
            if char_cnt < 1:
                lst_char.append(char)
            elif char == '9':
                lst_char.append('0')
            elif char not in '012345678':
                lst_char.append(char)
            else:
                lst_char.append(chr(ord(char) + 1))
            char_cnt += 1
        return ''.join(lst_char)
    except Exception as e:
        logger.write_log('scramble.Scramble', 'ERROR', 'Unexpected exception occurred. Returned Error: ' + str(e))
        sys.exit(1)


def _channel(val):
    try:
        if type(val) != str:
            str_val = str(val)
        else:
            str_val = val

        clean_val = str_val.strip('"')
        if re.match(r'^-?[0-9\.]*$', clean_val):
            scrambled_val = _dec_scramble(clean_val)
        else:
            scrambled_val = _str_scramble(clean_val)

        if str_val[0] == '"':
            return '"' + scrambled_val + '"'
        else:
            return scrambled_val
    except Exception as e:
        logger.write_log('scramble.Scramble', 'ERROR', 'Unexpected exception occurred. Returned Error: ' + str(e))
        sys.exit(1)


def scramble(src_df, config):
    try:
        tgt_df = src_df.copy()
        for col in config.get('COLS_IN_SCOPE', src_df.columns):
            tgt_df[col] = src_df[col].apply(_channel)
        return tgt_df
    except Exception as e:
        logger.write_log('scramble.Scramble', 'ERROR', 'Unexpected exception occurred. Returned Error: ' + str(e))
        sys.exit(1)


# if __name__ == '__main__':
#     print('''This scripts will ask for two inputs during run time:
#     (Mandatory)
#     1: Pandas Data frame (with header),
#     (Optional)
#     2: config dict object containing at least "COLS_IN_SCOPE" key which contains the column list of the data frame on which scrambling will be executed. This is an optional argument.
#     This script will print out a pandas data frame containing scrambled data.
#     P.S. We recommend you to use this script as a module by importing it into your script.
#
#                             Happy Scrambling!!!''')
#
#     input_df = input("Please provide the pandas data frame: ")
#     config_dict = input("Please provide the config dictionary: ")
#     print(scramble(input_df, config_dict))
