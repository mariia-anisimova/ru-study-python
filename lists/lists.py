class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """

        if input_list:
            max_numb = input_list[0]
            for value in input_list[1:]:
                if value > max_numb:
                    max_numb = value

            for position, value in enumerate(input_list):
                if value > 0:
                    input_list[position] = max_numb

        return input_list

    @staticmethod
    def binary_search(sorted_list: list[int], left: int, right: int, query: int) -> int:
        if left > right:
            return -1
        mid = (left + right) // 2
        if query == sorted_list[mid]:
            return mid
        elif query < sorted_list[mid]:
            return int(ListExercise.binary_search(sorted_list, left, mid - 1, query))
        else:
            return int(ListExercise.binary_search(sorted_list, mid + 1, right, query))

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        if input_list:
            input_list.sort()
            left, right = 0, len(input_list) - 1
            index = ListExercise.binary_search(input_list, left, right, query)
            return index
        else:
            return -1
