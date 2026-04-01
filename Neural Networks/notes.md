## Neural Networks
We can model a single neuron with a metric called activation. Let us say that we are trying to determing if a given shirt will be a top seller in a store based on its price. If x = price, then we can define the activation, $a = f(x) = \frac{1}{1 + e^{-(wx + b)}}$.

## Tensorflow
For each layer in Tensorflow, we have ```layer = Dense(units=3, activation="sigmoid")```. This means that we have a hidden layer with 3 hidden nodes and has an activation function that is the sigmoid function.