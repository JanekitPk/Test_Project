def caesarCipher(s, k):
  # Write your code here
  k = k%26
  ans = ''
  for ch in s:
    if ch.isupper():
      ch = ord(ch) + k
      if ch > ord('Z'):
        ch = ord('A') + (ch - ord('Z')) - 1

    elif ch.islower():
      ch = ord(ch) + k
      if ch > ord('z'):
        ch = ord('a') + (ch - ord('z')) - 1
        
    else:
      ch = ord(ch)
    
    ans += chr(ch)
  return ans