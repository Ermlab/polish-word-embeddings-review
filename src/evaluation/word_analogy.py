import logging
import os

import coloredlogs
from gensim.models import KeyedVectors
from gensim.models.fasttext import FastText
from gensim.models.word2vec import Word2Vec


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
            self.paths = [
                os.path.join(input_paths, path)
                for path in os.listdir(input_paths)
                if path.endswith(".txt") or path.endswith(".bin")
            ]
        else:
            self.paths = [os.path.abspath(input_paths)]

        self.path_to_analogy = os.path.abspath(path_to_analogy)
        self.logger = self.__init_logger()

    def iter_models(self):
        for path in self.paths:
            if path.endswith(".txt"):
                model = KeyedVectors.load_word2vec_format(path)
            elif path.endswith(".bin"):
                model = KeyedVectors.load(path)
            else:
                self.logger.error("Wrong file extension. Should be .txt or .bin.")
                continue
            self.logger.info(f"\nPath: {path}")
            if not isinstance(model, FastText):
                self.logger.info(f"Vocab size = {len(model.wv.vocab)}")
            self.logger.info(f"Vector size = {model.vector_size}")
            yield model, path

    def evaluate_word_analogy(self, model, model_path, more_info=False):
        """
        Evaluate every embedding in self.paths. Logs Path of embedding, Vocab and vector size, total and each section accuracy
        """
        if isinstance(model, FastText):
            analogy = model.wv.evaluate_word_analogies(self.path_to_analogy)
            len_vocab = len(model.wv.vocab)
        else:
            analogy = model.evaluate_word_analogies(self.path_to_analogy)
            len_vocab = len(model.vocab)

        self.logger.info(f"Word analogies accuracy: {analogy[0]}\n")
        if more_info:
            for item in analogy[1]:
                sum_of_samples = len(item["correct"]) + len(item["incorrect"])
                if sum_of_samples == 0:
                    continue
                acc = round((len(item["correct"]) / sum_of_samples) * 100, 2)

                self.logger.info(f"Section: {item['section']}")
                self.logger.info(f"Acc: {acc}")

        return {
            "name": os.path.basename(model_path),
            "vocab": len_vocab,
            "vector": model.vector_size,
            "analogy acc": analogy[0],
        }

    def evaluate_word_pairs(self, model, model_path, path_to_simlex):
        """
        Evaluate word pairs
        """

        if isinstance(model, FastText) or isinstance(model, Word2Vec):
            similarity = model.wv.evaluate_word_pairs(path_to_simlex)
        else:
            similarity = model.evaluate_word_pairs(path_to_simlex)

        pearson = similarity[0]
        spearman = similarity[1]
        self.logger.info(
            f"Pearson correlation coefficient: {round(pearson[0], 4)}, p-value: {round(pearson[1], 4)}"
        )
        self.logger.info(
            f"Spearman correlation coefficient: {round(spearman.correlation, 4)}, p-value: {round(spearman.pvalue, 4)}"
        )
        self.logger.info(f"Out of vocab %: {round(similarity[2], 4)}")
        return {
            "name": os.path.basename(model_path),
            "pearson": round(pearson[0], 4),
            "spearman": round(spearman.correlation, 4),
            "out of vocab": round(similarity[2], 4),
        }

    @staticmethod
    def __init_logger(path_to_logger: str = "../data/w2v.log") -> logging.Logger:
        """
        Logger initializer


        Parameters
        ----------
        path_to_logger: str
            path where to save logs

        Return
        ------

        """
        formatter = logging.Formatter("%(message)s")
        fh_logger_path = os.path.abspath(path_to_logger)

        log_level = os.getenv("LOG_LEVEL", "INFO")
        log_level = "CRITICAL" if log_level == "false" else log_level

        coloredlogs.install(level=log_level)

        logger = logging.getLogger("WordEmbeddingLogger")
        fh_logger = logging.FileHandler(filename=fh_logger_path, mode="a+")
        fh_logger.setFormatter(formatter)
        logger.addHandler(fh_logger)
        return logger
