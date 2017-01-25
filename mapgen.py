import sys
from random import randrange
from colorama import init, Fore, Back, Style
init(autoreset=True)
width=20
length=10
pos='0 0'
rounds=170

def outland1():
    for i in land:
        for I in i:
            sys.stdout.write(str(I))
        print

def depth_outland(arrayx):
    for i in range(0,length):
        for I in range(0,width):
            if thickness[i][I]==7:
                sys.stdout.write(Style.BRIGHT+Fore.RED+'7'+Fore.WHITE+Style.NORMAL)
            elif thickness[i][I]==6:
                sys.stdout.write(Style.BRIGHT+Fore.YELLOW+'6'+Fore.WHITE+Style.NORMAL)
            elif thickness[i][I]==5:
                sys.stdout.write(Style.NORMAL+Fore.YELLOW+'5'+Fore.WHITE+Style.NORMAL)
            elif thickness[i][I]==4:
                sys.stdout.write(Style.BRIGHT+Fore.GREEN+'4'+Fore.WHITE+Style.NORMAL)
            elif thickness[i][I]==3:
                sys.stdout.write(Style.BRIGHT+Fore.CYAN+'3'+Fore.WHITE+Style.NORMAL)
            elif thickness[i][I]==2:
                sys.stdout.write(Style.NORMAL+Fore.CYAN+'2'+Fore.WHITE+Style.NORMAL)
            elif thickness[i][I]==1:
                sys.stdout.write(Style.BRIGHT+Fore.BLUE+'1'+Fore.WHITE+Style.NORMAL)
            else:
                sys.stdout.write(Style.NORMAL+Fore.BLUE+'0'+Fore.WHITE+Style.NORMAL)

        print
    sys.stdout.write( Style.BRIGHT+Fore.RED+'#'+Fore.WHITE+Style.NORMAL)
    sys.stdout.write( Style.BRIGHT+Fore.YELLOW+'#'+Fore.WHITE+Style.NORMAL)
    sys.stdout.write( Style.NORMAL+Fore.YELLOW+'#'+Fore.WHITE+Style.NORMAL)
    sys.stdout.write( Style.BRIGHT+Fore.GREEN+'#'+Fore.WHITE+Style.NORMAL)
    sys.stdout.write( Style.BRIGHT+Fore.CYAN+'#'+Fore.WHITE+Style.NORMAL)
    sys.stdout.write( Style.NORMAL+Fore.CYAN+'#'+Fore.WHITE+Style.NORMAL)
    sys.stdout.write( Style.BRIGHT+Fore.BLUE+'#'+Fore.WHITE+Style.NORMAL)
    sys.stdout.write( Style.NORMAL+Fore.BLUE+'#'+Fore.WHITE+Style.NORMAL)
    print
    for i in range(0,8):
        sys.stdout.write(str(i))
    print

def pretty_outland(arrayx,required_surroundings):
    for i in range(0,length):
        for I in range(0,width):
            if land[i][I]==1 and thickness[i][I]==7:
                sys.stdout.write(Style.BRIGHT+Fore.BLACK+chr(127)+Fore.WHITE+Style.NORMAL)
            elif land[i][I]==1 and thickness[i][I]>=required_surroundings:
                sys.stdout.write(str(Style.BRIGHT+Fore.GREEN+chr(6)+Fore.WHITE+Style.NORMAL))
            else:
                sys.stdout.write(Style.BRIGHT+Fore.BLUE+chr(247)+Fore.WHITE+Style.NORMAL)
        print
    print

density=0.0
trys=0
#get thickness
while density<4.0:
    thickness= [[0 for x in range(width)] for x in range(length)] 
    land= [[0 for x in range(width)] for x in range(length)] 
    previous_pos=pos
    trys=randrange(40,(width*length)-(width*2))
    for i in range(0,trys):
        pos=str(randrange(1,width-1))+' '+str(randrange(1,length-1))
        x,y=int(pos.split()[0]),int(pos.split()[1])
        land[y][x]=1
    
    for i in range(0,length):
        for I in range(0,width):
            land[i][I]==float(land[i][I])

    def outland(arrayx):
        for i in arrayx:
            for I in i:
                sys.stdout.write(str(I))
            print
        print

    def horizontal_check():
        global thickness,length,width
        for i in range(0,length):
            for I in range(0,width):
                try:
                    if I-1>=0 and land[i][I]==1:
                        if land[i][I-1]==1:
                            thickness[i][I]+=1
                except:
                    pass
                try:
                    if I+1<=width and land[i][I]==1:
                        if land[i][I+1]==1:
                            thickness[i][I]+=1
                except:
                    pass

    horizontal_check()
    def vertical_check():
        global thickness
        for i in range(0,length):
            for I in range(0,width):
                try:
                    if i-1>=0 and land[i][I]==1:
                        if land[i-1][I]==1:
                            thickness[i][I]+=1
                except:
                    pass
                try:
                    if i+1<=width and land[i][I]==1:
                        if land[i+1][I]==1:
                            thickness[i][I]+=1
                except:
                        pass

    vertical_check()
    def diagonal_check():
        global thickness
        for i in range(0,length):
            for I in range(0,width):
                try:
                    if i-1>=0 and I-1>=0 and land[i][I]==1:
                        if land[i-1][I-1]==1:
                            thickness[i][I]+=1
                except:
                    pass
                try:
                    if i-1>=0 and I+1<=width and land[i][I]==1:
                        if land[i-1][I+1]==1:
                            thickness[i][I]+=1
                except:
                    pass
                try:
                    if i+1<=width and I-1>=0 and land[i][I]==1:
                        if land[i+1][I-1]==1:
                            thickness[i][I]+=1
                except:
                    pass
                try:
                    if i+1<=width and I+1<=width and land[i][I]==1:
                        if land[i+1][I+1]==1:
                            thickness[i][I]+=1
                except:
                    pass
    diagonal_check()
    total=0
    zero_count=0
    for i in range(0,length):
            for I in range(0,width):
                total+=float(thickness[i][I])
                if thickness[i][I]==0:
                    zero_count+=1
    try:
        density= total/((width*length)-zero_count)
    except:
        density= 0.0
print trys, density
pretty_outland(land,4)
depth_outland(thickness)