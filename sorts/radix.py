def radix_sort(to_be_sorted):
  maximum_value = max(to_be_sorted)
  max_exponent = len(str(maximum_value))
  being_sorted = to_be_sorted[:]

  for exponent in range(max_exponent):
    position = exponent + 1
    index = -position

    digits = [[] for i in range(10)]

    for number in being_sorted:
      number_as_a_string = str(number)
      try:
        digit = number_as_a_string[index]
      except IndexError:
        digit = 0
      digit = int(digit)

      digits[digit].append(number)
      print(digits)

    being_sorted = []
    for numeral in digits:
      being_sorted.extend(numeral)

  return being_sorted
