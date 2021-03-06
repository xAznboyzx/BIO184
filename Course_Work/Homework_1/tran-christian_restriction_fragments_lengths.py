#Restriction fragment lengths
#Write a program which will calculate the size of the two fragments that will be produced when the DNA is digested with EcoRI\
#Cuts at the motif G*ATTC
short_dna_sequence_fragment ="ACTGATCGATTACGTATAGTAG*AATTCTATCATACATATATATCGATGCGTTCAT"
split=short_dna_sequence_fragment.find("*") #.find searches for the index at which said string is located. In this case it is *.
fragment_1=short_dna_sequence_fragment[:split] #prints the start to said index. The range [:] is exclusive or half open.
# Range(0,n) provides an index of length n not n+1. 0 is includes as a value in length. So from range (0,10) for numbers 0-10 would provide 0-9 which are 10 in length.
# Essentially in math, the range would look like this [0,10)
fragment_2=short_dna_sequence_fragment[split+1:] #prints from said index to the end of the total index. One is added to split because the start of the index is not * itself. 
length_of_fragment_1=len(fragment_1) #length of fragment 1
length_of_fragment_2=len(fragment_2) # length of fragment 2
print("Fragment on the left is ",fragment_1,"& it's length is",length_of_fragment_1)
print("Fragment on the right is ",fragment_2, "& it's length is", length_of_fragment_2)
