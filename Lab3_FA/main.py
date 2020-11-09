#class used for states
class State:
    def __init__(self, state, final=False):
        #initial set up
        self.state = state
        self.final = final
    def __str__(self):
        return self.state + str(self.final)
#class used for FA
class FA:
    def __init__(self, file):
        #creating list of states 
        self.states = []
        #creating a dictionary for transitions 
        self.transitions = {}
        #creating list for alphabet 
        self.alphabet = []
        #reading input file
        file_open = open(file,"r")
        with file_open:
            #read the states:
            states_list = file_open.readline().split()
            #number of final states:
            number_final_states = int(file_open.readline())
            #alphabet: 
            self.alphabet = file_open.readline().split()
            #transitions:
            for line in file_open:
                line = line.split()
                if line[2] not in self.transitions.keys():
                    self.transitions[line[2]] = []
                self.transitions[line[2]].append((line[0], line[1]))
        #setting state as final state
        for state in states_list:
            self.states.append(State(state))
            if len(self.states) > len(states_list) - number_final_states:
                self.states[-1].final = True
#main function + menu          
def main():
    #create FA from input
    print("Give input file name + extension")
    file_name = input()
    fa = FA(file_name)
    #menu 
    while True:
        print("\nChoose what you would like to see: ")
        print("1. List all states.  Q")
        print("2. Initial state. q0 ")
        print("3. Final state(s). F ")
        print("4. Alphabet. Σ")
        print("5. Transitions. δ ")
        print("0. Exit")
        choice = input("Choice: ")
        #elif for each possible choice
        if choice == "0":
            #exit program
            break
        elif choice == "1":
            #states
            for states in fa.states:
                print(states.state)
        elif choice == "2":
            #initial state 
            print(fa.states[0].state)
        elif choice == "3":
            #final state(s)
            for states in fa.states:
                if states.final:
                    print(states.state)
        elif choice == "4":
            #alphabet
            print(fa.alphabet)
        elif choice == "5":
            #transitions
            for key in fa.transitions.keys():
                print("{}: {}".format(key, fa.transitions[key]))
        else:
            print("Choice doesn't exist. Would you like to exit?") 
#run program
if __name__ == '__main__':
    main()