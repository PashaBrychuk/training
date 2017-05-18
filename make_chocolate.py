""" My dead end solution
def make_chocolate(small, big, goal):
  if small+big*5>=goal:
    if goal%5<=small:
      if goal%5!=0:
        return goal%5
      if goal == big*5:
        return 0
  return -1

"""
"""def make_chocolate(small, big, goal):
  maxBig = goal / 5
   
  if big >= maxBig:
    if small >= (goal - maxBig * 5):
      return goal - maxBig * 5
  if big < maxBig:
    if small >= (goal - big * 5):
      return goal - big * 5
  return -1"""

def make_chocolate(small, big, goal):
  if small+big*5<goal or goal%5>small:
    return -1
  maxbig = goal/5
  if big>=maxbig:
    return goal-maxbig*5
  return goal-big*5

print 21/ 5