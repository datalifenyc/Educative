from Trie import Trie
from TrieNode import TrieNode


# TrieNode => {children, is_end_word, char}
def total_words(root):
	result = 0

	# Leaf denotes end of a word
	if root.is_end_word:
		result += 1

	for letter in root.children:
		if letter is not None:
			result += total_words(letter)
	return result


keys = ["the", "a", "abc"]

trie = Trie()

for key in keys:
    trie.insert(key)

print(total_words(trie.root))
