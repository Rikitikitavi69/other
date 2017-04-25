"""
У Маши есть список ее любимых фильмов, но они хранятся в необычной структуре — списке списков,
которые могут иметь произвольную вложенность.

Она хочет преобразовать их в простой плоский список.

Например, такой список

["a", ["b", "c", ["d"], "e"]]

превратить в такой

["a", "b", "c", "d", "e"].

Интерфейс списка списков на Java выглядит так:
public interface NestedList {

     // @return true если данный элемент содержит название фильма, а не список
     public boolean isName();

     // @return возвращает название фильма, если элемент содержит название, иначе null
     public String getName();

     // @return the nested list that this NestedInteger holds, if it holds a nested list
     // Return null if this NestedInteger holds a single integer
     public List getList();
 }
"""


def nested2flat(lst):
    flat_list = []
    for i in range(len(lst)):
        if type(lst[i]) == list:
            flat_list.extend(nested2flat(lst[i]))
        else:
            flat_list.append(lst[i])
    return flat_list

