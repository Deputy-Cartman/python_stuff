#!/usr/bin/env python3

# Written with Python 3.6.8.

import sys
import re

def credit_card_check():
    while True:
        try:
            number_of_cards = int(input("Please input # of credit cards to process. 1 to 100 only: "))
            if (number_of_cards <= 0) or (number_of_cards >= 100):
                print("Between 1 and 100 only. Try again.") 
                continue
        except ValueError:
            print(f"Integers only. Try again.")
            continue
        else:
            break

    credit_card_input = []
    credit_card_results = ""
    num_of_ints=num_of_hyphens=0
    min_str_length = 4
    
    for i in range(number_of_cards):
        line = input()
        if line:
            credit_card_input.append(line)
        else:
            pass
        num_of_ints = sum(c.isdigit() for c in line)        # Count integers in a line.
        num_of_hyphens = line.count("-")                    # Counts hyphens.
        pattern_acceptable = r'[^\0-9\-]'                   # Defines acceptable characters.
        
        pattern_4_repeat = r'(\d){4}'
        if re.search(pattern_acceptable, line):        # check for valid characters.
            credit_card_results+="Invalid"+"\n"
        else:
            if num_of_ints != int(16):       # Check for number of integers, rejecting anything not 16.
                credit_card_results+="Invalid"+"\n"
            else:
                if num_of_hyphens != int(0) and num_of_hyphens != int(3):   # Rejects any number of hyphens other than 0 or 4.
                    credit_card_results+="Invalid"+"\n"
                else:
                    if int(line[0]) != 4 and int(line[0]) != 5 and int(line[0]) != 6:
                        credit_card_results+="Invalid"+"\n"
                    else:
                        if [i for i,j in re.findall(r"((.)\2{3,})",line)]:
                            credit_card_results+="Invalid"+"\n"
                        else:
                            credit_card_results+="Valid"+"\n"

    print(credit_card_results)

credit_card_check()
