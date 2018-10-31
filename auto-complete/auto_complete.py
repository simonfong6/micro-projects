import logging


class Node:

    def __init__(self, char):
        self.value = char
        self.words = []
        self.nodes = {}

    def add(self, word):
        self.words.append(word)


class Trie:

    def __init__(self):
        self.trie = Node('')

    def get_node(self, node, char):
        if char not in node.nodes:
            node.nodes[char] = Node(char)

        the_node = node.nodes[char]
        return the_node

    def insert(self, word):
        node = self.trie
        for c in word:
            node = self.get_node(node, c)
            node.add(word)

    def get_words(self, string):
        node = self.trie
        for c in string:
            if c not in node.nodes:
                return []
            node = node.nodes[c]

        return node.words


class AutoComplete:

    def __init__(self, business_names):
        self.names = business_names
        self.word_map = {}
        self.trie = Trie()

        self.process()

    def insert_word_map(self, word, name):
        message = "Inserting into word map: (word: '{}', name: '{}')".format(word, name)
        logging.debug(message)

        if word not in self.word_map:
                    self.word_map[word] = []
        words = self.word_map[word]
        words.append(name)

    def process(self):
        for name in self.names:
            words = name.split(' ')

            for word in words:
                self.insert_word_map(word, name)
                self.trie.insert(word)

    def auto_complete(self, string):
        words = self.trie.get_words(string)
        all_names = set()

        for word in words:
            names = self.word_map[word]
            for name in names:
                all_names.add(name)

        all_names_list = list(all_names)

        return all_names_list


def main():
    logging.basicConfig(level=logging.DEBUG)

    database = [
        'what',
        'nut cut',
        'sut',
        'sat',
    ]

    ac = AutoComplete(database)

    print(ac.auto_complete('a'))


if __name__ == '__main__':
    main()
