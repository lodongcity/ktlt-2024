print ("lovandong")
print ("235752021610070")


def so_nguyen_to_nho_hon(n):

  primes = [True for i in range(n+1)]
  p = 2
  while (p * p <= n):
    if (primes[p] == True):
      for i in range(p * 2, n+1, p):
        primes[i] = False
    p += 1

  result = []
  for p in range(2, n):
    if primes[p]:
      result.append(p)

  return tuple(result)

primes_tuple = so_nguyen_to_nho_hon(1000000)

print(primes_tuple)
