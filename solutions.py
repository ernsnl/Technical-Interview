from collections import Counter


def question1(s, t):
    # Clean Inputs
    s = s.strip().replace(' ', '')
    t = t.strip().replace(' ', '')
    if len(s) == 0 or len(t) == 0 or len(t) > len(s):
        return False
    number_of_letters = Counter(s.replace(' ', ''))
    for char in t:
        if char in number_of_letters and number_of_letters[char] > 0:
            number_of_letters[char] -= 1
        else:
            return False
    return True

# Anagram
assert question1('anagram', 'nag a ram') == True
assert question1('meats', 'steam') == True
assert question1('gregory house', 'huge ego sorry') == True
assert question1('clint eastwood', 'old west action')
# Not Anagram
assert question1('udacity', 'cities') == False
assert question1('clint eastwood', 'old east action') == False
assert question1('question', 'answer') == False
assert question1('', 'answer') == False


def question2(s):
    # If string is empty, it should return empty string.
    if len(s) == 0 and s is None:
        return ''
    # If string is already a palindrome, it should return the string itself.
    if s == s[::-1]:
        return s
    n = len(s)
    # If palindrome string has smaller length then string,
    # We need to iterate each partial smaller string. Starting from the n-1.
    for i in reversed(range(1, n + 1)):
        for j in range(0, n - i):
            if s[j:j + i:] == ''.join(list(reversed(s[j:j + i:]))):
                return s[j:j + i:]
    # If we done find any string that is longer than 1 character,
    # We can say that every character is a palindrome , therefore
    # First character is a palindrome.
    return s[0]

assert question2('baaba') == 'baab'
assert question2('racecar') == 'racecar'
assert question2('rodent') == 'r'
assert question2('assert') == 'ss'
##########################################################################
# Question 3


def find_minimum_edge(graph, visited_nodes):
    node_to = ''
    node_from = ''
    value = 9999999
    for key in graph:
        # Iterate nodes that are visited
        if key in visited_nodes:
            for to, val in graph[key]:
                # Only count edges that lead to unvisited nodes
                # If the value is lower than the previous selected nodes
                # Change the edges
                if to not in visited_nodes and val < value:
                    node_to = to
                    node_from = key
                    value = val
    # Returns minimum edge value with starting node and leading node
    return (node_from, node_to)


def question3(graph):
    # Start from the first node
    visited_nodes = []
    spanning_tree = []
    first_node = graph.items()[0]
    visited_nodes.append(first_node[0])
    while(len(visited_nodes) < len(graph.items())):
        min_edge = find_minimum_edge(graph=graph, visited_nodes=visited_nodes)
        # Add edges to the spanning tree
        spanning_tree.append(min_edge)
        # Visit the Node
        visited_nodes.append(min_edge[1])
    return spanning_tree

assert question3({'A': [('B', 2)],
                  'B': [('A', 2), ('C', 5)],
                  'C': [('B', 5)]}) == [('A', 'B'), ('B', 'C')]
assert question3({'A': [('B', 2), ('D', 4)],
                  'B': [('A', 2), ('C', 5), ('D', 3), ('E', 7)],
                  'C': [('B', 5), ('D', 1), ('E', 4), ('F', 2), ('G', 4)],
                  'D': [('A', 4), ('B', 3), ('C', 1), ('G', 3)],
                  'E': [('B', 7), ('C', 4), ('F', 3)],
                  'F': [('C', 2), ('E', 3), ('G', 2)],
                  'G': [('C', 4), ('D', 3), ('F', 2)]
                  }) == [('A', 'B'), ('B', 'D'), ('D', 'C'), ('C', 'F'), ('F', 'G'), ('F', 'E')]
assert question3({'A': [('B', 2), ('C', 1), ('D', 2)],
          'B': [('A', 2), ('C', 1), ('E', 2)],
          'C': [('A', 1), ('B', 1), ('D', 1), ('E',1)],
          'D': [('A', 2), ('C', 1), ('E', 2)],
          'E': [('B', 2), ('C', 1), ('D', 2)],
          }) == [('A','C'), ('C','B'),('C','D'),('C','E')]

# Question 4
# ##############################################


class TreeNode():

    def __init__(self, root=False, value=0):
        self.left = None
        self.right = None
        self.value = value
        self.root = root


def placeNode(tree, node):
    # Get Info matrix
    info = tree[node.value]
    for i in range(len(info)):
        if info[i] == 1:
            if i < node.value:
                left_node = TreeNode(False, value=i)
                node.left = left_node
                left_node = placeNode(tree, left_node)
            else:
                right_node = TreeNode(False, value=i)
                node.right = right_node
                right_node = placeNode(tree, right_node)
    return node


def findClosestParent(node, n1, n2):
    if n1 > node.value and n2 < node.value or n1 < node.value and n2 > node.value:
        return node.value
    if n1 == node.value or n2 == node.value:
        return node.value
    if n1 < node.value and n2 < node.value:
        return findClosestParent(node.left, n1, n2)
    if n1 > node.value and n2 > node.value:
        return findClosestParent(node.right, n1, n2)


def question4_legacy(tree, r, n1, n2):
    root = TreeNode(True, r)
    root = placeNode(tree, root)
    return findClosestParent(root, n1, n2)

def question4(tree, root, node1, node2):
    current_node = root
    while(True):
        if current_node > node1 and current_node > node2:
            # first encounter with smallest node
            for i in range(0, current_node):
                if tree[current_node][i] == 1:
                    current_node = i
                    break
        elif current_node < node1 and current_node < node2:
            # first encounter with largest node
            for i in range(current_node, len(tree[current_node])):
                if tree[current_node][i] == 1:
                    current_node = i
                    break
        elif node1 > current_node and node2 < current_node or node1 < current_node and node2 > current_node:
            return current_node
        elif node1 == current_node or node2 == current_node:
            return current_node

# Udacity Problem
assert question4([[0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0]],
                 3,
                 1,
                 4) == 3
# Custom Test
# Custom Binary Tree
#                  7
#                 / \
#                /   \
#               5     9
#              / \   / \
#             3   6 8   10
#            / \
#           1   4
#          / \
#         0   2
assert question4([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 7, 3, 6) == 5
assert question4([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 7, 1, 3) == 3
assert question4([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 7, 1, 4) == 3
assert question4([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 7, 5, 9) == 7
assert question4([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 7, 8, 10) == 9
##########################################################################
# Question 5


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


def question5(linked_list, m):
        # We need to get length of the LinkedList
        # So we iterate over the LinkedList
    traverse = linked_list
    length = 0
    while(traverse is not None):
        traverse = traverse.next
        length += 1

    if m > length:
        raise 'Wanted position cannot be bigger than the length of the list'
    position_from_the_start = length - m

    traverse = linked_list
    for _ in range(position_from_the_start):
        traverse = traverse.next

    return traverse.data

root = Node(0)
traverse = root
for _ in range(2, 14, 2):
    traverse.next = Node(_)
    traverse = traverse.next
# It will generate 0-2-4-6-8-10-12
assert question5(root, 1) == 12
assert question5(root, 2) == 10
assert question5(root, 4) == 6
assert question5(root, 7) == 0
