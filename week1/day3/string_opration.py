def reverse(n):   
    reverse_text = ''.join(reversed(n))
    return reverse_text

def count_vowels(n):
    a = 0
    i = 0
    u = 0
    e = 0
    o = 0
    for char in n:
        if char == 'a':
            a += 1
        elif char == 'i':
            i+= 1
        elif char == 'u':
            u += 1
        elif char == 'e':
            e += 1
        elif char == 'o':
            o += 1
    
    result = f"a = {a}, i = {i}, u = {u}, e = {e}, o = {o}"
    return result

def check_palindrome(n):
    if n == reverse(n):
        palindrome = True
    else:
        palindrome = False
    return palindrome
        

# n = "aku makan"
# print(reverse(n))
# print()
# print(count_vowels(n))
# print()
# print(check_palindrome(n))


