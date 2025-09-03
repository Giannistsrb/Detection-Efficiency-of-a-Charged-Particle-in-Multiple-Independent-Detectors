import scipy.stats as stats

#Define the binomial function:
def calculate_detection_probability(N, k):
    e = 0.6  # Efficiency of every detector
    detection_probability = 1 - stats.binom.cdf(k-1, N, e) 
    return detection_probability

#a. Calculation of the total detection probability using N=6 detector:
total_detection_probability = calculate_detection_probability(6, 4) #if k=4 then, k=1,2,3 are included.
print("Total detection probability using N=6 detectors:", total_detection_probability)

#b. Calculation of the minimum detectors in order to achieve a probability of at least 95%:

N = 1 #Initialization of the number of detectors 

while True:

    detection_probability = calculate_detection_probability(N, 4)

    if detection_probability >= 0.95:
        print("Minimum detectors:", N)
        break #if the probability is greater than 95%, then the process stops.

    N = N + 1  
