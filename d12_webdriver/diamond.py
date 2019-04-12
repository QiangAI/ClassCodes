#
# r = 10
# for y in range(2 * r + 1):
#     for x in range(2 * r + 1):
#         if y >= x - r and y <= x + r and y >= -x + r and y <= -x + 3 * r:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


r = 10
for y in range(1, r):
    for x in range(1, r):
        if y >= - x + r:
            print(F'{y}*{x}={x*y:2d} ', end='')
        else:
            print('       ', end='')
    print()
