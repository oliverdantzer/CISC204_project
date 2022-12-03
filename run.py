
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from nnf.operators import iff

# Encoding that will store all of your constraints
E = Encoding()

# DEFINITIONS

HANDS = [1, 2, 3, 4, 5]
VALUES = [i for i in range(1,14)] # Values go from 1-13
SUITS = ["spades", "clubs", "hearts", "diamonds"]


# Where we store proposition objects

prop_dict = {
    
}

PROPOSITIONS = []


##################
# HELP FUNCTIONS #
##################


class Unique(object):
    def __hash__(self):
        return hash(str(self))
    def __eq__(self, other):
        return hash(self) == hash(other)
    def __repr__(self):
        return str(self)
    def __str__(self):
        assert False, "You need to define the __str__ function on a proposition class"


def unFuncForArr(func, a):
    lis = []
    for x in a:
            lis.append(func(x))
    return lis


def binFuncForArrs(func, a1, a2):
    lis = []
    for x in a1:
        for y in a2:
            lis.append(func(x, y))
    return lis


def forAllDeck(func):
    return binFuncForArrs(func, VALUES, SUITS)


################
# PROPOSITIONS #
################


# e_ns

# At most 5 cards in hand, therefore only 5 of all the e_ns be true
@constraint.at_most_k(E, 5) # Slows down the program like crazy
@proposition(E)
class e_ns(Unique):
    def __init__(self, n, s):
        self.n = n
        self.s = s
    def __str__(self):
        return f"e_{self.n},{self.s}"

# PROPOSITIONS.extend(forAllDeck(e_ns))
prop_dict["e_ns"] = forAllDeck(e_ns)


#k_i

@proposition(E)
@constraint.exactly_one(E)
class k_i(Unique):
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return f"k_{self.i}"

for hand in HANDS:
    # PROPOSITIONS.append(k_i(hand))
    prop_dict["k_i"] = k_i(hand)


# p_ns

@constraint.exactly_one(E)
@proposition(E)
class p_ns(Unique):
    def __init__(self, n, s):
        self.n = n
        self.s = s
    def __str__(self):
        return f"p_{self.n},{self.s}"

# PROPOSITIONS.extend(forAllDeck(p_ns))
prop_dict["p_ns"] = forAllDeck(p_ns)


# m_nq

@proposition(E)
class m_nq(Unique):
    def __init__(self, n, q):
        self.n = n
        self.q = q
    def __str__(self):
        return f"m_{self.n},{self.q}"

# PROPOSITIONS.extend(binFuncForArrs(m_nq, VALUES, [1, 2, 3])) # can be 1-3 other cards with same value in hand
prop_dict["m_nq"] = binFuncForArrs(m_nq, VALUES, [1, 2, 3]) # can be 1-3 other cards with same value in hand

# sm_nq

@proposition(E)
class sm_nq(Unique):
    def __init__(self, n, q):
        self.n = n
        self.q = q
    def __str__(self):
        return f"sm_{self.n},{self.q}"

# PROPOSITIONS.extend(binFuncForArrs(sm_nq, VALUES, [1, 2, 3])) # can be 1-3 other cards with same value in hand
prop_dict["sm_nq"] = binFuncForArrs(sm_nq, VALUES, [1, 2, 3]) # can be 1-3 other cards with same value in hand


# f_sc

@proposition(E)
class f_sc(Unique):
    def __init__(self, s, c):
        self.s = s
        self.c = c
    def __str__(self):
        return f"f_{self.s},{self.c}"

# PROPOSITIONS.extend(binFuncForArrs(f_sc, SUITS, [1, 2, 3, 4])) # can be 1-4 other cards with same suit in hand
prop_dict["f_sc"] = binFuncForArrs(f_sc, SUITS, [2, 3, 4]) # can be 2-4 other cards with same suit in hand


# sf_sc

@proposition(E)
class sf_sc(Unique):
    def __init__(self, s, c):
        self.s = s
        self.c = c
    def __str__(self):
        return f"sf_{self.s},{self.c}"

# PROPOSITIONS.extend(binFuncForArrs(sf_sc, SUITS, [1, 2, 3, 4])) # can be 1-4 other cards with same suit in 
prop_dict["sf_sc"] = binFuncForArrs(sf_sc, SUITS, [2, 3, 4]) # can be 2-4 other cards with same suit in 


# g_d

@proposition(E)
class g_d(Unique):
    def __init__(self, d):
        self.d = d
    def __str__(self):
        return f"g_{self.d}"

# PROPOSITIONS.extend(unFuncForArr(g_d, [i for i in range(1,56)])) # ranges from the smallest group (1) to the largest group (9 + 10 + 11 + 12 + 13 = 55)
prop_dict["g_d"] = unFuncForArr(g_d, [i for i in range(1,56)]) # ranges from the smallest group (1) to the largest group (9 + 10 + 11 + 12 + 13 = 55)


# d_g

@proposition(E)
class d_g(Unique):
    def __init__(self, g):
        self.g = g
    def __str__(self):
        return f"d_{self.g}"

# PROPOSITIONS.extend(unFuncForArr(d_g, [i for i in range(1,56)])) # ranges from the smallest group (1) to the largest group (9 + 10 + 11 + 12 + 13 = 55)
prop_dict["d_g"] = unFuncForArr(d_g, [i for i in range(1,56)]) # ranges from the smallest group (1) to the largest group (9 + 10 + 11 + 12 + 13 = 55)


# sg_d

@proposition(E)
class sg_d(Unique):
    def __init__(self, d):
        self.d = d
    def __str__(self):
        return f"sg_{self.d}"

# PROPOSITIONS.extend(unFuncForArr(sg_d, [i for i in range(1,63)])) # ranges from the smallest group (1) to the largest group (8 + 9 + 10 + 11 + 12 + 13 = 55)
prop_dict["sg_d"] = unFuncForArr(sg_d, [i for i in range(1,63)]) # ranges from the smallest group (1) to the largest group (8 + 9 + 10 + 11 + 12 + 13 = 55)


# sd_g

@proposition(E)
class sd_g(Unique):
    def __init__(self, g):
        self.g = g
    def __str__(self):
        return f"sd_{self.g}"

# PROPOSITIONS.extend(unFuncForArr(sd_g, [i for i in range(1,63)])) # ranges from the smallest group (1) to the largest group (8 + 9 + 10 + 11 + 12 + 13 = 55)
prop_dict["sd_g"] = unFuncForArr(sd_g, [i for i in range(1,63)]) # ranges from the smallest group (1) to the largest group (8 + 9 + 10 + 11 + 12 + 13 = 55)


@proposition(E)
class BasicPropositions(Unique):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return f"{self.data}"

w = BasicPropositions("w")
c = BasicPropositions("c")
vd = BasicPropositions("vd")
rx = BasicPropositions("rx")
ry = BasicPropositions("ry")
us = BasicPropositions("us")
ud = BasicPropositions("ud")
l = BasicPropositions("l")

prop_dict["w"] = w
prop_dict["c"] = c
prop_dict["vd"] = vd
prop_dict["rx"] = rx
prop_dict["ry"] = ry
prop_dict["us"] = us
prop_dict["ud"] = ud
prop_dict["l"] = l

for key in prop_dict.keys():
    prop = prop_dict[key]
    if type(prop) != list:
        PROPOSITIONS.append(prop)
    else:
        PROPOSITIONS.extend(prop)

# PROPOSITIONS.extend([c,vd,rx,ry,us,ud,l])


###############
# CONSTRAINTS #
###############
# KEEP IN MIND THAT THE CONSTRAINT COMMENTS 
# TREAT EACH NEXY PROPOSITION LIKE IT HAS
# IS DIFFERENT, FOR EXAMPLE:
# e_ns and e_ns could be different, because
# their n or s could be different values

def constraint1():
    # CONSTRAINT #1: g_d IFF ((m_nq | f_sc | e_ns) & ~(m_nq & f_sc & e_ns) & ~(m_nq & f_sc) & ~(f_sc & e_ns) & ~(m_nq & e_ns))
    # g_d IFF (m_nq | f_sc | e_ns)
    for g in prop_dict["g_d"]:
        for m in prop_dict["m_nq"]:
            for f in prop_dict["f_sc"]:
                for e in prop_dict["e_ns"]:
                    E.add_constraint(g >> m | f | e)
                    E.add_constraint(m | f | e >> g)

    # g_d IFF ~(m_nq & f_sc & e_ns)
    for g in prop_dict["g_d"]:
        for m in prop_dict["m_nq"]:
            for f in prop_dict["f_sc"]:
                for e in prop_dict["e_ns"]:
                    E.add_constraint(g >> ~(m & f & e))
                    E.add_constraint(~(m & f & e) >> g)

    # g_d IFF ~(m_nq & f_sc)
    for g in prop_dict["g_d"]:
        for m in prop_dict["m_nq"]:
            for f in prop_dict["f_sc"]:
                E.add_constraint(g >> ~(m & f))
                E.add_constraint(~(m & f) >> g)

    # g_d IFF ~(f_sc & e_ns)
    for g in prop_dict["g_d"]:
        for f in prop_dict["f_sc"]:
            for e in prop_dict["e_ns"]:
                E.add_constraint(g >> ~(f & e))
                E.add_constraint(~(f & e) >> g)

    # g_d IFF ~(m_nq & e_ns))
    for g in prop_dict["g_d"]:
        for m in prop_dict["m_nq"]:
            for e in prop_dict["e_ns"]:
                E.add_constraint(g >> ~(m & e))
                E.add_constraint(~(m & e) >> g)

def constraint2():
    # sg_d IFF (sm_nq | sf_sc) & ~(sm_nq | sf_sc)

    # sg_d IFF (sm_nq | sf_sc)
    for sg in prop_dict["sg_d"]:
        for sm in prop_dict["sm_nq"]:
            for sf in prop_dict["sf_sc"]:
                E.add_constraint(sg >> (sm | sf))
                E.add_constraint((sm | sf) >> sg)
    
    # sg_d IFF ~(sm_nq | sf_sc)
    for sg in prop_dict["sg_d"]:
        for sm in prop_dict["sm_nq"]:
            for sf in prop_dict["sf_sc"]:
                E.add_constraint(sg >> (sm | sf))
                E.add_constraint((sm | sf) >> sg)

def constraint3():
    # d_x >> g_x
    for i, d in enumerate(prop_dict["d_g"]):
        E.add_constraint(d >> prop_dict["g_d"][i])

def constraint4():
    # sd_x >> sg_x
    for i, d in enumerate(prop_dict["sd_g"]):
        E.add_constraint(d >> prop_dict["sg_d"][i])

def constraint5():
    # ry IFF c & vd
    E.add_constraint(prop_dict["ry"] >> prop_dict["c"] & prop_dict["vd"])
    E.add_constraint(prop_dict["c"] & prop_dict["vd"] >> prop_dict["ry"])

def constraint6():
    E.add_constraint(prop_dict["rx"] >> ~prop_dict["c"])
    E.add_constraint(~prop_dict["c"] >> prop_dict["rx"])

def constraint7():
    # l | (ry & g_d & d_g) | (rx & sg_d & sd_g) >> us 
    for g in prop_dict["g_d"]:
        for d in prop_dict["d_g"]:
            for sg in prop_dict["sg_d"]:
                for sd in prop_dict["sd_g"]:
                    E.add_constraint(prop_dict["l"] | (prop_dict["ry"] & g & d) | (prop_dict["rx"] & sg & sd) >> prop_dict["uus"])

constraint1() # Slows down the program like crazy
constraint2() # Slows down the program like crazy
constraint3()
constraint4()
constraint5()
constraint6()
constraint7() # Slows down the program like crazy




########
# MAIN #
########


# T = example_theory()
# Don't compile until you're finished adding all your constraints!
T = E.compile()
# After compilation (and only after), you can check some of the properties
# of your model:
print("Compiled")

print("\nSatisfiable: %s" % T.satisfiable())
print("# Solutions: %d" % count_solutions(T))
print("   Solution: %s" % T.solve())

# The variable likelihoods take way too long to load
"""
print("\nVariable likelihoods:")
for v in PROPOSITIONS:
    # Ensure that you only send these functions NNF formulas
    # Literals are compiled to NNF here
    print(" %s: %.2f" % (str(v), likelihood(T, v)))
"""
print()

