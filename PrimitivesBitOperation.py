def PrimitivesBitOperation():
  def __init__():
    return self
    
  def countBits(x: int) -> int:
    numBits = 0
    while x:
      numBits += x & 1
      x >>= 1
    return numBits
  
  def shiftLeftBit (x:int) -> int:
    x_1 = x
    x_2 = x << 1
    print('before--> {}\tafter-->{}').format(x_1, x_2)
    return null
  
  def shiftRightBit (x:int) -> int:
    x_1 = x
    x_2 = x >> 1
    print('before--> {}\tafter-->{}').format(x_1, x_2)
    return null

  def andBinaryOperation (x:int) -> int:
    x_1 = x & 0
    x_2 = x & 1
    x_3 = x & 2
    x_4 = x & 4
    
    print('&0--> {}\t&2-->{}\t&3-->{}\t&4-->{}').format(x_1, x_2,x_3, x_4)
    return null