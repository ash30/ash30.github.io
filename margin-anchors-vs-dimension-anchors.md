title: Margin anchors vs Dimension anchors
date: 17th April 2017
tags: Swift, iOS-Gotcha

You've tested your view layout with dynamic typing right? If not read on...

If you want a view to completely fill its super views and dynamically adjust to size changes,
there are two configurations of autolayout constraints you could potentially use:

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

What's the difference between the two? When using the leading/trailing top/bottom anchors, the child view will respect layout margins, meaning 
there will be some padding between the child and super view due to UIEdgeInsets.

Layout margins change with dynamic type sizes, even when the cell has no text based content. This is because table cells have the property
```self.contentView.preservesSuperviewLayoutMargins``` which means table view margin changes are inherited per cell.

So if your table cell content is unexpectedly changing size with dynamic type changes, check how you're handling layout margin inheritance.
