title: Autolayout Margin anchors vs Dimension anchors
date: 17th April 2017
tags: Swift, AutoLayout

Recently I was testing my custom table cells with dynamic type sizes and even though I didn't have any text present I noticed sub views changing sizes - intrigued, I investigated.

My cell content was ridiculously simple, just one view that filled the whole parent content view, so what could be going wrong? It turns out it was auto layout related.
When Initially designing the layout I thought of two ways of creating the layout: match the height, width and centres of the parent view OR match horizontal and vertical anchors.

	::swift::
	let constraints = [
	view.centerXAnchor.constraint(equalTo: superview.layoutMarginsGuide.centerXAnchor),
	view.centerYAnchor.constraint(equalTo: superview.layoutMarginsGuide.centerYAnchor),
	view.heightAnchor.constraint(equalTo: superview.heightAnchor)
	view.widthAnchor.constraint(equalTo: superview.widthAnchor)
	]

	let altConstraints = [
	stackView.leadingAnchor.constraint(equalTo: superview.layoutMarginsGuide.leadingAnchor),
	stackView.trailingAnchor.constraint(equalTo:superview.layoutMarginsGuide.trailingAnchor),
	stackView.topAnchor.constraint(equalTo: superview.layoutMarginsGuide.topAnchor),
	stackView.bottomAnchor.constraint(equalTo: superview.layoutMarginsGuide.bottomAnchor),
	]

There is a difference though, and it's because I had opted to constrain anchors to the the margin guides. These are actually slightly offset from the edge by UIEdgeInsets and these change based on dynamic type sizes. I believe this is because table cells have the property
```self.contentView.preservesSuperviewLayoutMargins``` which means table view margin changes are inherited by the cell.

Ultimately this was a case of view hierarchies and layout constraints can appear the same to the user but there can be subtle differences when interacting with other subsystems.

On a simpler level, don't overlook your layout margins! 

