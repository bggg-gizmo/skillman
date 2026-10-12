"""HTTP-independent route dispatch."""
class Router:
    def __init__(self):self._routes={}
    def register(self,method,path,fn):
        if (method,path) in self._routes:raise ValueError('duplicate route')
        self._routes[(method,path)]=fn
    def dispatch(self,method,path):
        handler=self._routes.get((method,path))
        return (200,handler()) if handler else (404,{'error':'not found'})
