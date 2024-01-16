import sys
sys.path.append('..')
import numpy as np
import matplotlib.pyplot as plt
from common.util import most_similar, create_co_matrix, ppmi
from common.random_svd import svd
from common.random_svd2 import random_svd
from dataset import ptb

window_size = 2
wordvec_size = 100

corpus, word_to_id, id_to_word = ptb.load_data('train')
vocab_size = len(word_to_id)
print('counting co-ccurance ...')
C = create_co_matrix(corpus, vocab_size, window_size)
print('calculating PPMI ...')
W = ppmi(C, verbose=True)

# U, S, V = np.linalg.svd(W)
# S, U, V = svd(W)

from sklearn.utils.extmath import randomized_svd
# U, S, V = randomized_svd(W, n_components=wordvec_size, n_iter=5, random_state=None)
U, S, V = random_svd(W, wordvec_size)

word_vecs = U[:, :wordvec_size]

querys = ['you', 'year', 'car', 'toyota']
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)