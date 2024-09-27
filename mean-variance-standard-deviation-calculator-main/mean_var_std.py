import numpy as np

def calculate(list):

    my_list = np.array(list)

    if len(my_list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    matrix = np.reshape(my_list, (3,3))

    mean = [[matrix[:, 0].mean().item(), matrix[:, 1].mean().item(), matrix[:, 2].mean().item()], 
            [matrix[0, :].mean().item(), matrix[1, :].mean().item(), matrix[2, :].mean().item()], 
            matrix.mean().item()]
    variance = [[matrix[:, 0].var().item(), matrix[:, 1].var().item(), matrix[:, 2].var().item()], 
            [matrix[0, :].var().item(), matrix[1, :].var().item(), matrix[2, :].var().item()], 
            matrix.var().item()]
    standard_deviation = [[matrix[:, 0].std().item(), matrix[:, 1].std().item(), matrix[:, 2].std().item()], 
            [matrix[0, :].std().item(), matrix[1, :].std().item(), matrix[2, :].std().item()], 
            matrix.std().item()]
    max = [[matrix[:, 0].max().item(), matrix[:, 1].max().item(), matrix[:, 2].max().item()], 
            [matrix[0, :].max().item(), matrix[1, :].max().item(), matrix[2, :].max().item()], 
            matrix.max().item()]
    min = [[matrix[:, 0].min().item(), matrix[:, 1].min().item(), matrix[:, 2].min().item()], 
            [matrix[0, :].min().item(), matrix[1, :].min().item(), matrix[2, :].min().item()], 
            matrix.min().item()]
    sum = [[matrix[:, 0].sum().item(), matrix[:, 1].sum().item(), matrix[:, 2].sum().item()], 
            [matrix[0, :].sum().item(), matrix[1, :].sum().item(), matrix[2, :].sum().item()], 
            matrix.sum().item()]

    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': standard_deviation,
        'max': max,
        'min': min,
        'sum': sum
}

    return result
