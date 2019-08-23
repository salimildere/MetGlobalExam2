def error_handler():
    try:
        name = int('1232a')
        lastname = ['yilmaz', 'keskin'][3]
        other_dict = {"name": "merve", "lastname": "demir"}
        other_name = other_dict['other_name']
        age = 1 / 0
        print('OK!')
    except (ValueError, IndexError, KeyError, ZeroDivisionError):
        print('Error')
    '''
    Exception icerisinde sadece bir error tipi tanimlamak daha dogru olacaktir. Bu sebepten dogru olan asagidaki gibidir
    try:
        name = int('1232a')
    except ValueError:
        print('ValueError')

    try:
        lastname = ['yilmaz', 'keskin'][3]
    except IndexError:
        print('IndexError')
    try:
        other_dict = {"name": "merve", "lastname": "demir"}
        other_name = other_dict['other_name']
    except KeyError:
        print('KeyError')

    try:
        age = 1 / 0
        print('OK!')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    '''

error_handler()



