Sigma = []
NFA_States = []
NFA_Transitions = {}

NFA_F = []
S = -1


def NFA_parser( config_file ):
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
            NFA_States.append(line[0])

            if len(line) >= 2:

                if line[1] == 'F':
                    NFA_F.append( NFA_States[ len(NFA_States) - 1 ] )

                if line[1] == 'S':
                    if S == -1:
                        S = NFA_States[ len(NFA_States) - 1 ]
                    else:
                        print("Input invalid: Mai multe stari initiale; linia", nr)
                        f.close()
                        return;
                    if len(line) ==3:
                        if line[2] == 'F':
                            F.append(NFA_States[len(NFA_States) - 1])
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

            if state1 not in NFA_States:
                print("Input invalid: Nu exista starea", state1, "; linia", nr)
                f.close()
                return
            if state2 not in NFA_States:
                print("Input invalid: Nu exista starea", state2, "; linia", nr)
                f.close()
                return
            if word not in Sigma:
                print("Input invalid", word, "; linia", nr)
                f.close()
                return

            if (state1, word) not in NFA_Transitions:
                NFA_Transitions[(state1, word)] = []
            NFA_Transitions[(state1, word)].append(state2)
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

NFA_parser( "NFA_sample.txt" )

#print(Sigma)
#print(NFA_States)
#print(NFA_Transitions)
#print(S)
#print(NFA_F)

import collections

queue = collections.deque([ S ])
DFA_States = []
DFA_Transitions = {}
DFA_F = []

def Convert_NFA():
    global S
    import collections

    for word in Sigma:
        if (S, word) in NFA_Transitions:
            DFA_Transitions[(S, word)] = NFA_Transitions[(S, word)]

    while (len(queue)):
        state = queue.popleft()

        # print( state )

        for word in Sigma:
            if (state, word) in DFA_Transitions:
                new_state = '{' + ",".join(sorted(DFA_Transitions[(state, word)])) + '}'
                if new_state == state or new_state in DFA_States or new_state in queue:
                    continue

                for transition_state in DFA_Transitions[(state, word)]:
                    for transition_word in Sigma:
                        if (transition_state, transition_word) in NFA_Transitions:

                            if (new_state, transition_word) not in DFA_Transitions:
                                DFA_Transitions[(new_state, transition_word)] = []

                            for next_state in NFA_Transitions[(transition_state, transition_word)]:
                                if next_state not in DFA_Transitions[(new_state, transition_word)]:
                                    DFA_Transitions[(new_state, transition_word)].append(next_state)

                queue.append(new_state)

                # print( new_state )
                # print( DFA_Transitions )

        for final_state in NFA_F:
            if final_state in state:
                DFA_F.append(state)

        DFA_States.append(state)

Convert_NFA()

print("Sigma:", Sigma)
print("States:",DFA_States)
print("Transitions:",DFA_Transitions)
print("Initial_state:",S)
print("Final_states:",DFA_F)