from typing import Any
import heapq


class Node:
    def __init__(self, command: str | Any, count: int, left: "Node" = None, right: "Node" = None):
        self.left = left
        self.right = right
        self.command = command
        self.count = count

    def __str__(self):
        return f"|{self.command}, L = {self.left}, R = {self.right}|"

    def __lt__(self, other):
        return self.count < other.count


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, node: Node):
        heapq.heappush(self.heap, node)

    def get_heap_size(self):
        return len(self.heap)

    def get_least_node(self) -> Node | None:
        try:
            return heapq.heappop(self.heap)
        except IndexError:
            return None
