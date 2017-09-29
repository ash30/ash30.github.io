title: Swinject Thoughts and Patterns
date: 8th August 2017
tags: Swift, iOS, Swinject
status: draft 

I've written before about my admiration for swinject <INSERT HERE>, its a great dependency injection framework which
greatly helps clean up and centralise the required glue code to setup related objects.

Having used it throughout the development process for my side project HueInspired, I thought I'd take the time to
write about some the patterns I see around my own usage of Swinject.

## Application and Component Assemblers
One pattern I found quite successful was one of swinject's more opininiated features: Assemblers. 

Assembler is a protocol which defines a single function _Assemble_. The Assemblers sole responsibility
is to setup a container by registering desired factory callbacks.

When implementing new features to the app, I found it useful for individual features to define their own
assemblers which would later be applied to the root container. The knowledge of the object graph 
stays encapsulated within the feature whilst offering and easy way for clients to construct it.

## Private Containers

Sometimes we want the feature to register factories but not have them exposed to anyone who would 
include the assembler, they might expose construction of internal types that you want to keep isolated to the feature.
Or they may leak implementation details like Core data.

## Containers as Abstract Factories

If you register and rely on a protocol as your resolve target, you can effectively hide the implementation
from the client. This ties in naturally with feature level assemblers which already encapsulate the knowledge
required to setup the supporting objects in the graph.

In HueInspired, we are able to provide data layer objects without exposing the fact we're using Core Data

## Conditional inclusion of features
When features provide their own assemblers, we can conditionally include them in the app, opening the way
to ideas like feature flags etc.

In Hueinspired we have certain debug flags that change how we construct the initial object graph. 

## Rules for unwrapping resolve calls

As we must rely on other assemblers registering factories, we cannot always be sure if the resolve call will be fulfilled.
Hence I try and stick to the following rules

1. If the current assembler registers the factory then you can safely force unwrap
2. If Type is specified in Core, we can generally force unwrap
3. Else it should be left as optional

## Creating components at runtime

Not all objects are constructed at startup, for example we may need to construct a view controller and segue to it based on
a user interaction. Instead of hard coding the next view controller into the calling code, we can express it as dependency
that can injected in as required. 

The idea is to define a callback property that provides the next view controller but only exposes itself 
via the ViewController type. The initial construction of the object will inject in the factory so you are able centralise
construction logic in the container and just give out a strict interface.

This is prefered to having an object take the container as a dependency.



