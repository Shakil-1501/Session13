import math
class CustomerPolygon:
    def __init__(self,*n,cr=5):
        self.edges = list(n)
        self.circumradius= cr
        self.edgelength =list()
        self.apothem = list()
        self.area=None
        self.perimeter=None
        self.maxefficiency = None
        #self._el=list()
        
        
    
        
        
  
    
    @property
    def edgelength(self):
        return self._el
    
    @edgelength.setter
    def edgelength(self,el):
        self._el=list()
        #k=list()
        for i in self.edges:
            #k.append(i)
            self._el.append( (2*(self.circumradius)*(math.sin(math.pi/i))) )  
        #print(k)
    
    @property
    def apothem(self):
        return self._ap
    
    @apothem.setter
    def apothem(self,ap):
        self._ap = list()
        for i in self.edges:
            self._ap.append((self.circumradius)*(math.cos(math.pi/i)))
    
    
    
    
    @property
    def area(self):
        return self._ar
    
    @area.setter
    def area(self,ar):
        self._ar=list()
        for i in range(0,len(self.edges)):
            self._ar.append((1/2)*(self.edges[i]*self._el[i]*self._ap[i]))
        
        
    @property
    def perimeter(self):
        return self._pr
    
    @perimeter.setter
    def perimeter(self,pr):
        self._pr = list()
        for i in range(0,len(self.edges)):
            self._pr.append((self.edges[i]*self._el[i]))  
        
      
    @property
    def maxefficiency(self):
        return self._me
    
    @maxefficiency.setter
    def maxefficiency(self,a):
        l=list()
        for i in range(0,len(self.edges)):
            l.append(self._ar[i]/self._pr[i])
        self._me = l.index(max(l))  
            
        
    
    
    
    def __len__(self):
        return len(self.edges)
    
    def __repr__(self):
        return CustomerPolygon({0}).format(self.edges)
    
    def __getitem__(self,i):
        if isinstance(i,int):
            if i < 0:
                i = len(self.edges) + i

            # Check index lies within the valid range and return value if possible
            if i < 0 or i >= len(self.edges):
                raise IndexError("CustomPolygon list index out of range")
            else:
                return self.edges[i]
        
    