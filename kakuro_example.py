from combinations import field_shared,printout,get_shared,save_variable,get_combinations

""" This file is used to show the basic functionality of combinations.py"""

# ------- FUNCTIONS ----------

def example():
    """ Create input sample and call field_shared() with the sample input.
        Then create output by calling "printout()"."""

    # create sample input
    input_summe1 = 13
    input_length1 = 2
    input_summe2 = 8
    input_length2 = 3

    # create output
    print ("sum1= " + str(input_summe1) + "\nlength1= " + str(input_length1) +
           "\nsum2= " + str(input_summe2) + "\nlength2= " + str(input_length2))
    
    # call field_shared() to calculate the possible combinations
    # output the returned values with printout()
    printout(field_shared(input_summe1, input_length1,
                          input_summe2, input_length2), 2)

# ------- MAIN PROGRAM ----------

example()
