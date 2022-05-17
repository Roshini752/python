Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2572624875296
2572624875296
True
False
{(2, 3), 4, 8.9, 'a', 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
None
a = {1,2,}
a.add(100)
print(a)
{1, 2, 100}
print(a.add(1000))
None

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
1292540530464
1292540530464
True
False
{(2, 3), 4, 8.9, 'a', 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
1363525783328
1363525783328
True
False
{(2, 3), 4, 'a', 'rosjini', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 'rosjini', 8.9, 30, None}
False
False
{1, 2, 'rosh', 4, 100, 6}
{1, 'rosh', 4, 100, 6}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'rosjini', 'a'}
1914447941408
1914447941408
True
False
{'a', (2, 3), 'rosjini', 4, 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{'rosh', 1, 2, 4, 100, 6}
{'rosh', 1, 4, 100, 6}
Traceback (most recent call last):
  File "C:/Python310/sets1.py", line 45, in <module>
    a.remove(2)
KeyError: 2

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
3022594330400
3022594330400
True
False
{(2, 3), 4, 8.9, 'a', 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'rosjini', 'a'}
2745542987552
2745542987552
True
False
{(2, 3), 'rosjini', 'a', 4, 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2804472369376
2804472369376
True
False
{(2, 3), 'a', 4, 8.9, 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
Traceback (most recent call last):
  File "C:/Python310/sets1.py", line 50, in <module>
    a.add({1,2,3,4})
TypeError: unhashable type: 'set'

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, None, 4, 'a'}
{(2, 3), 'rosjini', 'a'}
2792056442656
2792056442656
True
False
{(2, 3), 'rosjini', 4, 8.9, 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
Traceback (most recent call last):
  File "C:/Python310/sets1.py", line 50, in <module>
    a.add(1,2,3,4)
TypeError: set.add() takes exactly one argument (4 given)

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'rosjini', 'a'}
2026283683616
2026283683616
True
False
{(2, 3), 4, 'a', 8.9, 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, None, 4, 'a'}
{(2, 3), 'rosjini', 'a'}
1920205999904
1920205999904
True
False
{(2, 3), 'rosjini', 4, 'a', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
set()
{1}
{1}
{1}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2131355062048
2131355062048
True
False
{'a', (2, 3), 4, 8.9, 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 'rosh', 4, 100, 6}
{1, 'rosh', 4, 100, 6}
{1, 'rosh', 4, 100, 6}
set()
{1}
{1}
{1}
2131355061824
2131355062048
{1}
{1, 20}
2131355061824
2131355062048

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
1994948759328
1994948759328
True
False
{(2, 3), 4, 8.9, 'a', 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
1994948759104
1994948759328
{1}
{1, 20}
1994948759104
1994948759328

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'a', 'rosjini'}
1758470164256
1758470164256
True
False
{(2, 3), 'rosjini', 4, 8.9, 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
1758470164032
1758470164256
{1}
{1, 20}
1758470164032
1758470164256
{20}
set()

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2504266305088
2504266305088
True
False
{(2, 3), 'rosjini', 4, 8.9, 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
set()
{1}
{1}
{1}
2504266306880
2504266305088
{1}
{1, 20}
2504266306880
2504266305088
{20}
set()
{1, 2, 3}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, None, 4, 'a'}
{(2, 3), 'a', 'rosjini'}
1338012487232
1338012487232
True
False
{(2, 3), 4, 'a', 'rosjini', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 'rosjini', 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
1338012489024
1338012487232
{1}
{1, 20}
1338012489024
1338012487232
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'rosjini', 'a'}
1593305943616
1593305943616
True
False
{(2, 3), 4, 8.9, 'rosjini', 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
set()
{1}
{1}
{1}
1593305945408
1593305943616
{1}
{1, 20}
1593305945408
1593305943616
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, None, 4, 'a'}
{(2, 3), 'rosjini', 'a'}
2226928438848
2226928438848
True
False
{(2, 3), 'rosjini', 4, 'a', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
set()
{1}
{1}
{1}
2226928440640
2226928438848
{1}
{1, 20}
2226928440640
2226928438848
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
Traceback (most recent call last):
  File "C:/Python310/sets1.py", line 73, in <module>
    d = a.intersection(y)
NameError: name 'y' is not defined

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'rosjini', 'a'}
1528166698560
1528166698560
True
False
{'a', (2, 3), 'rosjini', 4, 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 'rosh', 4, 100, 6}
{1, 'rosh', 4, 100, 6}
{1, 'rosh', 4, 100, 6}
set()
{1}
{1}
{1}
1528166700352
1528166698560
{1}
{1, 20}
1528166700352
1528166698560
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
Traceback (most recent call last):
  File "C:/Python310/sets1.py", line 73, in <module>
    d = a.intersection(bs)
NameError: name 'bs' is not defined. Did you mean: 'b'?

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'rosjini', 'a'}
2618245598784
2618245598784
True
False
{(2, 3), 4, 'a', 8.9, 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2618245600576
2618245598784
{1}
{1, 20}
2618245600576
2618245598784
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2835597119040
2835597119040
True
False
{(2, 3), 4, 'rosjini', 8.9, 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 'rosjini', 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2835597120832
2835597119040
{1}
{1, 20}
2835597120832
2835597119040
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
set()
{4, 5, 6, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2708524715584
2708524715584
True
False
{(2, 3), 4, 'rosjini', 8.9, 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 'rosjini', 8.9, 30, None}
False
False
{1, 2, 'rosh', 4, 6, 100}
{1, 'rosh', 4, 6, 100}
{1, 'rosh', 4, 6, 100}
set()
{1}
{1}
{1}
2708524717376
2708524715584
{1}
{1, 20}
2708524717376
2708524715584
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2689510559296
2689510559296
True
False
{(2, 3), 'a', 4, 8.9, 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2689510561088
2689510559296
{1}
{1, 20}
2689510561088
2689510559296
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2640492580416
2640492580416
True
False
{(2, 3), 4, 'rosjini', 8.9, 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 'rosjini', 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2640492582208
2640492580416
{1}
{1, 20}
2640492582208
2640492580416
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
1663049944640
1663049944640
True
False
{(2, 3), 'a', 'rosjini', 4, 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
1663049946432
1663049944640
{1}
{1, 20}
1663049946432
1663049944640
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2702514736704
2702514736704
True
False
{'a', (2, 3), 'rosjini', 4, 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2702514738496
2702514736704
{1}
{1, 20}
2702514738496
2702514736704
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'rosjini', 'a'}
2284897586752
2284897586752
True
False
{(2, 3), 'rosjini', 4, 30, 8.9, 'a', None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 30, 8.9, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2284897588544
2284897586752
{1}
{1, 20}
2284897588544
2284897586752
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, None, 4, 'a'}
{(2, 3), 'rosjini', 'a'}
2823066504768
2823066504768
True
False
{(2, 3), 4, 'a', 8.9, 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2823066506560
2823066504768
{1}
{1, 20}
2823066506560
2823066504768
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
1491311283776
1491311283776
True
False
{(2, 3), 4, 8.9, 'a', 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 'rosh', 4, 100, 6}
{1, 'rosh', 4, 100, 6}
{1, 'rosh', 4, 100, 6}
set()
{1}
{1}
{1}
1491311285568
1491311283776
{1}
{1, 20}
1491311285568
1491311283776
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2411570090656
2411570090656
True
False
{(2, 3), 'a', 4, 'rosjini', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 'rosjini', 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2411570091104
2411570090656
{1}
{1, 20}
2411570091104
2411570090656
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
print(a.pop())
4

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'rosjini', 'a'}
3223533736608
3223533736608
True
False
{(2, 3), 'rosjini', 4, 'a', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
3223533737056
3223533736608
{1}
{1, 20}
3223533737056
3223533736608
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2716373504672
2716373504672
True
False
{(2, 3), 4, 8.9, 'a', 'rosjini', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2716373505120
2716373504672
{1}
{1, 20}
2716373505120
2716373504672
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, None, 4, 'a'}
{(2, 3), 'rosjini', 'a'}
2716860830368
2716860830368
True
False
{'a', (2, 3), 'rosjini', 4, 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2716860830816
2716860830368
{1}
{1, 20}
2716860830816
2716860830368
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'a', 'rosjini'}
1737303084608
1737303084608
True
False
{(2, 3), 4, 8.9, 'rosjini', 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
set()
{1}
{1}
{1}
1737303086400
1737303084608
{1}
{1, 20}
1737303086400
1737303084608
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'a', 'rosjini'}
2683123815072
2683123815072
True
False
{(2, 3), 'rosjini', 4, 'a', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2683123815520
2683123815072
{1}
{1, 20}
2683123815520
2683123815072
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
Traceback (most recent call last):
  File "C:/Python310/sets1.py", line 105, in <module>
    d=a.symmetric_difference-update(b)
NameError: name 'update' is not defined

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, None, 4, 'a'}
{(2, 3), 'rosjini', 'a'}
2555141837472
2555141837472
True
False
{(2, 3), 'rosjini', 4, 'a', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2555141837920
2555141837472
{1}
{1, 20}
2555141837920
2555141837472
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
1534673703584
1534673703584
True
False
{(2, 3), 'rosjini', 4, 8.9, 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
1534673704032
1534673703584
{1}
{1, 20}
1534673704032
1534673703584
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}
{4, 5, 7, 8}
None

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'rosjini', 'a'}
2823076008608
2823076008608
True
False
{(2, 3), 'rosjini', 4, 'a', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
{1, 4, 'rosh', 6, 100}
set()
{1}
{1}
{1}
2823076009056
2823076008608
{1}
{1, 20}
2823076009056
2823076008608
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}
{4, 5, 7, 8}
None
{4, 5, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
1706320089760
1706320089760
True
False
{(2, 3), 'a', 4, 'rosjini', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 'rosjini', 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
1706320090208
1706320089760
{1}
{1, 20}
1706320090208
1706320089760
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}
{4, 5, 7, 8}
None
{4, 5, 7, 8}

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'a', 'rosjini'}
2041491968896
2041491968896
True
False
{(2, 3), 4, 'rosjini', 8.9, 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 'rosjini', 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2041491970016
2041491968896
{1}
{1, 20}
2041491970016
2041491968896
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}
{4, 5, 7, 8}
None
{4, 5, 7, 8}
all-a: True
all-b: False
all-c: False

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
1848199435360
1848199435360
True
False
{(2, 3), 'rosjini', 4, 'a', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
1848199436704
1848199435360
{1}
{1, 20}
1848199436704
1848199435360
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}
{4, 5, 7, 8}
None
{4, 5, 7, 8}
all-a: True
all-b: False
all-c: False
any-a: True
any-b: True
any-c: False

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, None, 4, 'a'}
{(2, 3), 'rosjini', 'a'}
3053590107232
3053590107232
True
False
{(2, 3), 'rosjini', 4, 'a', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 'rosh', 4, 100, 6}
{1, 'rosh', 4, 100, 6}
{1, 'rosh', 4, 100, 6}
set()
{1}
{1}
{1}
3053590108576
3053590107232
{1}
{1, 20}
3053590108576
3053590107232
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}
{4, 5, 7, 8}
None
{4, 5, 7, 8}
all-a: True
all-b: False
all-c: False
any-a: True
any-b: True
any-c: False
<enumerate object at 0x000002C6F826C600>

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'a', 'rosjini'}
3188063163488
3188063163488
True
False
{(2, 3), 'rosjini', 4, 'a', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
3188063164832
3188063163488
{1}
{1, 20}
3188063164832
3188063163488
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}
{4, 5, 7, 8}
None
{4, 5, 7, 8}
all-a: True
all-b: False
all-c: False
any-a: True
any-b: True
any-c: False
<enumerate object at 0x000002E6475EC600>

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'rosjini', 'a'}
2631728583776
2631728583776
True
False
{(2, 3), 4, 8.9, 'rosjini', 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, 'rosjini', 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2631728585120
2631728583776
{1}
{1, 20}
2631728585120
2631728583776
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}
{4, 5, 7, 8}
None
{4, 5, 7, 8}
all-a: True
all-b: False
all-c: False
any-a: True
any-b: True
any-c: False
<enumerate object at 0x00000264BD29C300>
(0, 1)(1, 2)(2, 3)(3, 4)

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, None, 4, 'a'}
{(2, 3), 'rosjini', 'a'}
2063532250208
2063532250208
True
False
{(2, 3), 4, 8.9, None, 'rosjini', 30, 'a'}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 8.9, None, 'rosjini', 30}
False
False
{'rosh', 1, 2, 4, 100, 6}
{'rosh', 1, 4, 100, 6}
{'rosh', 1, 4, 100, 6}
set()
{1}
{1}
{1}
2063532251552
2063532250208
{1}
{1, 20}
2063532251552
2063532250208
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}
{4, 5, 7, 8}
None
{4, 5, 7, 8}
all-a: True
all-b: False
all-c: False
any-a: True
any-b: True
any-c: False
<enumerate object at 0x000001E071FEC300>
(0, 1)
(1, 2)
(2, 3)
(3, 4)

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 'a', 4, None}
{(2, 3), 'a', 'rosjini'}
2619709084768
2619709084768
True
False
{(2, 3), 'rosjini', 4, 8.9, 'a', 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 'rosjini', 4, 8.9, 30, None}
False
False
{1, 2, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
{1, 4, 100, 6, 'rosh'}
set()
{1}
{1}
{1}
2619709086112
2619709084768
{1}
{1, 20}
2619709086112
2619709084768
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}
{4, 5, 7, 8}
None
{4, 5, 7, 8}
all-a: True
all-b: False
all-c: False
any-a: True
any-b: True
any-c: False
<enumerate object at 0x00000261F0B87500>
(0, 1)
(1, 2)
(2, 3)
(3, 4)
4

======================== RESTART: C:/Python310/sets1.py ========================
<class 'dict'>
<class 'set'>
<class 'set'>
False
{8.9, 4, 'a', None}
{(2, 3), 'rosjini', 'a'}
2781251982432
2781251982432
True
False
{(2, 3), 4, 'rosjini', 'a', 8.9, 30, None}
{'a'}
{8.9, 4, 30, None}
{(2, 3), 4, 'rosjini', 8.9, 30, None}
False
False
{1, 2, 'rosh', 4, 100, 6}
{1, 'rosh', 4, 100, 6}
{1, 'rosh', 4, 100, 6}
set()
{1}
{1}
{1}
2781251983776
2781251982432
{1}
{1, 20}
2781251983776
2781251982432
{20}
set()
{1, 2, 3}
{4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8}
set()
None
{4, 5}
{4, 5, 6, 7, 8}
{4, 5}
False
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5}
False
{4, 5, 6, 7, 8}
False
True
False
4
{5, 6, 7, 8}
None
{5, 7, 8}
{4, 5}
{8, 4, 7}
{5, 7, 8}
{8, 4, 7}
None
{5, 7, 8}
{4, 5, 7, 8}
None
{4, 5, 7, 8}
all-a: True
all-b: False
all-c: False
any-a: True
any-b: True
any-c: False
<enumerate object at 0x000002878D667500>
(0, 1)
(1, 2)
(2, 3)
(3, 4)
len  4
list  [1, 2, 3, 4]
max  4
min  1
sum  10

=============== RESTART: C:/Python310/python_program/frozenset.py ==============
<class 'set'>
<class 'frozenset'>

=============== RESTART: C:/Python310/python_program/frozenset.py ==============
<class 'set'>
<class 'frozenset'>
Traceback (most recent call last):
  File "C:/Python310/python_program/frozenset.py", line 6, in <module>
    fs.update(y)
AttributeError: 'frozenset' object has no attribute 'update'
dir(frozenset)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']

=============== RESTART: C:/Python310/python_program/frozenset.py ==============
<class 'set'>
<class 'frozenset'>
Traceback (most recent call last):
  File "C:/Python310/python_program/frozenset.py", line 6, in <module>
    fs.update(y) #no update is there as frozen set is immutable
AttributeError: 'frozenset' object has no attribute 'update'

=============== RESTART: C:/Python310/python_program/frozenset.py ==============
<class 'set'>
<class 'frozenset'>
frozenset({8.27, 27, 'roshini', 23.5})
frozenset({8.27, 27, 'roshini', 23.5})

=============== RESTART: C:/Python310/python_program/frozenset.py ==============
<class 'set'>
<class 'frozenset'>
frozenset({8.27, 27, 'roshini', 23.5})
frozenset({8.27, 27, 'roshini', 23.5})
frozenset()
Traceback (most recent call last):
  File "C:/Python310/python_program/frozenset.py", line 15, in <module>
    b.discard(9) # removes the required ele
AttributeError: 'frozenset' object has no attribute 'discard'

=============== RESTART: C:/Python310/python_program/frozenset.py ==============
<class 'set'>
<class 'frozenset'>
frozenset({8.27, 'roshini', 27, 23.5})
frozenset({8.27, 'roshini', 27, 23.5})
frozenset()
frozenset({8.27, 'roshini', 27, 23.5})
frozenset({8.27, 'roshini', 27, 23.5})
False
frozenset({8.27, 'roshini', 27, 23.5})
True
False
False
Traceback (most recent call last):
  File "C:/Python310/python_program/frozenset.py", line 30, in <module>
    print(b.pop())
AttributeError: 'frozenset' object has no attribute 'pop'

=============== RESTART: C:/Python310/python_program/frozenset.py ==============
<class 'set'>
<class 'frozenset'>
frozenset({8.27, 27, 'roshini', 23.5})
frozenset({8.27, 27, 'roshini', 23.5})
frozenset()
frozenset({8.27, 27, 'roshini', 23.5})
frozenset({8.27, 27, 'roshini', 23.5})
False
frozenset({8.27, 27, 'roshini', 23.5})
True
False
False
{4, 5}
{4, 5, 8.27, 'roshini', 23.5, 27}
frozenset({8.27, 27, 'roshini', 23.5})
{4, 5, 23.5, 8.27, 27, 'roshini'}
all-a: True
all-b: False
all-c: False
any-a: True
any-b: True
any-c: False
<enumerate object at 0x000001FAC90EC600>
(0, 1)
(1, 2)
(2, 3)
(3, 4)
len  4
list  [1, 2, 3, 4]
max  4
min  1
sum  10

=============== RESTART: C:/Python310/python_program/frozenset.py ==============
<class 'set'>
<class 'frozenset'>
frozenset({8.27, 'roshini', 27, 23.5})
frozenset({8.27, 'roshini', 27, 23.5})
frozenset()
frozenset({8.27, 'roshini', 27, 23.5})
frozenset({8.27, 'roshini', 27, 23.5})
False
frozenset({8.27, 'roshini', 27, 23.5})
True
False
False
{4, 5}
{4, 5, 8.27, 'roshini', 23.5, 27}
frozenset({8.27, 'roshini', 27, 23.5})
{4, 5, 23.5, 8.27, 'roshini', 27}
all-a: True
all-b: False
all-c: False
any-a: True
any-b: True
any-c: False
<enumerate object at 0x00000194B58083C0>
(0, 1)
(1, 2)
(2, 3)
(3, 4)
len  4
list  [1, 2, 3, 4]
max  4
min  1
sum  10

=============== RESTART: C:/Python310/python_program/frozenset.py ==============
<class 'set'>
<class 'frozenset'>
frozenset({8.27, 'roshini', 27, 23.5})
frozenset({8.27, 'roshini', 27, 23.5})
frozenset()
frozenset({8.27, 'roshini', 27, 23.5})
frozenset({8.27, 'roshini', 27, 23.5})
False
frozenset({8.27, 'roshini', 27, 23.5})
True
False
False
{4, 5}
{4, 5, 8.27, 23.5, 'roshini', 27}
frozenset({8.27, 'roshini', 27, 23.5})
{4, 5, 23.5, 8.27, 'roshini', 27}
<class 'frozenset'> <class 'frozenset'> <class 'frozenset'>
all-a: True
all-b: False
all-c: False
any-a: True
any-b: True
any-c: False
<enumerate object at 0x000002C3401AC300>
(0, 1)
(1, 2)
(2, 3)
(3, 4)
len  4
list  [1, 2, 3, 4]
max  4
min  1
sum  10
