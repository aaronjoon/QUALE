from perceval.components.unitary_components import PS, BS, PERM
import numpy as np
import perceval as pcvl
import main

num_samples = 1000000000

def loss(circuit):
    processor = pcvl.Processor("SLOS", circuit)
    processor.with_input(main.input_state)
    sampler = pcvl.algorithm.Sampler(processor)

    sample_count = sampler.sample_count(num_samples)

    prob_22 = sample_count['results'][pcvl.BasicState("|0,0,1,0,0,0,1,0>")]/num_samples

    return ((1-prob_22) + (1 - np.sqrt(prob_22)) ** 2)

main.set_weights(main.full_circuit, np.zeros(42))
main.set_weights(main.disc_circuit, np.ones(12))

# for param in main.full_circuit.get_parameters():
#     print(param)

# print(loss(main.full_circuit))

def disc_loss(disc_weights):
    main.set_weights(main.disc_circuit, disc_weights)
    return loss(main.full_circuit)

def gen_loss(gen_weights):
    main.set_weights(main.gen_circuit, gen_weights)
    return loss(main.full_circuit)
