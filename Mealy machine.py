
f = open( "Mealy.txt", 'r' ) #input file

Transitions = {}

states_nr, transitions_nr = [ int(x) for x in f.readline().split() ]

for t in range( transitions_nr ):

    state1, state2, in_value, out_value = f.readline().split()

    Transitions[ (state1, in_value) ] = (state2, out_value)

S = f.readline()
S = S[:-1]
F = []

for final_state in f.readline().split():
    F.append( final_state )

def Translate( string ):

    word = str()
    track = [ S ]
    current_state = S

    for character in string:

        if ( current_state, character ) not in Transitions:
            print( "NU" ) # rejected
            return;

        current_state, value = Transitions[ (current_state, character) ]
        word += value
        track.append( current_state )

    if current_state not in F:
        print( "NU" )
        return

    #accepted
    print( "DA" )
    print( word )
    print( "Traseu:", " ".join( track ) )

strings_nr = int( f.readline() )

for string in f.read().split('\n'):
    Translate( string )