from src.doc2vecTR import Doc2VecTR
from src.config import *

if __name__ == '__main__':

    doc2vec = Doc2VecTR(unlabeled, groups)
    doc2vec.run()