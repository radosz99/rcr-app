from typing import List
from collections import Counter

from app.structures import Node, MinHeap


def find_path(node: Node, array_path: List[chr], command: str):
    if not node:
        return False

    if node.command == command:
        return True

    if find_path(node.left, array_path, command):
        array_path.append('0')
        return True
    if find_path(node.right, array_path, command):
        array_path.append('1')
        return True
    return False


def get_path(node: Node, command: str):
    array_path: List[chr] = []
    find_path(node, array_path, command)
    return "".join(reversed(array_path))


def create_tree_from_commands(commands: List[str]):
    min_heap = MinHeap()

    for k, v in Counter(commands).items():
        min_heap.insert(Node(command=k, count=v))

    while min_heap.get_heap_size() >= 2:
        ck = min_heap.get_least_node()
        cj = min_heap.get_least_node()
        node = Node(None, ck.count + cj.count, left=ck, right=cj)
        min_heap.insert(node)
    return min_heap.get_least_node()