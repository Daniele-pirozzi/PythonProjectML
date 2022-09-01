#hashing functions
#sorting algorithms
#stacks and queues
#binary trees and search trees
#recursion
#caching
#lambda functions
#

# 0.5kg per pecora 4000 kg/ht

# ht_bestiame;
# ht_coltivati;
# giorni_coltivati;
# consumo_per_capo;
# produzione_yr_ht;

def countBits(x: int) -> int:
    numBits = 0
    while x:
      numBits += x & 1
      x >>= 1
    return numBits