class student():
    def s_kto_ya(self):
        print("Я клас - студент")


class group(student):
    def __init__(self, _mark):
        self.my_mark = _mark

    def read_mark(self):
        print("Моя оцінка: %s" % self.my_mark)

    def write_mark(self, new_mark):
        self.my_mark = new_mark

    def num(self):
        print("Я підклас - група")


fzf51 = group(5)  # my_mark = 5
fzf51.s_kto_ya()  # Я підклас - група
fzf51.num()
fzf51.read_mark()
fzf51.write_mark(4)
fzf51.read_mark()
print("")
fzf52 = group(3)
fzf52.read_mark()
