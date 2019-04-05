# ITERATION
#
# for x in [1, 2, 3]:
#     print(x)
#
#
#





# class CounterIterator:
#     def __init__(self):
#         self.current = 0
#
#     def __next__(self):
#         # pass
#         self.current += 1
#         return self.current
#
#
# if __name__ == '__main__':
#     c = CounterIterator()
#     print(next(c))
#     print(next(c))
#     print(next(c))

#     >> 1
#     >> 2
#     >> 3







# class MaxCounterIterator:
#     def __init__(self, max_num):
#         self.start_num = 0
#         self.max = max_num
#
#     def __next__(self):
#         if self.start_num >= self.max:
#             print('😰')
#             raise StopIteration
#         self.start_num += 1
#         return self.start_num
#
#     def __iter__(self):
#
# #
# #
# #
# if __name__ == '__main__':
#     c = MaxCounterIterator(3)
    # print(next(c))
    # print(next(c))
    # print(next(c))
    # print(next(c))




# class MaxCounterIterable:
#     def __init__(self, max_num):
#         self.start_num = 0
#         self.max = max_num
#
#     def __next__(self):
#         if self.start_num >= self.max:
#             print('😰')
#             raise StopIteration
#         self.start_num += 1
#         return self.start_num
#
#     def __iter__(self):
#         return self
#
# if __name__ == '__main__':
#     our_iterable = MaxCounterIterable(3)
#     # our_iterator = iter(our_iterable)
#     # print(next(our_iterator))
#     # print(next(our_iterator))
#     # print(next(our_iterator))
#     # print(next(our_iterator))
#     for num in our_iterable:
#         print(num)
#
#
#
#



# 1, 1, 2, 3, 5, 8, 13, ...
#
# class FibIter:
#     def __init__(self):
#         self.prev = 0
#         self.curr = 1
#
#     def __next__(self):
#         val = self.curr
#         self.curr = self.prev + self.curr
#         self.prev = val
#         return val
#         # todo
#
# #
# if __name__ == '__main__':
#     f = FibIter()
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))









# iterable_counter = IterableCounter(3)
# next(iterable_counter)
# 1
# next(iterable_counter)
# 2
# next(iterable_counter)
# 3
# next(iterable_counter)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "<input>", line 9, in __next__
# StopIteration

# class IterableCounter:
#     def __init__(self, max):
#         pass
#
#     def __next__(self):
#         pass
#
#     def __iter__(self):
#         pass

#
# if __name__ == '__main__':
#     iterable_counter = IterableCounter(3)
#     next(iterable_counter)
#     next(iterable_counter)
#     next(iterable_counter)
#     next(iterable_counter)







# class MaxCounterIterable:
#     def __init__(self, max_num):
#         self.start_num = 0
#         self.max = max_num
#
#     def __next__(self):
#         if self.start_num >= self.max:
#             print('😰')
#             raise StopIteration
#         self.start_num += 1
#         return self.start_num
#
#     def __iter__(self):
#         return self
#

class ReverseIter:
    def __init__(self, our_list):
        self.our_list = our_list
        self.curr_idx = len(our_list)

    def __next__(self):
        if self.curr_idx <= 0:
            raise StopIteration
        self.curr_idx -= 1
        return self.our_list[self.curr_idx]

    def __iter__(self):
        return self



if __name__ == '__main__':
    # for el in ReverseIter([1, 2, 3]):
    #     print(el)
    print(list(ReverseIter([1, 2, 3])))

