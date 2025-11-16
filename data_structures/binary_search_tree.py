'''
Question : As a senior backend engineer, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:

1. Insert the profile information for a new user.
2. Find the profile information of a user, given their username
3. Update the profile information of a user, given their username
4. List all the users of the platform, sorted by username
You can assume that usernames are unique.
'''
 
class User:
  def __init__(self, username, name, email):
    self.username = username
    self.name = name
    self.email = email
    print('User created!')

  def __repr__(self):
    return 'User(username="{}", name="{}", email="{}")'.format(self.username, self.name, self.email)

  def __str__(self):
    return self.__repr__()

  def introduce_yourself(self, guest_name):
    print('Hi {}, I am {}! Contact me at {}.'.format(guest_name, self.name, self.email))

user = User('john', 'john doe', 'john@doe.com')

print('user', user)
print('username', user.username)
print('name', user.name)
print('email', user.email)

user.introduce_yourself('David')

class UserDatabase:

  def __init__(self):
    self.users = []

  def insert(self, user):
    i = 0
    while i < len(self.users):
      if self.users[i].username > user.username:
        break
      i += 1
    self.users.insert(i, user)

  def find(self, username):
    for user in self.users:
      if user.username == username:
        return user
    return None

  def update(self, user):
    target = self.find(user.username)
    target.name, target.email = user.name, user.email

  def list_all(self):
    print(self.users)

# 2. Come up with some example inputs and outputs

aakash = User('aakash', 'Aakash rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Sinha', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Sinha', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

database = UserDatabase()

# Lets insert some entries into the object

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

# we can retrieve the data for a user, given their username

user = database.find('siddhant')
print(user)

# Let's try changing/updating the information for a user

database.update(User(username='siddhant', name='Siddhant Updated', email='siddhant@example.com'))
user = database.find('siddhant')
print(user)

# Let's list all the users

users = database.list_all()
print(users)

# Let's verify that a new user is getting inserted into correct position(in alphabetical order)

database.insert(biraj)
database.list_all()

# 5. Analyze the algorithm's complexity and identify inefficiencies if any:

'''
The operations insert, find, update involves iterating a list of users, in the worst case they may take upto N iterations to return a result, where N is the total number of users.
list_all however, simply returns the existing internal list of users.

thus, the time complexities of various operations are:
1. Insert: O(N)
2. Find: O(N)
3. Update: O(N)
4. List: O(1)
'''

class TreeNode:

  def __init__(self, key):
    self.key, self.left, self.right = key, None, None

# lets create objects representing each node of the above tree

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

print(node0, node0.key, node0.left, node0.right)

node0.left = node1
node0.right = node2

print(node0, node0.key, node0.left.key, node0.right.key)

#

tree = node0
print(tree.key, tree.left.key, tree.right.key)

def parse_tuple(data):
  if isinstance(data, tuple) and len(data) == 3:
    node = TreeNode(data[1])
    node.left = parse_tuple(data[0])
    node.right = parse_tuple(data[2])
  elif data is None:
    node = None
  else:
    node = TreeNode(data)
  return node

tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree1 = parse_tuple(tree_tuple)
print(tree1)

def tree_to_tuple(node):
  if node is None:
    return None
  elif node.left is None and node.right is None:
    return node.key
  else:
    return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))

print(tree_to_tuple(tree1))

def display_keys(node, space='\t', level=0):

  # print( node.key if node else none, level)

  # if the node is empty
  if node is None:
    print(space*level + 'None')
    return

  # if the node is a leaf node
  if node.left is None and node.right is None:
    print(space*level + str(node.key))
    return

  # if the node has children
  display_keys(node.right, space, level+1)
  print(space*level + str(node.key))
  display_keys(node.left, space, level+1)

display_keys(tree1, '  ')

# Traversing a binary tree
'''Question: Write a function to perform the inorder, preorder and postorder traversal techniques on a binary tree.'''


  