import ExecUtil as eu
from scrambler.ScramblerUtil import Logger
import scrambler.Scramble as scram
import pandas as pd
import csv
import time

try:
    logger = Logger()
except Exception as e:
    print('Executor :: INFO :: Unexpected exception occurred. Returned Error: ' + str(e))
    sys.exit(1)


for config in eu.CONFIGURATION_SET:
    try:
        logger.write_log('Executor', 'INFO', f'Starting to scramble '+config['SRC']+'.')
        src_df = pd.read_csv(config['SRC'], sep=config.get('SRC_COL_DELIM', ','), dtype='object', quoting=3)
        logger.write_log('Executor', 'INFO', 'Source file - ' + config['SRC'] + ' is read.')
        old_headers = list(src_df.columns)
        new_headers = []
        for header in src_df.columns:  # data.columns is your list of headers
            header = header.strip('"')  # Remove the quotes off each header
            new_headers.append(header)  # Save the new strings without the quotes
        src_df.columns = new_headers  # Replace the old headers with the new list
        chunk_size = config.get('CHUNK_SIZE', 0)
        if not chunk_size:
            logger.write_log('Executor', 'INFO', f'Starting to apply scrambling algorithm on ' + config['SRC'] + '.')
            tgt_df = scram.scramble(src_df, config)
            logger.write_log('Executor', 'INFO', f'Scrambling algorithm is successfully applied on ' + config['SRC'] + '. Starting to write target file - ' + config['TGT'] + '.')
            tgt_df.to_csv(config['TGT'], sep=config.get('TGT_COL_DELIM', '~'), index=False, quoting=csv.QUOTE_NONE, header=old_headers)
            logger.write_log('Executor', 'INFO', f'Scrambled data is successfully written in target file - ' + config['TGT'] + '.')
            logger.write_log('Executor', 'INFO', f'Entire source file - ' + config['SRC'] + f' is scrambled at one go.')
        else:
            iter_count = 0
            max_iter = int(src_df.shape[0]/chunk_size)
            for i in range(max_iter + 1):
                lower_bound = i*chunk_size
                upper_bound = lower_bound + chunk_size
                iter_df = src_df[lower_bound:upper_bound].copy()
                logger.write_log('Executor', 'INFO', f'Starting to apply scrambling algorithm on {i}th slice of ' + config['SRC'] + '.')
                tgt_df = scram.scramble(iter_df, config)
                logger.write_log('Executor', 'INFO', f'Scrambling algorithm is successfully applied on {i}th slice of ' + config['SRC'] + '. Starting to write target file - ' + config['TGT'] + '.')
                if i == 0:
                    tgt_df.to_csv(config['TGT'], sep=config.get('TGT_COL_DELIM', '~'), index=False, quoting=csv.QUOTE_NONE, header=old_headers)
                    logger.write_log('Executor', 'INFO', f'Scrambled data is successfully appended in target file - ' + config['TGT'] + '.')
                else:
                    tgt_df.to_csv(config['TGT'], sep=config.get('TGT_COL_DELIM', '~'), mode='a', index=False, quoting=csv.QUOTE_NONE, header=False)
                    logger.write_log('Executor', 'INFO', f'Scrambled data is successfully appended in target file - ' + config['TGT'] + '.')

            logger.write_log('Executor', 'INFO', f'Entire source file - ' + config['SRC'] + f' is scrambled part by part in {max_iter + 1} iterations.')
            time.sleep(2)

    except Exception as e:
        logger.write_log('Executor', 'ERROR', 'Unexpected exception occurred. Returned Error: '+str(e))
        sys.exit(1)
