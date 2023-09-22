How to use this tool by Julobulo:
-use the function "useCLIarguments"
    -create two dictionnaries: one for the arguments and one for the options
        -ex: dictOfArguments = {'name': None, 'lastName': None}
             dictofOptions = {'-firstOption': None, '-t': None, '-e': None}
    -assign the value of the two dictionnaries to the function, and pass the two dict in the function as arguments
        -ex: dictOfArgsFilledIn, dictOfOptFilledIn = useCLIarguments(dictOfArgumentsGiven=dictOfArguments, dictOfOptionsGiven=dictOfOptions, caseInsensitive=True)
    -enter True of False as argument for the "CaseSensitive" variable