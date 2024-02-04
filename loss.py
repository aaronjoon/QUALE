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


def traces(disc1, disc2, gen1, gen2):
    Mhat = np.kron(np.array(disc1.compute_unitary()), np.array(disc2.compute_unitary()))
    Phat = np.kron(np.array(gen1.compute_unitary()), np.array(gen2.compute_unitary()))
    
    out1 = np.trace(np.matmul(Mhat, Phat))
    out2 = np.trace(np.matmul(Mhat, main.Tauhat))

    return out1, out2

main.set_weights(main.full_circuit, np.zeros(42))
main.set_weights(main.disc_circuit, np.ones(12))

# for param in main.full_circuit.get_parameters():
#     print(param)

# print(loss(main.full_circuit))

def disc_loss(disc_weights):
    main.set_weights(main.disc_circuit, disc_weights)
    trace1, trace2 = traces(main.discriminator1, main.discriminator2, main.generator1, main.generator2)
    return np.abs(trace2 - trace1), np.abs(trace2), np.abs(trace1)

def gen_loss(gen_weights):
    main.set_weights(main.gen_circuit, gen_weights)
    trace1, trace2 = traces(main.discriminator1, main.discriminator2, main.generator1, main.generator2)
    return np.abs(trace2 - trace1), np.abs(trace2), np.abs(trace1)
