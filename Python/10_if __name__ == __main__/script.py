if __name__ == "__main__":      # This code block will only execute if this script is run directly
    print("This script is being run directly.")
else:
    # This code block will only execute if this script is run Indirectly(through another script)
    print("This script is being imported as a module into another script.")
    
 
# When you run this script directly, you will see the output: 
# "This script is being run directly." 
# However, if you import this script as a module into another script, you will see the output: 
# "This script is being imported as a module into another script." 
# This allows you to reuse code from one script in another while controlling the execution of specific parts of the code.    
