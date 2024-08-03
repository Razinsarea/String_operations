user_input = input('Enter a string')

u = user_input.upper()
print('Upper case : ' + u)

L = user_input.lower()
print('Lowercase : ' + L)


#  function to count the number of vowels
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in s:
        if char in vowels:
            count = count + 1
    return count


vowels_count = count_vowels(user_input)
print('No.of vowels :', +vowels_count)


#  function to reverse the string
def string_reverse():
    opposite = user_input[::-1]
    return opposite


reversed_string = string_reverse()
print('Reversed string : ' + reversed_string)


#  function to replace space with _

def space_replace():
    cut_space = user_input.replace(' ', '_')
    return cut_space


replace_space = space_replace()
print('Space replaced : ' + replace_space)
