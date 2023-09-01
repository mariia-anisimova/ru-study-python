from functools import reduce
from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран

        """

        def filter_movies(movies: dict) -> float:
            number_of_countries: int = movies['country'].count(',') + 1
            if movies['rating_kinopoisk'] != '' and float(movies['rating_kinopoisk']) != 0 and number_of_countries >= 2:
                return float(movies['rating_kinopoisk'])

        filtered_rating_kinopoisk = map(filter_movies, list_of_movies)
        rating_kinopoisk_list = [rating for rating in filtered_rating_kinopoisk if rating is not None]
        average_rating_kinopoisk = sum(rating_kinopoisk_list)/len(rating_kinopoisk_list)

        return average_rating_kinopoisk

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def filter_movies(movies: dict, rating: Union[float, int]) -> int:
            print('ok')
            if movies['rating_kinopoisk'] != '' and float(movies['rating_kinopoisk']) >= float(rating):
                print('good')
                count_of_letters: int = 0
                for letter in movies['name']:
                    if letter.lower() == 'и':
                        count_of_letters += 1
                return count_of_letters

        list_count_of_letters_i = map(lambda movies: filter_movies(movies, rating), list_of_movies)
        print(list_count_of_letters_i)

        return reduce((lambda x, y: x+y), list_count_of_letters_i)






