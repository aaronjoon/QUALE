from perceval.components.unitary_components import PS, BS, PERM
import numpy as np
import perceval as pcvl

#phi = pcvl.P('phi')

bs1 = pcvl.BasicState([1, 1, 1, 1])

main_circuit = pcvl.Circuit(4,"The Top Circuit")
secondary_circuit = pcvl.Circuit(4, "The Bottom Circuit")
generator1 = pcvl.Circuit(4,"generator1")
discriminator1 = pcvl.Circuit(4,'discriminator1')
generator2 = pcvl.Circuit(4,"generator2")
discriminator2 = pcvl.Circuit(4,'discriminator2')

full_circuit = pcvl.Circuit(8, "Full Circuit")


def generate_generator(generator, top_bottom):
    generator.add(1, PS(phi=pcvl.P(f'phi.g1.1.{top_bottom}')))
    generator.add(2, PS(phi=pcvl.P(f'phi.g1.2.{top_bottom}')))
    generator.add(3, PS(phi=pcvl.P(f'phi.g1.3.{top_bottom}')))
    generator.add(1, BS())
    generator.add(1, PS(phi=pcvl.P(f'phi.g1.4.{top_bottom}')))
    generator.add(1, BS())
    generator.add(0, BS())
    generator.add(2, BS())
    generator.add(0, PS(phi=pcvl.P(f'phi.g1.5.{top_bottom}')))
    generator.add(2, PS(phi=pcvl.P(f'phi.g1.6.{top_bottom}')))
    generator.add(0, BS())
    generator.add(2, BS())
    generator.add(1, PS(phi=pcvl.P(f'phi.g1.7.{top_bottom}')))
    generator.add(1, BS())
    generator.add(1, PS(phi=pcvl.P(f'phi.g1.8.{top_bottom}')))
    generator.add(1, BS())

    generator.add(0, PS(phi=pcvl.P(f'phi.g1.9.{top_bottom}')))
    generator.add(2, PS(phi=pcvl.P(f'phi.g1.10.{top_bottom}')))
    generator.add(0, BS())
    generator.add(2, BS())
    
    generator.add(0, PS(phi=pcvl.P(f'phi.g1.11.{top_bottom}')))
    generator.add(2, PS(phi=pcvl.P(f'phi.g1.12.{top_bottom}')))
    generator.add(0, BS())
    generator.add(2, BS())

    generator.add(0, PS(phi=pcvl.P(f'phi.g1.13.{top_bottom}')))
    generator.add(1, PS(phi=pcvl.P(f'phi.g1.14.{top_bottom}')))
    generator.add(2, PS(phi=pcvl.P(f'phi.g1.15.{top_bottom}')))

    return generator

def generate_discriminator(discriminator, top_bottom):
    discriminator.add(0, PS(phi=pcvl.P(f'phi.d1.1.{top_bottom}')))
    discriminator.add(1, PS(phi=pcvl.P(f'phi.d1.2.{top_bottom}')))
    discriminator.add(2, PS(phi=pcvl.P(f'phi.d1.3.{top_bottom}')))
    discriminator.add(0, BS())
    discriminator.add(2, BS())
    discriminator.add(0, PS(phi=pcvl.P(f'phi.d1.5.{top_bottom}')))
    discriminator.add(2, PS(phi=pcvl.P(f'phi.d1.6.{top_bottom}')))
    discriminator.add(0, BS())
    discriminator.add(2, BS())
    discriminator.add(1, PS(phi=pcvl.P(f'phi.d1.7.{top_bottom}')))
    discriminator.add(1, BS())
    discriminator.add(1, PS(phi=pcvl.P(f'phi.d1.8.{top_bottom}')))
    
    return discriminator

def generate_input_state():
    state1 = pcvl.StateVector([1, 0, 0, 0, 1, 0, 0, 0])
    state2 = pcvl.StateVector([0, 1, 0, 0, 0, 1, 0, 0])
    state3 = pcvl.StateVector([0, 0, 1, 0, 0, 0, 1, 0])
    state4 = pcvl.StateVector([0, 0, 0, 1, 0, 0, 0, 1])


    input_state = state1 + state2 + state3 + state4

    return input_state

def possible_output_states():

    return [pcvl.BasicState([1, 0, 0, 0, 1, 0, 0 , 0]),
            pcvl.BasicState([1, 0, 0, 0, 0, 1, 0 , 0]),
            pcvl.BasicState([1, 0, 0, 0, 0, 0, 1 , 0]),
            pcvl.BasicState([1, 0, 0, 0, 0, 0, 0 , 1]),
            pcvl.BasicState([0, 1, 0, 0, 1, 0, 0 , 0]),
            pcvl.BasicState([0, 1, 0, 0, 0, 1, 0 , 0]),
            pcvl.BasicState([0, 1, 0, 0, 0, 0, 1 , 0]),
            pcvl.BasicState([0, 1, 0, 0, 0, 0, 0 , 1]),
            pcvl.BasicState([0, 0, 1, 0, 1, 0, 0 , 0]),
            pcvl.BasicState([0, 0, 1, 0, 0, 1, 0 , 0]),
            pcvl.BasicState([0, 0, 1, 0, 0, 0, 1 , 0]),
            pcvl.BasicState([0, 0, 1, 0, 0, 0, 0 , 1]),
            pcvl.BasicState([0, 0, 0, 1, 1, 0, 0 , 1]),
            pcvl.BasicState([0, 0, 0, 1, 0, 1, 0 , 0]),
            pcvl.BasicState([0, 0, 0, 1, 0, 0, 1 , 0]),
            pcvl.BasicState([0, 0, 0, 1, 0, 0, 0 , 1])]
            

def main():

    generate_generator(generator1, 'top')
    generate_discriminator(discriminator1, 'top')

    generate_generator(generator2, 'bottom')
    generate_discriminator(discriminator2, 'bottom')
    

    main_circuit.add(0, generator1)
    main_circuit.add(0, discriminator1)

    secondary_circuit.add(0, generator2)
    secondary_circuit.add(0, discriminator2)

    full_circuit.add(0, main_circuit).add(4, secondary_circuit)

    input_state = generate_input_state()
    outputs = possible_output_states()

    #params=generator1.get_parameters()
    #print(params)
    #pcvl.pdisplay(discriminator1)
    pcvl.pdisplay(main_circuit) #,recursive=True)
    pcvl.pdisplay(secondary_circuit)
    pcvl.pdisplay(full_circuit)

    processor = pcvl.Processor("SLOS", pcvl.Circuit(8))
    processor.with_input(pcvl.BasicState([0, 1, 0, 0, 1, 1, 0, 0]))
    sampler = pcvl.algorithm.Sampler(processor)

    sample_count = sampler.sample_count(1000)
    return sample_count

if __name__ == "__main__":
    main()