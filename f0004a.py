név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') 
kor = int(kor) 
születési_év = 2020 - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')
érettségi_év = születési_év + 18
print(név, ', kend ', érettségi_év, '-ban érettségizik.', sep='')