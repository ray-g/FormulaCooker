import collections
import queue
import multiprocessing
import numpy as np

class DataProvider(object):
    def __init__(self,
                 loader,
                 shape,
                 batch_size=1,
                 preprocessor=None,
                 shuffle=False,
                 drop_last=False,
                 cache_size=0,
                 num_workers=0):
        self.loader = loader
        self.shape = shape
        self.batch_size = batch_size
        self.preprocessor = preprocessor
        self.shuffle = shuffle
        self.drop_last = drop_last
        self.cache_size = cache_size
        self.num_workers = num_workers
        # self.loader_cache = np.ndarray()

    def __run__(self):
        return self

    def _load(self):
        pass

    def _next_batch(self):
        pass

    def __next__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        return self
