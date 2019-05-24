def calculate_delta(seq):
    """ Return the constant difference of the seq

        :param seq: list
        :return: int
    """
    
    alfa = seq[1] - seq[0]
    beta = seq[2] - seq[1]
    kappa = seq[3] - seq[2]

    return alfa if alfa == beta or alfa == kappa else beta

def find_missing(seq):
    """ Return missing value in the seq if exists

        :param seq: list
        :return: mixed
    """

    if len(seq) >= 3:

        d = calculate_delta(seq)

        for index in range(len(seq) - 1):
            if not (seq[index + 1] - seq[index] == d):
                return seq[index] + d

        return "Correct Arithmetic sequence"

    else:
        return "Invalid seq"


if __name__ == "__main__":

    print(find_missing([1, 3, 7, 9, 11]))