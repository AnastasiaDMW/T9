#!/usr/bin/env python3
from typing import List
# """
# Suffix tree to search in dictionary
# """

class SuffixTreeNode:
    def __init__(self):
        self.edges = {}
        self.isTerminal = False

class SSet:
    def __init__(self, fname):
        self.fname = fname
        self.root = SuffixTreeNode()
        self.load()

    def load(self):
        self.words = []
        with open(self.fname, 'r') as f:
            for line in f:
                word = line.rstrip()
                self.words.append(word)
                self.add_word(word)

    def add_word(self, word):
        current_node = self.root
        
        for i in range(len(word)):
            char = word[i]
            if char not in current_node.edges:
                current_node.edges[char] = SuffixTreeNode()
            current_node = current_node.edges[char]
            if i == len(word) - 1:
                current_node.isTerminal = True

    def search(self, substring):
        node = self.root
        for char in substring:
            if char not in node.edges:
                return []
            node = node.edges[char]
        
        return self.find(node, substring)

    def find(self, node, prefix):
        words = []
        data = [[node, prefix]]
        while data:
            current_node, current_prefix = data.pop()
            if current_node.isTerminal:
                words.append(current_prefix)
            for char, cur_node in current_node.edges.items():
                data.append([cur_node, current_prefix + char])
        return words
    
# sset = SSet('words.txt')
# print(sset.search('test'))