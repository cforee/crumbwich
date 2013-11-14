#!/usr/bin/python
import getopt, os, sys, yaml, string
lib_path = os.path.abspath('./lib')
sys.path.append(lib_path)


# crumbwich-specific modules
import cw_new, cw_post, cw_save, cw_help


# a list of available command line options
# mapped to their respective modules
available_options = {
	"new":cw_new.new,
	"post":cw_post.post,
	"help":cw_help.help
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
