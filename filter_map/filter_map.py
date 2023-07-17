from typing import Any, Callable, List, Tuple
from multiprocessing import Pool


class FilterMapExercise:
    @staticmethod
    def filter_arr(input_array: List[Any]) -> List[Any]:
        out_list = []
        for i in input_array:
            if i[0]:
                out_list.append(i[1])
        return out_list

    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        """
        Реализовать функцию, которая ведет себя как filter и map. К каждому значению из
        списка применяется функция, которая в ответ возвращает кортеж
        (булево значение, результат работы функции).
        Если первый элемент кортежа истина, то результат добавляется в список.

        Принимает в качестве аргументов функцию и итерируемый источник, а возвращает список.
        :param func: Функция, применяемая к каждому элементу списка.
        :param input_array: Исходный список.
        :return: Отфильтрованный список.
        """

        pool = Pool(8)
        mapped = pool.map(func, input_array)
        filtered = FilterMapExercise.filter_arr(mapped)
        return filtered
