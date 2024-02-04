from perceval.components.unitary_components import PS, BS, PERM
import numpy as np
import perceval as pcvl
from scipy.optimize import minimize
import main
import loss

np.random.seed(1729)

initial_gen_weights = np.random.rand(30) * 2 * np.pi
initial_disc_weights = np.random.rand(12) * 2 * np.pi

main.set_weights(main.gen_circuit, initial_gen_weights)
main.set_weights(main.disc_circuit, initial_disc_weights)

# optimized = minimize(loss.disc_loss, initial_disc_weights, method='BFGS', options={"c1": 10**-6, "c2":})
# print(optimized)
# print("")
# optimized2 = minimize(loss.disc_loss, optimized.x, method='BFGS')
# print(optimized2)
# print("")
# optimized3 = minimize(loss.disc_loss, optimized2.x, method='BFGS')
# print(optimized3)
# print("")
# optimized4 = minimize(loss.disc_loss, optimized3.x, method='BFGS')
# print(optimized4)
# print("")
# print(optimized4.x - initial_disc_weights)


def compute_dthetas(loss, init_weights, alpha):

    length = np.size(init_weights)

    if length == 12:
        main.set_weights(main.disc_circuit, init_weights)
    else:
        main.set_weights(main.gen_circuit, init_weights)

    dthetas = np.zeros(length)

    weights = init_weights.copy()

    for i in range(length):
        weights[i] += 0.1
        upper = loss(weights)
        weights[i] -= 0.2
        lower = loss(weights)
        dthetas[i] = (upper + lower) / 0.2

    dthetas *= alpha

    return dthetas

disc_weights = initial_disc_weights.copy()
gen_weights = initial_gen_weights.copy()

weight_data = []

def disc_phase(init_weights, alpha):
    weights = init_weights.copy()
    for i in range(5):
        dthetas = compute_dthetas(loss.disc_loss, weights, alpha)
        weights -= dthetas

        disc_loss = loss.disc_loss(weights)
        print(f"disc_loss: {disc_loss}")
        weight_data.append(np.array([disc_loss, 0]))

    return weights, disc_loss

def gen_phase(init_weights, alpha, disc_loss):
    weights = init_weights.copy()
    for i in range(5):
        dthetas = compute_dthetas(loss.gen_loss, weights, alpha)
        weights += dthetas
        
        gen_loss = loss.gen_loss(weights)
        print(f"gen_loss: {gen_loss}")
        weight_data.append(np.array([gen_loss, 1]))

        if (gen_loss > disc_loss):
            weights -= dthetas
            print("heheheha")
            break

    return weights


for i in range(250):
    disc_weights, disc_loss = disc_phase(disc_weights, 1/(i+1))
    main.set_weights(main.disc_circuit, disc_weights)

    gen_weights = gen_phase(gen_weights, 1/((i+1)), disc_loss)
    main.set_weights(main.gen_circuit, gen_weights)
    np.save("data2.npy", weight_data, np.array(weight_data))






