import os
import re
import csv
import argparse
import pandas as pd
from unidecode import unidecode
from nltk.tokenize import WhitespaceTokenizer


def is_valid_file(parser, arg):
    """
    ref: http://stackoverflow.com/questions/11540854/
    """
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')


def read_notes(file_name):
    """Read pathology report lines"""
    lines = [l for l in csv.reader(open(file_name, 'r'))][1::]
    lines_join = list(map(lambda text: unidecode(' '.join(text)), lines))
    return lines_join


def process_notes(line):
    """
    Split given string from text file with '|' separator
    format of given text is as follows
        id||date||||pathology text
    """
    splits = re.split('\|\|\|\|\|', line)
    idx = int(re.sub('\t', '', splits[0])) # identification number
    date = re.sub('\|', '', splits[1])
    contexts = ' '.join(splits[2::])
    contexts_tokenize = w_tokenizer.tokenize(contexts)
    return [idx, date, ' '.join(contexts_tokenize)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Progress note text parser")
    parser.add_argument('-i', '--input', dest='input', required=True,
                        help="input pathology file",
                        type=lambda x: is_valid_file(parser, x))
    parser.add_argument('-o', '--output', dest='output',
                        default='progress_notes_out.csv')

    args = parser.parse_args()

    print('read and process progress notes from %s' % args.input)
    progress_notes = read_notes(args.input)
    progress_notes_proc = list(map(process_notes, progress_notes))
    progress_notes_proc_df = pd.DataFrame(progress_notes_proc,
                                          columns=['identification', 'date', 'report'])
    print('process text documents and saved to %s' % args.output)
    progress_notes_proc_df.to_csv(args.output, index=False)
