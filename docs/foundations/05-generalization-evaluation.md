# Generalization and evaluation

## The big idea

A model is useful when it works on examples it has not seen before. This ability is called **generalization**. A model that remembers its practice examples but struggles with new ones has **overfit**.

```text
training examples → learn model → new examples → check if learning transfers
```

Think of studying for an exam: memorizing the practice questions may earn a good practice score, but understanding the ideas helps with new questions too.

## Three data splits, three jobs

| Data | Job | Simple analogy |
|---|---|---|
| **Training set** | Teach the model; its weights are learned from these examples | Practice questions |
| **Validation set** | Compare choices and decide when to stop | A practice exam used to guide study |
| **Test set** | Give a final check after choices are made | The final exam, kept unseen until the end |

If you repeatedly use the test set to make choices, it stops being a fair final check. Keep examples that are closely related together when splitting—for example, photos from the same person, or measurements from the same patient. For time-based data, train on earlier times and evaluate on later times. Otherwise, information can leak between the sets.

## Underfitting and overfitting

| Pattern | Training results | New-data results | What it can suggest |
|---|---|---|---|
| **Underfitting** | Poor | Poor | The model has not captured the useful pattern |
| **Good fit** | Good | Good | The learned pattern carries over |
| **Overfitting** | Very good | Poorer | The model may have learned practice-specific details |

This table is a starting point, not a diagnosis by itself. Poor data or a mismatch between training and real use can also cause problems.

## Ways to help a model generalize

- **Weight decay:** discourage very large weights.
- **Dropout:** randomly switch off some signals while training, to reduce reliance on any one path.
- **Data augmentation:** make valid variations of training examples, such as slightly cropping a photo when the crop still shows the same object.
- **Early stopping:** keep the version that performs best on validation data.
- **More representative examples or a simpler model:** sometimes solve the problem more directly.

These tools can help, but applying them too strongly—or changing an example so its correct answer changes—can hurt.

## Pick a useful metric

For yes/no predictions, **accuracy** is the fraction of all answers that are correct. **Precision** asks, “Of the things flagged as positive, how many really were?” **Recall** asks, “Of all real positive cases, how many did we find?”

Imagine checking for a rare illness that affects 1 person in 1,000. A model that says “no illness” every time is 99.9% accurate, but finds none of the sick people: its recall is zero. Accuracy alone hides that failure.

| Term | Counts |
|---|---|
| True positive (TP) | Correctly flagged positive |
| False positive (FP) | Incorrectly flagged positive |
| False negative (FN) | Missed positive |
| True negative (TN) | Correctly identified negative |

$$\text{accuracy} = \frac{TP+TN}{TP+FP+FN+TN} \qquad \text{precision} = \frac{TP}{TP+FP} \qquad \text{recall} = \frac{TP}{TP+FN}$$

For number predictions, common measures include mean absolute error (average size of the error) and root mean squared error (which gives large errors extra weight). Choose a measure that reflects what matters for the task.

## Remember

> Training data teaches; validation data guides choices; test data gives the final check. Generalization means doing well on new, relevant examples. Pick evaluation metrics that reveal the mistakes you care about, and keep related or future data from leaking into training.
