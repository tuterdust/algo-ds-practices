class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.end_of_word = False
        self.counter = 1

def add(parent_node, word):
    node = parent_node
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True

def find_prefix(root, prefix):
    node = root
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0
    return True, node.counter

root_node = TrieNode('*')
add(root_node, "hackathon")
add(root_node, 'hack')

print(find_prefix(root_node, 'hac'))
print(find_prefix(root_node, 'hack'))
print(find_prefix(root_node, 'hackathon'))
print(find_prefix(root_node, 'ha'))
print(find_prefix(root_node, 'hammer'))