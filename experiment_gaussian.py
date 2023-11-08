'''
this file is used to run experiments on the GA algorithm for the gaussian distribution
author : Yu-Cheng Chung
email  : ycchung@ntnu.edu.tw
date   : 2023 13 Sep

dependencies:
    GA.py
    gene.py
    gaussian.py
    transform.py
    numpy
    os
    multiprocessing

'''
import numpy as np
from GA import GA
from gaussian import gaussian
from transform import normalize_prob_distribution
from transform import normalize_state_vector
import multiprocessing as mp
from qiskit_algorithms import optimizers

#set the parameters
num_genes = mp.cpu_count()
num_qubit = 5
length_gene = 100
mutation_rate = 0.1
cpu_count = mp.cpu_count()
path = 'data/GA-data/gaussian/diff-genetic'
optimizer = optimizers.SPSA(maxiter=1000)
maxiter = 100
miniter = 10
threshold = 0.90
GPU = False
'''
'num_genes':20,
'length_gene':10,
'mutation_rate':0.1,
'cpu_count':mp.cpu_count(),               
'path':'data',
'experiment':'test',
'optimizer':optimizers.SPSA(maxiter=1000),
'maxiter':30,
'miniter':10, 
'threshold':0.90,
'num_types':7,
'GPU':_gpu_avaliable()
'''

#set the target distribution
#generate 15 mu from 0 to 15
mu = np.linspace(0,31,8)
#generate 15 sigma from 0 to 15
sigma = np.linspace(0,31,8)
#generate the target distribution
#use mu and sigma to generate 15*15 target distribution
for i in range(6):
    for j in range(6):
        target_distribution=gaussian(np.arange(2**num_qubit),mu[i],sigma[j])
        target_distribution=normalize_prob_distribution(target_distribution)
        target_statevector=normalize_state_vector(np.sqrt(target_distribution))
        #set the experiment name as 'gaussian_mu_{mu}_sigma_{sigma}'
        experiment = f'gaussian_mu_{mu[i]}_sigma_{sigma[j]}'
        #do the experiment
        GA(target_statevector=target_statevector,
           num_qubit=num_qubit,
           num_genes=num_genes,
           length_gene=length_gene,
           mutation_rate=mutation_rate,
           cpu_count=cpu_count,
           path=path,
           optimizer=optimizer,
           maxiter=maxiter,
           miniter=miniter,
           threshold=threshold,
           experiment=experiment,
           GPU=GPU)

        









