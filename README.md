# Logistic Regression using SGD [100 points]#

In this assignment you will be predicting income from census data using logistic regression. Specifically, you will predict the probability that a person earns more than $50k per year.

[https://en.wikipedia.org/wiki/Logistic_regression](https://en.wikipedia.org/wiki/Logistic_regression)

First get the assignment by running:
    
    git clone https://github.com/pjreddie/Logistic-SGD
    cd Logistic-SGD

You will be modifying the file `sgd.py`. Tests for your program are in `test.py`. To test your implementation, run:

    python test.py

You will see the number of tests your implementation passes and any problems that arise.

The data is in `adult.data`, it is from the Adult dataset:

[http://www.cs.toronto.edu/~delve/data/adult/adultDetail.html](http://www.cs.toronto.edu/~delve/data/adult/adultDetail.html)

Note: Please use Python 2.7 for the assignment and only modify the `sgd.py` file. This is the only file you will be submitting.

### Logistic Function [10 points]###

To perform logistic regression you have to be able to calculate the logistic function:

[https://en.wikipedia.org/wiki/Logistic_regression#Definition_of_the_logistic_function](https://en.wikipedia.org/wiki/Logistic_regression#Definition_of_the_logistic_function)

Fill in the `logistic` function.

### Dot Product [5 points]###

The model you are training is just a bunch of numerical weights. To run your model on a data points you will need to take the dot product of your weights and the features for that data point and run the result through your logistic function.

First fill in the `dot` function to take the dot product of two vectors:

[https://en.wikipedia.org/wiki/Dot_product](https://en.wikipedia.org/wiki/Dot_product)

### Prediction [5 points]###

Now that you can calculate the dot product, predicting new data points should be easy! Fill in the `predict` function to run your model on a new data point. Take a look at `test.py` to see what the format for data points is.

Prediction should be straightforward, to predict new points you simply multiply your model's weights by the corresponding features, sum up the result, and pass it through the logistic function. This should be easy with your dot product and logistic functions.


### Accuracy [10 points]###

Once you start training your model you are going to want to know how well you are doing. Modify the `accuracy` function to calculate your accuracy on a dataset given a list of data points and the associated predictions.

### Train Your Model [20 points]###

Fill in the `train` and `update` functions to train your model! You should use logistic regression with L2 regularization where `rate` is the learning rate and `lam` is the regularization parameter.

The training should run for some number of `epochs` performing stochastic gradient descent:

[https://en.wikipedia.org/wiki/Stochastic_gradient_descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent)

This means you will randomly select a point from the dataset and run the model on that data point. Then you will calculate the error for that point and adjust your model weights based on the gradient of that error. An epoch refers to a full pass over the dataset. In practice it is easier (and more statistically valid) to sample randomly with replacement. Thus an epoch just means examining `N` data points where `N` is the number of points in your training data. 

This is different than batch gradient descent where you look at all of the data points before updating. SGD converges faster but can also be less stable because you have a noisy estimate of the gradient instead of the true gradient. In practice it is often much better to use SGD than full batch gradient descent.

When you see a new data point, your prediction will be:

    Prediction = P(income > 50k | W, x) = logistic(W·x)

Your loss function will be:

    Loss = (Prediction - Truth)^2 + Lambda * || W ||

There are two components to the loss:

- the squared error from `(Prediction - Truth)^2`
- the loss from regularization, `Lambda * || W ||`

By minimizing this loss, the model learns to make correct predictions and also use small weights to avoid overfitting.

To adjust the model you have to calculate the gradient of the loss at a given point. The gradient will come from two sources, the error and the regularization.

While this minimizing this loss looks different than maximizing the conditional log likelihood, the gradient is actually the same, just with opposite sign. Thus you can either descend the gradient of this loss function or ascend the gradient of the conditional log likelihood and you will be performing the same updates. If you want, you can derive why this is the case by taking the partial derivative of the above loss function with respect to a single weight in the model. Use the update rule from class to adjust the model, but remember, since we are doing SGD you only look at one point before updating the model:

![update](http://pjreddie.com/media/files/update.png)

When you run `python test.py` it will tell you your current accuracy on the training and validation set. By default these are the same dataset! To get a more accurate evaluation you can modify `data.py` to use different training and validation sets by splitting your data.

### Extract Better Features [20 points]###

Take a look at the feature extracting code in `extract_features`, and at the raw data in `adult.data`. Right now your model is only considering age, education, and one possible marital status.

Good feature extraction is often the key to making good machine learning models. Add more feature extraction rules to help improve your model's performance. This is very open ended, be creative and find features that work well with your model.


### Tune Your Submission [30 points]###

Tune your `submission` function to train your final model. You should change your feature extraction and training code to produce the best model you can. Try different learning rates and regularization parameters, how do they compare? Often it is good to start with a high learning rate and decrease it over time, feel free to add this to your training code.

Your final model will be trained on the full training data and run on test data that you don't have access to. Your grade for this section will be based on your performance relative to an untuned baseline and to the other other students in class. Good luck!

### Submitting ###

Submit your modified `sgd.py` file to the class dropbox here:

[https://catalyst.uw.edu/collectit/assignment/farhadi/37186/150095](https://catalyst.uw.edu/collectit/assignment/farhadi/37186/150095)



