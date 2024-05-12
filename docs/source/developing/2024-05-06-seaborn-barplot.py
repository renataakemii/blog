"""
Seaborn Barplots with Matplotlib
================================

**Data**: 06/05/2024 | **Tags**: Seaborn, Matplotlib, Python

**...**

Let me be honest with you: I don't hate Matplotlib! Quite the opposite, I love it very much.
But I think it falls short when it comes to a beautiful design, and that's when Seaborn comes
in. `Seaborn <https://seaborn.pydata.org/>`_ is a data visualization library, with an interface 
with Matplotlib, which allows the users to plot data from Pandas DataFrames (if you are curious
about it, I strongly encourage you to 
`read its paper <https://joss.theoj.org/papers/10.21105/joss.03021>`_).

In this post, I'll plot some bars with data, and we can talk about the *design* decisions I've
made. If you wish to collaborate with me, giving me suggestions, just open up an issue in our
GitHub page.

A bit of context
----------------


Let's code!
-----------

"""

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%
