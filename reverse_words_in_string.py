
## method1
def reverse_words_in_string(s):
    return " ".join(s.split()[::-1])
print(reverse_words_in_string("hello vinod"))

## method2: with out using builtins

def reverse_words_in_string(s):
    temp = ""
    words = []
    for char in s:
        if char != " ":
            temp += char
        else:
            words.append(temp)
            temp = ""
    words.append(temp)
    return " ".join(words[::-1])

        
 