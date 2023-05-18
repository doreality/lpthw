class TheUntamed:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_couple_bjyx(self):
        print("博君一肖版：")
        for singer, lyric in self.lyrics:
            print(f"{singer}:\t{lyric}")

    def sing_single_wyb(self):
        print("王一博版：")
        for lyric in self.lyrics:
            print(lyric[1])

    def sing_single_xz(self):
        print("肖战版：")
        for lyric in self.lyrics:
            print(lyric[1])


theUntamedLyrics = [
    ("肖战", "闻笛声　独惆怅 云深夜未央"),
    ("王一博", "是与非　都过往　醒来了　怎能当梦一场"),
    ("肖战", "红尘中　毁誉得失如何去量"),
    ("合", "萧萧血热刀锋凉"),
    ("肖战", "山高水远"),
    ("王一博", "又闻琴响"),
    ("合", "陈情未绝　卧荻花月如霜"),
    ("肖战", "煮一壶生死悲欢　祭少年郎　明月依旧何来怅惘"),
    ("王一博", "不如潇潇洒洒　历遍风和浪"),
    ("合", "天涯一曲共悠扬"),
    ("王一博", "穿万水　过千山路尽人茫茫"),
    ("肖战", "是与非　都过往　醒来了　就当它梦一场"),
    ("王一博", "红尘中　毁誉得失如何去量"),
    ("合", "萧萧血热刀锋凉"),
    ("王一博", "山高水远"),
    ("肖战", "又闻琴响"),
    ("合", "陈情未绝　笑世事多无常"),
    ("王一博", "煮一壶生死悲欢　祭少年郎　明月依旧何来怅惘"),
    ("肖战", "不如坦坦荡荡　历遍风和浪"),
    ("合", "天涯一曲共悠扬"),
    ("王一博", "煮一壶生死悲欢　祭少年郎　明月依旧何来怅惘"),
    ("肖战", "不如坦坦荡荡　历遍风和浪"),
    ("合", "天涯一曲共悠扬　天涯一曲共悠扬")
]

theUntamed = TheUntamed(theUntamedLyrics)

theUntamed.sing_couple_bjyx()
print('-' * 10)
theUntamed.sing_single_wyb()
print('-' * 10)
theUntamed.sing_single_xz()
