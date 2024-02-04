from perceval.components.unitary_components import PS, BS, PERM
import numpy as np
import perceval as pcvl

#phi = pcvl.P('phi')

# bs1 = pcvl.BasicState([1, 1, 1, 1])

gen_circuit = pcvl.Circuit(8,"The Generator Circuit")
disc_circuit = pcvl.Circuit(8, "The Discriminator Circuit")
generator1 = pcvl.Circuit(4,"generator1")
discriminator1 = pcvl.Circuit(4,'discriminator1')
generator2 = pcvl.Circuit(4,"generator2")
discriminator2 = pcvl.Circuit(4,'discriminator2')

full_circuit = pcvl.Circuit(8, "Full Circuit")



def generate_generator(generator, top_bottom):
    generator.add(1, PS(phi=pcvl.P(f'phi.g{top_bottom}.1')))
    generator.add(2, PS(phi=pcvl.P(f'phi.g{top_bottom}.2.')))
    generator.add(3, PS(phi=pcvl.P(f'phi.g{top_bottom}.3.')))
    generator.add(1, BS())
    generator.add(1, PS(phi=pcvl.P(f'phi.g{top_bottom}.4')))
    generator.add(1, BS())
    generator.add(0, BS())
    generator.add(2, BS())
    generator.add(0, PS(phi=pcvl.P(f'phi.g{top_bottom}.5')))
    generator.add(2, PS(phi=pcvl.P(f'phi.g{top_bottom}.6')))
    generator.add(0, BS())
    generator.add(2, BS())
    generator.add(1, PS(phi=pcvl.P(f'phi.g{top_bottom}.7')))
    generator.add(1, BS())
    generator.add(1, PS(phi=pcvl.P(f'phi.g{top_bottom}.8')))
    generator.add(1, BS())

    generator.add(0, PS(phi=pcvl.P(f'phi.g{top_bottom}.9')))
    generator.add(2, PS(phi=pcvl.P(f'phi.g{top_bottom}.10')))
    generator.add(0, BS())
    generator.add(2, BS())
    
    generator.add(0, PS(phi=pcvl.P(f'phi.g{top_bottom}.11')))
    generator.add(2, PS(phi=pcvl.P(f'phi.g{top_bottom}.12')))
    generator.add(0, BS())
    generator.add(2, BS())

    generator.add(0, PS(phi=pcvl.P(f'phi.g{top_bottom}.13')))
    generator.add(1, PS(phi=pcvl.P(f'phi.g{top_bottom}.14')))
    generator.add(2, PS(phi=pcvl.P(f'phi.g{top_bottom}.15')))

    return generator

def generate_discriminator(discriminator, top_bottom):
    discriminator.add(0, PS(phi=pcvl.P(f'phi.d{top_bottom}.1')))
    discriminator.add(1, PS(phi=pcvl.P(f'phi.d{top_bottom}.2')))
    discriminator.add(2, PS(phi=pcvl.P(f'phi.d{top_bottom}.3')))
    discriminator.add(0, BS())
    discriminator.add(2, BS())
    discriminator.add(0, PS(phi=pcvl.P(f'phi.d{top_bottom}.5')))
    discriminator.add(2, PS(phi=pcvl.P(f'phi.d{top_bottom}.6')))
    discriminator.add(0, BS())
    discriminator.add(2, BS())
    discriminator.add(1, PS(phi=pcvl.P(f'phi.d{top_bottom}.7')))
    discriminator.add(1, BS())
    
    return discriminator

def generate_input_state():
    state1 = pcvl.StateVector([1, 0, 0, 0, 1, 0, 0, 0])
    state2 = pcvl.StateVector([0, 1, 0, 0, 0, 1, 0, 0])
    state3 = pcvl.StateVector([0, 0, 1, 0, 0, 0, 1, 0])
    state4 = pcvl.StateVector([0, 0, 0, 1, 0, 0, 0, 1])


    input_state = state1 + state2 + state3 + state4

    return input_state

# def possible_output_states():

#     return [pcvl.BasicState([1, 0, 0, 0, 1, 0, 0 , 0]),
#             pcvl.BasicState([1, 0, 0, 0, 0, 1, 0 , 0]),
#             pcvl.BasicState([1, 0, 0, 0, 0, 0, 1 , 0]),
#             pcvl.BasicState([1, 0, 0, 0, 0, 0, 0 , 1]),
#             pcvl.BasicState([0, 1, 0, 0, 1, 0, 0 , 0]),
#             pcvl.BasicState([0, 1, 0, 0, 0, 1, 0 , 0]),
#             pcvl.BasicState([0, 1, 0, 0, 0, 0, 1 , 0]),
#             pcvl.BasicState([0, 1, 0, 0, 0, 0, 0 , 1]),
#             pcvl.BasicState([0, 0, 1, 0, 1, 0, 0 , 0]),
#             pcvl.BasicState([0, 0, 1, 0, 0, 1, 0 , 0]),
#             pcvl.BasicState([0, 0, 1, 0, 0, 0, 1 , 0]),
#             pcvl.BasicState([0, 0, 1, 0, 0, 0, 0 , 1]),
#             pcvl.BasicState([0, 0, 0, 1, 1, 0, 0 , 1]),
#             pcvl.BasicState([0, 0, 0, 1, 0, 1, 0 , 0]),
#             pcvl.BasicState([0, 0, 0, 1, 0, 0, 1 , 0]),
#             pcvl.BasicState([0, 0, 0, 1, 0, 0, 0 , 1])]

def set_weights(circuit, weights):
    for i in range(np.size(weights)):
        circuit.get_parameters()[i].set_value(weights[i])


generate_generator(generator1, 1)
generate_discriminator(discriminator1, 1)

generate_generator(generator2, 2)
generate_discriminator(discriminator2, 2)

gen_circuit.add(0, generator1).add(4, generator2)

disc_circuit.add(0, discriminator1).add(4,discriminator2)

full_circuit.add(0, gen_circuit).add(0, disc_circuit)

input_state = generate_input_state()

# for param in full_circuit.get_parameters():
#     param.set_value(np.random.rand()*2*np.pi)
#     print(param)

# Mhat = np.kron(np.array(discriminator1.compute_unitary()), np.array(discriminator2.compute_unitary()))
# Phat = np.kron(np.array(generator1.compute_unitary()), np.array(generator2.compute_unitary()))

Tauhat = np.array([[1/4, 0, 0, 0, 0, 1/4, 0, 0, 0, 0, 1/4, 0, 0, 0, 0, 1/4], [0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1/4, 0, 0, 0,
        0, 1/4, 0, 0, 0, 0, 1/4, 0, 0, 0, 0, 1/4], [0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
   0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1/4, 0, 0, 0, 0, 1/4, 0, 0,
   0, 0, 1/4, 0, 0, 0, 0, 1/4], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 
  0, 0, 0, 0, 0, 0, 0, 0, 0], [1/4, 0, 0, 0, 0, 1/4, 0, 0, 0, 0, 1/4, 
  0, 0, 0, 0, 1/4]])

# print(len(full_circuit.get_parameters()))

# set_weights(full_circuit, np.zeros(42))

# for param in full_circuit.get_parameters():
#     print(param)


# processor = pcvl.Processor("SLOS", full_circuit)
# processor.with_input(input_state)
# sampler = pcvl.algorithm.Sampler(processor)

# sample_count = sampler.sample_count(1000)
# print(sample_count['results'][pcvl.BasicState("|0,0,1,0,0,0,1,0>")])

pcvl.pdisplay(discriminator1) #,recursive=True)
pcvl.pdisplay(generator1) #,recursive=True)

# def main():

    
    # outputs = possible_output_states()

    #params=generator1.get_parameters()
    #print(params)
    #pcvl.pdisplay(discriminator1)
    # pcvl.pdisplay(main_circuit) #,recursive=True)
    # pcvl.pdisplay(secondary_circuit)
    # pcvl.pdisplay(full_circuit)

    
    #return sample_count

# if __name__ == "__main__":
#     main()