import math, queue
from collections import Counter


class TreeNode(object):
  # we assume data is a tuple (frequency, character)
  def __init__(self, left=None, right=None, data=None):
    self.left = left
    self.right = right
    self.data = data

  def __lt__(self, other):
    return (self.data[0] < other.data[0])

  def children(self):
    return ((self.left, self.right))


def get_frequencies(fname):
  ## This function is done.
  ## Given any file name, this function reads line by line to count the frequency per character.
  f = open(fname, 'r')
  C = Counter()
  for l in f.readlines():
    C.update(Counter(l))
  return (dict(C.most_common()))


# given a dictionary f mapping characters to frequencies,
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
  p = queue.PriorityQueue()

  # construct heap from frequencies, the initial items should be
  # the leaves of the final tree
  for c in f.keys():
    p.put(TreeNode(None, None, (f[c], c)))
  # greedily remove the two nodes x and y with lowest frequency,
  # create a new node z with x and y as children,
  # insert z into the priority queue (using an empty character "")
  while (p.qsize() > 1):

    x = p.get()
    y = p.get()

    z = TreeNode(x, y, (x.data[0] + y.data[0], ""))

    p.put(z)

  # # return root of the tree
  return p.get()


# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
  # TODO - perform a tree traversal and collect encodings for leaves in code
  #recursively visit the visit the left and right subtrees

  ## if node has left, increase prefix with 0
  ## if node has right, increase prefix with 1
  ## the stop condition is the node has no childrenm then we assign the predix to this coding
  if node.left != None:
    get_code(node.left, prefix + "0", code)
  if node.right != None:
    get_code(node.right, prefix + "1", code)
  if node.left == None and node.right == None:
    code[node.data[1]] = prefix

  return code


# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
  # cost = 0
  # for i in len(f):
  #   for j in len(f):

  ###################################

  numChars = len(f)

  lentgh = math.sqrt(numChars)

  totChars = sum(f.values())

  return lentgh * totChars


##############################################


# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
  total_cost = 0
  ## we need to use the key in f to identify the encoding in C
  for c in f.keys():
    # prefix = encoding[0]
    length_of_code = len(C[c])

    frequency = f[c]

    total_cost += length_of_code * frequency
  return total_cost


f = get_frequencies('fields.c')

print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)

print("Huffman cost:  %d" % huffman_cost(C, f))
