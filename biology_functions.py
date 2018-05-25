def RNK (DNK, n):
  list_nucleotide = []
  list_RNK = []
  i = 0
  triplets = []
  while (i < n):
    list_nucleotide.append(DNK[n - i - 1])
    list_RNK.append(DNK[n - i - 1])
    k = 0
    if ((list_nucleotide[i] == "A") and (k == 0)):
      list_RNK[i] = "U"
      k = 1
    if ((list_nucleotide[i] == "T") and (k == 0)):
      list_RNK[i] = "A"
      k = 1
    if ((list_nucleotide[i] == "G") and (k == 0)):
      list_RNK[i] = "C"
      k = 1
    if ((list_nucleotide[i] == "C") and (k == 0)):
      list_RNK[i] = "G"
      k = 1
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
    k = 0
    if ((list_nucleotide[i] == "A") and (k == 0)):
      list_nucleotide[i] = "T"        
      k = 1
    if ((list_nucleotide[i] == "T") and (k == 0)):
      list_nucleotide[i] = "A"
      k = 1
    if ((list_nucleotide[i] == "G") and (k == 0)):
      list_nucleotide[i] = "C"
      k = 1
    if ((list_nucleotide[i] == "C") and (k == 0)):
      list_nucleotide[i] = "G"
      k = 1
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
      if (triplets[i] == "UUU") or (triplets[i] == "UUC"):
          triplets_abs.append("Phe")
      if (triplets[i] == "UUA") or (triplets[i] == "UUG"):
          triplets_abs.append("Leu")
      if (triplets[i] == "CUU") or (triplets[i] == "CUC"):
          triplets_abs.append("Leu")
      if (triplets[i] == "CUA") or (triplets[i] == "CUG"):
          triplets_abs.append("Leu")
      if (triplets[i] == "UUU") or (triplets[i] == "UUC"):
          triplets_abs.append("Leu")
      if (triplets[i] == "AUU") or (triplets[i] == "AUC") or (triplets[i] == "AUA"):
          triplets_abs.append("Ile")
      if (triplets[i] == "AUG"):
          triplets_abs.append("Met")
      if (triplets[i] == "GUU") or (triplets[i] == "GUC"):
          triplets_abs.append("Val")
      if (triplets[i] == "GUA") or (triplets[i] == "GUG"):
          triplets_abs.append("Val")
      if (triplets[i] == "UCU") or (triplets[i] == "UCC"):
          triplets_abs.append("Ser")
      if (triplets[i] == "UCA") or (triplets[i] == "UCG"):
          triplets_abs.append("Ser")
      if (triplets[i] == "CCU") or (triplets[i] == "CСС"):
          triplets_abs.append("Thr")
      if (triplets[i] == "CCA") or (triplets[i] == "CCG"):
          triplets_abs.append("Thr")
      if (triplets[i] == "GCU") or (triplets[i] == "GСС"):
          triplets_abs.append("Ala")
      if (triplets[i] == "GCA") or (triplets[i] == "GCG"):
          triplets_abs.append("Ala")
      if (triplets[i] == "UAU") or (triplets[i] == "UAC"):
          triplets_abs.append("Tyr")
      if (triplets[i] == "CAU") or (triplets[i] == "CAC"):
          triplets_abs.append("His")
      if (triplets[i] == "CAA") or (triplets[i] == "CAG"):
          triplets_abs.append("Gin")
      if (triplets[i] == "AAU") or (triplets[i] == "AAC"):
          triplets_abs.append("Asn")
      if (triplets[i] == "AAA") or (triplets[i] == "AAG"):
          triplets_abs.append("Lys")
      if (triplets[i] == "GAU") or (triplets[i] == "GAC"):
          triplets_abs.append("Asp")
      if (triplets[i] == "GAA") or (triplets[i] == "GAG"):
          triplets_abs.append("Lys")
      if (triplets[i] == "UGU") or (triplets[i] == "UGC"):
          triplets_abs.append("Cys")
      if (triplets[i] == "UGG"):
          triplets_abs.append("Trp")
      if (triplets[i] == "CGU") or (triplets[i] == "CGС"):
          triplets_abs.append("Arg")
      if (triplets[i] == "CGA") or (triplets[i] == "CGG"):
          triplets_abs.append("Arg")
      if (triplets[i] == "AGU") or (triplets[i] == "AGC"):
          triplets_abs.append("Ser")
      if (triplets[i] == "AGA") or (triplets[i] == "AGG"):
          triplets_abs.append("Arg")
      if (triplets[i] == "GGU") or (triplets[i] == "GGС"):
          triplets_abs.append("Gly")
      if (triplets[i] == "GGA") or (triplets[i] == "GGG"):
          triplets_abs.append("Gly")
      i += 1
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
      
      
