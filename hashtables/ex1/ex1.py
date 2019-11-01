#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        #hash_table_remove,
                        hash_table_retrieve,)
                        #hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    ret  = None
    for i,j in enumerate(weights):
        hash_table_insert(ht,j,i)

    for i,j in enumerate(weights):
        #hash_table_remove(ht,j)
        a = hash_table_retrieve(ht,int(limit-j))
        if a is not None and i!=a:
            ret =  (max(a,i),min(a,i))
            #print(ret,type(ret))
        else:
            continue


    return ret


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
