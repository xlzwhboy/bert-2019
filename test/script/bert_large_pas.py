# coding: utf-8
import pickle

from bertsota.common.data import ParserVocabulary, DataLoader
from bertsota.common.utils import init_logger
from bertsota.parser.dep_parser import SDPParser

if __name__ == '__main__':
    save_dir = 'data/model/bert-pas-sum'
    parser = SDPParser()
    parser.train(train_file='data/semeval15/en.pas.train.conllu',
                 dev_file='data/semeval15/en.pas.dev.conllu',
                 save_dir=save_dir,
                 pretrained_embeddings_file='data/embedding/glove.6B.100d.shrinked.txt',
                 bert_path=['data/embedding/bert_large_sum/en.train.bert',
                            'data/embedding/bert_large_sum/en.dev.bert'])
    parser.load(save_dir)
    logger = init_logger(save_dir, 'test.log')
    parser.evaluate(test_file='data/semeval15/en.id.pas.conllu', save_dir=save_dir,
                    bert_path='data/embedding/bert_large_sum/en.id.bert', logger=logger)
    parser.evaluate(test_file='data/semeval15/en.ood.pas.conllu', save_dir=save_dir,
                    bert_path='data/embedding/bert_large_sum/en.ood.bert', logger=logger)
