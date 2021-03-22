from blackJack import BlackJack as B

test = B(0)
prompt = "default"
while (prompt != "end"):
    prompt = input()
    pars = prompt.split(' ')
    test.getCards(prompt.split(' '))
    test.debugParams()

#test.debugParams()