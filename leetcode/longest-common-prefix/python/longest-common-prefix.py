class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        # 단어의 끝 표시
        current.word = True


class Solution:
    def longestCommonPrefix(self, strs):
        word_trie = Trie()
        word_ans = ""

        # make prefix trie
        for word in strs:
            if len(word) == 0:
                return ""
            word_trie.insert(word)

        # check
        current = word_trie.root
        while len(current.children) == 1:
            c = list(current.children.keys())[0]
            word_ans += c

            current = current.children[c]

            if current.word:
                break

        return word_ans

