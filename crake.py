#!/usr/bin/python
import getopt, sys, yaml, string

# main execution handlers
def new(target):
	if target:
	  print "\n===> creating new crumbwich at path: " + target + "\n"
	else:
	  no_target_error('new', '<path>')
def post(target):
	print (
	  "\n===> creating new crumb: \"" + target + "\"\n"
	)
def help(target):
  print(
    "\n===> available commands:\n"
    + "         \"new <path>\": create new crumbwich at <path>\n"
    + "         \"post <name>\": create new crumb called <name>\n"
  )


# error handlers: an incorrect command line
# argument was specified, let the user know
def no_target_error(action, suggestion):
  print "\n===> please specify a target in the form of: " + suggestion + "\n"


# a list of available command line options
available_options = {
	"new":new,
	"post":post,
	"help":help
}


# get options from command line
opts, args = getopt.getopt(sys.argv[1:], "help:new", ["help", "new"])


# execute the specified command line argument,
# if a second parameter is specified, pass it
# into the handler.  Most arguments will require
# two command line args, a notable exception being
# "help"
target = None
if len(args) > 1:
  target = args[1]
for arg in args:
  if arg in available_options:
    available_options[arg](target)
