# coding: utf-8

import numpy as np


class NeuralNetworks(object):
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # statistical weigts
        self.weights_input_to_hidden = np.random.normal(0.0, self.hidden_nodes ** -0.5,
                                                        (self.hidden_nodes, self.input_nodes))

        self.weights_hidden_to_output = np.random.normal(0.0, self.output_nodes ** -0.5,
                                                         (self.output_nodes, self.hidden_nodes))
        self.lr = learning_rate

        # activation is given by the sigmoid function
        self.activation_function = lambda x: (1 / (1 + np.exp(-x)))
        self.activation_function_prime = lambda x: (x * (1 - x))

        self.output_activation_function = lambda x: (x)
        self.output_activation_function_prime = lambda x: (1)

    def train(self, inputs, targets_list):
        inputs = np.array(inputs, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        # hidden layers
        hidden_inputs = np.dot(self.weights_input_to_hidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.weights_hidden_to_output, hidden_outputs)
        final_outputs = self.output_activation_function(final_inputs)

        # the cute error function
        error = targets - final_outputs

        output_errors = error * self.output_activation_function_prime(final_inputs)

        # propagated error
        hidden_errors = np.dot(output_errors.T, self.weights_hidden_to_output).T
        hidden_grad = self.activation_function_prime(hidden_outputs)

        self.weights_hidden_to_output += self.lr * np.dot(output_errors, hidden_outputs.T)
        self.weights_input_to_hidden += self.lr * np.dot((hidden_errors * hidden_grad), inputs.T)

    def run(self, inputs):
        inputs = np.array(inputs, ndmin=2).T

        hidden_inputs = np.dot(self.weights_input_to_hidden, inputs)
        hidden_outputs = self.activation_function(hidden_inputs, inputs)

        final_inputs = np.dot(self.weights_hidden_to_output, hidden_outputs)
        final_outputs = self.output_activation_function(final_inputs, hidden_outputs)

        return final_outputs

    @staticmethod
    def classificate(emotions):
        # TODO: finish it
        return 0.8


def MSE(y, Y):
    return np.mean((y - Y) ** 2)
