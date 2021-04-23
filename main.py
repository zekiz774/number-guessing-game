import random
rdn_nbr=random.randint(0,10)
i=0
outpt='false'


def ifst(rdn_nbr, inp):
    if rdn_nbr > inp:
        outpt='to low'
    elif rdn_nbr < inp:
        outpt='to high'
    elif rdn_nbr==inp:
        outpt='correct'
      
    print(outpt)
    return outpt


while True:
  inp=input('>')
  try:
    inp=int(inp)
    if ifst(rdn_nbr,inp) == 'correct':
      break
    i+=1
  except:
    print('invalid input')


print(f'You needed {i} tries')