def test_hypot():
  assert hypot(3,4) == 5
  
def test_hypot1():
   print hypot(0, 0) == 0
    
def test_hypot2():
   print hypot(-1, 1) == 0
    
def test_hypot3():
  print hypot(-2, 0) == 2 ** 0.5

test_hypot1()
test_hypot2()
test_hypot3()
