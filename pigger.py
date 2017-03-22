'''
Not the worst pig latin translator out there.
'''

class pigger(object):
    def translate(x):
        container = []
        vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
        initial = str(input("Please enter the word you would like translated:\n"))
        for i in initial:
            container.append(i)
        for i in container[0]:
            if i in vowels:
                container.append('way')
            else:
                pigged = str(container.pop(0) + 'ay')
                container.append(pigged)
        new_word = "".join(container)
        print(new_word)

        try_again = input("Would you like another?")
        if 'yes' in try_again:
            fresh_pig.translate()
        else:
            pass

fresh_pig = pigger()
fresh_pig.translate()
