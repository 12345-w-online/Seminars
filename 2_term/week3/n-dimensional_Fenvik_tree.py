import numpy as np
from itertools import combinations


class FT:
    def __init__(self, data: np.ndarray) -> None:
        self.old_data = np.array(data)
        self.data = self.build_data(data)

    def build_data(self, data: np.ndarray) -> None:
        if isinstance(data[1], (np.ndarray, list)):
            for index in range(data.shape[0] - 1, -1, -1):
                sub_ft = FT(np.array(data[index]))
                data[index] = sub_ft.get_array()
        for index_elem in range(data.shape[0] - 1, -1, -1):
            for index in range(self.f_function(index_elem), index_elem):
                data[index_elem] = data[index_elem] + data[index]
        return data

    def f_function(self, i: int) -> int:
        return i & (i + 1)

    def calculate(self, array_cords_st: np.ndarray, array_cords_fin: np.ndarray) -> int:
        array_cords_fin = array_cords_fin - 1
        sum_to_return = 0
        for count_index_replace in range(len(array_cords_st) + 1):
            if count_index_replace % 2 == 0:
                sign = "+"
            else:
                sign = "-"
            indexs_replacement = list(map(list, combinations(range(len(array_cords_st)), count_index_replace)))
            for index_replace in indexs_replacement:
                array_for_sum = np.array(array_cords_st)
                if index_replace != []:
                    for index in index_replace:
                        array_for_sum[index] = array_cords_fin[index]

                if sign == "+":
                    sum_to_return += self.calculate_to_st(array_for_sum)
                    # print("+", self.calculate_to_st(array_for_sum))
                else:
                    sum_to_return -= self.calculate_to_st(array_for_sum)
                    # print("-", self.calculate_to_st(array_for_sum))
        return sum_to_return

    def calculate_to_st(self, array_cords_st: np.ndarray) -> int:
        now_array_cords = np.array(array_cords_st)
        sum_cube = 0
        last_index = array_cords_st.shape[0] - 1
        while now_array_cords[0] >= 0:
            zeros_index = np.where(now_array_cords == -1)[0]
            if zeros_index.shape[0] != 0:
                index_replace = zeros_index[0] - 1
                now_array_cords[index_replace] = self.f_function(now_array_cords[index_replace]) - 1
                now_array_cords[zeros_index[0]] = array_cords_st[zeros_index[0]]
                # print(now_array_cords)
            else:
                sum_cube += self.data[tuple(now_array_cords)]
                now_array_cords[last_index] = self.f_function(now_array_cords[last_index]) - 1
                # print(now_array_cords)
        return sum_cube

    def update(self, array_cords_update: np.ndarray, new_value: int) -> None:
        self.old_data[tuple(array_cords_update)] = new_value
        data = np.array(self.old_data)
        self.data = self.build_data(data)

    def get_array(self) -> np.ndarray:
        return self.data

    def get_old_data(self) -> np.ndarray:
        return self.old_data


# Tests
a = FT(np.array([np.array([np.array([1, 2, 5, 6, 2, 3, 4, 7]) for _ in range(8)]) for __ in range(8)]))
print(a.get_array())
print(a.calculate_to_st(np.array([1, 2, 3])))
print(a.calculate_to_st(np.array([5, 4, 4])))
print(a.calculate(np.array([5, 4, 4]), np.array([1, 1, 1])))
a.update(np.array([1, 1, 1]), 10)
print(a.get_array())
print(a.calculate_to_st(np.array([1, 2, 3])))
print(a.calculate_to_st(np.array([5, 4, 4])))
print(a.calculate(np.array([5, 4, 4]), np.array([1, 1, 1])))
