""" Datele de intrare vor fi:

q0                          <- starea initiala
qAccept                     <- starea finala

q0,0,qRight0,_,>            <- o deplasare: separate prin ',' avem: starea actuala, caracterul de pe banda, noua stare, ce scrie pe banda (_ inseamna caracterul gol/vid), >/</_ este deplasarea)

qRight0,0,qRight0,0,>
qRight0,1,qRight0,1,>
q0,1,qRight1,_,>
qRight1,0,qRight1,0,>
qRight1,1,qRight1,1,>
qRight0,_,qSearch0L,_,<
qSearch0L,0,q1,_,<
qRight1,_,qSearch1L,_,<
qSearch1L,1,q1,_,<
q1,0,qLeft0,_,<
qLeft0,0,qLeft0,0,<
qLeft0,1,qLeft0,1,<
q1,1,qLeft1,_,<
qLeft1,0,qLeft1,0,<
qLeft1,1,qLeft1,1,<
qLeft0,_,qSearch0R,_,>
qSearch0R,0,q0,_,>
qLeft1,_,qSearch1R,_,>
qSearch1R,1,q0,_,>
qSearch0R,1,qReject,1,-
qSearch1R,0,qReject,0,-
qSearch0L,1,qReject,1,-
qSearch1L,0,qReject,0,-
q0,_,qAccept,_,-
q1,_,qAccept,_,-
qSearch0L,_,qAccept,_,-
qSearch0R,_,qAccept,_,-
qSearch1L,_,qAccept,_,-
qSearch1R,_,qAccept,_,-

"""

"""

Ati citit masina Turing cu configurarea ... (si sa afisati datele citite aici)
Puteti introduce cuvinte pe care sa le testeze MT :).

cuvant: 0110
OK
cuvant: 001
not OK..
cuvant: 11100110111
OK
cuvant: 01
not OK..

"""

f = open("Turing.txt", "rt")

inputfile = f.read().split("\n")

temp = []

for i in range(len(inputfile)):
    if inputfile[i] != '':
        temp.append(inputfile[i]);

inputfile = temp

initial_state = inputfile[0]
final_state = inputfile[1]

transitions = {}

for i in range(2, len(inputfile)):
    x = inputfile[i].split(",")

    start = x[0]
    value = x[1]
    end = x[2]
    write = x[3]
    move = x[4]

    if (start, value) not in transitions:
        transitions[(start, value)] = []

    transitions[(start, value)].append((end, write, move))

current_position = 0
tape = []

def Move(direction):
    global current_position
    global tape

    if direction == 'right':
        current_position += 1
    else:
        current_position -= 1


def Write(character):
    global tape
    global current_position

    if current_position >= len(tape):
        tape.append('_')

    tape[current_position] = character


def Read():
    global tape
    global current_position

    if current_position >= len(tape):
        tape.append('_')

    return tape[current_position]

accepted = False

def Turing(current_state):
    global accepted
    global final_state
    global current_position
    global tape

    if current_state == final_state:
        accepted = True

    if accepted: return

    if (current_state, Read()) in transitions:
        for x in transitions[(current_state, Read())]:
            save_current = current_position
            save_tape = tape

            next_state = x[0]
            Write(x[1])

            if x[2] == '<':
                Move('left')

            if x[2] == '>':
                Move('right')

            Turing(next_state)

            current_position = save_current
            tape = save_tape


if __name__ == '__main__':
    while True:
        word = input("Input: ")

        if word == "quit":
            break

        accepted = False
        tape = [x for x in word]
        current_position = 0
        current_state = initial_state

        Turing(initial_state)

        if accepted:
            print("Accepted")
        else:
            print("Rejected")