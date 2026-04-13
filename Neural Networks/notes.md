## Neural Networks
We can model a single neuron with a metric called activation. Let us say that we are trying to determing if a given shirt will be a top seller in a store based on its price. If x = price, then we can define the activation, $a = f(x) = \frac{1}{1 + e^{-(wx + b)}}$.

## Tensorflow
For each layer in Tensorflow, we have ```layer = Dense(units=3, activation="sigmoid")```. This means that we have a hidden layer with 3 hidden nodes and has an activation function that is the sigmoid function.

# How to Build a Neural Network
First, create both layers:
* ```layer_1 = Dense(units=3, activation="sigmoid")```
* ```layer_2 = Dense(units=1, activation="sigmoid")```

Instead of manually passing the data into layer 1 and layer 2, we can tell Tensorflow to string together the two layers. This is what ```model = Sequential([layer_1, layer_2])``` means. Precisely, this tells Tensorflow that you want to create a neurla network that takes in some data and, since layer_1 and layer_2 are strung together, the data goes into the model, layer_1 outputs some information, and that information is then passed into layer_2, which outputs our final result.

Additionally, ```model.comple(...)``` and ```model.fit(x, y)``` precisely tell the Tensorflow to train the model on the training data x and y, where x is the input and y is the correct output.

Lastly, if we have some new input data ```x_new``` and want the model's prediction for it, we can just run ```model.predict(x_new)```. It should be noted that by convention, we don't typically assign the two layers to variables as we have done above. Instead, we typically run the following:

```model = Sequential([Dense(units=3, activation="sigmoid"), Dense(units=1, activation="sigmoid")])```.

The same process would apply if we have more layers. We'd just insert more layer definitions within ```Sequential```.

## Other Activation Functions
Before, we had always used the sigmoid function $f(x) = \frac{1}{1 + e^{-x}}$. Another common activation function is the piecewise function $g(z) = max(0, z)$ (0 on the left and g(z) = z on the right). This is the ReLU function (which stands for "rectified linear unit").

The most commonly used activation functions are:
* The linear activation function: $f(x) = w \cdot x + b$.
* The sigmoid activation function: $f(x) = \frac{1}{1 + e^{-x}}$.
* The ReLU activation function: $f(x) = max(0, x)$.

## Choosing Activation Functions
Depending on the type of target label, y, there will be some fairly natural activation functions we should choose for the output layer.

* If you are performing binary classification, the sigmoid activation function will almost always be the best choice.
* If you are performing regression where $y$ can be positive or negative, use a linear activation function.
* If you are performing regression where $y$ can only take on non-negative values, then use the ReLU activation function.

For the hidden layers, the ReLU activation function is by far the most common choice for each of the hidden layers. The machine learning field used to use the sigmoid activation function a while ago, but has now transitioned to use the ReLU activation function much more often.
* The ReLU activation function is easier to compute since you only need to take the $max()$ of two values.
* The ReLU activation function only flattens out on the left, unlike the sigmoid activation function which flattens out on both sides. If you are using gradient descent, if you have a function that flattens out in muliple places, then it takes longer to perform gradient descent.