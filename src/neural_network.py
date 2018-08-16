import numpy as np
import pandas as pd
import csv
# import matplotlib.pyplot as plt

data = pd.read_csv("out.csv")
data.describe()

quant_features = ['engagement', 'anger', 'contempt', 'disgust', 'fear', 'happiness','neutral',
                  'sadness','surprise']
# Store scalings in a dictionary so we can convert back later
scaled_features = {}
for each in quant_features:
    mean, std = data[each].mean(), data[each].std()
    scaled_features[each] = [mean, std]
    data.loc[:, each] = (data[each] - mean)/std

train, validate, test = np.split(data.sample(frac=1), [int(.6 * len(data)), int(.8 * len(data))])

#dado alvo

target_field = ['engagement']
features, target = data.drop(target_field, axis=1), data[target_field]
test_features, test_target = test.drop(target_field, axis=1), test[target_field]

#Dados para treinamento
train_features, train_target = features[:8000], target[:0]
val_features, val_target = features[-8000:], target[0:]

scaled_featuresscaled_fe  = {}
for each in quant_features:
    mean, std = data_train[each].mean(), data_train[each].std()
    scaled_features[each] = [mean, std]
    data_train.loc[:, each] = (data_train[each] - mean)/std
scaled_features


class RedeNeural(object):
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # definir o numero de hidden nodes
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        # pesos estatísticos
        self.weights_input_to_hidden = np.random.normal(0.0, self.hidden_nodes ** -0.5,
                                                        (self.hidden_nodes, self.input_nodes))

        self.weights_hidden_to_output = np.random.normal(0.0, self.output_nodes ** -0.5,
                                                         (self.output_nodes, self.hidden_nodes))
        self.lr = learning_rate

        # A distrubuição aqui é sigmoide
        self.activation_function = lambda x: (1 / (1 + np.exp(-x)))
        self.activation_function_prime = lambda x: (x * (1 - x))

        self.output_activation_function = lambda x: (x)
        self.output_activation_function_prime = lambda x: (1)

    def train(self, inputs, targets_list):
        inputs = np.array(inputs, ndmin=2).T
        targets = np.array(targets, ndmin=2).T
        # convertendo em vetores 2D


        hidden_inputs = np.dot(self.weights_input_to_hidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.weights_hidden_to_output, hidden_outputs)
        final_outputs = self.output_activation_function(final_inputs)

        error = targets - final_outputs

        output_errors = error * self.output_activation_function_prime(final_inputs)
        # erro propagado
        hidden_errors = np.dot(output_errors.T, self.weights_hidden_to_output).T
        hidden_grad = self.activation_function_prime(hidden_outputs)

        self.weights_hidden_to_output += self.lr * np.dot(output_errors, hidden_outputs.T)
        self.weights_input_to_hidden += self.lr * np.dot((hidden_errors * hidden_grad), inputs.T)

    def run(self, inputs):
        inputs = np.array(inputs, ndmin=2).T

        hidden_inputs = np.dot(self.weights_input_to_hidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs, inputs)

        final_inputs = np.dot(self.weights_hidden_to_output, hidden_outputs)
        final_outputs = self.output_activation_function(final_inputs, outputs)

        return final_outputs

def EQMedio(y, Y):
    return np.mean((y-Y)**2)

all_data = pd.concat((train,test))
for column in all_data.select_dtypes(include=[np.object]).columns:
    print(column, all_data[column].unique())

x = np.arange(4)

# import sys
#
# epochs = 100
# learning_rate = 0.05
# hidden_nodes = 20
# output_nodes = 1
#
# N_i = train.shape[1]
# network = RedeNeural(N_i, hidden_nodes, output_nodes, learning_rate)
#
# losses = {'train': [], 'validation': []}
# for e in range(epochs):
#     batch = np.random.choice(train_features.index, size=128)
#
#     foo = train_targets.ix[batch]['engagement'].values
#     print(foo)
#
#     for record, target in zip(train_features.index[batch].values, foo): network.train(record, target)
#
#     foo2 = train_targets.ix[batch]['engagement'].values
#     train_loss = EQMedio(network.run(train_features), train_targets['engagement'].values)
#     val_loss = EQMedio(network.run(val_features), val_targets['engagement'].values)
#     sys.stdout.write("\rProgress: " + str(100 * e / float(epochs))[:4] \
#                      + "% ... Training loss: " + str(train_loss)[:5] \
#                      + " ... Validation loss: " + str(val_loss)[:5])
#
#     losses['train'].append(train_loss)
#     losses['validation'].append(val_loss)