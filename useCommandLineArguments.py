def useCLIarguments(dictOfArgumentsGiven: dict, dictOfOptionsGiven: dict, caseInsensitive: bool):
    import sys
    import os
    # get the name of the script
    pythonFileName = os.path.basename(__file__)
    # If no arguments are specified
    if sys.argv == None:
        print("\nYou must write arguments after the script's name!")
        print("To get help, just type \"python {}.py --help\"".format(pythonFileName))
        exit()
    
    # Describe how to use the script
    if "--help" in sys.argv:
        print("\n-How to use this tool by Julobulo:")
        # arguments
        if not len(dictOfArgumentsGiven) == 0:
            print("\n\t\tYou MUST write these arguments and assign them a value (don't know what to write?: \"None\"):")
        for item in dictOfArgumentsGiven:
            print("\t\t\t\t-" + "\"" + item + "\"")
        # options
        if not len(dictOfOptionsGiven) == 0:
            print("\n\t\tYou CAN write these options (don't know if you have to write them?: don't write them):")
        for item in dictOfOptionsGiven:
            print("\t\t\t\t-" + "\"-" + item + "\"")
        if len(dictOfArgumentsGiven) == 0 and len(dictOfOptionsGiven) == 0:
            print("There are no arguments/options availiable for this script!")
            exit()
        def getAnExample():
            finalExample = "python " + pythonFileName + " "
            for item in dictOfArgumentsGiven:
                finalExample += item + "=" + "xyz "
            for item in dictOfOptionsGiven:
                from random import randint
                if randint(0, 1) == 0:
                    finalExample += item + " "
            return finalExample.strip()
        print("\nA simple example of this script could be: \"" + getAnExample() + "\"")
        print("\nAnother simple example of this script could be: \"" + getAnExample() + "\"")
        print("\nNOTE:  Use this script legally please!\n")
        exit()
    
    if caseInsensitive:
        print('\nevery argument/options names are caseInsensitive!\n')
        # lower each argument/option name
        dictOfArgumentsGiven =  {k.lower(): v for k, v in dictOfArgumentsGiven.items()}
        dictOfOptionsGiven =  {k.lower(): v for k, v in dictOfOptionsGiven.items()}
    else:
        print('every argument/options names are caseINSensitive!')
    
    for argument in sys.argv:
        # if the argument name is the name of the python file then skip it
        if argument == pythonFileName or pythonFileName in argument:
            continue
        if caseInsensitive:
            argument = argument.lower()
            argumentList =  [k.lower() for k in argument.split("=")]
        else:
            argumentList = argument.split("=")
        if argument in dictOfOptionsGiven:
            dictOfOptionsGiven[argument] = True
            continue
        if len(argumentList) != 2:
            print("\n{}: Argument/Option not valid!\n".format(argument))
            exit()
        
        isArgumentInGivenDict = False
        for argGiven in dictOfArgumentsGiven:
            if argumentList[0] == argGiven:
                # if it is a number
                if argumentList[1].isnumeric():
                    dictOfArgumentsGiven[argumentList[0]] = int(argumentList[1])
                else:
                    dictOfArgumentsGiven[argumentList[0]] = argumentList[1]
                isArgumentInGivenDict = True
                break
        if not isArgumentInGivenDict:
            print("\nThis argument \"{}\" was not expected!\nExiting program...\n".format(argument))
            exit()

    return dictOfArgumentsGiven, dictOfOptionsGiven


if __name__ == '__main__':
    dictOfArgsFilledIn, dictOfOptFilledIn = useCLIarguments(dictOfArgumentsGiven={'name': None, 'lastName': None}, dictOfOptionsGiven={'-firstOption': None, '-t': None, '-e': None}, caseInsensitive=True)
    print(dictOfArgsFilledIn, '\n', dictOfOptFilledIn)
