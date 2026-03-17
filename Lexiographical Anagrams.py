''' Write a code to segregate the anagrams w.r.t their
lexiographical orde and group  '''
#input : eat tea ate tan bat nat

from collections import defaultdict
words = input("Words: ").split()
amp = defaultdict(list)
for word in words:
    key= ' '.join(sorted(word))
    amp[key].append(word)
for group in amp.values():
    print(group)