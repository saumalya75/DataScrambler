from datetime import datetime
import ExecUtil as eu

DATE_SCRAMBLE_FLAG = eu.DATE_SCRAMBLE_FLAG or False
DATE_FOMARTS = [
    {'TYPE': 'DT', 'FORMAT': '%Y%m%d%H%M%S'}
    , {'TYPE': 'DT', 'FORMAT': '%Y%m%d%I%M%S'}
    , {'TYPE': 'D', 'FORMAT': '%Y%m%d'}
	
    # , {'TYPE': 'D', 'FORMAT': '%d-%m-%Y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d-%m-%Y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d-%m-%Y %I:%M:%S'}
    , {'TYPE': 'D', 'FORMAT': '%m-%d-%Y'}
    , {'TYPE': 'DT', 'FORMAT': '%m-%d-%Y %H:%M:%S'}
    , {'TYPE': 'DT', 'FORMAT': '%m-%d-%Y %I:%M:%S'}
    # , {'TYPE': 'D', 'FORMAT': '%d-%m-%y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d-%m-%y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d-%m-%y %I:%M:%S'}
    # , {'TYPE': 'D', 'FORMAT': '%m-%d-%y'}
    # , {'TYPE': 'DT', 'FORMAT': '%m-%d-%y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%m-%d-%y %I:%M:%S'}
    
	# , {'TYPE': 'D', 'FORMAT': '%d/%m/%Y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d/%m/%Y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d/%m/%Y %I:%M:%S'}
    , {'TYPE': 'D', 'FORMAT': '%m/%d/%Y'}
    , {'TYPE': 'DT', 'FORMAT': '%m/%d/%Y %I:%M:%S'}
    , {'TYPE': 'DT', 'FORMAT': '%m/%d/%Y %H:%M:%S'}
    # , {'TYPE': 'D', 'FORMAT': '%d/%m/%y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d/%m/%y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d/%m/%y %I:%M:%S'}
    # , {'TYPE': 'D', 'FORMAT': '%m/%d/%y'}
    # , {'TYPE': 'DT', 'FORMAT': '%m/%d/%y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%m/%d/%y %I:%M:%S'}
    
	# , {'TYPE': 'D', 'FORMAT': '%d %m %Y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %m %Y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %m %Y %I:%M:%S'}
    # , {'TYPE': 'D', 'FORMAT': '%m %d %Y'}
    # , {'TYPE': 'DT', 'FORMAT': '%m %d %Y %I:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%m %d %Y %H:%M:%S'}
    # , {'TYPE': 'D', 'FORMAT': '%d %m %y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %m %y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %m %y %I:%M:%S'}
    # , {'TYPE': 'D', 'FORMAT': '%m %d %y'}
    # , {'TYPE': 'DT', 'FORMAT': '%m %d %y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%m %d %y %I:%M:%S'}
	
    # , {'TYPE': 'D', 'FORMAT': '%d-%B-%Y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d-%B-%Y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d-%B-%Y %I:%M:%S'}
    # , {'TYPE': 'D', 'FORMAT': '%d-%B-%y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d-%B-%y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d-%B-%y %I:%M:%S'}
    
	# , {'TYPE': 'D', 'FORMAT': '%d/%B/%Y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d/%B/%Y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d/%B/%Y %I:%M:%S'}
    # , {'TYPE': 'D', 'FORMAT': '%d/%B/%y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d/%B/%y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d/%B/%y %I:%M:%S'}
    #
	# , {'TYPE': 'D', 'FORMAT': '%d %B %Y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %B %Y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %B %Y %I:%M:%S'}
    # , {'TYPE': 'D', 'FORMAT': '%d %B %y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %B %y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %B %y %I:%M:%S'}
	
    , {'TYPE': 'D', 'FORMAT': '%d-%b-%Y'}
    , {'TYPE': 'DT', 'FORMAT': '%d-%b-%Y %H:%M:%S'}
    , {'TYPE': 'DT', 'FORMAT': '%d-%b-%Y %I:%M:%S'}
    , {'TYPE': 'D', 'FORMAT': '%d-%b-%y'}
    , {'TYPE': 'DT', 'FORMAT': '%d-%b-%y %H:%M:%S'}
    , {'TYPE': 'DT', 'FORMAT': '%d-%b-%y %I:%M:%S'}
    
	, {'TYPE': 'D', 'FORMAT': '%d/%b/%Y'}
    , {'TYPE': 'DT', 'FORMAT': '%d/%b/%Y %H:%M:%S'}
    , {'TYPE': 'DT', 'FORMAT': '%d/%b/%Y %I:%M:%S'}
    , {'TYPE': 'D', 'FORMAT': '%d/%b/%y'}
    , {'TYPE': 'DT', 'FORMAT': '%d/%b/%y %H:%M:%S'}
    , {'TYPE': 'DT', 'FORMAT': '%d/%b/%y %I:%M:%S'}
    #
	# , {'TYPE': 'D', 'FORMAT': '%d %b %Y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %b %Y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %b %Y %I:%M:%S'}
    # , {'TYPE': 'D', 'FORMAT': '%d %b %y'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %b %y %H:%M:%S'}
    # , {'TYPE': 'DT', 'FORMAT': '%d %b %y %I:%M:%S'}
]
DATE_PATTERNS = r'(^\d{8}$)|(^\d{14}$)|(^\d{2}[/-]\d{2}[/-]\d{4}\s\d{2}[:\s]\d{2}[:\s]\d{2}$)|(^\d{2}[/-][a-zA-Z]{3}[/-]\d{2,4})|(^\d{2}[/-][a-zA-Z]{3}[/-]\d{2,4}\s\d{2}[:\s]\d{2}[:\s]\d{2}$)'
LOG_TYPE = eu.LOG_TYPE or 'CONSOLE'


class Logger:

    def __init__(self, dest=eu.LOG_TYPE):
        self.dest = dest

    def write_log(self, class_name='MAIN', level='INFO', msg='Success'):
        log_dtime = datetime.now().strftime('%Y%m%d%H%M%S')
        log_msg = level + '::' + log_dtime + '::' + class_name + '::' + msg
        if self.dest == 'CONSOLE':
            print(log_msg)
        elif self.dest == 'FILE':
            with open(eu.LOG_DIR + '\\' + eu.LOG_FILE_PREFIX + '_' + eu.RUN_DATE_TIME + '.log', 'w') as f:
                f.write(log_msg)


if __name__ == '__main__':
    print(DATE_FOMARTS)
