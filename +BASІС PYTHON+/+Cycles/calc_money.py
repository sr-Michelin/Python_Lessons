import sys

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['D:\\Games\\PythonProject', 'D:/Games/PythonProject'])

ti = 0
found_coins = 0
ad_coins = 0
ad_coins_ex = 0
used_coins = 0
coins = found_coins

# print(found_coins+ti*(ad_coins_from_work+ad_coins-used_coins))

for i in range(0, ti):
    coins = coins + ad_coins + ad_coins_ex - used_coins
    print('Місяць {0}, {1} гривень. '.format(i + 1, coins))

