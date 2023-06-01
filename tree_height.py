# python3
# 221RDB432

import sys
import threading
import numpy

def compute_height(n, parents):
    tree = [[] for _ in range(n)] # tree creating
    
    root = 0
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    def compute_node_height(node): # computing tree's height
        if not tree[node]:
            return 1
        heights = [compute_node_height(child) for child in tree[node]]
        return max(heights) + 1

    return compute_node_height(root)


def main():
    n = int(input())
    parents = list(map(int, input().split()))


    height = compute_height(n, parents)
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of a bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get a stack of such size
threading.Thread(target=main).start()
