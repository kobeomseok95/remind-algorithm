from bisect import bisect_left
import sys

sys.setrecursionlimit(100000)
read = sys.stdin.readline


def post_order(start, end):
    if start > end:
        return

    root = pre_order[start]
    mid = bisect_left(pre_order, root, start + 1, end + 1)
    post_order(start + 1, mid - 1)
    post_order(mid, end)
    print(root)


pre_order = []
while True:
    try:
        pre_order.append(int(read().strip()))
    except:
        break

post_order(0, len(pre_order) - 1)
