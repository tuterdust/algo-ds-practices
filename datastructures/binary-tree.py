def set_root(tree, key):
  if tree[0] is None:
    tree[0] = key
  else:
    print("Tree already have root key")

def set_left(tree, key, parent_idx):
  if tree[parent_idx] == None:
        print("Can't set child at", (parent_idx * 2) + 1, ", no parent found")
  elif parent_idx*2+1 >= len(tree):
      print("invalid index for key")
  else:
    tree[parent_idx*2+1] = key

def set_right(tree, key, parent_idx):
  if tree[parent_idx] == None:
        print("Can't set child at", (parent_idx * 2) + 2, ", no parent found")
  elif parent_idx*2+2 >= len(tree):
      print("invalid index for key")
  else:
    tree[parent_idx*2+2] = key

def print_tree(tree):
  for i in range(len(tree)):
    if tree[i] is not None:
      print(tree[i], end="")
    else:
      print("-", end="")


def main():
  print("Binary Tree practice")
  n = 10
  b_tree = [None] * n
  set_root(b_tree, 'A')
  set_root(b_tree, 'b')
  set_right(b_tree, 'C', 0)
  set_left(b_tree, 'D', 1)
  set_right(b_tree, 'E', 1)
  set_right(b_tree, 'F', 2)
  b_tree[9] = 'G'
  set_right(b_tree, 'Z', 9)
  print_tree(b_tree)


if __name__ == "__main__":
  main()
