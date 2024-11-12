for i in range(99):
    m="fizz" if i%3==0 else ""+"buzz" if i%5==0 else ""
    if m:print(f"{i}: {m}")