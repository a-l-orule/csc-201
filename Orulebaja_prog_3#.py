#Abdul-Lateef Orulebaja
#Program 3

#WHAT TO DO part 1
#TWO
#2.1
sequence = "ACTGAT" #string used for executing mirror
s = sequence #shorten variable for "sequence" to write more efficiently

s = s.replace("A","x") #replacing for A and T
s = s.replace("T","A")
s = s.replace("x","A")

s = s.replace("C","y") #replacing for C and G
s = s.replace("G","C")
s = s.replace("y","G")

print(s) #print new DNA sequence sting 


#2.2

sequence = "ACTGAT" #string used for executing mirror
s = sequence[::-1] #taking the reverse of the sequence string 
print(s) #print revers DNA sequence sting

#2.3

sequence = "ACTGAT" #string used for executing mirror

s = s.replace("A"," ") #sequence replace for varification
s = s.replace("T"," ")
s = s.replace("G"," ")
s = s.replace("C"," ")

seq = len(s) #setting variable to verify
#if and else conditiions for verification
if sq > 0: 
    print("Not Valid")
else:
    print("Valid")

#2. 4
#string used for executing mirror
seq1 = "GCTCAAGC" 
seq2 = "CGAGTTCG"

#function for valid sequence verification
def valid_seq(sequence):
    s = s.replace("A"," ")
    s = s.replace("T"," ")
    s = s.replace("G"," ")
    s = s.replace("C"," ")

    seq = len(s)
    if sq > 0:
        v = "Not Valid"
    else:
        v = "Valid"
#function for sequence match verification
def seq_match(sequence):
    s = s.replace("A","x")
    s = s.replace("T","A")
    s = s.replace("x","A")

    s = s.replace("C","y")
    s = s.replace("G","C")
    s = s.replace("y","G")

    return s
#function for reverse sequence
def seq_reverse(sequence):
    s = sequence[::-1]
    return s
#printing valid dna sequence
print("Sequence 1 is ", valid_seq(seq1))
print("Sequence 2 is ", valid_seq(seq2))

#set conditions to check for matching dna sequence 
if valid_seq(seq1) == "Valid" and valid_seq(seq2) == "Valid":
    if seq_match(seq1) == seq2:
        print(" Sequence reperent the same DNA fragment ")
    elif seq_match(seq1) == seq_reverse(seq2):
        print(" Sequence reperent the same DNA fragment ")
    else:
        print(" Sequence does not reperent the same DNA fragment ")


#WHAT TO DO Part 2
#3.1

#string used for executing mirror
seq1 = "GCTCAAGCCGAGTTCGGA"
seq2 = "CGAGTTCGGCTCAAGCCTGGCAC"

#function for valid sequence verification
def valid_seq(sequence):
    s = s.replace("A"," ")
    s = s.replace("T"," ")
    s = s.replace("G"," ")
    s = s.replace("C"," ")

    seq = len(s)
    if sq > 0:
        v = "Not Valid"
    else:
        v = "Valid"
#function for sequence match verification
def seq_match(sequence):
    s = s.replace("A","x")
    s = s.replace("T","A")
    s = s.replace("x","A")

    s = s.replace("C","y")
    s = s.replace("G","C")
    s = s.replace("y","G")

    return s
#function for reverse sequence
def seq_reverse(sequence):
    s = sequence[::-1]
    return s
#printing valid dna sequence
print("Sequence 1 is ", valid_seq(seq1))
print("Sequence 2 is ", valid_seq(seq2))
#checking the length of the given sequences  
if valid_seq(seq1) == "Valid" and valid_seq(seq2) == "Valid":
    sq1 = len(seq1)
    sq2 = len(seq2)
#second condition set for finding the length
    if sq1 >= sq2:
        long_seq = seq1
        short_seq = seq2
        sq_0 = sq1 - sq2 + 1
        longs = sq2

    else:
        sq2 >= sq2:
        long_seq = seq2
        short_seq = seq1
        sq_0 = sq2 - sq1 + 1
        longs = sq1
#function based on resulting condition above 
    short_s = seq_match(short_seq)
    print("The matches for cases:")
#condtionals befor for short_s equations in range if the length of the sequences given intially 
    for i in range(sq_0):
        n = 0
        for k in range(longs):
            if short_s[k] == long_seq[i+k]:
                n += 1
        print(n)
        print("The matches in (reverse) cases")
        longr = seq_reverse(longr)
        
        for i in range(sq_0):
            n = 0
            for k in range(longs):
                if longr[k] == long_seq[i + k]:
                    n += 1

#3.2
#string used for executing mirror
seq1 = "GCTCAAGCCGAGTTCGGA"
seq2 = "CGAGTTCGGCTCAAGCCTGGCAC"
#function for valid sequence verification
def valid_seq(sequence):
    s = s.replace("A"," ")
    s = s.replace("T"," ")
    s = s.replace("G"," ")
    s = s.replace("C"," ")

    seq = len(s)
    if sq > 0:
        v = "Not Valid"
    else:
        v = "Valid"
#function for sequence match verification
def seq_match(sequence):
    s = s.replace("A","x")
    s = s.replace("T","A")
    s = s.replace("x","A")

    s = s.replace("C","y")
    s = s.replace("G","C")
    s = s.replace("y","G")

    return s
#function for reverse sequence
def seq_reverse(sequence):
    s = sequence[::-1]
    return s
#printing valid dna sequence
print("Sequence 1 is ", valid_seq(seq1))
print("Sequence 2 is ", valid_seq(seq2))
#checking the length of the given sequences
if valid_seq(seq1) == "Valid" and valid_seq(seq2) == "Valid":
    sq1 = len(seq1)
    sq2 = len(seq2)

    if sq1 >= sq2:
        long_seq = seq1
        short_seq = seq2
        sq_0 = sq1 - sq2 + 1
        longs = sq2

    else:
        sq2 >= sq2:
        long_seq = seq2
        short_seq = seq1
        sq_0 = sq2 - sq1 + 1
        longs = sq1
    
    short_s = seq_match(short_seq)
    print("The matches for cases:")
#checking for consecutive matches in 
    for i in range(sq_0):
        n = 0
        ncon = []
        for k in range(longs):
            if short_s[k] == long_seq[i+k]:
                n += 1
        print(ncon)
        print("Longest consecutive match", max(nc)
        print(sum(nc))
        
        print("The matches in (reverse) cases")
        longr = seq_reverse(longr)
        
        for i in range(sq_0):
            n = 0
            for k in range(longs):
                if longr[k] == long_seq[i + k]:
                    n += 1

