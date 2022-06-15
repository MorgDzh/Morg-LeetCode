# Функция Python max() возвращает самый большой элемент итерабельного объекта. Ее также можно использовать для поиска максимального значения между двумя или более параметрами.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Переменная для максимального подмассива, 0 потому что идет с начала и массив точно не пустой
        maxSubArr = nums[0]
        # Текущая сумма
        curSum = 0
        # Цикл для итераций массива (перебору чисел)
        for n in nums:
            # Если у нас есть отрицательный подмассив(подмассив может быть даже одним числом), делаю его нулем
            if curSum < 0:
                curSum = 0
            # Добавляю к сумме наш подмассив(числа или число)
            curSum += n 
            # Обновляю максимальный подмассив до максимума самого себя
            maxSubArr = max(maxSubArr, curSum)
        # Вощвращаю максимальный подмассив
        return maxSubArr
        