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

def generate_generator(generator):
    generator.add(1, PS(phi=pcvl.P('phi.g1.1')))
    generator.add(2, PS(phi=pcvl.P('phi.g1.2')))
    generator.add(3, PS(phi=pcvl.P('phi.g1.3')))
    generator.add(1, BS())
    generator.add(1, PS(phi=pcvl.P('phi.g1.4')))
    generator.add(1, BS())
    generator.add(0, BS())
    generator.add(2, BS())
    generator.add(0, PS(phi=pcvl.P('phi.g1.5')))
    generator.add(2, PS(phi=pcvl.P('phi.g1.6')))
    generator.add(0, BS())
    generator.add(2, BS())
    generator.add(1, PS(phi=pcvl.P('phi.g1.7')))
    generator.add(1, BS())
    generator.add(1, PS(phi=pcvl.P('phi.g1.8')))
    generator.add(1, BS())

    generator.add(0, PS(phi=pcvl.P('phi.g1.9')))
    generator.add(2, PS(phi=pcvl.P('phi.g1.10')))
    generator.add(0, BS())
    generator.add(2, BS())
    
    generator.add(0, PS(phi=pcvl.P('phi.g1.11')))
    generator.add(2, PS(phi=pcvl.P('phi.g1.12')))
    generator.add(0, BS())
    generator.add(2, BS())

    generator.add(0, PS(phi=pcvl.P('phi.g1.13')))
    generator.add(1, PS(phi=pcvl.P('phi.g1.14')))
    generator.add(2, PS(phi=pcvl.P('phi.g1.15')))

    return generator

def generate_discriminator(discriminator):
    discriminator.add(0, PS(phi=pcvl.P('phi.d1.1')))
    discriminator.add(1, PS(phi=pcvl.P('phi.d1.2')))
    discriminator.add(2, PS(phi=pcvl.P('phi.d1.3')))
    discriminator.add(0, BS())
    discriminator.add(2, BS())
    discriminator.add(0, PS(phi=pcvl.P('phi.d1.5')))
    discriminator.add(2, PS(phi=pcvl.P('phi.d1.6')))
    discriminator.add(0, BS())
    discriminator.add(2, BS())
    discriminator.add(1, PS(phi=pcvl.P('phi.d1.7')))
    discriminator.add(1, BS())
    discriminator.add(1, PS(phi=pcvl.P('phi.d1.8')))
    
    return discriminator

def main():

    generate_generator(generator1)
    generate_discriminator(discriminator1)

    generate_generator(generator2)
    generate_discriminator(discriminator2)
    

    main_circuit.add(0, generator1)
    main_circuit.add(0, discriminator1)

    secondary_circuit.add(0, generator2)
    secondary_circuit.add(0, discriminator2)

    #params=generator1.get_parameters()
    #print(params)
    #pcvl.pdisplay(discriminator1)
    pcvl.pdisplay(main_circuit) #,recursive=True)
    pcvl.pdisplay(secondary_circuit)

if __name__ == "__main__":
    main()