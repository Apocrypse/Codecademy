# Returns the truthiness of the null_hypothesis
# Takes a p-value as it's input and assumes p > 0.05 is significant
def accept_null_hypothesis(p_value):
    """
    :type p_values: float
    :rtype: List[int]
    """
    return p_value > 0.05

hypothesis_tests = [0.1, 0.009, 0.051, 0.012, 0.37, 0.6, 0.11, 0.025, 0.0499, 0.0001]

for p_value in hypothesis_tests:
    print(accept_null_hypothesis(p_value))
