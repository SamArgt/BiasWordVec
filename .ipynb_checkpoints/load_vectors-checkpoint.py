from gensim.test.utils import datapath
from gensim.models import fasttext as ft


cap_path = datapath("/home/samuel_argouet/datascience/cc.en.300.bin")
# class  gensim.models.keyedvectors.FastTextKeyedVectors
wv = ft.load_facebook_vectors(cap_path)