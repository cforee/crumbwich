import cw_errors
def post(target):
  if target:
    print "\n===> creating new crumb: \"" + target + "\"\n"
    print "to save, type \":::save\" on a single line"
    print "when finished, type \":::cancel\" or \":::done\" on a single line"
    print "(NOTE: \":::done\" will save your crumb)"
    input_list = []
    exit_strings = [":::save",":::cancel",":::done"]
    while True:
      input_str = raw_input(">")
      if input_str in exit_strings:
        break
      else:
        input_list.append(input_str)
    print input_list
  else:
    cw_errors.no_target_error('new', '<path>')