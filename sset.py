#!/usr/bin/env python3
from typing import List
# """
# Suffix tree to search in dictionary
# """

class SuffixTreeNode:
    def __init__(self):
        self.edges = {}
        self.is_terminal = False
        self.suffix_link = None

class SSet:
    def __init__(self, fname: str):
        self.fname = fname
        self.root = SuffixTreeNode()
        self.load()

    def load(self) -> None:
        self.words = []
        with open(self.fname, 'r') as f:
            for line in f:
                word = line.rstrip()
                self.words.append(word)
                self.add_word(word)

    def add_word(self, word: str) -> None:
        node = self.root
        for i, char in enumerate(word):
            print(node.edges)
            if char not in node.edges:
                node.edges[char] = SuffixTreeNode()
            node = node.edges[char]
            if i == len(word) - 1:
                node.is_terminal = True

    def search(self, substring: str) -> List[str]:
        pass

    def find(self, node: SuffixTreeNode, prefix: str) -> List[str]:
        pass
    
sset = SSet('words.txt')
print(sset.search('test'))