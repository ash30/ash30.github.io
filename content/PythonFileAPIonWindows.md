title: Use Unittests to Explore 3rd Party APIs
date: 10th March 2017
tags: Python

One of the ideas I've adopted recently is to use unittests to assert the contract between you and a 3rd party API.
It's pretty normal to explore api usage in the REPL but by writing it formally as a series of tests you can record
your findings and review them next time. Even better, you can tests your assumptions if the library ever changes.

FileIO is always a little platfrom specific, even with cross platform librarys like
python's ```os.path```. I was tasked recently with porting some tools to windows and found myself
questioning some of my long held assumptions when working with file paths. The obvious question
is what happens with all the backslashes?

Without futher ado:

<script src="https://gist.github.com/ash30/cb2e77610bfbd789767ff9eb3ee2d599.js"></script>
