class MaxSizeList:

    def __init__(self, max_size=0):
        if max_size < 0:
            self.internal_list = None
            raise ValueError( f'max_size {max_size} cannot be < 0' )
        else:
            self.internal_list = []
            self.max_size = max_size

    def push(self, element):
        self.internal_list.append(element)
        if len(self.internal_list) > self.max_size:
            self.internal_list.pop(0)

    def get_list(self):
        return self.internal_list.copy()
