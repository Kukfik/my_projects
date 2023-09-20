# eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# def data():
#     s = "Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd."
#     choice = int(input("input shifr or not (1,2) > "))
#     alp = int(input("input lang (1-rus, 2-eng) > "))
#     n = int(input("chag sdviga > "))
#     ss = [s, choice, alp, n]
#     return ss

# def shifr(li):
#     s, choice, alp, n = li
#     s=list(s)
#     l=[]
#     if choice == 1 and alp ==1:
#         for i in s:
#             if i.islower():
#                 k = rus_lower_alphabet.find(i)
#                 t = rus_lower_alphabet[(k+n)%32]
#                 l.append(t)
#             elif i.isupper():
#                 k = rus_upper_alphabet.find(i)
#                 t = rus_upper_alphabet[(k+n)%32]
#                 l.append(t)
#             else:
#                 l.append(i)
                
#     if choice == 1 and alp == 2:
#         for i in s:
#             if i.islower():
#                 k = eng_lower_alphabet.find(i)
#                 t = eng_lower_alphabet[(k+n)%25]
#                 l.append(t)
#             elif i.isupper():
#                 k = eng_upper_alphabet.find(i)
#                 t = eng_upper_alphabet[(k+n)%25]
#                 l.append(t)
#             else:
#                 l.append(i)
#     return l


# def reshifr(li):
#     s, choice, alp, n = li
#     s = list(s)
#     l = []
#     if  alp == 1:
#         for i in s:
#             if i.islower():
#                 k = rus_lower_alphabet.find(i)
#                 t = rus_lower_alphabet[(k-n)%32]
#                 l.append(t)
#             elif i.isupper():
#                 k = rus_upper_alphabet.find(i)
#                 t = rus_upper_alphabet[(k-n)%32]
#                 l.append(t)
#             else:
#                 l.append(i)

#     if alp==2:
#         for i in s:
#             if i.islower():
#                 k = eng_lower_alphabet.find(i)
#                 t = eng_lower_alphabet[(k-n)%25]
#                 l.append(t)
#             elif i.isupper():
#                 k = eng_upper_alphabet.find(i)
#                 t = eng_upper_alphabet[(k-n)%25]
#                 l.append(t)
#             else:
#                 l.append(i)
#     return l


# f = data()
# if f[1] == 1:
#     d = "".join(shifr(f))

# elif f[1] == 2:
#     d = "".join(reshifr(f))
# print(d)

def data():
    s = "Day, mice. 'Year' is a mistake!"
    ch_shifr = "shifr"
    lang = "eng"
    n = int(input("input the number of your shift > "))
    if ch_shifr == "shifr" or ch_shifr == "not" and lang == "rus" or lang == "eng":
        if lang == "rus":
            lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
            upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        elif lang == "eng":
            lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
            upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return s, ch_shifr, lower_alphabet, upper_alphabet,n
    else: 
        return "please, check the input and try again"

s, ch_shifr, low, up, n = data()
new = []

def shifr(new):
    for i in list(s):
        if i.islower():
            f = low.find(i) 
            if ch_shifr == "shifr":
                shift = low[(f + n) % len(low)]
            else:
                shift = low[(f-n) % len(low)]
        elif i.isupper():
            f = up.find(i)
            if ch_shifr == "shifr":
                shift = up[(f + n) % len(up)]
            else:
                shift = up[(f-n) % len(up)]
        else:
            shift = i
        new.append(shift)
    new = ''.join(new)
    return new

print(shifr(new))