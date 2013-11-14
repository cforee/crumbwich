# error handlers: an incorrect command line
# argument was specified, let the user know
def no_target_error(action, suggestion):
  print "\n===> please specify a target in the form of: " + suggestion + "\n"