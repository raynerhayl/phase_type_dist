import numpy

filename = str(raw_input("File name: "))
with open(filename) as f:
    lines = [line.rstrip('\n') for line in open(filename)]

#Read first matrix
initial_arr = []
transition_arr = []
state = 0
for line in lines:
    row = []
    if line.__contains__("#")==False:
        tokens = line.split(",")
        for token in tokens:
            product = token.strip().split("*")
            prod = 1.0
            for x in product:
                prod = prod * float(x)
            if state == 0:
                initial_arr.append(prod)
            row.append(prod)
    if state == 1 and len(row)> 0:
        transition_arr.append(row)
    else:
        state = 1

e = []
for i in range(0, len(initial_arr)):
    row = [1.0]
    e.append(row)

initial_mat = numpy.matrix(initial_arr)
transition_mat = numpy.matrix(transition_arr)
e_mat = numpy.matrix(e)

print("Entry Matrix: \n")
print(initial_mat)
print("Transition Matrix: \n")
print(transition_mat)

E = numpy.matmul((-numpy.matmul(initial_mat, numpy.linalg.inv(transition_mat))), e_mat)
inv_sq = numpy.matmul(numpy.linalg.inv(transition_mat), numpy.linalg.inv(transition_mat))
V = (2 * numpy.matmul(initial_mat, numpy.matmul(inv_sq, e_mat)) - E*E)

E = E.tolist()[0][0]
V = V.tolist()[0][0]

print("E(X) = "+str(E))
print("Var(X) = "+str(V))
