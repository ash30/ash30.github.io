title: Swinject Patterns
date: 8th August 2017
tags: Swift, iOS, Swinject

Swinject is a dependency injection framework for Swift which I've been using in some of my side projects recently. 
Having ran the app dev gauntlet with it, I've seen some nice patterns emerge that simplify setup code and promotes loose coupling
between different features. Here's a non exhaustive list of some of benefits I've seen in my code.

## Encapsulating new feature setup with Assemblers
For most features or area of functionality, we create a group of related entities that work together. For example implementing a new ViewController may require new delegate object as well. 

	::swift
	class Foo: ViewController {
		var weak delegate: NewDelegateProtocol?

		// ....
	}

To integrate this new vc, the existing code will need to instantiate the delegate and the data controller. This leaks implementation details into the rest of the system. Time for Assemblers! Here's what the protocol looks like:

	::swift
	protocol Assembly {
		public func assemble(container: Swinject.Container)
		public func loaded(resolver: Resolver)
	}

And here's a simple implementation for our Foo View Controller

	::swift
	class FooAssembler: Assembly {

		func assemble(container: Container) {
			container.register(NewDelegateProtocol.self) { r in
				return NewDelegate()
			}

			container.register(Foo.self) { r in
				let vc = Foo()
				vc.delegate = container.resolve(NewDelegateProtocol.self)! 
			}
		}
	}

An Assembler is a protocol which defines a single function _Assemble_. The Assembler's responsibility is to setup a container by registering factory callbacks. Why is this useful? We can augment existing containers with knowledge of Foo's setup requirements without leaking it to calling code, all they need to do is this:

	::swift
	mainContainer.resolve(Foo.self)!	

Hoorah for encapsulation! Knowledge of the object graph is no longer required. As an added bonus, with features providing their own assemblers we can start conditionally including them, a step in the direction of feature flags.

## Private Containers
Sometimes we want the feature to register factories but not have all of them exposed to anyone who includes the assembler. Going back to our example, maybe we don't want people accidentally instantiating  our `NewDelegate`? We can use private internal containers:


	::swift
	class FooAssembler: Assembly {
		private let internalContainer = { 
			let container = Container()
			container.register(NewDelegateProtocol.self) { r in
				return NewDelegate()
			}
			return container
		}()

		func assemble(container: Container) {
			container.register(Foo.self) { r in
				let vc = Foo()
				vc.delegate = internalContainer.resolve(NewDelegateProtocol.self)! 
			}
		}
	}

Here only `Foo` will be registered in the target container.

## Containers as Abstract Factories

Obvious but worth mentioning: registering protocols instead of concrete classes in the container is an easy way to implement an abstract factory. Containers centralise the definition of the specified concrete class and allow you to easily pass around opaque references to objects.

## Rules for unwrapping resolve calls

As I rely on other assemblers registering factories, we cannot always be sure if the resolve call will be fulfilled. Hence I try and stick to the following rules

1. If the current assembler registers the factory then you can safely force unwrap
2. If Type is specified in Core (i.e. never conditionally included), we can generally force unwrap
3. Else it should be left as optional

## Creating components at runtime

Not all objects are constructed at startup, for example we may need to construct a view controller and present it based on a user interaction aka the master-detail pattern. Instead of hard coding the next view controller into the master vc, we can express it as dependency that can injected in as required. 

	::swift
	typealias ViewControllerFactory = () -> ViewController?

	class Bar: ViewController {
		var nextVC: ViewControllerFactory?

		// ....

		func showDetail() {
			present(nextVC(), animated:true)
		}
	}

	class BarAssembler: Assembly
		func assemble(container: Container) {
			container.register(Bar.self) { r in
				var vc = Bar()
				vc.factory = { container.resolve(Spam.self) }				
				return vc 
			}
		}

Why does this matter? It decouples the master and detail vcs which allow for better modularity. We could easily add an alternative presented vc:

	class BarAssembler: Assembly
		func assemble(container: Container) {
			container.register(Bar.self) { r in
				var vc = Bar()
				vc.factory = { container.resolve(Spam.self) }				
				return vc 
			}
			container.register(Bar.self, named:"AlternativeDetail") { r in
				var vc = Bar()
				vc.factory = { container.resolve(NewSpam.self) }				
				return vc 
			}
		}

A/B Test anyone? Or maybe increased testability? As a side note I prefer this approach as apposed to having an object take the container as a dependency as it keeps your vc decoupled from swinject itself.

Some of you maybe asking what about setting up the new view controller? That's easily taken care of:

	::swift
	typealias ViewControllerFactory = (Model) -> ViewController?

	class Bar: ViewController {
		var nextVC: ViewControllerFactory?

		// ....

		func showDetail() {
			// ....
			present(nextVC(model), animated:true)
		}
	}

	class BarAssembler: Assembly
		func assemble(container: Container) {
			container.register(Bar.self) { r in
				var vc = Bar()
				vc.factory = { 
					nextvc = container.resolve(Spam.self)
					nextvc.data = $0
					return nextvc
				 }				
				return vc 
			}
		}

This is very similar to the previous example but instead we now take in some input parameter to the ViewControllerFactory. What's great about this approach is within the callback we have knowledge of what concrete class we're setting up but returning to the outside world the more general ViewController class keeping things nice and opaque.

## Is that all?

I'm still only scratching the surface of this great framework so I look forward to using it more over the coming projects. In my last: [HueInspired](https://github.com/ash30/HueInspired) I saw great improvements in modularity which helped improve overall testability (disclaimer: I like a good unittest). All I can say is go forth and swinject!


