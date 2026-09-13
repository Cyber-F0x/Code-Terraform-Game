class Coord():
    def convert_char_to_ord(self):
        return ord(self.row)

    def toString(self):
        return self.row + str(self.col)
    
    def __init__(self,row,col):
        self.row = chr(row)
        self.col = col
        
        




