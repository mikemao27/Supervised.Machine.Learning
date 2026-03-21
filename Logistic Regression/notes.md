## Logistic Regression
The sigmoid function (also know as the logistic function) is the function $g(z) = \frac{1}{1 + e^{-z}}$. Note, the sigmoid function takes in values between 0 and 1 ($0 < g(z) < 1$), this makes it very helpful for classification problems where we have two categories (as well as it's shape, which fits classification data much better than linear regression).

To get logistic regression, we plug $z = \vec{w} \cdot \vec{x} + b$ in for $z$ in the sigmoid function equation. Now, we get that $f_{\vec{w}, b}(\vec{x}) = \frac{1}{1 + e^{-(\vec{w} \cdot \vec{x} + b)}}$. This can be interpreted as $P(y = 1 | x; \vec{w}, b)$.

## Decision Boundary
$z = \vec{w} \cdot \vec{x} + b = 0$. We can define this to be what we want, typically we have this when $g(z) = f_{\vec{w}, b}(\vec{x}) = 0.5$, but this can be adjusted if we want more certainty.

## Logistic Loss Function
The typical cost function is not particularly good for logistic regression. Thus, we need to define a new cost function. The loss function for logistic regression is defined as $L(f_{\vec{w}, b}(\vec{x}^{(i)}, y^{(i)})) = \begin{cases} -log(f_{\vec{w}, b}(\vec{x}^{(i)})) & \text{if } y^{(i)} = 1 \\ -log(1 - f_{\vec{w}, b}(\vec{x}^{(i)})) & \text{if } y^{(i)} = 0\end{cases}$. Thus, the cost function for logistic regression then becomes $J(\vec{w}, b) = \frac{1}{m} \sum_{i = 1}^{m} L(f_{\vec{w}, b}(x^{(i)}), y^{(i)})$. It should be noted that the cost function will always be convex. Thus, gradient descent will always lead us to a global minimum. 

If simplified, the loss function becomes $-y^{(i)}log(f_{\vec{w}, b}(\vec{x}^{(i)})) - (1 - y^{(i)})log(1 - f_{\vec{w}, b}(\vec{x}^{(i)}))$.