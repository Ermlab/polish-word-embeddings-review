import argparse
import csv
import os
import sys
from typing import Dict, Generator

from evaluation.word_analogy import WordAnalogyW2VFormat

WORD_ANALOGY_CSV_PATH = os.path.abspath('../data/analogy.csv')
WORD_PAIRS_CSV_PATH = os.path.abspath('../data/word_pairs.csv')


def save_to_csv(dict_gen: Generator[Dict, None, None], path):
    with open(path, 'a+') as csv_file:
        data_to_save = list(dict_gen)
        keys_from_dict = list(data_to_save[0].keys())
        csv_writer = csv.DictWriter(csv_file, keys_from_dict)
        csv_writer.writeheader()
        csv_writer.writerows(data_to_save)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]),
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=__doc__)
    parser.add_argument('-i',
                        '--input',
                        type=str,
                        required=True,
                        help='Directory or Path to word2vec format file.')
    parser.add_argument('-a',
                        '--analogy-path',
                        type=str,
                        required=True,
                        help='Path to questions words file with analogy words.')
    parser.add_argument('-sp',
                        '--simlex-path',
                        type=str,
                        help='Path to SimLex File file with words pairs.')

    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    analogy_path = os.path.abspath(args.analogy_path)

    w2v_val = WordAnalogyW2VFormat(input_path, analogy_path)
    analogy_gen = w2v_val.evaluate_word_analogy()
    save_to_csv(analogy_gen, WORD_ANALOGY_CSV_PATH)

    if args.simlex_path:
        path_to_simlex = os.path.abspath(args.simlex_path)
        words_pairs = w2v_val.evaluate_word_pairs(path_to_simlex)
        save_to_csv(words_pairs, WORD_PAIRS_CSV_PATH)
