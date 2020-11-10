## https://book.apeland.cn/details/157/
class ShenXian:
    """神仙类"""
    def fly(self):
        print("神仙都会飞...")

    def fight(self):
        print("神仙在打架...")


class Monkey:
    def eat_peach(self):
        print("猴子都喜欢吃桃子...")

    def fight(self):
        print("猴子在打架...")


class MonkeyKing(ShenXian, Monkey):
    def play_goden_stick(self):
        print("孙悟空玩金箍棒...")


sxz = MonkeyKing()
sxz.eat_peach()
sxz.fly()
sxz.play_goden_stick()
sxz.fight()