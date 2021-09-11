import sys

print("--------------------------------------------------")
print("File generator for Phaser 3 - By Gabriel Galindo")
print("Bogotá - Col - 2021 - Sep")
print("v.0.1")
print("--------------------------------------------------")


main_option = None

if __name__ == "__main__":    
    try:
        main_option = sys.argv[1]
        print(main_option)
        if main_option == "atlas":
            print("The process of creating an atlas file will start")
        elif main_option == "scene":
            print("The process of creating an Scene file will start")
        else:
            print("Cannot read the option")
    except IndexError as e:
        print("Cannot recivied any param, please read the documentation")
        
    
