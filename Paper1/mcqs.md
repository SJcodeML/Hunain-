1- Which category do str, list, tuple, and range collectively belong to in Python?

A) Mapping Types

B) Numeric Types

C) Sequence Types

D) Set Types
----------------

2-What happens when you perform s2 = set("hello")?

A) It creates a set with all letters including duplicates: {'h', 'e', 'l', 'l', 'o'}.

B) It raises a syntax error because strings cannot initialize sets.

C) It creates a set of unique characters: {'h', 'e', 'l', 'o'}.

D) It sorts the characters alphabetically into a list.
---------------------

3- Which of the following operations creates an empty dictionary rather than an empty set?

A) {}

B) set()

C) dict()

D) Both A and C


--------------------

4 - What does Python return when evaluating the boolean expression bool(0)?

A) True

B) False

C) None

D) 0


--------------------

5-Which built-in function converts an iterable like a string or list into a set?

A) dict()

B) list()

C) set()

D) tuple()
-------------------
6- Which method can be used to remove an item from a set without raising an error if the item is missing?

A) remove()

B) pop()

C) discard()

D) delete()
-------------------
7-Why can a tuple be used as a dictionary key while a list cannot?

A) Tuples are ordered while lists are unordered.

B) Tuples are immutable and hashable, whereas lists are mutable and unhashable.

C) Tuples take up less memory than lists.

D) Dictionaries natively disallow any type containing numbers.

-------------------
8- What is the output or behavior when you define a dictionary with duplicate keys, such as d = {"a": 1, "a": 2}?

A) It raises a duplicate key error.

B) It keeps both entries as a list of values.

C) The second assignment overwrites the first, resulting in {"a": 2}.

D) The first assignment takes precedence, resulting in {"a": 1}.

Answer: C (The second assignment overwrites the first, resulting in {"a": 2})

-----------------------

9- How can you safely access a value in a dictionary without risking a KeyError if the key does not exist?

A) my_dict.find(key)

B) my_dict[key]

C) my_dict.get(key)

D) my_dict.search(key)
----------------------

10- Which of the following operations is valid for a mutable list but invalid for a str or tuple?

A) Slicing a subset of elements

B) Modifying an element in place using its index (e.g., item[0] = new_value)

C) Checking membership using the in keyword

D) Finding the length using the len() function

-----------------------

11- Which statement accurately describes a range object?

A) It stores all its generated numbers simultaneously in memory.

B) It is a mutable sequence that allows item assignment.

C) It is an immutable sequence that generates numbers lazily on demand.

D) It can only count upwards with a step of 1.

-----------------
12- What will happen if you try to add an item to a tuple using my_tuple.append(5)?

A) The item will be added successfully.

B) It will raise an AttributeError because tuples do not have an append method.

C) It will convert the tuple into a list automatically.

D) It will raise a TypeError during syntax checking.

-----------------

13- How do you access the imaginary part of a complex number variable z = 3 + 4j?

A) z.imaginary

B) z[imag]

C) z.imag

D) imag(z)


