from __future__ import print_function
from ctypes import *
nnue = cdll.LoadLibrary("./nnue-probe/src/libnnueprobe.so")
nnue.nnue_init(b"kb2300-20201230-0906.bin")
start_score = nnue.nnue_evaluate_fen(b"r4bkr/p1p1p3/1p6/3b2N1/6nP/4qPP1/4P3/R6K b - - 0 21")
end_score = -nnue.nnue_evaluate_fen(b"r5kr/p1p1p1b1/1p6/3b2N1/6nP/4qPP1/4P3/R6K w - - 1 22")
score = end_score - start_score
print("start_score = ", start_score)
print("end_score = ", end_score)
print("score = ", score)  