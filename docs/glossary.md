# Glossary

Short, plain-language definitions for the words used in these notes. Follow the links to see each idea in context.

| Term | Simple meaning |
|---|---|
| [Activation function](foundations/02-neurons-layers-activations.md) | A rule that changes a neuron's output, helping a network learn varied patterns. |
| AI | The broad field of making computers do tasks that seem intelligent. |
| [Backpropagation](foundations/03-mlp-forward-backprop.md) | The backward step that traces how each learned number affected the loss. |
| Batch / minibatch | A group of examples processed together in one training step. |
| [Bias](foundations/02-neurons-layers-activations.md) | A learned adjustment added to a neuron's weighted input. |
| [Cross-entropy](foundations/04-optimization-losses.md) | A classification loss that is smaller when the model gives the right answer a high probability. |
| Epoch | One pass through all the training examples. |
| [Generalization](foundations/05-generalization-evaluation.md) | How well a model works on relevant examples it did not train on. |
| [Gradient](foundations/03-mlp-forward-backprop.md) | A measure of how the loss would change if a learned number changed. |
| [Hidden layer](foundations/02-neurons-layers-activations.md) | A layer inside the model, between the input and final answer. |
| [Learning rate](foundations/04-optimization-losses.md) | The size of a parameter update during learning. |
| [Loss](foundations/04-optimization-losses.md) | A score for how wrong a model's prediction is. |
| Logit | A model's raw score before it is turned into a probability. |
| MLP | A common feedforward neural network built from connected layers. |
| [Neuron](foundations/02-neurons-layers-activations.md) | A small calculation that combines inputs and produces an output. |
| [Optimizer](foundations/04-optimization-losses.md) | A method for updating the model using gradients. |
| [Overfitting](foundations/05-generalization-evaluation.md) | Learning details of the training examples that do not help on new examples. |
| Parameter | A learned number in a model, such as a weight or bias. |
| [Regularization](foundations/05-generalization-evaluation.md) | Techniques that help discourage overfitting. |
| [Tensor](foundations/02-neurons-layers-activations.md) | A container of numbers arranged in one or more dimensions, such as a batch of feature rows. |
| [Underfitting](foundations/05-generalization-evaluation.md) | Failing to learn the useful pattern, even from training examples. |
| [Validation set](foundations/05-generalization-evaluation.md) | Examples used to compare choices during model development. |
| [Weight](foundations/02-neurons-layers-activations.md) | A learned number that controls how strongly an input counts. |
| [Weight decay](foundations/05-generalization-evaluation.md) | A training technique that discourages very large weights. |

## Where to start

- [AI, machine learning, and deep learning](foundations/01-ai-ml-deep-learning.md)
- [Neurons, layers, and activation functions](foundations/02-neurons-layers-activations.md)
- [MLPs, forward propagation, and backpropagation](foundations/03-mlp-forward-backprop.md)
- [Optimization and loss functions](foundations/04-optimization-losses.md)
- [Generalization and evaluation](foundations/05-generalization-evaluation.md)
