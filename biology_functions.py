import triplets_dictionary

def RNK (DNK, n):
  list_nucleotide = []
  list_RNK = []
  i = 0
  triplets = []
  while (i < n):
    list_nucleotide.append(DNK[n - i - 1])
    list_RNK.append(DNK[n - i - 1])
    if (list_nucleotide[i] == "A"):
      list_RNK[i] = "U"
    elif (list_nucleotide[i] == "T"):
      list_RNK[i] = "A"
    elif (list_nucleotide[i] == "G"):
      list_RNK[i] = "C"
    elif (list_nucleotide[i] == "C"):
      list_RNK[i] = "G"
    i += 1
  i = 0
  RNK = ""
  while (i < n):
    RNK += list_RNK[n - i - 1]
    i += 1
  return RNK
  
  
def reverse_DNK (DNK, n):
  list_nucleotide = []
  i = 0
  while (i < n):
    list_nucleotide.append(DNK[n - i - 1])
    if (list_nucleotide[i] == "A"):
      list_nucleotide[i] = "T"        
    elif (list_nucleotide[i] == "T"):
      list_nucleotide[i] = "A"
    elif (list_nucleotide[i] == "G"):
      list_nucleotide[i] = "C"
    elif (list_nucleotide[i] == "C"):
      list_nucleotide[i] = "G"
    i += 1
  i = 0
  reverse_DNK = ""
  while (i < n):
    reverse_DNK += list_nucleotide[i]
    i += 1
  return reverse_DNK
  
  
def triplets (RNK, first_counter):
  i = 0
  string = ""
  triplets = []
  while (i < first_counter):
    string += RNK[i]
    if (i % 3 == 2):
      triplets.append(string)
      string = ""
    i += 1
  return triplets 
  
def triplets_abc (triplets, new_number):
  triplets_abs = []
  i = 0
  while (i < new_number):
     triplets_abs.append(triplets_dictionary[triplets[i]])
  return triplets_abs  
  
  
  def stop_codon (i, RMK, first_counter):
        while (i < n - 1):
          if RNK[i - 1] + RNK[i] + RNK[i + 1] == "UAA":
            stop_codon = "UAA"
            first_counter = i - 1
          if RNK[i - 1] + RNK[i] + RNK[i + 1] == "UAG":
            stop_codon = "UAG"
            first_counter = i - 1
          if RNK[i - 1] + RNK[i] + RNK[i + 1] == "UGA":
            stop_codon = "UGA"
            first_counter = i - 1
          i += 1
        return stop_codon
      
      
