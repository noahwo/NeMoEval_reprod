## Few conclusive points in minds:

- Uncertain answers ffrom LLM
  - Different answers from same code but different invocations.
  - Does not follow instructions about output formatting.
  - Sometimes, LLM is crazy and outputs interpretable output (messy output).
  - May get different answers when the question is in a list of questions and a single question itself.
- Answers might be right but not correctly parsed by code (evaluation scripts etc). thus affecting pass/fail results.
- Results might be quite different when switching mosdel, regarding format guidelines, token limits, and so on. You may need to adapt the code to the model.
