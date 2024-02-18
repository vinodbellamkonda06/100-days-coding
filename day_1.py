#python prgram to  identify the palindrom  


def validate_palindrom(input_string):
    return input_string == input_string[::-1]
    
  
 validate_palindrom("home")