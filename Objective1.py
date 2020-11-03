import math

class Polygon:
    def __init__(self,n,R):
        self.edges=n
        self.circumradius = R
        self.interiorangle=None
        self.edgelength=None
        self.apothem=None
        self.area=None
        self.perimeter=None
    
    @property
    def edges(self):
        return self._edges
    
    @edges.setter
    def edges(self,new_edge):
        if new_edge<=0:
            raise ValueError("edges must be positive")
        else:
            self._edges=new_edge
            
    @property
    def circumradius(self):
        return self._circumradius
    
    @circumradius.setter
    def circumradius(self,new_circumradius):
        if new_circumradius<=0:
            raise ValueError("circumradius must be positive")
        else:
            self._circumradius=new_circumradius       
            
      
    @property
    def interiorangle(self):
        return self._ia
    
    @interiorangle.setter
    def interiorangle(self,ia):
        self._ia = ((self._edges-2)*(180))/self._edges
        
    @property
    def edgelength(self):
        return self._el
    
    @edgelength.setter
    def edgelength(self,el):
        self._el = 2*(self._circumradius)*(math.sin(math.pi/self._edges))
    
    @property
    def apothem(self):
        return self._ap
    
    @apothem.setter
    def apothem(self,ap):
        self._ap = (self._circumradius)*(math.cos(math.pi/self._edges))
        
    @property
    def area(self):
        return self._ar
    
    @area.setter
    def area(self,ar):
        self._ar=(1/2)*(self._edges*self._el*self._ap)
        
        
    @property
    def perimeter(self):
        return self._pr
    
    @perimeter.setter
    def perimeter(self,pr):
        self._pr = (self._edges*self._el)
        
        
        
        
        
            
            
     
    def __repr__(self):
        return 'Polygon({0},{1})'.format(self.edges,self.circumradius)
    def __eq__(self,other):
        if isinstance(other,Polygon):
            return self.edges==other.edges and self.circumradius==other.circumradius
    def __gt__(self,other):
        if isinstance(other,Polygon):
            return self.edges > other.edges
        else:
            return False