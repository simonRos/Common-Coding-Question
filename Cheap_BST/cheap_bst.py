class BST:
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
            if self.tree[index_pointer] == None:
                #base case first
                return 1
            elif value <= self.tree[index_pointer]:
                left = self.left_of(index_pointer)
                #base case
                if self.tree[left] == None:
                    return left
                #recurse case
                else:
                    return inner_insert(self, value, left)
            else:
                right = self.right_of(index_pointer)
                #base case
                if self.tree[right] == None:
                    return right
                #recurse case
                else:
                    return inner_insert(self, value, right)
        new_index = inner_insert(self, value, 1)
        #The None nodes are a good way to identify the end of the tree
        #due to the way python inserts new elements to a list,
        #   list.insert(100,1) will actually insert at the smallest element
        #   which is less than 100
        #we have to do something hacky and inneficient
        def force_expand(self, start, end):
            for x in range(start-1,end+1):
                try:
                    temp = self.tree[x]
                except IndexError:
                    self.tree.insert(x,None)
        force_expand(self, len(self.tree), self.right_of(self.right_of(new_index)))
        self.tree.insert(new_index, value)


    def delete(self, value):
        '''delete value from tree'''
        def inner_delete(self, value, index):
            '''traverse tree to find deletion point'''
            if value == self.tree[index]:
                #base case
                self.delete_at(index)
            elif self.tree[index] == None:
                #null base case
                return None
            elif value < self.tree(index):
                #recurse left
                self.delete(value, left_of(index))
            elif value > self.tree(index):
                #recurse right
                self.delete(value, right_of(index))
        self.inner_delete(value,1)
                
                
    def delete_at(self, index):
        '''delete node from tree'''
        self.tree[index] = self.tree[left_of(index)]
        if self.tree[index] != None:    #recurse
            self.delete_at(left_of(index))


    def print_tiered(self, blanks = False):
        level_count = 0
        level_cap = 1
        out_strings = []
        for x in range(1,len(self.tree)):
            if self.tree[x] != None:
                out_strings.append(self.tree[x])
            elif blanks:
                out_strings.append('_')
            level_count += 1
            if level_count == level_cap:
                if out_strings != []:
                    print(out_strings)
                    out_strings = []
                level_cap *= 2
                level_count = 0 
        



        
