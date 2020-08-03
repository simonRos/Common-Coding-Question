Class BST:
    '''Represents a binary search tree'''
    def __init__ (self, head=None):
        '''initialize the BST'''
        #None
        #|
        #head
        #/      \
        #None   None
        self.tree = [None,head,None,None]


    def left_of(self, index):
        '''get index left of current index'''
        return index * 2


    def right_of(self, index):
        '''get index right of current index'''
        return (index * 2) + 1


    def insert(self, value):
        '''insert new node into tree'''
        def inner_insert(self, value, index_pointer):
            '''traverse tree to find insertion point'''
            if value <= self.tree[index_pointer]:
                left = left_of(index_pointer)
                #base case
                if self.tree[left] == None:
                    return left
                else:
                    return inner_insert(self, value, left)
            else:
                right = right_of(index_pointer)
                #base case
                if self.tree[right] == None:
                    return right
                else:
                    return inner_insert(self, value, right)
        new_index = inner_insert(value, 1)
        self.tree.insert(new_index, value)
        #The None nodes are a good way to identify the end of the tree
        self.tree.insert(left_of(new_index), None)
        self.tree.insert(right_of(new_index),None)


    def delete(self, value):
        pass


        
