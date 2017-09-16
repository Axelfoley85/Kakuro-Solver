# This program returns all combinations for one field in a specific Kakuro scenario


from operator import itemgetter
import pickle


def save_variable(filename, var_name):
    """Saves any variable to filename in user path of
        python file"""

    file = open(filename, 'w')
    pickle.dump(var_name, file)
    file.close()


def printout(to_print, depth):
    """ Used for bug fixing and to easily print variable content
        depth is used to enter/output different levels of matrices"""

    splitter = "------------------------------------"
    if depth == 1:
        print splitter
        for i in xrange(len(to_print)):
            print to_print[i]
    elif depth == 2:
        print splitter
        for i in xrange(len(to_print)):
            print splitter
            for j in xrange(len(to_print[i])):
                print to_print[i][j]
  #  ALLALL.sort(key=itemgetter(1,0))
 #   print splitter,"\nAnzahl Kombinationen: ",len(ALLALL),"\n",splitter
 #    save_any_file("alle_Kombinationen.txt",transform(ALLALL,2))


def initialization():
    """ Initialize matrix to create all possible combinations"""

    global test, ALLALL

    test = [[],[],[],[],[],[],[],[],[]]
    test[ 0 ].extend( [1] )
    test[ 1 ].extend( [1, 2] )
    test[ 2 ].extend( [1, 2, 3] )
    test[ 3 ].extend( [1, 2, 3, 4] )
    test[ 4 ].extend( [1, 2, 3, 4, 5] )
    test[ 5 ].extend( [1, 2, 3, 4, 5, 6] )
    test[ 6 ].extend( [1, 2, 3, 4, 5, 6, 7] )
    test[ 7 ].extend( [1, 2, 3, 4, 5, 6, 7, 8] )
    test[ 8 ].extend( [1, 2, 3, 4, 5, 6, 7, 8, 9] )

    #get_ALL()  #only once necessary, if "all_combinations.txt" doesn't exist

    file = open("all_combinations.txt", 'r')
    ALLALL = pickle.load(file)


def get_ALL():
    """creates a database of all possible combinations
       in kakuro and saves them (ALLALL) into all_combinations.txt"""

    global ALLALL, output, test
    
    # initialize matrix for all possible combinations independent of field length
    ALLALL = []

    # loop around all possible lengths
    for i in xrange(8):
        next_combination = []

        # add the first and lowest combination
        next_combination.append(list(test[i+1]))
        stop = 0
        count = 0
        while stop == 0:
            count += 1
            digit_reset = 0
            output = []
            temp = []
            temp = check_sum(next_combination[0], 15, 2)
            ALLALL.append([temp[0],
                           temp[1],
                           list(temp[2])
                           ])
            next_combination = increment(next_combination[0],
                                         len(next_combination[0])-1,
                                         i)
            if next_combination[0] == []:
                if digit_reset == 1:
                    stop = 0
                else:
                    stop = 1
    ALLALL = sorted(ALLALL,key=itemgetter(1,0))
    save_variable("all_combinations.txt", ALLALL)


def check_sum(value, sub_summe, sub_length):
    """ Calculate sum and length for
        each data entry."""

    found = 0
    get_sum = 0

    # sum up all values of one entry (value)
    for j in xrange(len(value)):
        get_sum += value[j]
    if len(value) == sub_length:
        if get_sum == sub_summe:
            found = 1
    return get_sum, len(value), value, found


def increment(value, digit, actual_length):
    """ Increment/Get to the next number series."""

    global output
    output = []
    digit_reset = 0
    if digit >= 0:
        if value[digit] <= 8:
            if digit == (len(value)-1):
                value[digit] += 1
                output = value
            else:
                if value[digit+1] >= (value[digit]+2):
                    value[digit] += 1
                    digit_reset = 1
                    output = value
                else:
                    if (value[digit] - value[digit - 1]) >= 3:
                        for n in xrange( len(value) - digit ):
                            value[n + digit] = value[digit-1] +n +2
                    increment(value,digit-1, actual_length)
        else:
            if (value[digit] - value[digit - 1]) >= 3:
                for n in xrange( len(value) - digit ):
                    value[n + digit] = value[digit-1] +n +2
            increment(value,digit-1, actual_length)
    return output, digit_reset


def get_combinations(the_summe, the_length):
    """ Create out of sum and lengths all possible
        combinations sum=3, lengths=2 --> ALL=[1,2]"""

    global ALLALL
    ALL = []
    ALL = [list(elem[2]) for elem in ALLALL if check_sum(elem[2], the_summe, the_length)[3] == 1]
    return ALL


def get_shared(combinations1, combinations2):
    """ Out of the intersection of the two lists reduce
        to the left combinations possible at the intersection field
        and also return the possible numbers for the specific field """

    keep1 = []
    keep2 = []
    shared_numbers = []
    numbers = []
    for j in xrange(9):
        shared_numbers.append([(j+1), 0])
    for j in xrange(len(combinations2)):
        keep2.append(0)
    shared_combinations1 = []
    shared_combinations2 = []
    for i in xrange(len(combinations1)):
        keep1.append(0)
        for j in xrange(len(combinations2)):
            for k in xrange(len(combinations1[i])):
                for l in xrange(len(combinations2[j])):
                    if combinations1[i][k] == combinations2[j][l]:
                        shared_numbers[combinations2[j][l]-1][1] = 1
                        keep2[j] = 1
                        keep1[i] = 1
    for j in xrange(len(combinations2)):
        if keep2[j] == 1:
            shared_combinations2.append(combinations2[j])
    for j in xrange(len(combinations1)):
        if keep1[j] == 1:
            shared_combinations1.append(combinations1[j])
    for j in xrange(9):
        if shared_numbers[j][1] == 1:
            numbers.append(j+1)
    return shared_combinations1, shared_combinations2, numbers


def field_shared(summe, length, summe2, length2):
    """ Main function to calculate out of one kakuro field all
        possible combinations. The function returns the possible combinations
        for the row and the column as well as the possible numbers for
        the regarding kakuro field."""

    initialization()
    temp1 = list(get_combinations(summe, length))
    temp2 = list(get_combinations(summe2, length2))
    shared = get_shared(temp1, temp2)
    return shared

