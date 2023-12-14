def main():
    # athletic = a
    # food = f
    # entertainment = e
    # serious_relationship = s
    # religious = r
    # religion = specific religion
    # politics = p,
    # political_leaning = l
    #           a   f  e  s  r    religion   p  l
    person_1 = (7, 10, 8, 9, 10, "buddhism", 6, 8)
    person_2 = (4, 5, 6, 10, 8, "judaism", 3, 2)
    person_3 = (8, 3, 7, 7, 8, "christianity", 8, 3)
    person_4 = (3, 7, 10, 9, 8, "islam", 5, 4)
    print("Person_1 and Person_2:")
    match(person_1, person_2)
    print("Person_3 and Person_4:")
    match(person_3, person_4)
    rate(1,4)


def rate(rating_1, rating_2):
    z=abs(rating_1-rating_2)
    if z <= 6 and z > 3:
        print("40% probability of match.")
    if z <= 3 and z > 1:
        print("70% probability of match.")
    if z <= 1:
        print("100% probability of match.")
    if z > 6:
        print("0% probability of match.")



def match(tuple_1, tuple_2):
# constants for determing weight of each character trait:
    athleticism = 0.15
    food = 0.10
    entertainment = 0.15
    relationship = 0.20
    politics = 0.20
    religion = 0.20

# zeroing weight of each character trait calculation:
    a_contribut = 0
    f_contribut = 0
    e_contribut = 0
    r_contribut = 0
    p_contribut = 0
    pl_contribut = 0
    re_contribut = 0

# tuple differences in values to calculate character trait contributions
    a_diff = tuple_1[0] - tuple_2[0]
    f_diff = tuple_1[1] - tuple_2[1]
    e_diff = tuple_1[2] - tuple_2[2]
    r_diff = tuple_1[3] - tuple_2[3]
    p_diff = tuple_1[6] - tuple_2[6]
    pl_diff = tuple_1[7] - tuple_2[7]
    re_diff = tuple_1[4] - tuple_2[4]

# athleticism match calculation
    if a_diff <= 1:
        a_contribut = 1 * athleticism
    if a_diff <= 3 and a_diff > 1:
        a_contribut = 0.70 * athleticism
    if a_diff > 3 and a_diff <= 6:
        a_contribut = 0.40 * athleticism
    if a_diff > 6:
        a_contribut = 0 * athleticism

# food out match calculation
    if f_diff <= 1:
        f_contribut = 1 * food
    if f_diff <= 3 and f_diff > 1:
        f_contribut = 0.70 * food
    if f_diff > 3 and f_diff <= 6:
        f_contribut = 0.40 * food
    if f_diff > 6:
        f_contribut = 0 * food

# entertainment match calculation
    if e_diff <= 1:
        e_contribut = 1 * entertainment
    if e_diff <= 3 and e_diff > 1:
        e_contribut = 0.70 * entertainment
    if e_diff > 3 and e_diff <= 6:
        e_contribut = 0.40 * entertainment
    if e_diff > 6:
        e_contribut = 0 * entertainment

# serious relationship match calculation
    if r_diff <= 1:
        r_contribut = 1 * relationship
    if r_diff <= 3 and r_diff > 1:
        r_contribut = 0.70 * relationship
    if r_diff > 3 and r_diff <= 6:
        r_contribut = 0.40 * relationship
    if r_diff > 6:
        r_contribut = 0 * relationship
    
# politics match calculation
    if tuple_1[6] >= 9 or tuple_2[6] >= 9:
        p_diff = 0
        p_contribut = 0
        if pl_diff <= 1:
            pl_contribut = 1 * politics
        if pl_diff <= 3 and pl_diff > 1:
            pl_contribut = 0.70 * politics
        if pl_diff > 3 and pl_diff <= 6:
            pl_contribut = 0.40 * politics
        if pl_diff > 6:
            pl_contribut = 0 * politics
    if tuple_1[6] < 9 or tuple_2[6] < 9:
        pl_diff = 0
        pl_contribut = 0
        if p_diff <= 1:
            p_contribut = 1 * politics
        if p_diff <= 3 and p_diff > 1:
            p_contribut = 0.70 * politics
        if p_diff > 3 and p_diff <= 6:
            p_contribut = 0.40 * politics
        if p_diff > 6:
            p_contribut = 0 * politics
# religion match calculation
    if tuple_1[5] == tuple_2[5]:
        if tuple_1[4]>=8 or tuple_2[4]>=8:
            re_contribut = 1 * religion
            re_diff = 0
        if tuple_1[4] < 8 and tuple_2[4] < 8:
            if re_diff <= 1:
                re_contribut = 1 * religion
            if re_diff <= 3 and re_diff > 1:
                re_contribut = 0.70 * religion
            if re_diff > 3 and re_diff <= 6:
                re_contribut = 0.40 * religion
            if re_diff > 6:
                re_contribut = 0 * religion
    if tuple_1[5] != tuple_2[5]:
        if tuple_1[4]>=8 or tuple_2[4]>=8:
            re_contribut = 0.5 * religion
            re_diff = 0
        if tuple_1[4] < 8 and tuple_2[4] < 8:
            if re_diff <= 1:
                re_contribut = 1 * religion
            if re_diff <= 3 and re_diff > 1:
                re_contribut = 0.70 * religion
            if re_diff > 3 and re_diff <= 6:
                re_contribut = 0.40 * religion
            if re_diff > 6:
                re_contribut = 0 * religion
    total_match = (a_contribut + f_contribut + e_contribut + r_contribut + p_contribut + pl_contribut + re_contribut) * 100.0
    # return total_match
    print(f"The match percentage of these two people is {total_match}%.")
'''
    print(f"a_contribut = {a_contribut}")
    print(f"f_contribut = {f_contribut}")
    print(f"e_contribut = {e_contribut}")
    print(f"r_contribut = {r_contribut}")
    print(f"p_contribut = {p_contribut}")
    print(f"pl_contribut = {pl_contribut}")
    print(f"re_contribut = {re_contribut}")
'''

main()