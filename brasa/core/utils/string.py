def parse_string(string):
  result=[]
  i=0

  while i<len(string):
    char=string[i]

    if char!="\\":
      result.append(char)
      i+=1
      continue

    if i+1>=len(string):
      raise Exception('Invalid escape: trailing "\\"')

    nxt = string[i + 1]

    if nxt=='n': result.append('\n')
    elif nxt=='t': result.append('\t')
    elif nxt=='\\': result.append('\\')
    elif nxt=='\'': result.append('\'')
    elif nxt=='\"': result.append('\"')
    else: raise Exception(f'Invalid escape: \\{nxt}')

    i+=2

  return ''.join(result)
