Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> python3 print('Mijn naam is <Ryan>')
naam = '<Ryan>'
print(naam)
print(naam.upper())
print(naam[0:2])
print(naam[::-1])
SyntaxError: invalid syntax
>>> print(Mijn naam is Ryan)
naam = Ryan
print(naam)
print(naam.upper())
print(naam[0:2])
print(naam[::-1])
SyntaxError: invalid syntax
>>> print ('mijn naam is Ryan')
mijn naam is Ryan
>>> naam = 'Ryan'
>>> print(naam.upper())
RYAN
>>> print(naam[0:2])
Ry
>>> print(naam[::-1])
nayR
>>> leeftijd = 15
>>> print('Hallo ' + naam ' + ' ben je al ' + str(leeftijd) + ' jaar?')
      
SyntaxError: invalid syntax
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Ryan ben je al 15 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
16
>>> leeftijd-=1
>>> leeftijd
15
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar word je 18')
	elif leeftijd >18:
		
SyntaxError: invalid syntax
>>> elif leeftijd >18:
	
SyntaxError: invalid syntax
>>> print('Over ' + str(hoelang_tot18jaar) + ' jaar word je 18')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print('Over ' + str(hoelang_tot18jaar) + ' jaar word je 18')
NameError: name 'hoelang_tot18jaar' is not defined
>>> 
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')

    
Over 3 jaar wordt je 18
>>> elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
    
SyntaxError: invalid syntax
>>> 
>>> elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
    
SyntaxError: invalid syntax
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
    elif leeftijd > 18:
	    
SyntaxError: invalid syntax
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18-leeftijd
	print('over' + str(hoelang_tot18jaar)) + 'jaar wordt je 18')
	
SyntaxError: unmatched ')'
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18-leeftijd
	print('over' + str(hoelang_tot18jaar) + 'jaar wordt je 18')
elif leeftijd > 18:
	hoelang_al18jaar = leeftijd - 18
	print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
	print('Je bent precies ' + str(leeftijd) + ' jaar')

	
over3jaar wordt je 18
>>> from random import randint
>>> randint (0,1000)
882
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
657
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 657
>>> from datetime import datetime
>>> datum =datetime.now()
>>> print(datum)
2020-09-16 15:31:55.805321
>>> datum.strftime('%A %d %B %Y')
'Wednesday 16 September 2020'
>>> import locale
>>> locale.setlocate(locale.LC_TIME, 'nl_NL')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    locale.setlocate(locale.LC_TIME, 'nl_NL')
AttributeError: module 'locale' has no attribute 'setlocate'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 16 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')

'it_IT'
>>> datum.strftime('%A %d %B %Y')
'Mercoledì 16 Settembre 2020'
>>> 