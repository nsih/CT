import select
from array import array
import collections
import math
from functools import reduce
from collections import deque
import math
from collections import Counter
import sys

def DFS():
    if len(lst) == M:
        print(" ".join(map(str,lst)))
        return

    for i in range(1,N+1):
        if i not in lst:
            if len(lst) == 0:
                lst.append(i)
                DFS()
                lst.pop()
            else:
                if i > lst[-1]:
                    lst.append(i)
                    DFS()
                    lst.pop()

N = int(sys.stdin.readline())
answer = 0
lst = []

DFS()

'''
일단 내가 둔 퀸 좌표 리스트가 필요하겠지?
퀸이 퀸을 못잡으려면 퀸 새로 놓을때마다 앞서 둔 퀸 좌표 검사해야겠지?
잡힐 수 있으면 놓지말고 진행해야겠지?
N개 다 놓으면 마지막꺼 하나 씩 빼고 재귀가 알아서 해주겠지?
'''