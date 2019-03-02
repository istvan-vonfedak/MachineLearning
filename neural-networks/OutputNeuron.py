import random
from math import e

# This class describes a single output neuron
# it constains the value of the output neuron and the set of weights
# that come from the hidden neurons
class OutputNeuron:
  def __init__(self, hiddenSize):
    # the output signals that are going to classify the attribute
    self.value = None
    self.hiddenSize = hiddenSize
    # the weights that the hidden neurons have towards
    # this output neuron
    self.weights = []
    # initialize the weights
    i = 0
    while i < hiddenSize:
      self.weights.append(random.uniform(-0.1, 0.1))
      i += 1

  # gets the inputs for the output neuron
  # it takes uses the array of hidden neurons and returns the input
  # value for the output neuron
  # TODO test to see if it works
  def getOutputLayerInput(self, hiddenNeurons):
    # makes sure that the hidden neuron array is the same size as
    # output weights
    if len(hiddenNeurons) != self.hiddenSize:
      print('Error:: getOutputLayerInput::', end='')
      print('len(hiddenInpit != self.hiddenSize')
      exit()
    i = 0
    value = 0
    while i < self.hiddenSize:
      # multiplies the weight of that hidden neuron by the output value 
      # of that hidden neuron and adds it to the value accumulator
      value += hiddenNeurons[i].value * self.weights[i]
      i += 1
    # returns the total input value for that neuron
    return value

  # Given an array of hidden Neurons it updates the value of the
  # output neuron
  # TODO test to see if it works
  def storeOutputLayerOutput(self, hiddenNeurons):
    # makes sure that the hidden neuron array is the same size as
    # output weights
    if len(hiddenNeurons) != self.hiddenSize:
      print('Error:: storeOutputLayerOutput::', end='')
      print('len(hiddenInpit != self.hiddenSize')
      exit()
    # gets the input value to the given neuron
    inputVal = self.getOutputLayerInput(hiddenNeurons)
    # calculates and updates the output value of the hidden neuron
    self.value = 1.0 / (1 + e**(-1*inputVal))

  # print the Output neuron
  def print(self):
    if(self.value is None):
      print('  Output neuron value = None')
      return
    #print out the values
    print('  Output neuron value = ', '%.2f' % self.value)
    i = 0
    # print out the weights
    print('       Weights', end=' ')
    i = 0
    while i < self.hiddenSize:
      print('%.2f' % self.weights[i], end=' ')
      i += 1
    print()