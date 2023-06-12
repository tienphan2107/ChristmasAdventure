

map1 = [
    '                                                                      ',
    '                                                     9                ',
    '                                7      0       8 0   213             G',
    '           0T 23       9   8  T2113   2113    2113     53         0  1',
    '          21114513    23   2111466513    513     513             23   ',
    'P 9 8 0   466666653 7 453                              9              ',
    '21111113  66666666513                         1   8 0T 23            1',
    '46666665               9  23 8      0     23  6 211111145  8   7  23 6',
    '66666666            0  2114513      23 1  45  6 466666666  23  23 45 6',
    '66666666  9     7 T 211466666513  1 45 6  66  6 666666666  45  45 66 6',
    '66666666  213  21111466666666665  6 66 6  66  6 666666666  66  66 66 6',
]

map = [
    '                                                  ',
    '                                                  ',
    '                                              G   ',
    '                   8         9             9  23  ',
    '          0  1    213 7     213           213     ',
    '       8 23   7       23         8T  23  24      2',
    ' P    23      23 T              2113           214',
    '  8       7 2145113 0     7              T 7 21466',
    '2113  8T9211466666513 7   23          9 2111146666',
    '4665 21114666666666651113 45  0 7     214666666666',
    '6666 46666666666666666665 66 21113  21466666666666'
]

tile_size = 64  # kích thước 1 block 64x64
screen_width = 1200
screen_height = len(map) * tile_size  # 11 * 64

tile_directory = {
    '1': 'graphics/block/snow.png',
    '2': 'graphics/block/leftsnow.png',
    '3': 'graphics/block/rightsnow.png',
    '4': 'graphics/block/leftbottomsnow.png',
    '5': 'graphics/block/rightbottomsnow.png',
    '6': 'graphics/block/bottomsnow.png',
    '7': 'graphics/decorate/snowman.png',
    '8': 'graphics/decorate/sign.png',
    '9': 'graphics/decorate/tree.png',
    '0': 'graphics/decorate/combotree.png'
}

