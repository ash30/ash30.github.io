title: Swifty Animation Enums
date: 13th June 2017
tags: Swift, iOS
status: draft 

In traditional animation you create a set of discrete drawings that represent the key moments (or key poses) of an action at specific points in time. You then creatively interpolate between these moments to give the illusion of movement. Interestingly I found implicit animations within UIKit follow this mental model quite well.
When you’re setting the model tree state, its like setting the next key pose and you can then gratefully hand it off to Core Animation to work out the interpolation.

Animation code can become quite dense as you manipulate the different states of a View / CALayer and it can quickly become hard to manage. Drawing inspiration from traditional keyframe animation, I found a nice pattern that helps me organise my thoughts:

<script src="https://gist.github.com/ash30/87b259001f615d591c1bf85ec09bfa45.js"></script>

Firstly the enum represents a finite set of poses the animation is going to transition through. The property observers ties individual 
enum cases to specific configurations of view state, mentally I picture this as each enum case being one pose.
As the observer's switch is declare in one place you get a high level overview of all the different poses that will complete the action, away from the tested requirements of animation calling code. Additionally, like the keyframe animator, you can worry about exact timing separately, allowing you to refactor more cleanly.

Its a bit different from my [previous animation work](http://www.imdb.com/name/nm6416515/?ref_=ttfc_fc_cr376), but overall I'm really digging core animation in Swift.
