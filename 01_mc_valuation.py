
"""

Adapted from Python for Finance by Yves Hilpisch (2014).

Monte Carlo valuation of European call option
in Black-Scholes-Merton model.

"""

from numpy import *

# The parameters
S0 = 1000.0 # initial stock index level at time 0
K = 1500.0 # strike price of European call option
T = 1.0 # time to maturity. T = 1 if option has 1 year to maturity
r = 0.05 # risk-free interest rate (constant riskless short rate)
sigma = 0.2 # volatility

I = 100000 # number of Monte Carlo simulations

# Valuation algorithm
z = random.standard_normal(I)
ST = S0 * exp((r - 0.5 * sigma ** 2) * T + sigma * sqrt(T) * z)
hT = maximum(ST - K, 0)
C0 = exp(-r * T) * sum(hT) / I

print "Value of the European Call Option is %5.3f" % C0