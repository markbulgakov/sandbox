def array_amplitude(array, n):
    ma = array[1] - array[0]

    # Check for both sides adjacent elements that both must be less or both must be greater than current element
    for i in range(1, n-1):
        if array[i] > array[i-1] and array[i+1] < array[i] or array[i] < array[i-1] and array[i+1] > array[i]:
            # Update amplitude with max value
            ma = max(ma, abs(array[i] - array[i+1]))
        else:
            return -1

    return ma


if __name__ == '__main__':
    test_value = [1, 2, 1, 5, 0, 7, -6]
    print('Amplitude: %s' % array_amplitude(array=test_value, n=len(test_value)))
