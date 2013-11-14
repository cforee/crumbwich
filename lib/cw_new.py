import cw_errors
def new(target):
  if target:
    print "\n===> creating new crumbwich at path: " + target + "\n"
  else:
    cw_errors.no_target_error('new', '<path>')