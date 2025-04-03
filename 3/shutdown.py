def shutdown():
    a = "Shutting Down.."
    b = "Error: Unable to shutdown"
    
    x = input("Do you want to shutdown? (yes/no): ")
    
    if x == "yes":
        print(a)
    else:
        print(b)

shutdown()
