import random


def move(possibility):
    rnd = random.random()
    if rnd < possibility:
        return True
    else:
        return False


if __name__ == '__main__':
    sample_num = 1000000
    query1 = 0
    query2 = 0
    query3_numerator = 0
    query3_denominator = 0
    query4_numerator = 0
    query4_denominator = 0
    query5_numerator = 0
    query5_denominator = 0
    for a in range(sample_num):
        result_a = move(0.2)
        if result_a is True:
            pos_b = 0.8
            pos_c = 0.2
        else:
            pos_b = 0.2
            pos_c = 0.05
        result_b = move(pos_b)
        result_c = move(pos_c)
        if result_b is True and result_c is True:
            pos_d = 0.8
            pos_e = 0.8
        elif result_b is True and result_c is False:
            pos_d = 0.8
            pos_e = 0.6
        elif result_b is False and result_c is True:
            pos_d = 0.8
            pos_e = 0.8
        elif result_b is False and result_c is False:
            pos_d = 0.05
            pos_e = 0.6
        result_d = move(pos_d)
        result_e = move(pos_e)
        # The result of the query 1 is added below with query1 counter.
        # If the D node is True, then increment query1 counter.
        if result_d is True:
            query1 += 1
        # The result of the query 2 is added below with query2 counter.
        # If the node D is True and the node A is False, then increment query1 counter.
        if result_a is False and result_d is True:
            query2 += 1
        # The result of the query 3 can be found via query3_numerator counter and query3_denominator counter.
        # If the node B is False, then increment the denominator. Also, if the node E is True when B is False,
        # then increment the query3_numerator counter.
        if result_b is False:
            query3_denominator += 1
            if result_e is True:
                query3_numerator += 1
        # The result of the query 4 can be found via query4_numerator counter and query4_denominator counter.
        # If the node E is False and the node D is True, then increment query4_denominator. Also, if the node A is True
        # when the node E and the node D are True, then increment the query4_denominator counter.
        if result_e is False:
            if result_d is True:
                query4_denominator += 1
                if result_a is True:
                    query4_numerator += 1
        # The result of the query 5 can be found via query5_numerator counter and query5_denominator counter.
        # If the node A is False, then increment the query5_denominator. If the node E is False and the node B is True
        # when the node B is True, then increment the query5_numerator counter.
        if result_a is True:
            query5_denominator += 1
            if result_e is False:
                if result_b is True:
                    query5_numerator += 1

    print("P(D) = " + str(query1 / sample_num))
    print("P(D,-A) = " + str(query2 / sample_num))
    print("P(E|-B) = " + str(query3_numerator / query3_denominator))
    print("P(A|D,-E) = " + str(query4_numerator / query4_denominator))
    print("P(B,-E|A) = " + str(query5_numerator / query5_denominator))
