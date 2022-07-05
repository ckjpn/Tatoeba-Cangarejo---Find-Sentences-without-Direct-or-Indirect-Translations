from re import findall

source = "deu"
target = "eng"

input = open("links.csv")
adjacency = {}
print("Reading links...")
for line in input:
  split = findall("[^\t\n]+", line)
  if split[0] not in adjacency:
    adjacency[split[0]] = []
  adjacency[split[0]].append(split[1])

input = open("sentences.csv")
output = open("adjacency.csv", "w")
print("Writing unlinked...")
for line in input:
  split = findall("[^\t\n]+", line)
  if split[0] not in adjacency:
    print(split[0], file = output)

print("Writing linked...")
for id1 in adjacency:
  print(id1, end = "", file = output)
  for id2 in adjacency[id1]:
    print("\t", id2, sep = "", end = "", file = output)
  for id2 in adjacency[id1]:
    for id3 in adjacency[id2]:
      print("\t", id3, sep = "", end = "", file = output)
  print("\n", end = "", file = output)

del adjacency

input = open("sentences.csv", encoding="utf-8")
language = {}
print("Reading languages...")
for line in input:
  split = findall("[^\t\n]+", line)
  language[split[0]] = split[1]

input = open("adjacency.csv")
output = open("ids.csv", "w")
print("Writing IDs...")
for line in input:
  split = findall("[^\t\n]+", line)
  if split[0] in language and language[split[0]] == source and all(id not in language or language[id] != target for id in split):
    print(split[0], file = output)

del language

untranslated = set()
input = open("ids.csv")
print("Reading IDs...")
for line in input:
  split = findall("[^\t\n]+", line)
  untranslated.add(split[0])

input = open("sentences.csv", encoding="utf-8")
output = open("untranslated.csv", "w", encoding="utf-8")
print("Writing untranslated...")
for line in input:
  split = findall("[^\t\n]+", line)
  if split[0] in untranslated:
    print(line, end = "", file = output)

print("Done!")
