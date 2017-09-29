title: Restoring ViewControllers and their Data sources (WIP)
date: 25/11/2016
tags: Swift; iOS

The traditional flow for restoring view controllers in UIKit goes likes this:
 
1. (Required) Assign restoration identifiers to the view controllers
2. (Required) Tell iOS how to create or locate new view controller objects at launch time.
3. (Optional) Encode current State for later restoration

Recreating the hierarchy of view controllers is indeed easy and mostly automated 
but a lot of the articles out there gloss over how to restore their dependencies
(hint: Grabbing references to singletons in the VC’s decodeRestorableState method is not the correct answer!)

Normally you pass dependencies like a baton between controllers. When restoring a controller,
the segue isn’t called and you get an ‘empty’ controller and its up to you to restore the dependencies.
It turns out the data source can adopt the same state restoring protocol as the view controller and come along for the ride.  

## Assign restoration ids for dependencies

Normally as apart of the app launch you’ll have some code to initialise 
backing data sources for your view controllers. As a small extension to this routine,
we also now have to give them an ID so that the VC’s can indirectly reference them on app restore.

The app delegate method __willFinishLaunchingWithOptions__ is called after bootstrapping 
but before the restoration process so is a good place to register objects. 

	:::swift
	func application(_ application: UIApplication, willFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = nil) -> Bool {

		// Register Data Source

		UIApplication.registerObject(
		  forStateRestoration: dataStore,
		  restorationIdentifier: "DataSource"
		)
		return true
	}


## Tell iOS how to create or locate the dependency 

Any registered dependency must conform to ‘UIStateRestoring’ protocol 
(UIViewControllers automatically conform to this) and allows you to define a restoration class

	:::swift
	optional var objectRestorationClass: UIObjectRestoration.Type? { get }

If you return nil from this method, UIKIT assumes the app startup code recreated 
the dependency already and will be able to find it as you’ve registered it to a restoration id.

If you do specify a restoration class, it needs to define the following static method:

	:::swift
	static func object(withRestorationIdentifierPath identifierComponents: [String], coder: NSCoder) -> UIStateRestoring?

It can return a reference to a global, init a new instance or return nil if no restoration is possible. 

## Restoring the Dependency as part of the Controller Decode Process

Now when you restore the view controllers state, any request to decode the 
datasources’s restoration id will simply be passed the registered instance.
Voila! You can now reconstruct the VC’s dependencies.


	:::swift
	class controller : UIViewController {
		// ... 

		override func decodeRestorableState(with: NSCoder) {
			super.decodeRestorableState(with: with)
			guard
				let object = with.decodeObject(forKey: "DataSource"), // Any 
				let dataSource = object as? DateSourceKlass 
			else {
				return
			}
			self.dataSource = dataSource
		}
	}

The one draw back to this approach, as others have noted, is how it separates 
Controller Restoration and Dependency Restoration into 2 distinct phases. 
You’ve just lost your paddle if you’ve declared your dependencies as const.
I think this hints at UIKits own opinion that controllers don’t actually own 
their datasources and so should be declared weakly.

## References 

- <https://developer.apple.com/videos/play/wwdc2013/222/>

