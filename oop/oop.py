# Object and Classes

# Apart from what we've seen till now, python also has an object oriented approach

# Up to this point we've seen one way of programming in python, using functions

# Object oriented programming is based on classes, objects and Methods

# In short as a definition, a class is a data type containing its own variables, attributes and functins, by the way, in object-oriented programming are called methods.
# A standard definition of a class would tell you tha a class is like a blueprint/template for creating objects.

# An object maybe regarded as an instance of a defined class and attribute values for a particular object define the state of the object.

# An object is a real world entity.

# Another term very much used when discussing classes is inheritance.
# This means that a new class may inherit all the names and functionalities from an existing class
# We will talk more about inheritance later
# In order to properly define a class we use the class keyword, then type in the class name

# Now, be careful here because the convetion is to use camelcase for class names. This means each word in the name of the class will be capitalised and no spaces allowed.

# actually the camelcase rule, all function names apply to class names, as well

# So, lets name our class simply MyRouter

# After the name of the class, in between parentheses, you should type in the word "object", all lowercase.

# This is the new style of defining classes, starting with python 2.2.
# The thing you should keep in mind here is the taht is a class doesn't inherit from another class, then yoi should always type in the word object insideparentheses a class.

# This is a default setting and it means that this class inherits from a default class names object

# I know this may seem confusing, so, we won't get into any more details on this topic

# just don't forget to add the word object.

# So, we have class MyRouter(Object) then, as for aby another block of code we've seen so far, we'll type in a colon

# class MyRouter(object):

# On the next row using one level of indentation, of course, we shall input the content of the class
# As with functions, on the first row after the class definition you can type in a documentation string or docstring in btwn quotes, to provide a hint about that class' functionality

# So lets enter some text in btwn double quotes

# class MyRouter(object):
#     "This is a class that describes the characteristics of a router"
    
# Following the optional docstring, the first thing we defined inside a python class is the special __init__() method, also called a class constructor

# The word init will be preceeded and followed by double underscores. This is the way python identifies a special method.

# The role of the __init__ is to initialize some variables and the method is called whenever you create a new instance of the classin which it precides.
# So actually it is the first call that is executed whenever you create a new object or instance of the class

# Any special method orregular method within a class is defined using the def keyword, as you would with a regular functions.

# The diffeence here is that each time you define a method inside a class the first paramerter inside the parentheses itself
# Ypu have to remember to always iput this word as the first parameter of every class method.

# self is no more than just a reference to the current instance of the class.

# Now, after typing in self, you define any other parameters that you want to be defined and initialized whenever you create a new instance of the class in which it resides.

# IN our class, we want to define some parameters that characterize our router, so we will add router name, model, serialno, ios

# Now, lets define the object or instance attributes we need to describe the router, according to the parameters of the __init__ method

# Remember that self is used to point out that we are referring to the current instance of the class

# The next lines of code will again be indented under the definition of the __init__ method

# Thats how you define object attributes

# Now, lets also define a new method inside the class, that will do nothing more than just print out the attributes and concatenate the model of the router within the manufacturing date.

# The definition of this new method will sit at the level of indentation as the definiton of the __init__ method

# Notice that self is again inserted as the first parameter

# You should do this every time you define a method inside a class.

# Next inside the method, again indenting our code one level to the right, we enter the print() functions we need

# Now, lets see what the deal is with the objects we talked about

# You can create as many objects as we want, by simply calling the class name and entering the arguments required by the __init__ method, in between parentheses - all of them, except self, which is automatically paused by python.

class MyRouter(object):
    "This is a class that describes the characteristics of a router"
    # The class constructor 
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
        
    # Amethod to print the router properties
    def print_router(self, manuf_date):
        print("The router is : ", self.routername)
        print("The router model is: ", self.model)
        print("The router number is: ", self.serialno)
        print("The ios version is: ", self.ios)
        print("The model and date combined is: ", self.model  +  manuf_date)
        
        
# Now, lets create our first object
router1 = MyRouter('R1', '2600', '123456789', '12.4')

# print(router1)

# Indeed we see that we created an object. python confirms it

# /What can you do with this object

# First, you can access each of its attributes, lets see how
print(router1.routername)
print(router1.model)
print(router1.serialno)
print(router1.ios)

router1.print_router("23-04-2024")