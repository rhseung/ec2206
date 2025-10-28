import time
from contextlib import contextmanager

from insertion_sort import *
from merge_sort import *
from quick_sort import *
from selection_sort import *


@contextmanager
def timeit(label: str):
    start = time.time()
    yield
    end = time.time()
    print(f'{label}: {end - start}s')


with timeit('selection_sort'):
    sort_test(selection_sort, ignore_print=True)

with timeit('insertion_sort'):
    sort_test(my_insertion_sort, ignore_print=True)

with timeit('merge_sort'):
    sort_test(my_merge_sort, ignore_print=True)

with timeit('quick_sort'):
    sort_test(my_quick_sort, ignore_print=True)
