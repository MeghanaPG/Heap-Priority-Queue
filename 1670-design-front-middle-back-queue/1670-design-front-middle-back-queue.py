class FrontMiddleBackQueue:

    def __init__(self):
        self.queue=[]
        

    def pushFront(self, val: int) -> None:
        self.queue.insert(0,val)

    def pushMiddle(self, val: int) -> None:
        leng=len(self.queue)
        mid=leng//2
        
        self.queue.insert(mid,val)
        

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        

    def popFront(self) -> int:
     
        if(len(self.queue)==0):
            return(-1)
        
        return(self.queue.pop(0))
        

    def popMiddle(self) -> int:
        if(len(self.queue)==0):
            return(-1)

        leng=len(self.queue)
        mid=leng//2
        if(leng%2!=0):
            
            return(self.queue.pop(mid))
        else:
            return(self.queue.pop(mid-1))


    def popBack(self) -> int:
        if(len(self.queue)==0):
            return(-1)
        return(self.queue.pop(-1))