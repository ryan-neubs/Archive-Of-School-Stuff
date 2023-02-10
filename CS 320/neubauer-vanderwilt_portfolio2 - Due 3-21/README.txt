Ryan Neubauer and Jacob Vanderwilt Portfolio Due 3-21
-------------------------------------------------------------------------------
Top Directory:
-graph.py
-graphalgs.py
-topsort.py
-subsets.py

sortalgs Directory:
-insertion_sort.py
-merge_sort.py
-quick_sort.py

examples Directory:
-graph1.txt
-graph2.txt
-graph3.txt
-graph4.txt
-graph5.txt
(graph.txt 1-4 are from handouts, graph5 is a test directed graph for topsort)

binarytree Directory:
-binarytree.py
-BTalgs.py
-binarytree1.txt
-binarytree2.txt
-------------------------------------------------------------------------------

graph.py
-------------------------------------------------------------------------------
Graph class works excellent! Ran all the test graphs to make sure they were put
together in the proper order. Definitely had to back track plenty of times to
get it correct as it ran into issues through following projects. But it works
wonderful now!
-------------------------------------------------------------------------------

graphalgs.py
-------------------------------------------------------------------------------
Contains an implementation of a DFS and brute force K-clique. Admittedly the 
K-clique solution is quite sloppy and does more comparisons in the helper 
function than it needs to. The algorithm produces the correct results but it 
needs some polishing. DFS appears to work but we didn't get enough time to test
it thoroughly to see if it works 100%.
-------------------------------------------------------------------------------

topsort.py
-------------------------------------------------------------------------------
This one took way too many hours to get down. At this point I still feel as
if though I need to build more understanding of the code I wrote. But besides
that, the code works great and produces the correct results for each graph it
was tested with.
-------------------------------------------------------------------------------

subsets.py
-------------------------------------------------------------------------------
subsets.py works excellent. Both approches produce the same results and are
simplified to only a few lines of code for each.
-------------------------------------------------------------------------------

insertionsort.py
-------------------------------------------------------------------------------
insertionsort.py works well. This was the easiest of the sorting methods as it 
the algorithm was very easy to translate into python. We used the test case 
from the book as well as our own to make sure it works. It produces the correct
results. 
-------------------------------------------------------------------------------

nlogn sorts: mergesort.py and quicksort.py
-------------------------------------------------------------------------------
Quicksort and mergesort both were harder to impliment from the algorithm to 
python. Quicksort required lots of extra steps including a helper function. We
also implimented the median sort for l and r in quicksort. Both programs work
correctly and used the test case from the book. 
-------------------------------------------------------------------------------

binarytree.py and BTalgs.py
-------------------------------------------------------------------------------
The homework from 5.3 caught our eye. We wanted to see if we could represent
inorder, preorder, and postorder traversals of a binary tree. It was done by creating
a BinaryTree class partly based off the graph class. In general, the class could
be tweaked to be an overall tree class, but we had limited time. We were able
to use our two test trees (binarytree1.txt and binarytree2.txt) to test the 
traversals in BTalgs.py. Inorder and Preorder both work properly and also work
in a very similar way. We tried postorder in the same way, but it's going to
need a different design to work properly. We didn't have time to fix postorder,
but inorder and preorder work properly.

Note: binarytree.py has a fromfile method similar to graph.py in order to use
the test binary trees (binarytree1.txt and binarytree2.txt)
-------------------------------------------------------------------------------

