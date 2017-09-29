title: Python Bindings for TargetProcess
date: 28th May 2016
tags: Python; RestAPIs

Where can you find them? In one of my side projects: <a href='https://github.com/ash30/tpapi'>tpapi</a> - an unoffical python client for TargetProcess. It takes care of interacting with the REST api and returns nice model objects
for you to interact with. Some useful features worth mentioning:

### Transparent Pagination of Resource Requests
Every collection of entities is actually a generator which will lazily send http requests
as needed. This way we can expose a standard iterator interface over paginated resources.

### Nested Model Lookup
For resource or collection attributes we return an iterator over the correct class automatically
so you can continue to chain queries or pluck values.

Theres also a gist showcasing usage: <a href="https://gist.github.com/ash30/cfebdf200df7e96242755c80c06ade91">here</a>
