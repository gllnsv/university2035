
# def strcounter(s):
#     for sym in s:
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)
#
# s = 'aaabc'
# strcounter(s)

#
# s = 'aaabc'
#
# def strcounter(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)
#
# s = 'aaabc'
# strcounter(s)

def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    print('hello!')
    print(syms_counter)

strcounter('aaabca')

def func(c):
    if c==c[::-1]:
        return True
    else:
        return False

print(func('шалаш'))