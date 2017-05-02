title: HueInspired - an iOS App Post Mortem 
date: 2nd May 2017
tags: Swift, iOS

My current project is “HueInspired” - an iOS app for color palette generation from photos and I’m coming close to completing v1.0. Its been a blast and as a form of catharsis / chance to share what I learnt, I’m here to coherently ramble about the interesting points of the journey.

### Swinject

In the initial prototype of the app I did my dependency injection manually through a combination of initialiser injection and pass through parameters. It worked but there was a lot of boiler plate that I had to maintain and it also conflated ownership as it required some classes to hold additional dependencies purely to pass it to constructors at runtime.

Swinject definitely cleaned up the boilerplate, centralising construction in container callbacks and through its storyboard extension helped remove any hardcoding in the view controllers. I really liked the fact singletons became implementation detail of the class rather than the calling code, helping to keep things testable.

The down side was I faced a lot of implicitly unwrapped optionals in said callbacks which makes me uneasy. It almost feels like you should include the Swinject container in your test coverage just to make sure all those assumptions hold, especially for parts of the object graph created dynamically at runtime. 

### CoreData

The main difficulty I had was ensuring reliable change notifications when working with FetchResultsController and multiple contexts. Mike Abdullah writes about it here: http://mikeabdullah.net/merging-saved-changes-betwe.html but in short: Any new objects that are merged into a context will only receive future update notifications if they are retained.

Ultimately it meant merging in new objects was easy, but merging in edits for the same object was tricky. I generally came to the conclusion that any user interaction with managed objects should happen in the shared view context to ensure all FetchResultsControllers can see the change.

----

Overall I’m still a fan of both frameworks just now slightly more aware of the trade offs involved. 
Swinject is a pleasure to use and Core data, whilst not as charming has first party credentials that make it hard to ignore. 

Regardless, I can't wait to start the next project! 

### References 

<a href="https://github.com/ash30/HueInspired">HueInspired Github Repro</a>
