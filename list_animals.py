def list_animals(animals):
    '''Your collegue wrote an simple loop to list his favourite animals. 
But there seems to be a minor mistake in the grammar, which prevents the program to work. Fix it! :)
If you pass the list of your favourite animals to the function, you should get the 
list of the animals with orderings and newlines added.'''
    list = ''
    b = 0
    for i in animals:
        b += 1
        list += str(b) + '. ' + i + '\n'
    return list