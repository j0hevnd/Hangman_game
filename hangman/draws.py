def draw(self, cant_lives):
    """ Game images depending on the amount of life """
    if cant_lives == 7:
        print("""
||=========|||=
||          |
||         
||     
||         
||          
||
||
||
========°--------=====____
========°--------=====____
    """)

    if cant_lives == 6:
        print("""
||=========|||=
||          |
||         ___
||        |^O^|
||         \_/ 
||          
||
||
||
========°--------=====____
========°--------=====____
    """)

    if cant_lives == 5:
        print("""
||=========|||=
||          |
||         ___
||        |^o^|
||         \_/ 
||          |
||          |
||
||
========°--------=====____
========°--------=====____
    """)

    if cant_lives == 4:
        print("""
||=========|||=
||          |
||         ___
||        |O.O|
||         \_/ 
||          |\ 
||          |
||
||
========°--------=====____
========°--------=====____
    """)

    if cant_lives == 3:
        print("""
||=========|||=
||          |
||         ___
||        |ಠ_ಠ|
||         \_/ 
||         /|\ 
||          |
||
||
========°--------=====____
========°--------=====____
    """)

    if cant_lives == 2:
        print("""
||=========|||=
||          |
||         ___
||        |_´_|
||         \_/  
||         /|\ 
||          |
||           \ 
||
========°--------=====____
========°--------=====____
    """)

    if cant_lives == 1:
        print("""
||=========|||=
||          |
||         ___
||        |T_T|
||         \_/ 
||         /|\ 
||          |
||         / \ 
||
========°--------=====____
========°--------=====____
    """)

    if cant_lives == 0:
        print("""
||=========|||===
||          |
||         ___
||        |X_X|
||         \_/ 
||         /|\ 
||          |
||         / \ 
||
========°\        =====____
=======°\ \       =====____
        \ \ 
    """)

    if cant_lives == 10:
        print("""
||=========|||===
||          |
||       🌟🌟🌟
||     🌟 ____  🌟
||        |⌐■_■|
||        _\_/_
||         \|/ 
||          |
||         / \ 
========°--------=====____
========°--------=====____
    """)