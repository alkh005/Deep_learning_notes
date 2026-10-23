# AI, machine learning, and deep learning

## The big idea

**Artificial intelligence (AI)** is the broad idea of making computers do tasks that seem intelligent. A computer can play chess using hand-written rules, for example.

**Machine learning (ML)** is one way to build AI: instead of writing every rule, we show a computer examples and let it learn patterns. **Deep learning (DL)** is a kind of machine learning that uses neural networks with many layers.

```text
Artificial intelligence
└── Machine learning: learns patterns from examples
    └── Deep learning: learns with multi-layer neural networks
```

Think of these as nested boxes: deep learning belongs to machine learning, and machine learning belongs to AI.

## Example: sorting email

- A rule-based system might flag every message containing “win a prize.” It follows a rule someone wrote.
- A machine-learning system learns from emails already marked “spam” or “not spam.”
- A deep-learning system can learn richer patterns from the words and their order.

All three are AI solutions. Only the latter two learn from examples, and deep learning is one particular way of doing that.

## How learning from examples works

For supervised learning, each example has an **input** and the right **answer** (called a target). The model makes a guess, measures how far it is from the answer, and adjusts its internal numbers.

```text
example (input + answer) → model makes a guess → measure the mistake
                                                     ↓
                                            adjust model numbers
```

The core notation is:

| Symbol | Plain meaning |
|---|---|
| `x` | The input, such as an email or photo |
| `y` | The correct answer, such as “spam” |
| `ŷ` (“y-hat”) | The model’s guess |
| `θ` (“theta”) | All the model’s learned numbers, such as weights and biases |
| `loss` | A number describing how wrong the guess was |

Training tries to make the average loss smaller across many examples:

$$\text{average loss} = \frac{\text{sum of the examples' losses}}{\text{number of examples}}$$

You may see this written as $\hat\theta = \arg\min_\theta \frac{1}{N}\sum_i \ell(f_\theta(x_i),y_i)$. Read `arg min` as “choose the settings that make the average loss smallest.” The equation says the same thing as the diagram: adjust the model to make its mistakes smaller.

## Remember

> AI is the broad field. ML learns from data. DL is ML that uses multi-layer neural networks. A good model should learn patterns that work on new examples, not just memorize the examples it saw.
