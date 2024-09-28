from  typing import Union

def func(data_structure) -> Union[int, float]:

    counter = 0
    if isinstance(data_structure, dict):
        for key,value in data_structure.items():
            counter += func(key)
            counter += func(value)

    elif isinstance(data_structure, int):
        counter += data_structure
    elif isinstance(data_structure, str):
        counter += len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        for a in data_structure:
            counter += func(a)

    return counter

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = func(data_structure)
print(result)


