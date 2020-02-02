

class Node(object):
    def __init__(self,item,rchild=None,lchild=None):
        self.elem = item
        self.rchild = rchild
        self.lchild = lchild

class Tree(object):
    def __init__(self,root=None):
        self.root = root

    def add(self,item):
        node =Node(item)

        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        '''广度遍历==>层次遍历'''
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)



    # 深度遍历的三种方式
    def preorder(self,root_node):
        '''先序遍历'''
        if root_node is None:
            return
        print(root_node.elem,end=' ')
        self.preorder(root_node.lchild)
        self.preorder(root_node.rchild)

    def inorder(self,root_node):
        '''中序遍历'''
        if root_node is None:
            return
        self.inorder(root_node.lchild)
        print(root_node.elem,end=' ')
        self.inorder(root_node.rchild)

    def postorder(self,root_node):
        '''后序遍历'''
        if root_node is None:
            return
        self.postorder(root_node.lchild)
        self.postorder(root_node.rchild)
        print(root_node.elem,end=' ')




if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(' ')
    tree.preorder(tree.root)
    print(' ')
    tree.inorder(tree.root)
    print(' ')
    tree.postorder(tree.root)