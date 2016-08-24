"""
Author      : Fabio Lenine Vilela da Silva
Objective   : Count words in a sentence, whose return will be by quantitative descrecente order and in the case of a tie in order Alphabetic
App         : count_words.py
"""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    lista = s.lower().split(" ")
    lista.sort()
    result = []

    # TODO: Count the number of occurences of each word in s
    for i in range(len(lista)):
        quant = sum(x.count(lista[i]) for x in result)
        if quant == 0:
            result += [(lista[i],lista.count(lista[i]))]

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    top_n = sorted(result, key=lambda tup: tup[1], reverse=True)
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n[:n]

def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))

if __name__ == '__main__':
    test_run()