# Дан список:
get_list = ['в', '5', 'часов', '17', 'минут',
            'температура', 'воздуха', 'была', '+5', 'градусов']

# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:

for i, el in reversed(list(enumerate(get_list))):
    el = el.replace('+' or '-', '')
    if el.isdigit():
        get_list.insert(i + 1, '"')
        get_list[i] = get_list[i].replace(el, f'{int(el):02}')
        get_list.insert(i, '"')

get_str = ' '.join(get_list)
get_str = get_str.split('"')
for i in range(1, len(get_str), 2):
    get_str[i] = get_str[i].replace(' ', '"')
get_str = ''.join(get_str)
print(get_str)