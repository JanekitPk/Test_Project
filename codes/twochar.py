def alternate(s):
  chars = list(set(s))

  valid_ans = ''
  for a in chars:
    for b in chars:
      try_str = ''
      for ch in s:
        if (ch == a or ch == b) and a != b:
          if len(try_str) <= 0 or try_str[-1] != ch:
            try_str += ch
          else:
            try_str = ''
            break
      
      if len(try_str) > 1 and len(try_str) > len(valid_ans):
        valid_ans = try_str

  return len(valid_ans)