from collections import OrderedDict
def f(**kwargs):
	return kwargs.get('interface',None)
class Task:
	def __init__(self,**kwargs):
		for field in ('id','name','config'):
			setattr(self, field, kwargs.get(field, None))
            
class Interface:
	def __init__(self,**kwargs):
		for field in ('id','name'):
			setattr(self,field,kwargs.get(field,None))