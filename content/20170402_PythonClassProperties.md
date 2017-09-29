title: Creating Class level Properties in Python 
date: 2nd April 2017
tags: Python

So what happens when you want a computed class property in python? 

Descriptors are invoked via the \_\_getattribute\_\_ so simply assigning a 
descriptor to a class level attribute won't do. Instead you need to 
create the class level property as a instance variable on the classes
type object and rely on the fact attribute look up will eventually
look there via the base classes \_\_class\_\_ attribute.

<script src="https://gist.github.com/ash30/08ab5a96d7cfb8d5c8fad58ffea93970.js"></script>

Obligatory meta class warning: you better be sure you really need todo this :P 

## References
http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.pdf


