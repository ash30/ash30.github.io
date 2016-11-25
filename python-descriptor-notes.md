title: Python Descriptor Notes
date: 11th March 2014
tags: Python

- Descriptors are any object that conform to the descriptor protocol \_\_get\_\_,\_\_set\_\_ and \_\_del\_\_. Properties are a common example
- Descriptors are class level objects and you must use the obj reference passed to it in order to access the parent object.
- This is because the descriptor protocol methods are invoked via an objects \_\_getattribute\_\_ - so be careful when overriding!
- Weirdly hasattr returns false for testing if an class objects holds a specific 
property.

## Example 
<script src="https://gist.github.com/ash30/cca24018f5153cf51b8c674d3fb94f5f.js"></script>

## References  

<a href="www.docs.python.org/2/howto/descriptor.html">www.docs.python.org/2/howto/descriptor.html</a>


