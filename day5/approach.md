## Approachg

#### Initial Thoughts
This problem seems very much like a graph problem. We need to create a connected graph between each document that needs to be updated. For the first part, once we have our graph set up, we simply need to make sure that all of the "pre-requisites" of a document are fulfilled prior to the document being updated. In the sense of a graph, this is enterpreted as going through the update list in reverse order and making sure that we do not have any updates that are occurring later than our current point as pre-requisites.

#### Correcting a List
When reversing a list, we will again go through the list, but this time, if we encounter an entry that is in the incorrect order, we will ammend this by identifying the offending prerequisite, and taking the incorrect doc (the current doc) and inserting it after the offending pre-requisite. We will then change our list index back to the newly inserted doc and continue with our process of evaluating the list. This change of index is important, because there is a possibility that a change of order affects further pre-requisites that we had previously assessed.


