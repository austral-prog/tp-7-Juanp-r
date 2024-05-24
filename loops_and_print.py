def enumerate_list(list):
    temp_list = []
    for elemento in list:
        if elemento != "":
            temp_list.append(f'{len(temp_list)}. {elemento}')
    return temp_list


def enumerate_backwards(other_list):
    temp_list = []
    for index, color in enumerate(other_list):
        if other_list[index] != "":
            temp_list.append(f'{len(temp_list)}. {color[::-1]}')
    return temp_list
print(enumerate_list(list_v1))
print(enumerate_backwards(list_v2))
