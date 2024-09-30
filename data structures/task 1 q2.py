pupil_name = input()
name = []
index = 0


def searchForName(wanted_name):
    for i in range(0, max):     
        if name[i] == wanted_name:
            index = i
            return index + 1
            break
#         endif
#     endfor
# endfunction
    
    
        
        