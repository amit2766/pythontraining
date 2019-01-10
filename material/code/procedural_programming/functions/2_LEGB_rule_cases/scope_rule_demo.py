# Indentation Level 0 
g-st1
g-st2
g-st3
#g-st4
def f1 (): 
    # Indentation level 1
    f1-st1
    f1-st2
    f1-st3
    f1-st4
    #f1-st5
    def f2 (): 
        # Indetation level 2 
        f2-st1
        f2-st2
        f2-st3
        f2-st4
        f2-st5
        # f2-st6
        def f3 (): 
            # Indentation level 3
            f3-st1
            f3-st2
            f3-st3
            # f3-st4
            def f4 (): 
                # Indentation level 4
                f4-st1
                f4-st2
                f4-st3
                f4-st4
                f4-st5
            # f3-st5 IL 3
            f4 () 
            f3-st6
        # f2 - st7 IL 2 
        f3 () 
        f2-st8
    # f1- st6 IL 1
    f2 () 
    f1-st7
# g-st5 IL 0 
f1 () 
g-st6
g-st7 
