## Issue: the "data" in output is a text instead of the updated graph JSON, nor in a dictionary. This repeated almost every time.
> Also the test for 'Min degree failed'
> (10 nodes experiments, model: gpt-4-turbo-preview)

**Fixed** by modifying the prompt part: "If the output type is 'graph' then the 'data' key should contain the updated graph JSON. If there is no update, return the original graph JSON."

**Error record:**

```shell
=========Current query process is done!=========
Remove the label 'type=VM' from all the nodes. Return the networkx graph object.
Total test times:  1
Testing accuracy:  1.0
Current prompt:  What are max degree and min degree in the graph? Return a table with with header 'Max degree', 'Min degree' on the first row.
Find the prompt in the list.
Calling model
Spent a total of 289 tokens
model returned
llm_answer:  "type": "table",
"data": [
    ["Max degree", "Min degree"],
    [2, 1]
]
Fail the test, and here is more info:
ground truth:  [['Max degree', 'Min degree'], [2, 0]]
model output:  [['Max degree', 'Min degree'], [2, 1]]
=========Current query process is done!=========
What are max degree and min degree in the graph? Return a table with with header 'Max degree', 'Min degree' on the first row.
Total test times:  1
Testing accuracy:  0.0
Current prompt:  Color all of the nodes with label 'app:prod' purple. Return the networkx graph object.
Find the prompt in the list.
Calling model
Spent a total of 315 tokens
model returned
llm_answer:  "type": "graph",
"data": "The original graph data does not contain any nodes with the label 'app:prod', therefore no changes were made to the node colors."

Traceback (most recent call last):
  File "/Users/hann/Projects/NeMoEval/app_traffic_analysis/baseline/test_with_golden.py", line 294, in <module>
    main()
  File "/Users/hann/Projects/NeMoEval/app_traffic_analysis/baseline/test_with_golden.py", line 290, in main
    userQuery(prompt_list, graph_json)
  File "/Users/hann/Projects/NeMoEval/app_traffic_analysis/baseline/test_with_golden.py", line 132, in userQuery
    ret_graph_copy = json_graph.node_link_graph(ret["data"])
  File "/Users/hann/anaconda3/envs/nemoeval/lib/python3.10/site-packages/networkx/readwrite/json_graph/node_link.py", line 302, in node_link_graph
    multigraph = data.get("multigraph", multigraph)
AttributeError: 'str' object has no attribute 'get'
```
