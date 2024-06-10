#Sequential Numeric List Transformation: Implement a function transform_list(nums) that takes a list of integers and replaces each number with the sum of itself and its immediate neighbors. For the first and last elements, treat the missing neighbor as 0
def list(N):
    S = []
    if N[1:]:
        S += [N[0] + N[1]]
    else:
        S += [N[0]]
    for i in range(1, len(N) - 1):
        S += [N[i-1] + N[i] + N[i+1]]
    if N[:-1]:
        S += [N[-1] + N[-2]]
    else:
        S += [N[-1]]

    return S
print(list([1, 2, 3, 4]))  # Output: [3, 6, 9, 7]

