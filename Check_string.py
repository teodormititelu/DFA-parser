Sigma = []
States = []
Transitions = {}

F = []
S = -1


def DFA_parser( config_file ):
    global S
    sigma = False
    states = False
    transitions = False

    f = open( config_file, 'r')

    for nr, line in enumerate(f.read().split('\n'), start=1):

        line = line.strip()

        if len(line) == 0:
            continue

        if line[0] == '#':
            continue

        line = line.replace(',', ' ').replace(':', ' ').split()

        if '#' in line:
            line = line[:line.index('#')]

        if line[0] == "End":
            sigma = states = transitions = False
            continue

        if sigma == True:
            Sigma.append(line[0])
            continue

        if states == True:
            States.append(line[0])

            if len(line) >= 2:

                if line[1] == 'F':
                    F.append( States[ len(States) - 1 ] )

                if line[1] == 'S':
                    if S == -1:
                        S = States[ len(States) - 1 ]
                    else:
                        print("Input invalid: Mai multe stari initiale; linia", nr)
                        f.close()
                        return;
                    if len(line) ==3:
                        if line[2] == 'F':
                            F.append(States[len(States) - 1])
                        else:
                            print("Input invalid: Stare neidentificata; linia", nr)
                            f.close()
                            return;

                if line[1] != 'F' and line[1] != 'S':
                    print("Input invalid: Stare neidentificata; linia", nr)
                    f.close()
                    return;
            continue

        if transitions == True:

            if len(line) != 3:
                print("Input invalid; linia", nr)
                f.close()
                return

            state1 = line[0]
            word = line[1]
            state2 = line[2]

            if state1 not in States:
                print("Input invalid: Nu exista starea", state1, "; linia", nr)
                f.close()
                return
            if state2 not in States:
                print("Input invalid: Nu exista starea", state2, "; linia", nr)
                f.close()
                return
            if word not in Sigma:
                print("Input invalid", word, "; linia", nr)
                f.close()
                return

            Transitions[(state1, word)] = state2
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

        print("Input invalid; linia", nr)
        f.close()
        return

    f.close()

import sys

def Check_string( input ):

    config_file = input[0]

    if( len(input) > 1 ):
        word = input[1]
    else: word = []

    DFA_parser( config_file )

    current_state = S
    for sigma in word:
        if (current_state, sigma) in Transitions:
            current_state = Transitions[(current_state, sigma)]
        else:
            print( "Rejected" )
            return
    if current_state in F:
        print( "Accepted" )
    else: print( "Rejected" )

Check_string(sys.argv[1:])
