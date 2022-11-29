
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BasicPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_most_one(E)
@proposition(E)
class At_most_onePropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# need to fix constraints to add all at same time
def createProposition(name, constr=None):
    prop = BasicPropositions(name)
    if constr == "at_most_one":
        constraint.add_exactly_one(E, prop)
    return prop


def createListProposition(name, r, constr=None):
    lis = []
    for i in range(r[0], r[1] + 1):
        name_string = name + "_" + str(i)
        prop = createProposition(name_string, constr)
        lis.append(prop)
    return lis


def create2dListProposition(name, r1, r2, constr=None):
    lis = []
    for i in range(r1[0], r1[1] + 1):
        lis.append(createListProposition(name + "_" + str(i), r2, constr))
    return lis


"""
def get_var_dim(var):
    if type(var) != list:
        return 0
    elif type(var[0]) != list:
        return 1
    elif type(var[0][0]) != list:
        return 2
"""
        

def get_all_props(lis):
    props = []
    for elem in lis:
        if type(elem) is list:
            for elem1 in elem:
                if type(elem1) is list:
                    for elem2 in elem1:
                        props.append(elem2)
                else:
                    props.append(elem1)
        else:
            props.append(elem)
    return props


def get_props_names_str(lis):
    big_string = ""
    for prop in lis:
        big_string += repr(prop)
    return big_string

e_ns = create2dListProposition("e", [1,13], [1,4])  # e_n_s
k_i = createListProposition("k", [1,5])  # k_i
p_ns = create2dListProposition("p", [1,13], [1,4])  # p_n_s
w = createProposition("w")  # w
m_nq = create2dListProposition("m", [1,13], [1,4])  # m_n_q
sm_nq = create2dListProposition("sm", [1,13], [1,4])  # sm_nq
f_sc = create2dListProposition("f", [1,4], [2,4])  # f_s_c (c is consecutive cards not including itself)
sf_sc = create2dListProposition("sf", [1,4], [2,4])  # sf_s_c (c is consecutive cards not including itself)
g_d = createListProposition("g", [1,55])  # g_d
d_g = createListProposition("d", [1,55])  # d_g
sg_d = createListProposition("sg", [1,63])  # sg_d
sd_g = createListProposition("sd", [1,63])  # sd_g
c = createProposition("c")  # c
vd = createProposition("vd")  # vd
rx = createProposition("rx")  # rx
ry = createProposition("ry")  # ry
us = createProposition("us")  # us
ud = createProposition("ud")  # ud
l = createProposition("l")  # l
prop_dict = {
    "e_ns": [e_ns, [1,13], [1,4]],
    "k_i": [k_i, [1,5]],
    "p_ns": [p_ns, [1,13], [1,4]],
    "w": w,
    "m_nq": [m_nq, [1,13], [1,4]],
    "sm_nq": [sm_nq, [1,13], [1,4]],
    "f_sc": [f_sc, [1,4], [2,4]],
    "sf_sc": [sf_sc, [1,4], [2,4]],
    "g_d": [g_d, [1,55]],
    "d_g": [d_g, [1,55]],
    "sg_d": [sg_d, [1,63]],
    "sd_g": [sd_g, [1,63]],
    "c": [c],
    "vd": [vd],
    "rx": [rx],
    "ry": [ry],
    "us": [us],
    "ud": [ud],
    "l": [l]
}


def rec(str_lis, prop_list_final, prop_list=[], i=0):
    if i >= len(str_lis):
        prop_list_final.append(prop_list)
        return None
    for elem in prop_dict[str_lis[i]][0]:
        rec(str_lis, prop_list_final, prop_list + [elem], i + 1)




# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    """
    # Add custom constraints by creating formulas with the variables you created. 
    E.add_constraint((a | b) & ~x)
    # Implication
    E.add_constraint(y >> z)
    # Negate a formula
    E.add_constraint((x & y).negate())
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)
    """

    # Constraint 0: g_d <-> (m_nq \/ f_sc \/ e_ns) /\ !(m_nq /\ f_sc /\ e_ns) /\ !(m_nq /\ f_sc) /\ !(f_sc /\ e_ns)  /\ !(m_nq /\ e_ns)
    # g_d >> ((m_nq | f_sc | e_ns) & ~(m_nq & f_sc & e_ns) & ~(m_nq & f_sc) & ~(f_sc & e_ns) & ~(m_nq & e_ns))
    prop_lis00 = ["g_d", "m_nq", "f_sc", "e_ns", "m_nq", "f_sc", "e_ns", "m_nq", "f_sc", "f_sc", "e_ns", "m_nq", "e_ns"]
    prop_lis_lis00 = []
    rec(prop_lis00, prop_lis_lis00)
    for prop_lis in prop_lis_lis00:
        E.add_constraint(prop_lis[0] >> ((prop_lis[1] | prop_lis[2] | prop_lis[3]) & ~(prop_lis[4] & prop_lis[5] & prop_lis[6]) & ~(prop_lis[7] & prop_lis[8]) & ~(prop_lis[9] & prop_lis[10])  & ~(prop_lis[11] & prop_lis[12])))
    # g_d << ((m_nq | f_sc | e_ns) & ~(m_nq & f_sc & e_ns) & ~(m_nq & f_sc) & ~(f_sc & e_ns) & ~(m_nq & e_ns))
    prop_lis01 = ["g_d", "m_nq", "f_sc", "e_ns", "m_nq", "f_sc", "e_ns", "m_nq", "f_sc", "f_sc", "e_ns", "m_nq", "e_ns"]
    prop_lis_lis01 = []
    rec(prop_lis01, prop_lis_lis01)
    for prop_lis in prop_lis_lis01:
        E.add_constraint(prop_lis[0] << ((prop_lis[1] | prop_lis[2] | prop_lis[3]) & ~(prop_lis[4] & prop_lis[5] & prop_lis[6]) & ~(prop_lis[7] & prop_lis[8]) & ~(prop_lis[9] & prop_lis[10])  & ~(prop_lis[11] & prop_lis[12])))
    
    

        
    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    all_props = get_all_props([e_ns, k_i, p_ns, w, m_nq, sm_nq, f_sc, sf_sc, g_d, d_g, sg_d, sd_g, c, vd, rx, ry, us, ud, l])
    for v,vn in zip(all_props, get_props_names_str(all_props)):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
