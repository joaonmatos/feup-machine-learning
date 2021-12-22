from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning


from sklearn.metrics import accuracy_score
from matplotlib import pyplot

def watch_random_forest_overfit(x_train, x_test, y_train, y_test):
    train_scores = []
    test_scores = []

    estimators = []
    # scores = []
    classifiers = []
    technique = []

    for estimator in range(1, 50):
        rf = RandomForestClassifier(n_estimators= estimator, random_state = 19)
        rf.fit(x_train, y_train)

        # Evaluate train
        train_yhat = rf.predict(x_train)
        train_acc = accuracy_score(y_train, train_yhat)
        train_scores.append(train_acc)

        # Evaluate test
        test_yhat = rf.predict(x_test)
        test_acc = accuracy_score(y_test, test_yhat)
        test_scores.append(test_acc)

        estimators.append(estimator)
        # scores.append(rf.score(x_test, y_test))
        classifiers.append(rf)
        technique.append("random forest")

    pyplot.plot(estimators, train_scores, '-o', label='Train')
    pyplot.plot(estimators, test_scores, '-o', label='Test')
    pyplot.legend()
    pyplot.show()


def watch_kneighbors_overfit(x_train, x_test, y_train, y_test):
    neighbors = []
    classifiers = []

    train_scores = []
    test_scores = []

    for neighbor in range(1,60):
        kn = KNeighborsClassifier(n_neighbors=neighbor)
        kn.fit(x_train, y_train)

        # Evaluate train
        train_yhat = kn.predict(x_train)
        train_acc = accuracy_score(y_train, train_yhat)
        train_scores.append(train_acc)

        # Evaluate test
        test_yhat = kn.predict(x_test)
        test_acc = accuracy_score(y_test, test_yhat)
        test_scores.append(test_acc)

        neighbors.append(neighbor)
        classifiers.append(kn)
    
    pyplot.plot(neighbors, train_scores, '-o', label='Train')
    pyplot.plot(neighbors, test_scores, '-o', label='Test')
    pyplot.legend()
    pyplot.show()


def watch_overfit_mlp(x_train, x_test, y_train, y_test): 
    # !!! No more convergence warnings
    simplefilter("ignore", category=ConvergenceWarning)

    shapes = []
    activations = []
    learn_rates = []
    # scores = []
    classifiers = []
    technique = []

    for activation in ["logistic", "tanh", "relu"]:
        print(f"Activation = {activation}")

        for learn_rate in ["constant", "invscaling", "adaptive"]:
            print(f"Learn Rate = {learn_rate}")

            for n_layers in range(1, 6):
                print(f"# Layers = {n_layers}")

                train_scores = []
                test_scores = []
                layer_sizes = []

                for layer_size in range(4, 20):
                    shape = tuple(layer_size for _ in range(n_layers))
                    shapes.append(shape)
                    activations.append(activation)
                    learn_rates.append(learn_rate)
                    layer_sizes.append(layer_size)

                    nn = MLPClassifier(hidden_layer_sizes=shape, activation=activation, learning_rate=learn_rate, random_state=19)
                    nn.fit(x_train, y_train)

                    # Evaluate train
                    train_yhat = nn.predict(x_train)
                    train_acc = accuracy_score(y_train, train_yhat)
                    train_scores.append(train_acc)

                    # Evaluate test
                    test_yhat = nn.predict(x_test)
                    test_acc = accuracy_score(y_test, test_yhat)
                    test_scores.append(test_acc)

                    classifiers.append(nn)
                    technique.append("Multi Layer Perceptron")
                    # scores.append(nn.score(x_test, y_test))

                pyplot.plot(layer_sizes, train_scores, '-o', label='Train')
                pyplot.plot(layer_sizes, test_scores, '-o', label='Test')
                pyplot.legend()
                pyplot.show()