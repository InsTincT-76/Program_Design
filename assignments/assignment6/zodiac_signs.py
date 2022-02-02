user_inp = input("what would you like to do? (V)iew signs, or see class (F)ortune:  ").lower().strip()


if user_inp == "v":
    print("Astrological Signs and Dates: \n - Aries: March 21 - April 19 \n - Taurus: April 20 - May 20 \n - Gemini: May 21 - June 21  \n - Cancer: June 22 - July 22 \
        \n - Leo: July 23 - August 22  \n - Virgo: August 23 - September 22  \n - Libra: September 23 - October 23   \n - Scorpius: October 24 - November 21 \
              \n - Sagittarius: November 22 - December 21   \n - Capricoronus: December 22 - January 19   \n - Aquarius: January 20 - Febuary 18   \n - Pisces: Febuary 19 - March 20")
    print(f"Have a nice day!")

    
elif user_inp == "f":
    sign_inp = input("Enter your sign:  ") .lower() .strip()
    
    
    
    if sign_inp == "aries":
        print(f"Do not worry, your efforts will be fruitful in time ")
        print(f"Have a nice day!")

       
    elif sign_inp == "taurus":
        print(f"A fresh start will put you on your way")
        print(f"Have a nice day!")


    elif sign_inp == "gemini":
        print(f"A lifetime of happiness lies ahead of you")       
        print(f"Have a nice day!")

        
    elif sign_inp == "cancer":
        print(f"Accept something you cannot change")
        print(f"Have a nice day!")

        
    elif sign_inp == "leo":
        print(f"A beautiful, smart, loving person will be coming into your life") 
        print(f"Have a nice day!")

        
    elif sign_inp == "virgo":
        print(f"A dubious friend may be an enemy in camouflage")
        print(f"Have a nice day!")

        
    elif sign_inp == "libra":
        print(f"Change is happening in your life, so go with the flow!")
        print(f"Have a nice day!")

        
    elif sign_inp == "scorpius":
        print(f"bide your time, for success is near")
        print(f"Have a nice day!")

        
    elif sign_inp == "sagittarius":
        print(f"If you continually give, you will continually have.")
        print(f"Have a nice day!")

        
    elif sign_inp == "Capricoronus":
        print(f"It is better to deal with problems before they arise.")
        print(f"Have a nice day!")

        
    elif sign_inp == "Aquarius":
        print(f"o Says: Pandas like eating bamboo, but I prefer mine dipped in chocolate.")
        print(f"Have a nice day!")

        
    elif sign_inp == "Pisces":
        print(f"Savor your freedom, it is precious.")
        print(f"Have a nice day!")

        
    else:
        print(f"Sign is incorrect")


else:
        print(f"Incorrect Enter v or f")
        
        
        
        




        
            