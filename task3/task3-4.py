class SlugConverter:
    def __init__(self,name):
        self.slug_list=[]
        self.slug=translit_to_eng(name)
        
    def __str__(self):
        return self.slug

def translit_to_eng(s):
        a = ["a", "b", "v", "g", "d", "e", "o", "gh", "z", "i", "y", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
             "f",
             "h", "tc", "ch", "ch", "ch", "", "i", "", "e", "yu", "ya", "-"]
        b = ['а', "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у",
             "ф",
             "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]
        c = []
        d = ""
        for i in range(len(s)):
            c.append(b.index(s[i]))
        for i in range(len(c)):
            d = d + (a[c[i]])
        return d
name=input("Введите имя:")
print(SlugConverter(name))