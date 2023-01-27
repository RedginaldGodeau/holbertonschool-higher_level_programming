#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for i in range(list_length):
        rep = 0
        try:
            rep = my_list_1[i] / my_list_2[i]
        except TypeError:
            rep = 0
            print("wrong type")
        except ZeroDivisionError:
            rep = 0
            print("division by 0")
        except IndexError:
            rep = 0
            print("out of range")
        except:
            rep = 0
        finally:
            new_list.append(rep)
    return new_list
