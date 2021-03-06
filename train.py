from utils import eprint, read_dataset, dataset_to_vectors, learning_rate, estimate_price, write_thetas_to_file
from plot import display_plot

def theta0_cumulate(theta0, theta1, km, price, m):
    theta0_sum = 0
    for i in range(m):
        theta0_sum += (estimate_price(km[i], theta0, theta1) - float(price[i]))
    return float(theta0_sum)

def theta1_cumulate(theta0, theta1, km, price, m):
    theta1_sum = 0
    for i in range(m):
        theta1_sum += (estimate_price(km[i], theta0, theta1) - float(price[i])) * float(km[i])
    return float(theta1_sum)

def update_theta0(theta0, theta1, km, price, m):
    tmp_theta0 = theta0 - (learning_rate * (float(1/m) * theta0_cumulate(theta0, theta1, km, price, m)))
    return tmp_theta0

def update_theta1(theta0, theta1, km, price, m):
    tmp_theta1 = theta1 - (learning_rate * (float(1/m) * theta1_cumulate(theta0, theta1, km, price, m)))
    return tmp_theta1

def gradient_decsent_algorithm(km, price):
    theta0 = 0
    theta1 = 0
    m = len(km)
    exit_criteria_prev_theta0 = 0 
    exit_criteria_prev_theta1 = 0 
    while (exit_criteria_prev_theta0 != theta0_cumulate(theta0, theta1, km, price, m) and 
        exit_criteria_prev_theta1 != theta1_cumulate(theta0, theta1, km, price, m)):
        theta0_updated = update_theta0(theta0, theta1, km, price, m)
        theta1_updated = update_theta1(theta0, theta1, km, price, m)
        exit_criteria_prev_theta0 = theta0_cumulate(theta0, theta1, km, price, m)
        exit_criteria_prev_theta1 = theta1_cumulate(theta0, theta1, km, price, m)
        theta0 = theta0_updated
        theta1 = theta1_updated
    return theta0, theta1

def normalize_vector(vect):
    max_value = max(vect)
    result = [x / max_value for x in vect]
    return result

def restore_after_normalisation(theta0, theta1, km, price):
    return theta0 * max(price), theta1 * max(price) / max(km)

if __name__=="__main__":
    dataset = read_dataset()
    km, price = dataset_to_vectors(dataset)
    km_normalized = normalize_vector(km)
    price_normalized = normalize_vector(price)
    theta0, theta1 = gradient_decsent_algorithm(km_normalized, price_normalized)
    theta0, theta1 = restore_after_normalisation(theta0, theta1, km, price)
    write_thetas_to_file(theta0, theta1)
    display_plot(km, price, theta0, theta1)
