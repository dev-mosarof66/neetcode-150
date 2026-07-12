from typing import List



def sort_words(words: List[str]) -> List[str]:
    sorted_words = words.copy()
    sorted_words.sort(key= lambda word: len(word),reverse=True)
    return sorted_words
    pass

def sort_numbers(numbers: List[int]) -> List[int]:
    sorted_nums = numbers.copy()
    sorted_nums.sort(key=lambda num: abs(num),reverse=False)
    return sorted_nums
    pass


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
