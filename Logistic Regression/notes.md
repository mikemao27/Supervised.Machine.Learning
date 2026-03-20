## Logistic Regression
The sigmoid function (also know as the logistic function) is the function $g(z) = \frac{1}{1 + e^{-z}}$. Note, the sigmoid function takes in values between 0 and 1 ($0 < g(z) < 1$), this makes it very helpful for classification problems where we have two categories (as well as it's shape, which fits classification data much better than linear regression).

To get logistic regression, we plug $z = \vec{w} \cdot \vec{x} + b$ in for $z$ in the sigmoid function equation. Now, we get that $f_{\vec{w}, b}(\vec{x}) = \frac{1}{1 + e^{-(\vec{w} \cdot \vec{x} + b)}}$. This can be interpreted as $P(y = 1 | x; \vec{w}, b)$.

## Decision Boundary
$z = \vec{w} \cdot \vec{x} + b = 0$. We can define this to be what we want, typically we have this when $g(z) = f_{\vec{w}, b}(\vec{x}) = 0.5$, but this can be adjusted if we want more certainty.