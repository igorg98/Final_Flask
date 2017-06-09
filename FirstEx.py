import math
letters = \
    {
        'a':
            [
                "   A   ",
                "  A A  ",
                " A   A ",
                "A     A",
                "AAAAAAA",
                "A     A",
                "A     A"
            ],
        'b':
            [
                "BBBBBB ",
                "B     B",
                "B     B",
                "BBBBBB ",
                "B     B",
                "B     B",
                "BBBBBB "
            ],
        'c':
            [
                " CCCCC ",
                "C     C",
                "C      ",
                "C      ",
                "C      ",
                "C     C",
                " CCCCC "
            ],
        'd':
            [
                "DDDDDD ",
                "D     D",
                "D     D",
                "D     D",
                "D     D",
                "D     D",
                "DDDDDD "
            ],
        'e':
            [
                "EEEEEEE",
                "E      ",
                "E      ",
                "EEEEEEE",
                "E      ",
                "E      ",
                "EEEEEEE"
            ],
        'f':
            [
                "FFFFFFF",
                "F      ",
                "F      ",
                "FFFF   ",
                "F      ",
                "F      ",
                "F      "
            ],
        'g':
            [
                " GGGGG ",
                "G     G",
                "G      ",
                "G      ",
                "G  GGGG",
                "G     G",
                " GGGGGG"
            ],
        'h':
            [
                "H     H",
                "H     H",
                "H     H",
                "HHHHHHH",
                "H     H",
                "H     H",
                "H     H"
            ],
        'i':
            [
                "IIIIIII",
                "   I   ",
                "   I   ",
                "   I   ",
                "   I   ",
                "   I   ",
                "IIIIIII"
            ],
        'j':
            [
                "JJJJJJJ",
                "      J",
                "      J",
                "      J",
                "      J",
                "J     J",
                " JJJJJ "
            ],
        'k':
            [
                "K    KK",
                "K   K  ",
                "K  K   ",
                "KKK    ",
                "K  K   ",
                "K   K  ",
                "K    KK"
            ],
        'l':
            [
                "L      ",
                "L      ",
                "L      ",
                "L      ",
                "L      ",
                "L      ",
                "LLLLLLL"
            ],
        'm':
            [
                "M     M",
                "MM   MM",
                "M M M M",
                "M  M  M",
                "M     M",
                "M     M",
                "M     M"
            ],
        'n':
            [
                "N     N",
                "NN    N",
                "N N   N",
                "N  N  N",
                "N   N N",
                "N    NN",
                "N     N"
            ],
        'o':
            [
                " OOOOO ",
                "O     O",
                "O     O",
                "O     O",
                "O     O",
                "O     O",
                " OOOOO "
            ],
        'p':
            [
                "PPPPPP ",
                "P     P",
                "P     P",
                "PPPPPP ",
                "P      ",
                "P      ",
                "P      "
            ],
        'q':
            [
                " QQQQQ ",
                "Q     Q",
                "Q     Q",
                "Q     Q",
                "Q   Q Q",
                "Q    QQ",
                " QQQQQQ"
            ],
        'r':
            [
                "RRRRRR ",
                "R     R",
                "R     R",
                "RRRRRR ",
                "R   R  ",
                "R    R ",
                "R     R"
            ],
        's':
            [
                " SSSSS ",
                "S     S",
                "S      ",
                " SSSSS ",
                "      S",
                "S     S",
                " SSSSS "
            ],
        't':
            [
                "TTTTTTT",
                "   T   ",
                "   T   ",
                "   T   ",
                "   T   ",
                "   T   ",
                "   T   "
            ],
        'u':
            [
                "U     U",
                "U     U",
                "U     U",
                "U     U",
                "U     U",
                "U     U",
                " UUUUU "
            ],
        'v':
            [
                "V     V",
                "V     V",
                "V     V",
                "V     V",
                " V   V ",
                "  V V  ",
                "   V   "
            ],
        'w':
            [
                "W     W",
                "W     W",
                "W     W",
                "W  W  W",
                "W W W W",
                "WW   WW",
                "W     W"
            ],
        'x':
            [
                "X     X",
                " X   X ",
                "  X X  ",
                "   X   ",
                "  X X  ",
                " X   X ",
                "X     X"
            ],
        'y':
            [
                "Y     Y",
                "Y     Y",
                " Y   Y ",
                "  Y Y  ",
                "   Y   ",
                "   Y   ",
                "   Y   "
            ],
        'z':
            [
                "ZZZZZZZ",
                "     Z ",
                "    Z  ",
                "   Z   ",
                "  Z    ",
                " Z     ",
                "ZZZZZZZ"
            ],
        ' ':
            [
                "       ",
                "       ",
                "       ",
                "       ",
                "       ",
                "       ",
                "       "
            ]
    }

def TrbuttunClicked(bukovi):
    bukovi = str(bukovi).lower()
    output = ""
    CBukovi = math.ceil(len(bukovi) / 12)
    B = 0
    try:
        for l in range(CBukovi):
            for j in range(7):
                for i in bukovi[12 * B:12 * (B + 1)]:
                    output += letters[i][j] + " "
                output += "\n"
            output += "\n"
            B += 1
        return output


    except LookupError:
        return "WRONG SYMBOL! YOU RUINED IT! IT'S YOUR FAULT"
    except TypeError:
        return "I SEE SOME MISTAKES HERE"