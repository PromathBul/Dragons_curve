from turtle import *

def dracons_curve(txt, n):
  if n < 0:
    return ''
  elif n == 0:
    return txt.replace('a', '').replace('b', '')
  else:
    return dracons_curve(''.join(('aRbFR' if i == 'a' else ('LFaLb' if i == 'b' else i)) for i in txt), n - 1)

def draw (txt):
  # Установка курсора для n = 15 и шага со значением 2
  # penup()
  # goto(0, -200)
  # pendown()
  bgcolor('black')
  color('red')
  speed(10)
  for item in txt:
      if item == 'L':
        left(90)
      elif item == 'R':
        right(90)
      else:
        forward(2)
  done()

txt = dracons_curve('Fa', 15)
draw(txt)