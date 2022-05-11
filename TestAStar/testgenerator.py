import sys;
class TestGenerator():

    def __init__(self, callback):
        self.callback = callback;
        self.data = [[]]
        self.width = 50
        self.height = 50

    def setDimension(self, width, height):
        self.width = width;
        self.height = height;

    def generateDict(self):
        
        for x in range(self.width):
            for y in range(self.height): 
                self.data.append([])
                if (x == 0) or (x == self.width-1):
                    self.data[x].append('X')
                elif (x == 0) and ((y == 0) or (y == self.width-1)):
                    self.data[x].append('X')
                else:
                    self.data[x].append('0')
            lastX = x;

    def getData(self, x, y):
        return self.data[x][y]
def main():
    
    something = 0
    test = TestGenerator(something)
    width = 50
    height = 50
    test.setDimension(width, height)
    test.generateDict()
    for x in range(width):
        
        for y in range(height): 
            sys.stdout.write(test.getData(x,y))
        sys.stdout.write('\n')    
    

if __name__ == '__main__':
    main()  

