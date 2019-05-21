def duplicate_ele(ele_list):
    new_list = []
    for x in ele_list:
        if x is not ele_list:
            new_list.append(x)
        return new_list



ele_list = [5, 9, 6, 8, 5, 2]
print("original elements List:", ele_list)
print("duplicate elements :", duplicate_ele(ele_list))

