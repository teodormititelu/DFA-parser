
Words = []
States = []
Transitions = {}

F = []
S = -1

def Language_parser():

    global S
    sigma = False
    states = False
    transitions = False

    f = open( "Language.txt", 'r' )

    for nr, line in enumerate( f.read().split('\n'), start = 1 ):

        line = line.strip()

        if line[0] == '#':
            continue

        line = line.replace(',',' ').replace(':', ' ').split()

        if '#' in line:
            line = line[:line.index('#')]

        if line[0] == "End":
            sigma = states = transitions = False
            continue

        if sigma == True:
            Words.append( line[0] )
            continue

        if states == True:
            States.append( line[0] )

            if len( line ) == 2:

                if line[1] == 'F':
                    F.append( len( States ) - 1 )

                if line[1] == 'S':
                    if S == -1:
                        S = len( States ) - 1
                    else:
                        print("Input invalid: Mai multe stari initiale; linia", nr)
                        f.close()
                        return;
                if line[1] != 'F' and line[1] != 'S':
                    print("Input invalid: Stare neidentificata; linia", nr)
                    f.close()
                    return;
            continue

        if transitions == True:

            if len(line) != 3:
                print( "Input invalid; linia", nr)
                f.close()
                return

            state1 = line[0]
            word = line[1]
            state2 = line[2]

            if state1 not in States:
                print( "Input invalid: Nu exista starea", state1, "; linia", nr )
                f.close()
                return
            if state2 not in States:
                print("Input invalid: Nu exista starea", state2, "; linia", nr)
                f.close()
                return
            if word not in Words:
                print( "Input invalid", word, "; linia", nr )
                f.close()
                return

            Transitions[ ( state1, word ) ] = state2
            continue

        if line[0] == "Sigma":
            sigma = True
            continue
        if line[0] == "States":
            states = True
            continue
        if line[0] == "Transitions":
            transitions = True
            continue

        print( "Input invalid; linia", nr )
        f.close()
        return


    f.close()

Language_parser()

print( Words )
print( States )
print( Transitions )
print( S )
print( F )