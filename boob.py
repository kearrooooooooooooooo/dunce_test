from string import ascii_letters

def letter_increment(s):
    news = ''
    for x in s:
        if x in ascii_letters:
            news = news+ascii_letters[(ascii_letters.index(x)+1)%len(ascii_letters)]
        else:
            news+=x
    return news

print(letter_increment("anna"))
