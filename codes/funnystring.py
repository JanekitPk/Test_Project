def funny_string(text):
    reverse_text = text[::-1]
    for i in range (len(text)-1):
        difference_text = abs(ord(text[i]) - ord(text[i+1]))  
     
    for i in range (len(reverse_text)-1):
        difference_reverse_text = abs(ord(reverse_text[i]) - ord(reverse_text[i+1]))
       
    if difference_text == difference_reverse_text:
        return 'Funny'
    return 'Not Funny'