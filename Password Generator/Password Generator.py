#Made by Awnsh
#Password generator that saves the generated password to a platform of the user's choice. The user is able to see the password they saved
#Users are able to add new passwords, change existing passwords, see past password, and delete passwords
"""
     @@@@@@                               @@@@@@  
    @@@@@@@@@                          @@@@@@@@@  
    @@@@@@@@@@@         @@@@#        @@@@@@@@@@@  
    @@@@@@@@@@@@@     @@@@@@@@      @@@@@@ @@@@@  
    @@@@@@  @@@@@@   @@@@@@@@@@@  @@@@@@@  @@@@@  
    @@@@@@   @@@@@@@@@@@@@ @@@@@@@@@@@@    @@@@@  
    @@@@@@     @@@@@@@@@    @@@@@@/@@@     @@@@@  
    @@@@@@      @@@@@@@       @@@@@@       @@@@@  
     @@@@@@  @@@@@@@@          *@@@@@@@@@@@@@@@@  
      @@@@@@@@@@@@@              @@@@@@@@@@@@@@   
         @@@@@@                      @@@@@@@      
         
"""
def generator():

  import random
  import pandas as pd

  #the characters used to make a new password
  ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  digits = '0123456789'
  punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

  global ds
  ds = pd.read_csv(r'passwords.csv')
  pd.set_option("display.max_columns", None)
  ds.set_index('Platforms', inplace = True)
  ds.astype(str)
  ds['Password'] = ds['Password'].astype('object')
  #print(ds)
  #print(ds.dtypes)

  newOrEnterreg = input('Do you want to want to enter a new password, see a past password, edit a password, delete a password, or see all passwords (new/past/edit/delete/all): ')
  print()
  newOrEnter = newOrEnterreg.lower()

  if newOrEnter == "new": 
    
    length_reg = input('Input the length you want your password (min 8 digits): '   )
    print()
    length = int(length_reg.lower())

    #makes the user input more than 8 digits                                    
    if length < 8:
      try:
        print("Input a password more than 8 digits")
        print()
        quit()
      except:
        print("An error has occurred")
        print("please try again")
    
    
    #asks the user the platform    
    platformReg = input("What website or plaform are you using this password for? (Name): ")
    print()
    global platform
    platform = str(platformReg.lower())

    #function to generate a random password
    def passwordfunction(length):
      conformation = input('To confirm, you want a ' + str(length) + ' digit password for ' + str(platform) + '? (y/n): ')
      
      if conformation.lower() == "y":
        allchars = ascii_letters + punctuation + digits
        global password
        password = ''.join(random.choice(allchars) for i in range(length))
        print()
        print("password: " + password)
        print("Password saved!")
        
      elif conformation.lower() == 'n':
        print()
        generator()
        
      else:
        print('An error occurred.')
        quit()
        exit()

      #function to put values into the csv
      def putInSheet():
        global data
        data = {
        'Platform': [platform],
        'Password': [password]
        }
        
        global df
        df = pd.DataFrame(data)
        pd.set_option("display.max_columns", None)
        df.to_csv('passwords.csv', mode='a', index=False, header=False)

      
      putInSheet()
    passwordfunction(length)

  elif (newOrEnter == "past"):
    try:
      #allows the loop to run 
      platform = None
      password = None
      nameOfPlatformreg = input("What platform do you want to see the password for?: ")
      print()
      
      nameOfPlatform = nameOfPlatformreg.lower()
  
      print('Your password for ' + nameOfPlatform +  ' is ' + ds.loc[str(nameOfPlatform)].to_string())
      
    except:
      print("You do not have a password saved for " + nameOfPlatform)

  elif newOrEnter == "edit":
    try:
      platform = None
      password = None
      editNamePlatformreg = input('What platform do you want to edit your password for?: ')
      editNamePlatform = editNamePlatformreg.lower()
  
      print('Your current password for ' + editNamePlatform +  ' is ' + ds.loc[str(editNamePlatform)].to_string())
      print()
  
      def changePass():
        randomOrCustom = input('Do you want a random new password or a custom password (random/custom)')
        if randomOrCustom.lower() == 'custom':
          
          changePassword = input('What do you want to change your password to: ')
          print()
          changePasswordConformation = input('You want to change your password to ' + changePassword + ' correct? (y/n): ')

          
          if changePasswordConformation == 'y':
            oldPassword = ds.loc[(str(editNamePlatform), 'Password')]
            ds.loc[(editNamePlatform, 'Password')] = changePassword
            ds.to_csv('passwords.csv', index=True, header=True)
            print('Password Updated!')
  
    
          elif changePasswordConformation == 'n':
            changePass()
    
          else:
            print('An error occured')
          
        elif randomOrCustom.lower() == 'random':
          
          length_reg = input('Input the length you want your password (min 8 digits): '   )
          print()
          length = int(length_reg.lower())
          
          if length < 8:
            try:
              print("Input a password more than 8 digits")
              print()
              quit()
            except:
              print("An error has occurred")
              print("please try again")
            
          conformation = input('To confirm, you want a ' + str(length) + ' digit password for ' + str(editNamePlatform) + '? (y/n): ')


          #does the same thing as the generate password function
          if conformation.lower() == "y":
            allchars = ascii_letters + punctuation + digits
            global password
            password = ''.join(random.choice(allchars) for i in range(length))
            print()
            print("password: " + password)
            print("Password saved!")
            
          elif conformation.lower() == 'n':
            print()
            generator()
            
          else:
            print('An error occurred.')
            quit()
            exit()
          oldPassword = ds.loc[(str(editNamePlatform), 'Password')]
          ds.loc[(editNamePlatform, 'Password')] = password
          ds.to_csv('passwords.csv', index=True, header=True)
          
          
    except:
      print("You do not have a password saved for " + editNamePlatform)

    changePass()

    
  elif newOrEnter == 'delete':
    try:
      delPlatformreg = input('What platform do you want to delete?: ')
      delPlatform = delPlatformreg.lower()
      
      print('Your current password for ' + delPlatform +  ' is ' + ds.loc[str(delPlatform)].to_string())
      print()
  
      delConformreg = input('Are you sure you want to delete the password for '+ delPlatform +'? (y/n): ')
      delConform = delConformreg.lower()

      #deletes the value in the csv
      if delConform == 'y':
        ds.drop(str(delPlatform) , axis = 'index', inplace = True)
        print(ds)
        ds.to_csv('passwords.csv', index=True, header=True)

        print('Password deleted')
  
      elif delConform == 'n':
        quit()
  
      else:
        print('There was an error')
        quit()
        
    except:
      print("You do not have a password saved for " + delPlatform)

  #lets the user see all of their passwords
  elif newOrEnter == 'all':
    #prints the dataframe
    print(ds)

  
  else:
    print("An error has occurred")
    quit()

    #makes the password a global variable
    globals()[platform] = password

generator()