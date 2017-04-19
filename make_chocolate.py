def make_chocolate(small, big, goal):
  if small+big*5>=goal:
    if goal%5<=small:
      return abs(goal - big*5)
  return -1
