import perceval as pcvl


#processor = pcvl.Processor("SLOS", pcvl.Circuit(8))
##processor.with_input(pcvl.BasicState([0, 1, 0, 0, 1, 1, 0, 0]))
#sampler = pcvl.algorithm.Sampler(processor)

#sample_count = sampler.sample_count(1000)
#print(sample_count)

p = pcvl.Processor("SLOS", pcvl.components.BS())
p.with_input(pcvl.BasicState([1,1]))

# The sampler holds 'probs', 'sample_count' and 'samples' calls. You can use the one that fits your needs!
sampler = pcvl.algorithm.Sampler(p)

# A sampler call will return a Python dictionary containing sampling results, and two performance scores
# sample_count = sampler.sample_count(1000)
# sample_count contains {'results': <actual count>, 'physical_perf': float [0.0 - 1.0], 'logical_perf': float [0.0 - 1.0]}
sample_count = sampler.sample_count(1000)
print(sample_count['results'])
print('test')