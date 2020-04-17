# -*- coding: utf-8 -*-
"""Copy of SAT_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fy26t18WpJxEH-ejXsxgaAoEnPp90gdx

Make sure you fill in any place that says `YOUR CODE HERE`.

---

# Homework 13 (SAT)

*This* is a Python Notebook homework.  It consists of various types of cells: 

* Text: you can read them :-) 
* Code: you should run them, as they may set up the problems that you are asked to solve.
* **Solution:** These are cells where you should enter a solution.  You will see a marker in these cells that indicates where your work should be inserted.  

```
    # YOUR CODE HERE
```    

* Test: These cells contains some tests, and are worth some points.  You should run the cells as a way to debug your code, and to see if you understood the question, and whether the output of your code is produced in the correct format.  The notebook contains both the tests you see, and some secret ones that you cannot see.  This prevents you from using the simple trick of hard-coding the desired output. 

### Working on Your Notebook

To work on your notebook: 

* Click on _File > Save a copy in Drive_ : this will create a copy of this file in your Google Drive; you will find the notebook in your _Colab Notebooks_ folder. 
* Work on that notebook.  Check that the runtime has GPUs (Runtime > Change Runtime Type, and check that GPU is selected).

### Submitting Your Notebook

Submit your work as follows: 

* Download the notebook from Colab, clicking on "File > Download .ipynb".
* Upload the resulting file to [this Google form](https://docs.google.com/forms/d/e/1FAIpQLSdT35_UogevqcRyJH8dYkA4znQrU_drehr6SrmnCqTt1FOjlQ/viewform?usp=sf_link).
* **Deadline: [see home page](https://sites.google.com/a/ucsc.edu/luca/classes/cse-30/cse-30-fall-2019)**

You can submit multiple times, and the last submittion before the deadline will be used to assign you a grade.

Let $p_1, p_2, \ldots$ be propositional variables. 
A SAT problem, represented in [conjunctive normal form](https://en.wikipedia.org/wiki/Conjunctive_normal_form), consists in a conjunction of disjunctions of propositional variables and their complements, such as

$$
(p_1 \vee \bar{p}_2 \vee p_3) \wedge (p_2 \vee p_5) \; .
$$

We call each conjuct a [_clause_](https://en.wikipedia.org/wiki/Clause_(logic);
in the above example, we have two clauses, $c_1 = p_1 \vee \bar{p}_2 \vee p_3$ and 
$c_2 = p_2 \vee p_5$. 
The disjuncts in a clause are called [_literals_](https://en.wikipedia.org/wiki/Literal_(mathematical_logic): 
for example, the first clause $c_1 = p_1 \vee \bar{p}_2 \vee p_3$ contains the literals $p_1$, $\bar{p}_2$, and $p_3$. 

The satisfiability question is: can we find a truth assignment to the variables that makes the expression true?
In the above case, the answer is yes: we can take: 

$$
p_1 = True, \; p_5 = True
$$

and any value for $p_2, p_3$.

### NP completeness of SAT and Sudoku

_This is optional material that can be skipped if desired._

In general, determining whether an expression for SAT (in conjunctive normal form) is satisfiable is an [NP-complete](https://en.wikipedia.org/wiki/NP-completeness) problem, which means, intuitively, two things: 

* **If you guess a solution, you can check it in polynomial time.** The problem being an NP problem means: if we could guess a solution (a truth assignment to the $m$ variables), we would be able to check that the solution is valid in time that is polynomial in $n$, that is, that is bounded by a polynomial of $n$. In general, NP is the set of problems that can be solved in nondeterministic polynomial time, and thus, the set of problems that can be solved by making a lucky guess, and checking the guess in polynomial time. 

* **The problem is as hard as any other NP problem** (or: the problem is NP-complete). Precisely, if we have another NP problem, we can reduce it in polynomial time to our problem, showing that if we could solve our problem in (deterministic) polynomial time, we could solve all other NP problems in polynomial time too.  Unfortunately, it is not known whether NP complete can be solved in deterministic polynomial time. 

Thus, NP-complete problems are problems such that, if you chance on the solution, you can check it efficiently, but the only way currently known for solving them consists in searching for a solution, perhaps with the help of heuristics. 
You will learn about NP completeness in courses on computational complexity; a marvelous book on the topic, which every competent computer scientist should read, is the one by [Garey and Johnson](https://www.amazon.com/Computers-Intractability-NP-Completeness-Mathematical-Sciences/dp/0716710455).

SAT is NP-complete; in fact, it is the prototypical NP-complete problem.  As we unfortunately do not know how to do lucky guesses, solving it involves search. 

Sudoku is actually not NP complete as defined: in fact, it can be solved _in constant time!_ 
For our Sudoku problems, the input size $n = 9^2 = 81$, constant -- and this constant-sized problem can be solved in constant time just by searching through the fixed number of $9^{81}$ solutions!  But $9^{81}$ is a large number, so our search algorithm is much better than the constant-time brute-force approach.
It has been shown that [a generalized version of Sudoku with unbounded input size is NP-complete](http://www-imai.is.s.u-tokyo.ac.jp/~yato/data2/SIGAL87-2.pdf) (the author has not checked the proof).

## SAT representation

To represent an instance of SAT, we represent literals, clauses, and the overall expression, as follows.

**Literals.** We represent the literal $p_k$ via the positive integer $k$, and the literal $\bar{p}_k$ via the negative integer $-k$. 

**Clauses.** We represent a clause via the set of integers representing the clause literals.  
For instance, we represent the clause $p_1 \vee \bar{p}_3 \vee p_4$ via the set $\{1, -3, 4\}$. 

**SAT problem.**  We represent a SAT problem (again, in conjunctive normal form) via the set consisting in the representation of its clauses. 
For instance, the problem 
$$
(p_1 \vee \bar{p}_2 \vee p_3) \wedge (p_2 \vee p_5)
$$
is represented by the set of sets:
$$
\{ \{1, -2, 3\}, \{2, 5\} \} \; .
$$

There are various operations that we need to do on clauses, and on the overall SAT problem, to solve it.  Thus, we encapsulate both clauses, and the SAT problem, in python classes, so we can associate the operations along with the representations.

### Clauses

We first define an auxiliary function, which tells us whether a set contains both an integer and its negative.  This will be used, for instance, to detect whether a clause contains both a literal and its complement.
"""
# Let us ensure that nose is installed.

from nose.tools import assert_equal, assert_true
from nose.tools import assert_false, assert_almost_equal

def has_pos_and_neg(l):
    return len(set(l)) > len({abs(x) for x in l})


"""This is the class representing a clause.  Note how it can be initialized either with a sequence of integers, representing the literals, or with a clause, in which case it returns a copy of the input clause."""


class Clause(object):

    def __init__(self, clause):
        """Initializes a clause.  Here, the input clause is either a list or set
        of integers, or is an instance of Clause; in the latter case, a shallow
        copy is made, so that one can modify this clause without modifying the
        original clause."""
        if isinstance(clause, Clause):
            # We use frozenset here, so that clauses are not modifiable.
            # This ensures that two equal clauses always have the same hash,
            # due also to our definition of the __hash__ method.
            self.literals = frozenset(clause.literals)
        else:
            for i in clause:
                # Sanity check.
                assert isinstance(i, int), "Not an integer: %r" % i
            self.literals = frozenset(clause)

    def __repr__(self):
        return repr(self.literals)

    def __eq__(self, other):
        return self.literals == other.literals

    def __hash__(self):
        """This will be used to be able to have sets of clauses,
        with clause equality defined on the equality of their literal sets."""
        return hash(self.literals)

    def __len__(self):
        return len(self.literals)

    @property
    def istrue(self):
        """A clause is true if it contains both a predicate and its complement."""
        return has_pos_and_neg(self.literals)

    @property
    def isfalse(self):
        """A clause is false if and only if it is empty."""
        return len(self.literals) == 0


"""### Truth assignments

We are seeking a truth assignment for the propositional variables that makes the expression true, and so, that makes each clause true.  

We represent the truth assignment that assigns True to $p_k$ via the integer $k$, and the truth assignment that assigns False to $p_k$ via $-k$.  Thus, if you have a (positive or negative) literal $i$, the truth assignment $i$ will make it true. 

We represent truth assignments to multiple variables simply as the set of assignments to individual variables. 
For example, the truth assignment that assigns True to $p_1$ and False to $p_2$ will be represented via the set $\{1, -2\}$.

### Truth assignments and clause simplification

To solve a SAT instance, we need to search for a truth assignment to its propositional variables that will make all the clauses true. 
As we try different truth assignments and evaluate their effect, a basic operation isWe will need to search for such a truth assignment.  So the basic operation will be: 

> Given a clause, and a truth assignment for one variable, compute the result on the clause. 

What is the result?  Consider a clause  with representation $c$ (thus, $c$ is a set of integers) and a truth assignment $i$ (recall that $i$ can be positive or negative, depending on whether it assigns True or False to $p_i$).  There are three cases:

* If $i \in c$, then the $i$ literal of $c$ is true, and so is the whole clause. We return True to signify it. 
* If $-i \in c$, then the $-i$ literal of $c$ is false, and it cannot help make the clause true.  We return the clause $c \setminus \{-i\}$, which corresponds to the remaining ways of making the clause true under assignment $i$. 
* If neither $i$ nor $-i$ is in $c$, then we return $c$ itself, as $c$ is not affected by the truth assignment $i$. 

Based on the above discussion, implement a _simplify_ method for a Clause that, given a truth assignment, returns a simplified clause or True.
"""


### Exercise: define simplify

def clause_simplify(self, i):
    """Computes the result simplify the clause according to the 
    truth assignment i."""
    # YOUR CODE HERE
    if i in self.literals:
        return True
    elif -i in self.literals:
        return Clause(self.literals - {-i})
    else:
        return self


Clause.simplify = clause_simplify

"""Here are some tests to help you verify that your implementation works."""

# Let's test our simplification function.  Here is a clause.
c = Clause([1, 2, -3, 4])
# If we assign True to p_1, the whole clause is True.
assert_equal(c.simplify(1), True)

c = Clause([1, 2, -3, 4])
# If we assign False to 1 and True to 3, p_1 and p_3 are not useful
# any more to make the clause true.
assert_equal(c.simplify(-4), Clause([1, 2, -3]))

c = Clause([1, 2, -3, 4])
# Left unchanged.
assert_equal(c.simplify(12), c)

"""## SAT Representation

A SAT instance consists in a set of clauses. 

The SAT instance is satisfiable if and only if there is a truth assignment to predicates that satisfies all of its clauses. 
Therefore: 

* If the SAT instance contains no clauses, it is trivially satisfiable.
* If the SAT instance contains an empty clause, it is unsatisfiable, since there is no way to satisfy that clause. 

Based on this idea, the initializer method for our SAT class will get a list of clauses as input.  It will discard the tautologically true ones (as indicated by the istrue clause method).  If there is even a single unsatisfiable clause, then we set the SAT problem to consist of only one unsatisfiable clause, as a shorthand for denoting that the SAT problem cannot be satisfied. 

We endow the SAT class with mehods isfalse and istrue, that detect SAT problems that are trivially satisfiable by any truth assignment, or trivially unsatisfiable by any truth assignment. 

You will need to implement the methods _generate_candidate_assignments_, _apply_assignment_, and _solve_, which together will be used to search for a solution of the SAT instance.  These methods are discussed below.
"""


class SAT(object):

    def __init__(self, clause_list):
        """clause_list is a list of lists (or better, an iterable of 
        iterables), to represent a list or set of clauses."""
        raw_clauses = {Clause(c) for c in clause_list}
        # We do some initial sanity checking.  
        # If a clause is empty, then it
        # cannot be satisfied, and the entire problem is False.
        # If a clause is true, it can be dropped. 
        self.clauses = set()
        for c in raw_clauses:
            if c.isfalse:
                # Unsatisfiable.
                self.clauses = {c}
                break
            elif c.istrue:
                pass
            else:
                self.clauses.add(c)

    def __repr__(self):
        return repr(self.clauses)

    def __eq__(self, other):
        return self.clauses == other.clauses

    @property
    def isfalse(self):
        return len(self.clauses) == 1 and list(self.clauses)[0] == Clause([])

    @property
    def istrue(self):
        return len(self.clauses) == 0


"""#### generate_candidate_assignments

In order to solve a SAT instance, we proceed with the choice-constraint propagation-recursion setting.  Let us build the choice piece first. 
The idea is this: if we are to make true a clause $c$, we have to make true at least one of its literals.  Thus, we can pick a clause $c$, and try the truth assignment corresponding to each of its literals in turn: at least one of them should work.  Which clause is best to pick?  As in the Sudoku case, one with minimal length, so that the probability of one of its literals being true is highest. 

Based on this, write a method _generate_candidate_assignments_ in the above SAT class, which returns the list or set of literals of one of the clauses of minimal length.  These will be the truth assignments we will need to try in turn.  Below are some tests that your code should pass.

_Note:_ the solution can (but need not) be written in one line of code.
"""


### Definition of `generate_candidate_assignments`

def sat_generate_candidate_assignments(self):
    """Generates candidate assignments.  
    If the SAT problem contains unary clauses (clauses with only
    one literal), then it returns a list of one candidate assignment,
    with the one candidate assignment consisting in the union of 
    all the unary clauses. 
    If the SAT problem does not contain any unary clause, then picks 
    one of its shortest clauses, and return as candidate assignments 
    a list of sets, one for each of the literals of the chosen clause."""
    # YOUR CODE HERE
    short = min(len(c) for c in self.clauses)
    for c in self.clauses:
        if len(c) == short:
            return set(c.literals)
    # return (set(x.literals) for x in self.clauses if len(x) == min(len(c) for c in self.clauses))


SAT.generate_candidate_assignments = sat_generate_candidate_assignments

### Tests for `generate_candidate_assignments`

s = SAT([[-1, -2, 3], [2, -3], [1, -4, 2, 1]])
assert_equal(set(s.generate_candidate_assignments()), {2, -3})

"""#### apply_assignment

Once we pick a truth assignment from one of the literals above, we need to propagate its effect to the clauses of the SAT instance. 

Write an _apply_assignment_ method in the SAT class given above, that takes as input a truth assignment $i$, and returns a new SAT object, whose clauses are obtained by simplifying the clauses of the current assignment according to $i$.  Clauses that are made true by $i$ (clauses where the _simplify_ method returns True) should not be part of the new SAT problem, since they are already satisfied. 

We provide below some tests for your code.

_Note:_ the solution can (but need not) be written in two lines of code.
"""


### Exercise: define `apply_assignment`

def sat_apply_assignment(self, assignment):
    """Applies the assignment to every clause, simplifying it.
    If a clause is false, the whole problem is unsatisfiable, 
    and we return False.  If a clause is True, it does not need
    to be included."""
    # YOUR CODE HERE
    o = set()
    print(s)
    print({x.simplify(assignment) for x in self.clauses if not isinstance(x.simplify(assignment), bool)})
    for x in s.clauses:
        if not isinstance(x.simplify(assignment), bool):
            o.add(x.simplify(assignment))
    print("ASSIGN SET", o)

    return SAT(o)
    # return SAT({x.simplify(assignment) for x in self.clauses if not isinstance(x.simplify(assignment), bool)})


SAT.apply_assignment = sat_apply_assignment

### Tests for `apply_assignment`

# First, examples in which each clause is simplified and is part of the
# new SAT problem.
s = SAT([[-1, -2, 3], [2, -3], [5, -4, 2, 10]])
t = s.apply_assignment(1)
assert_equal(t, SAT([[-2, 3], [2, -3], [5, -4, 2, 10]]))

s = SAT([[2, 3], [4, 2, -3], [2]])
t = s.apply_assignment(-2)
assert_equal(t, SAT([[3], [4, -3], []]))

### More tests for `apply_assignment`

# Second, an example in which some clauses are made True, and hence removed
# from the new SAT problem. 
s = SAT([[-1, -2, 3], [2, -3], [5, -4, 2, 10]])
t = s.apply_assignment(-1)
assert_equal(t, SAT([[2, -3], [5, -4, 2, 10]]))

s = SAT([[2, 3, -4], [-1, -3, 5], [-3]])
t = s.apply_assignment(3)
assert_equal(t, SAT([[-1, 5], []]))

"""#### solve

The main method for searching for a solution of the SAT instance is the _solve_ method. 
The _solve_ method takes no arguments, and should return either False, if the SAT instance is unsatisfiable, or a truth assignment that satisfies it.  The satisfying truth assignment should be returned as a set. 

The _solve_ method uses _generate_candidate_assignments_ and _apply_assignment_ above. 

First, the _solve_ method should check whether the SAT instance $S$ is trivially unsatisfiable (and return False) or trivially satisfiable (and return the empty set), using the _istrue_ and _isfalse_ methods. 
This takes care of the base cases of the search. 

If none of the above applies, _solve_ must generate candiate truth assignments, and try them one by one.  Each candidate truth assignment, once applied, gives rise to a new SAT problem $S'$; this new SAT problem can be solved by calling _SAT_ recursively.  If the new SAT problem $S'$ has no solution, you can move on to the next candidate assignment, if any; if the new SAT problem $S'$ has a solution, the solution can be combined with the candidate truth assignment that gave rise to $S'$, to form a complete solution of the original problem $S$.
"""


### Exercise: define `solve`

def sat_solve(self):
    """Solves a SAT instance.  
    First, it checks whether the instance is false (in which case
    it returns False) or true (in which case it returns an empty 
    assignment). 
    If neither of these applies, generates a list of candidate 
    assignments, and for each of them, applies them to the current SAT 
    instance, generating a new SAT instance, and solves it. 
    If the new SAT instance has a solution, merges it with the assignment,
    and returns it.  If it has no solution, tries the next candidate 
    assignment.  If no candidate assignment works, returns False, as 
    the SAT problem cannot be satisfied."""
    # YOUR CODE HERE
    o = frozenset()
    if self.isfalse:
        return False
    elif self.istrue:
        return set()
    l = self.generate_candidate_assignments()
    print("assignments,", l)
    for i in l:
        st = sat_apply_assignment(self, i)
        print("i:", i, "new set", st)

        if st.istrue:
            return {i}
        elif not st.isfalse:
            sat_solve(st)

    return {i}


SAT.solve = sat_solve

"""To help you verify your code, let us write a method _apply_assignment_ that, given a SAT problem, applies an assignment to it, and returns True if the SAT instance is satisfied."""


def sat_verify_assignment(self, assignment):
    assert not has_pos_and_neg(assignment), "The assignment is inconsistent"

    s = self
    for i in assignment:
        print("made it")
        print(i)
        print(s)
        s = s.apply_assignment(i)
        if s.istrue:
            return True
        if s.isfalse:
            return False
    return False


SAT.verify_assignment = sat_verify_assignment

### A solvable problem

s = SAT([[1, 2], [-2, 2, 3], [-3, -2]])
a = s.solve()
print("Assignment:", a)
assert_true(s.verify_assignment(a))

###  Another solvable problem.

s = SAT([[1, 2], [-2, 3], [-3, 4], [-4, 5], [8, -1]])
a = s.solve()
print("Assignment:", a)
assert_true(s.verify_assignment(a))

### Yet another solvable problem

s = SAT([[-1, 2], [-2, 3], [-3, 1]])
a = s.solve()
print("Assignment:", a)
assert_true(s.verify_assignment(a))

### An unsolvable problem

s = SAT([[1], [-1, 2], [-2]])
assert_false(s.solve())

### Another unsolvable problem

s = SAT([[-1, 2], [-2, 3], [-3, -1], [1]])
assert_false(s.solve())

### Yet another unsolvable problem

s = SAT([[-1, 2], [-2, 3], [-3, -1], [1], [-4, -3, -2]])
assert_false(s.solve())

"""## Epilogue

The above method for solving SAT instances works!  

Is that how it is done in real SAT solvers? 

Not quite.  What we wrote above is perhaps the simplest SAT solver, not the most efficient. 
Since SAT solvers are incredibly versatile -- many problems can be encoded into boolean satisfiability -- a very large amount of work has been done to make them faster and better.  Indeed, the study of strategies for SAT solvers is a field of computer science in itself, with its own conferences ([SAT](http://www.satisfiability.org/)) and [competitions](http://www.satcompetition.org/) dedicated to it. 
In particular, the constraint propagation generally uses three procedures in addition to those used above:

### Unary clauses correspond to truth assignments

If a clause contains only one literal, that literal must be part of the truth assignment, as it is the only way to satisfy the clause.  We note that we include this in an indirect way: when searching, we will preferentially select an unary clause if there is any, and take its literal as the (only) search option.

### Binary clauses correspond to implications and can be propagated quickly

If a clause is $p_1 \vee p_2$, it can also be read as $\neg p_1 \rightarrow p_2$, so that if $p_1$ is assigned False, we know that we need to assign True to $p_2$.  We can represent this via an edge from the literal $\bar{p}_1$ to the literal $p_2$.  Proceeding in this way, by looking at all binary clauses we can compute a graph (and keep it cached) that enables us to efficiently propagate truth assignments to literals. 

Our simple SAT solver also does a bit of this.  If we assign False to $p_1$, the binary clause $p_1 \vee p_2$ is simplified in $p_2$, and next time, $p_2$ as a unary clause will be likely to be chosen to become part of the truth assignment.  Thus, our use of _simplify_ and _solve_, along with the heuristic of choosing the shortest clauses in _solve_, go part of the way towards implementing this technique.  A cached, precomputed graph however leads to a much faster implementation. 

### Resolution

Consider two clauses that share a predicate variable, that appears positive (not complemented) in one clause, and complemented in the other:
$$
c_1 \, : \; p \vee q_1 \vee \cdots \vee q_n \\
c_2 \, : \; \bar{p} \vee r_1 \vee \cdots \vee r_m
$$
where $q_1, \ldots, q_n, r_1, \ldots, r_m$ are literals (positive or negative predicate variables). 
There are two cases: 

* either $p$ is False, and $q_1 \vee \cdots \vee q_n$ must be true, 
* or $p$ is True, and $r_1 \vee \cdots \vee r_m$ must be true.

In either case, the disjuction 
$$
c_{12}\, : \; q_1 \vee \cdots \vee q_n \; \vee \; r_1 \vee \cdots \vee r_m
$$
must hold.  
The process of merging $p_1$ and $p_2$ into $p_{12}$ is called _resolution_.  Resolution generates _more_ clauses: once $p_{12}$ is generated, we cannot discard $p_1$ or $p_2$.  However, having more clauses can lead to better constraint propagation: generally, what SAT solvers try to do is to cut down on the amont of exploration to be done, that is, they try to cut down the number of truth assignments that must be tried; limiting the number of clauses is a secondary concern.  Many heuristics are used to find clauses that are useful candidates for unification.

### Clause learning

Many modern SAT solvers, when they encounter a dead end in the exploration and need to backtrack, they summarize the fact that a particular truth assignment cannot be extended to a satisfying one via a _learned clause_.  These learned clauses are instrumental in pruning the remaining exploration to be performed.

Precisely, assume that the truth assignment so far is $x_1, \ldots, x_m$, where each $x_i$, $1 \leq i \leq m$, is a literal. 
If we find that there is no solution with this truth assignment, we need to backtrack in the search.  We can then add the clause 
$\neg(x_1 \wedge \cdots \wedge x_m) = \bar{x}_1 \vee \cdots \vee \bar{x}_m$ to remember that the truth assignment was shown to be a dead end.

### To learn more

To learn more, you can look at how the [MiniSat](http://minisat.se/Main.html) solver works; MiniSat is a simple yet efficient SAT solver.
"""