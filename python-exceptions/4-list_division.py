#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except TypeError as err:
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError as err:
            new_list.append(0)
            print("division by 0")
        except IndexError as err:
            new_list.append(0)
            print("out of range")
        finally:
            return (new_list)
