#!/usr/bin/python3
def delete_at(my_list=[], idx=3):
    if idx < 0 or idx >= len(my_list):
        return my_list[idx]
    del my_list[idx]
    return my_list
