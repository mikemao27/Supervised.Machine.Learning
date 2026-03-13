## Gradient Descent
Outline:
* Start with some $w$, $b$. Begin by setting $w$, $b$ = 0.
* Keep chaning $w$, $b$ to reduce J($w$, $b$).
* Until we settle at or near a minimum. May have >1 minimum.

The gradient descent algorithm is as follows:
> $w = w - \alpha \frac{d}{dw} J(w, b)$</br>
> $b = b - \alpha \frac{d}{db} J(w, b)$</br>

Here, $\alpha$ is the learning rate (a small positive number between 0 and 1 that controls how big of a step we take downhill in gradient descent). $\frac{d}{dw} J(w, b)$ is the partial derivative of the cost function. We want to repeatedly apply both formulas for $w$ and $b$ until we reach a local minimum.

Python code for implementing the gradient descent function is also provided for reference so that you can run it yourself.

The value for $\alpha$, the learning rate, is also important and can have a huge impact on the efficiency of our implementation of gradient descent. If $\alpha$ is chosen poorly, gradient descent may not even work at all.
* If $\alpha$ is too small, gradient descent may be too slow.
* If $\alpha$ is too large, we may overshoot and never reach the minimum. Gradient descent may diverge.

Near a local minimum, the magnitude of the derivative becomes smaller and the update steps become smaller.

A derivation of the gradient descent formulas are as follows:</br>
$$\begin{aligned}

\frac{d}{dw} J(w, b) &= \frac{d}{dw} \frac{1}{2m} \sum_{i = 1}^{m}(f_{w, b}(x^{(i)}) - y^{(i)})^2 \\ &= \frac{d}{dw} \frac{1}{2m} \sum_{i = 1}^{m}(wx^{(i)} + b - y^{(i)})^2 \\ &= \frac{1}{2m} \sum_{i = 1}^{m}(wx^{(x)} + b - y^{(i)}) \cdot 2x^{(i)} \\ &= \frac{1}{m} \sum_{i = 1}^{m}(f_{w, b}(x^{(i)} - y^{(i)})) \cdot x^{(i)}

\end{aligned}

\begin{aligned}
\frac{d}{db} J(w, b) &= \frac{d}{db} \frac{1}{2m} \sum_{i = 1}^{m}(f_{w, b}(x^{(i)}) - y^{(i)})^2 \\ &= \frac{d}{db} \frac{1}{2m} \sum_{i = 1}^{m}(wx^{(i)} + b - y^{(i)})^2 \\ &= \frac{1}{2m} \sum_{i = 1}^{m}(wx^{(i)} + b - y^{(i)}) \cdot 2 \\ &= \frac{1}{m} \sum_{i = 1}^{m}(f_{w, b}(x^{(i)}) - y^{(i)})
\end{aligned}$$

As such, the gradient descent algorithm can then be simplied into:</br>
> $w = w - \alpha \frac{1}{m} \sum_{i = 1}^{m}(f_{w, b}(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$</br>
> $b - b - \alpha \frac{1}{m} \sum_{i = 1}^{m}(f_{w, b}(w^{(i)}) - y^{(i)})$</br>

One problem that we may be concerned about is that perhaps the we may only be able to reach a local minimum and not the global minimum. Luckily, it turns out that when we are using a squared error cost function with linear regression, the cost function does not and will never have multiple local minima. Instead, it will only have a single global minimum because of its bowl-shape.