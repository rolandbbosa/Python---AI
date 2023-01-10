while True:
  #1. Create a neural network
  class NeuralNetwork:
    def __init__(self):
      self.greetings = {
        "hello": "Hi there!",
        "howdy": "Greetings!",
        "hi": "Good day!",
        "hey": "What's up?",
        "greetings": "Salutations!"
      }

  #2. Train that neural network with 5 different greetings and give each of those greetings reponses using dictionaries
  nn = NeuralNetwork()

  #3. Create a variable input called ipt
  ipt = input("Greeting: ")

  #4. Print the ipt variable 
  print(ipt)

  #5. Point the ipt variable to the neural network to check if the greetings contain the values in the variable ipt
  if ipt in nn.greetings:

  #6. If the greetings contain the values in the variable ipt
  #7. Get the response for the values in ipt from the dictionaries in the neural network and get the response as rsp
    rsp = nn.greetings[ipt]

  #8. Print the rsp
    print(rsp)

  #9. else print Sorry....
  else:
    print("Sorry....")