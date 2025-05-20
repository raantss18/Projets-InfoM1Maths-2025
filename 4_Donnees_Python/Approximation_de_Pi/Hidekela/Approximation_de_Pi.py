"""
    Approximation_de_Pi.py

    Author: Hidekela (MAFI)

    Description: A program trying to approximate Pi by Monte Carlo method

    Requirement: For visualizing the points inside the circle, we need matplotlib

"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from math import fabs as fabs, pi as pi
import random

def set_figure():
	"""
		Set the ax config, square and circle
		
	"""
	
	fig, ax = plt.subplots()
	C = patches.Circle((0,0), 1, ec='#ff7f0e', fc='none', linewidth=2)
	S = patches.Rectangle((-1,-1), 2, 2, fc='none', ec='#1f77b4', linewidth=2)
	ax.set_aspect('equal')
	ax.set_xlim(-1.5, 1.5)
	ax.set_ylim(-1.5, 1.5)
	ax.add_patch(S)
	ax.add_patch(C)
	plt.title("Approximation de Pi: méthode de Monte Carlo")
	plt.xlabel("Axe X")
	plt.ylabel("Axe Y")

def approx_pi_monte_carlo(error_bound):
	"""
		Monte Carlo Pi approximation implementation
	
	"""
	
	inside, pt_inside = 0, []
	outside, pt_outside = 0, []
	
	Pi = pi
	Pi_approximation = 0
	
	Pi_approx_evolutions = []

	while fabs(Pi - Pi_approximation) > error_bound :
		x = random.uniform(-1, 1)
		y = random.uniform(-1, 1)
		
		if x**2 + y**2 <= 1:
			inside += 1
			pt_inside.append((x,y))
		else:
			outside += 1
			pt_outside.append((x,y))
		
		Pi_approximation = (inside / (outside + inside)) * 4
		
		Pi_approx_evolutions.append(Pi_approximation)
		
	return Pi_approximation, pt_inside, pt_outside, Pi_approx_evolutions

def draw_result(pt_inside, pt_outside, Pi_approx_evolutions):
	"""
		Draw the final result: the points inside/outside the circle 
		and evolution of the estimation
	
	"""
	
	# Figure 1: circle & square & points
	# set the figure
	set_figure()
	
	# plot the points inside the circle
	x, y = [], []
	for x_, y_ in pt_inside:
		x.append(x_)
		y.append(y_)
	plt.scatter(x, y, fc='blue', ec='none')
	
	# plot the points outside the circle
	x, y = [], []
	for x_, y_ in pt_outside:
		x.append(x_)
		y.append(y_)
	plt.scatter(x, y, fc='gray', ec='none')
	
	# Figure 2: the evolution of the estimation
	plt.subplots()
	x = [i for i in range(len(Pi_approx_evolutions))]
	plt.plot(x, Pi_approx_evolutions)
	plt.title("Evolution de l'approximation de Pi")
	plt.xlabel("Axe X")
	plt.ylabel("Axe Y")
	
	# finally show the figure
	plt.show()
	
if __name__ == '__main__':
	print("-------------------------------------------------------------------------------")
	print("----------------  Approximation de Pi: méthode de Monte Carlo  ----------------")
	print("-------------------------------------------------------------------------------")
	print("")

	error_bound = float(input("Saisissez la marge d'erreur (ex: 10**(-2), 0.0001,...) :\n"))

	Pi_approx, pt_inside, pt_outside, Pi_approx_evolutions = approx_pi_monte_carlo(error_bound)

	print("La valeur de Pi est approximativement", Pi_approx, " avec une marge d'erreur de", error_bound)
	print("Il y a eu", len(pt_inside) + len(pt_outside), "nombre de points aléatoires générés, dont", len(pt_inside), "sont inscrit dans le cercle.")

	draw_result(pt_inside, pt_outside, Pi_approx_evolutions)
