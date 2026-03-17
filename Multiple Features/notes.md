## Multiple Features
* $x_j$: the $j^{th}$ feature.
* $n$: the number of features.
* $\vec{x}^{(i)}$: the features of the $i^{th}$ training example.
* $x_j^{(i)}$: the value of feature $j$ in the $i^{th}$ training example.

Now, we have $f_{\vec{w}, b}(\vec{x}) = w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4 + b$. $\vec{w} = \begin{bmatrix} w_1 & w_2 & w_3 & \cdots & w_n \end{bmatrix}$. Now, we can represent $f_{\vec{w}, b}(\vec{x})$ as $\vec{w} \cdot \vec{x} + b$. What we now have is multiple linear regression (this is not known as multivariate regression).

## Vectorization
Using $f_{\vec{w}, b}(\vec{x}) = \vec{w} \cdot \vec{x} + b$, we can implement this quickly using `f = np.dot(w, x) + b`. The function `dot(w, x)` computes the dot-product of two vectors $w$ and $x$. This is faster than manual computation and a for-loop. 

It might not be obvious that vectorization actually makes an algorithm runs faster (at first glance, it may seem like because both algorithms have O(n) time complexity, then vectorization shouldn't be more efficient), but this is not the case.
* Without Vectorization:
    * ```python
        for j in range(0, 16):
            f = f + w[j] * x[j]
        ```
    This is executed in multiple steps (each with O(1) time complexity) for a grand total of O(n) time complexity.
    * $t_0$: `f + w[0] + x[0]`
    * $t_1$: `f + w[1] + x[1]`
    * ...
    * $t_15$: `f + w[15] + x[15]`
* With Vectorization:
    * `np.dot(w, x)`
    In comparison, this is executed in one single step. All of the computations are computed in parallel using special hardware. Thus, while the time complexity is still O(n), the algorithm is more efficient because all computations are done in parallel.
    
## Gradient Descent with Multiple Linear Regression
Remember that we define the model and model weights as follows:
* $\vec{w} = \begin{bmatrix} w_1 & w_2 & w_3 & \cdots & w_n \end{bmatrix}$.</br>
* $f_{\vec{w}, b}(\vec{x}) = \vec{w} \cdot \vec{x} + b$.</br>

Now, our cost function is: $J(w_1, w_2,..., w_n, b)$. Gradient descent is the same as with univariate regression except $w$ is replaced with $\vec{w}$.