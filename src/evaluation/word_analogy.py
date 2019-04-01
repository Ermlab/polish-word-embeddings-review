import logging
import os

import coloredlogs
from gensim.models import KeyedVectors


class WordAnalogyW2VFormat:
    """
    Class for evaluation of embeddings using gensim.

    Parameters
    ----------
    input_paths: str
        Input path or directory
    path_to_analogy: str
        Path to question words file with analogys
    """

    def __init__(self, input_paths: str, path_to_analogy: str):
        if os.path.isdir(input_paths):
            self.paths = [os.path.join(input_paths, path) for path in os.listdir(input_paths) if
                          path.endswith('.txt')]
        else:
            self.paths = [os.path.abspath(input_paths)]

        self.path_to_analogy = os.path.abspath(path_to_analogy)
        self.logger = self.__init_logger()

    def evaluate(self):
        """
        Evaluate every embedding in self.paths. Logs Path of embedding, Vocab and vector size, total and each section accuracy
        """
        for path in self.paths:
            model = KeyedVectors.load_word2vec_format(path)
            analogy = model.evaluate_word_analogies(self.path_to_analogy)

            self.logger.info(f'\nPath: {path}')
            self.logger.info(f'Vocab size = {len(model.vocab)}')
            self.logger.info(f'Vector size = {model.vector_size}')
            self.logger.info(f"Word analogies accuracy: {analogy[0]}\n")

            for item in analogy[1]:
                sum_of_samples = (len(item['correct']) + len(item['incorrect']))
                if sum_of_samples == 0:
                    continue
                acc = round((len(item['correct']) / sum_of_samples) * 100, 2)

                self.logger.info(f"Section: {item['section']}")
                self.logger.info(f"Acc: {acc}")

    @staticmethod
    def __init_logger(path_to_logger: str = '../data/w2v.log') -> logging.Logger:
        """
        Logger initializer


        Parameters
        ----------
        path_to_logger: str
            path where to save logs

        Return
        ------

        """
        formatter = logging.Formatter('%(message)s')
        fh_logger_path = os.path.abspath(path_to_logger)

        log_level = os.getenv("LOG_LEVEL", "INFO")
        log_level = 'CRITICAL' if log_level == 'false' else log_level

        coloredlogs.install(level=log_level)

        logger = logging.getLogger('WordEmbeddingLogger')
        fh_logger = logging.FileHandler(filename=fh_logger_path, mode='a+')
        fh_logger.setFormatter(formatter)
        logger.addHandler(fh_logger)
        return logger
