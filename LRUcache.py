class LRU(object):
    def __init__(self, capacity):
        self.capacity= capacity
        self.head= None
        self.end= None
        self.pairs= {}


    class _dlList_(object):
        def __init__(self, val):
            self.val= val
            self.prv= None
            self.nxt= None


    def get(self, key):
        if key not in self.pairs:
            print('Key %s not in LRU cache' % str(key))
            return None
        else:
            node= self.pairs[key][1]
            if node.prv != self.head:
                node.prv.nxt= node.nxt
                node.nxt.prv= node.prv
                node.prv= self.head
                node.nxt= self.head.nxt
                self.head.nxt.prv= node
                self.head.nxt= node
            return self.pairs[key][0]
       

    def get_LRUlist(self):
        outlist= [None for _ in range(self.capacity)]
        node= self.head.nxt
        for i in range(self.capacity):
            if node==self.end: break
            key= node.val
            outlist[i]= [key, self.pairs[key][0]]
            node= node.nxt
        return outlist


    def put(self, key, value):
        if key in self.pairs:
            node= self.pairs[key][1]
            if node.prv != self.head:
                node.prv.nxt= node.nxt
                node.nxt.prv= node.prv
                node.pve= self.head
                node.nxt= self.head.nxt
                self.head.nxt.prv= node
                self.head.nxt= node
            self.pairs[key][0]= value
            # if storage takes time, check bef assign
        else:
            node= self._dlList_(key)
            self.pairs[key]= [value, node]

            if len(self.pairs)==1:
                self.head= self._dlList_(None)
                self.end= self._dlList_(None)
                self.head.nxt= node
                self.end.prv= node
                node.prv= self.head
                node.nxt= self.end
            else:
                if len(self.pairs) > self.capacity:
                    rmkey= self.end.prv.val
                    del self.pairs[rmkey]
                    self.end.prv= self.end.prv.prv
                    self.end.prv.nxt= self.end
                node.prv= self.head
                node.nxt= self.head.nxt
                self.head.nxt.prv= node
                self.head.nxt= node
