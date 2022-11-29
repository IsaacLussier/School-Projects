import re

def main():
  Continue = True
  while Continue:

    #opperator input
    while True:
      op = input("Enter operation:")
      if op not in '|&^q':
        print("Please enter |, &, ^, or q")
      elif op == 'q':
        Continue = False
        break
      else:
        break
    if Continue == False:
      break

    #integer input
    while True:
      len = input("Enter number of integers:")
      if len.isdigit():
        len = int(len)
        if len > 1:
          break
        elif len <= 1:
          print("Please enter a valid integer greater than 1")
      else:
        print("Please enter a valid integer")

    #list input
    lst = []
    for a in range(1, len + 1):
      while True:
        item = input("Enter integer %a:"%(a))
        if check_hex(item):
          lst.append(item)
          break
        else:
          print("Please enter an 8-digit hexadecimal integer")

    #calls operations
    fixedList, operator = hex_operation(lst, op)
    hex_binary(fixedList, operator)


def check_hex(value):
  if len(value) > 8:
    return False
  elif len(value) < 8:
    value = value.zfill(8)
  regex = "^([A-Fa-f0-9]{8})$"
  p = re.compile(regex)
  if (re.search(p, value)):
    return True
  else:
    return False
  
def hex_operation(values, operation):
  
  valuesFix = []
  for a in values:
    valuesFix.append(a.zfill(8))
  print("Hexadecimal operation: ")
  result = 0
  
  if operation == '&':
    for b in valuesFix:
      if b == valuesFix[0]:
        result = int(b,16)
        print("  " + b)
      else:
        result = result & int(b,16)
        print("& " + b)
    result = hex(result)[2:]
    print("= " + result.zfill(8))

  elif operation == '|':
    for b in valuesFix:
      if b == valuesFix[0]:
        result = int(b,16)
        print("  " + b)
      else:
        result = result | int(b,16)
        print("| " + b)
    result = hex(result)[2:]
    print("= " + result.zfill(8))

  elif operation == '^':
    for b in valuesFix:
      if b == valuesFix[0]:
        result = int(b,16)
        print("  " + b)
      else:
        result = result ^ int(b,16)
        print("^ " + b)
    result = hex(result)[2:].zfill(8)
    print("= " + result)
  return valuesFix, operation


def hex_binary(values, operation):

  binValues = []
  for a in values: 
    binValues.append(decToBin(int(a, 16)))

  print("Binary operation: ")
  result = 0
  if operation == '&':
    for b in binValues:
      if result == 0:
        print("  " + cluster(b))
        result = int(b, 2) 
      else:
        print("& " + cluster(b))
        result = result & int(b, 2)
    print("= " + cluster(str(decToBin(result))))

  elif operation == '|':
    for b in binValues:
      if result == 0:
        print("  " + cluster(b))
        result = int(b, 2)
      else:
        print("| " + cluster(b))
        result = result | int(b, 2)
    print("= " + cluster(str(decToBin(result))))

  elif operation == '^':
    for b in binValues:
      if result == 0:
        print("  " + cluster(b))
        result = int(b, 2)
      else:
        print("^ " + cluster(b))
        result = result ^ int(b, 2)
    print("= " + cluster(str(decToBin(result))))

def cluster(binStr):
  binLst = list(binStr)
  binLst.insert(8, ' ')
  binLst.insert(17, ' ')
  binLst.insert(26, ' ')
  binStr = ''.join(binLst)
  return binStr

def decToBin(binTemp):
  result = []
  while binTemp > 0:
    n = binTemp % 2
    n = str(n)
    result.append(n)
    binTemp = binTemp//2
  result.reverse()
  result = ''.join(result).zfill(32)
  return result

main()
