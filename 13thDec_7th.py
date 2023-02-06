import numpy as np

numbers_1 = np.arange(1,6)

numbers_1 = numbers_1[1]*20

numbers_2 = numbers_1.view()

print(numbers_2)
