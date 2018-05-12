def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
        if char == nucleotide:
            count = count +1
    return count        



def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


def is_valid_sequence(dna):
    """ (str) -> bool
    Return True if and only if the DNA sequence is valid

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATNCG')
    False
    """
    for char in dna:
        return char in 'ATCG'
     

def insert_sequence(dna1,dna2,index):
    """(str,str,int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence into
    the first DNA sequence at the given index.
    >>>insert_sequence('ATCGGC','GG',3)
    'ATCGGGGC'
    >>insert_sequence('ATCGGC','GT',2)
    ATGTCGGC
    """
    return dna1[0:index]+ dna2 + dna1[index:len(dna1)]


def get_compliment(nucleotide):
    """(str) -> str
    Return the nucleotide's complement.
    >>>get_compliment('C')
    G
    >>>get_compliment('T')
    A
    """
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        return 'Not valid nucleotide'


def get_complimentary_sequence(dna):
    """(str) -> str
    Return the DNA sequence that is complementary to the given DNA sequence.

    >>>get_complimentary_sequence('AT')
    TA
    >>>get_complimentary_sequence('CG')
    GC
    """
    str = ''

    for i in range(0,len(dna)):
        str = dna[len(dna)-i-1]+str
    return str    

    
   
    
