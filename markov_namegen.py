import argparse
import random
from collections import defaultdict

def train_markov_chain(examples, order):
    markov_chain = defaultdict(list)
    for example in examples:
        for i in range(len(example) - order):
            state = example[i:i+order]
            next_char = example[i+order]
            markov_chain[state].append(next_char)
    return markov_chain

def generate_name(markov_chain, order, length):
    state = random.choice(list(markov_chain.keys()))
    name = list(state)
    while len(name) < length:
        next_char = random.choice(markov_chain[state])
        name.append(next_char)
        state = state[1:] + next_char
    return ''.join(name)

def main():
    parser = argparse.ArgumentParser(description='Generate names using a Markov chain.')
    parser.add_argument('--order', type=int, required=True, help='Order of the Markov chain')
    parser.add_argument('--examples', nargs='+', required=True, help='List of names to train the generator')
    parser.add_argument('--length', type=int, default=8, help='Length of the generated name')
    args = parser.parse_args()

    markov_chain = train_markov_chain(args.examples, args.order)
    name = generate_name(markov_chain, args.order, args.length)
    print(name)

if __name__ == '__main__':
    main()