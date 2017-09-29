title: Note to Unowned Self 
date: 20/11/2016
tags: Swift; iOS

Its easy to think that the answer to all closure woes is to just declare self unowned - no more reference cycles for me!
However this is a very easy way to crash! Been there, done that, never again. 

let me translate what 'unowned' means: 

> I am not the owner of this reference but I am __100%__ sure it will exist when I need it.

Said like that, you can see thats a pretty sizeable assumption! 

A Weak reference, most of the time, will be a better bet because it makes you deal with possiblity of nil. 

