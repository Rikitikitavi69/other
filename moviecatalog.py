"""
Маша хочет создать каталог своих любимых фильмов. В этом каталоге ей нужны операции добавления и удаления фильма.

Еще она хочет получать название случайного фильма (с равномерным распределением) из каталога.
При этом все методы должны работать быстро — в среднем за O(1).

На Java интерфейс такого каталога может выглядеть так:
public interface MovieCatalog {
    // Добавляет фильм в каталог, возвращает true, если фильм до добавления не был в каталоге
    public boolean add(String movie);

    // Удаляет фильм из каталога, возвращает true, если фильм был в каталоге
    public boolean remove(String movie);

    // Возвращает имя случайного фильма
    public String getRandomMovie();

}
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
"""
import random

class MovieCatalog:

    def __init__(self):
        self.catalog = set()

    def add(self, movie):
        if movie in self.catalog:
            return False
        else:
            self.catalog.add(movie)
            return True

    def remove(self, movie):
        if movie in self.catalog:
            self.catalog.remove(movie)
            return True
        else:
            return False

    def getRandomMovie(self):
        return list(self.catalog)[int(random.randint(0, len(self.catalog)-1))]
