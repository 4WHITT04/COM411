#first function
def short_pattern():

  pattern = {"sequence":"101", "occurences":5}

  return(pattern)

def medium_pattern():

  pattern = {"squence":"111000", "occourences":25}

  return(pattern)

def long_pattern():

  pattern = {"squence":"1100110011001100", "occourences":50}

  return(pattern)

def run():

  print ("Time to analyze these patterns, beep!")

  group_dicts = {"short sequence":short_pattern(),

  "medium sequence":medium_pattern(), 

  "long sequence":long_pattern()

  }

  for key, value in group_dicts.items():
    print ("{}: {}" .format(key, value))

run()
