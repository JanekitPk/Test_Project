def funny_string(s):
    reverse_text = s[::-1]
    difference_text =[]
    difference_reverse_text =[]
    for i in range (len(s)-1):
        difference_text.append(abs(ord(s[i]) - ord(s[i+1])))   
     
    for i in range (len(reverse_text)-1):
        difference_reverse_text.append(abs(ord(reverse_text[i]) - ord(reverse_text[i+1]))) 
       
    if difference_text == difference_reverse_text:
        return 'Funny'
    return 'Not Funny'