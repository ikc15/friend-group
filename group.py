"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {'Jill':{},'Zalika':{},'John':{},'Nash':{}}


Jill = {
	'name':'Jill',
	'age':26, 
	'job':'Biologist', 
	'connections':['me','friend','partner','NA'], 
	'Map':list(my_group.keys())
	}
Zalika = {
	'name':'Zalika',
	'age':28, 'job':'Artist',
	'connection':['friend','me','NA','NA'],
	'Map':list(my_group.keys())
	}
John = {
	'name':'John',
	'age':27, 'job':'Writer',
	'connection':['partner','NA','me','NA'],
	'Map':list(my_group.keys())
	}
Nash = {
	'name':'Nash',
	'age':34, 'job':'Chef',
	'connection':['NA','landlord','cousin','me'],
	'Map':list(my_group.keys())
	}

my_group = {'Jill':Jill,'Zalika':Zalika,'John':John,'Nash':Nash}