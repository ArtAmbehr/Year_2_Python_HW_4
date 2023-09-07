# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def dictionary_key(data):
    new_dictionary = {}
    if type(data) == list or type(data) == bytearray or type(data) == dict or type(data) == frozenset:
        new_dictionary[str(data)] = type(data)
        return new_dictionary
    else:
        new_dictionary[data] = type(data)
        return new_dictionary


print(dictionary_key({3:4}))
