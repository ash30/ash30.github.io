title: Testing Mac Gatekeeper
date: 29th April 2015
tags: Testing;OSX

Gatekeeper on macOS guards against the execution and installation of applications from unknown sources.
In order to pass this security check an application needs to be correctly signed which means its
a good requirement to check before a release.

The key gotcha to watch out for when testing is to ensure the executable has been quarantined.
By that I mean it has the ''com.apple.quarantine'' extended attribute present as Gatekeeper 
is triggered specifically at the first time you execute or install a quarantined file.

To verify the existence of the quarantine flag, you can show 'ls' output in terminal and look
for the '@' at the end of the permission fields. Better yet you can use the 'xattr' command to
show any extended attributes that exist on a file.
	
	$ xattr /path/to/file

	com.apple.quarantine

A programatic method to verify if the application's signature will pass gate keeper is to run the 'spctl' command.

	spctl --assess --type install ./path/to/file

Spctl will exit zero on success or return one if anything failed.

Additionally you can check the actual signature use 'pkgutil' for futher details.

	pkgutil --check-signature ./path/to/file

