# Write a Python program to simulate a Deterministic Finite Automaton (DFA).
# The program should accept a transition table, initial state, final states,
# and an input string, then output whether the string is accepted or rejected.

def simulate_dfa(transition_table, initial_state, final_states, input_string):
    current_state = initial_state

    for symbol in input_string:
        if symbol not in transition_table[current_state]:
            return "Rejected"
        current_state = transition_table[current_state][symbol]

    return "Accepted" if current_state in final_states else "Rejected"
transition_table = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q2', '1': 'q0'},
    'q2': {'0': 'q1', '1': 'q2'}
}

initial_state = 'q0'
final_states = {'q2'}

# Input string
input_string = input("Enter input string: ")

result = simulate_dfa(transition_table, initial_state, final_states, input_string)
print("Result:", result)