data_list_in_dict = [{
    "name": "ahmet",
    "lastname": "yilmaz"
}]

data_list_in_tuple = [('name', 'mehmet'), ('lastname', 'yilmaz')]
data_list_in_list = [['name', 'aysel'], ['lastname', 'yilmaz']]

data_tuple_in_tuple = (('name', 'mesut'), ('lastname', 'oncel'))
data_tuple_in_list = (['name', 'serkan'], ['lastname', 'inan'])


def tutorial_talent(data) -> list:
    data_output = []
    # Gelen data icerisindeki tiplerde degisme olmadigi icin ilk girdiye bakilmistir. Aksi takdirde uzunlugu kadar
    # dongu uzerinde donmek gerekirdi
    if type(data[0]) == dict:
        for item in data:
            temp = [value for key, value in item.items() if key == 'name']
            data_output.append(temp[0])

    elif type(data[0]) == tuple:
        temp = [item for item in data if item[0] == 'name']
        data_output.append(temp[0])

    elif type(data[0]) == list:
        temp = [item for item in data if item[0] == 'name']
        data_output.append(temp[0])

    else:
        return data_output

    return data_output



print('---- data_list_in_dict -----')
print(tutorial_talent(data_list_in_dict))


print(' --- data_list_in_tuple -----')
print(tutorial_talent(data_list_in_tuple))


print('---- data_list_in_list -----')
print(tutorial_talent(data_list_in_list))


print(' --- data_tuple_in_tuple -----')
print(tutorial_talent(data_tuple_in_tuple))


print('---- data_tuple_in_list -----')
print(tutorial_talent(data_tuple_in_list))