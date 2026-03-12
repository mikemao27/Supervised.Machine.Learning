## What is Machine Learning?
> "Field of study that gives computers the ability to learn without being explicity programmed." - Arthur Samuel (1959)

The two major types of machine learning algorithms are:
* Supervised learning.<br>
    * Used most in real-world applications. <br>
    * The most rapid advancements.<br>
    * Courses 1 & 2.<br>
* Unsupervised learning.<br>
    * Course 3.
* Recommender systems.<br>
* Reinforcement learning.<br>

## Supervised Learning
Refers to algorithms that learn from `input -> output`. You give your algorithm examples to learn from. The algorithm learns from being given "right answers."

**Examples:**<br>
| Input | Output | Application |
| ----- | ------ | ----------- |
| email | spam? (0, 1) | spam filtering |
| audio | text transcripts | speech recognition |
| English | Spanish | machine translation |
| ad, user info | click? (0, 1) | online advertising |
| image, radar info | position of other cars | self-driving car|
| image of phone | defect? (0, 1) | visual inspection|

Regression (housing price prediction) and Classification (breast cancer detection) are both examples of supervised learning.

## Unsupervised Learning
We want to find something interesting in unlabeled data. Takes data without labels and tries to group them into clusters based on some observed pattern. Data only comes with inputs (x) but not output labels (y). The algorithm has to find structure in the data.

Clustering Algorithms (Google News, DNA microarrays, grouping customers) are examples of unsupervised learning. Anomaly detection (finding unusual data points) and dimensionality reduction (compressing data using fewer numbers) are other examples of unsupervised learning.

## Jupyter Notebooks
The most widely used tool by machine learning and data science practitioners today. It is a default environment that we use to code, experiment, and try things out.

There are two types of cells:
* Markdown Cells: a bunch of text.
* Code Cell: a block where you can write code in.

The file extension for a Jupyter Notebook is `.ipynb`.

**Short-cuts When Using Jupyter Notebook**<br>
`Shift + Enter` runs the code in a given cell.
