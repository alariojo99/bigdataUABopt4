def delete_duplicates(list):
    new_list = []

    for item in list:
        if item not in new_list:
            new_list.append(item)

    return new_list

