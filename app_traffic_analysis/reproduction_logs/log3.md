## Issue: token limit reached, the test for 'Min degree failed'

> (10 nodes experiments, model: gpt-4, token limit: 4000)

**Solved by:** changing model to `gpt-4-turbo`
**error record:**

```shell
Remove the label 'type=VM' from all the nodes. Return the networkx graph object.
Total test times:  1
Testing accuracy:  1.0
Current prompt:  What are max degree and min degree in the graph? Return a table with with header 'Max degree', 'Min degree' on the first row.
Find the prompt in the list.
Calling model
Spent a total of 281 tokens
model returned
llm_answer:  "type": "table",
"data": [["Max degree", "Min degree"], [3, 1]]
Fail the test, and here is more info:
ground truth:  [['Max degree', 'Min degree'], [2, 0]]
model output:  [['Max degree', 'Min degree'], [3, 1]]
```
