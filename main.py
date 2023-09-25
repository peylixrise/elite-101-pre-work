#set up/ initialization
loop = True
#welcoming message function

def weclome():
  print('please enter your name and age below')
  print('')
  age = input('Age: ')
  if age.isdigit() == False:
    weclome()
  name = input('Name: ')
  if name.isalpha() == False:
    name = input('Name: ')
  print('')
  print(f'Hello, {name} whom is {age} I will be your robotic assistant')

#user assistance prompt (placeholder)
def UserAssistanceMenu():
  print('')
#conversation menu (placeholders)
  print('---------------------------------------')
  print('1. what is your purpose')
  print('2. what is the name of the company that made you')
  print('3. how many products do you have')
  print('4. what services do you offer')
  print('5. how much does a service usually cost')
  print('6. can I order products online')
  print('7. exit')
  print('')
  choice = input('please select one of my options of assistance from the menu to begin ')
  if choice.isalpha() == False:
    MenuAnswers(choice)
  else:
    print()
    print('invalid option')
    UserAssistanceMenu()

def MenuAnswers(choice):
  if choice == '1':
    print()
    print('I have been designed to assist you in navigating our ecommerce store on this website')
    print()
    UserAssistanceMenu()
  elif choice == '2':
    print()
    print('My company is name Jaksons Cleaning services')
    print()
    UserAssistanceMenu()

  elif choice == '3':
    print()
    print('We currently have 200 unique cleaning products')
    print()
    UserAssistanceMenu()

  elif choice == '4':
    print()
    print('We offer both home and business cleaning service at a nominal price')
    print()
    UserAssistanceMenu()

  elif choice == '5':
    print()
    print('home cleaning services cost 50$ USD / business cleaning services cost 100$ USD')
    print()
    UserAssistanceMenu()

  elif choice == '6':
    print()
    print('yes it is very simple and straight forward')
    print()
    UserAssistanceMenu()
#exit option (full and to menu)
  elif choice == '7':
    loop = False
    print()
    print('Have good day')
    return loop


weclome()
while(loop):
  loop = UserAssistanceMenu()