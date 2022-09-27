from time import sleep

def start():
    print('''
            You get out of your car after reaching your family home that's been abandoned for a while.
            Nothing has ever been the same since the incident.... not after what you did. You have a strong urge to leave.
            
            You remember your dad telling you to turn on the generator before heading in.
            ''')

    def generator():
        ans=input(">>> ").lower()
        if 'generator' in ans:
            print('''
                    You go to the back of the house and give the generator a spin and it spins back to life after a couple of tries.
                    You then head back to the front porch of the house. You are hesistant to head inside.
                    ''')

            def opendoor():
                ans = input(">>> ").lower()
                if 'door' in ans or 'inside' in ans:
                    print('''
                            You get the masterkey out and give the knob a spin. After some brute force, the door budges open and you head inside.
                            You get blasted by the stale air within the house and let out an echoey cough. 
                            
                            You walk around the living room and recall the party before the incident, when all was fine...
                            Your pals were having fun playing "Cards Against Humanity" while you secretly had a cold beer.
                            
                            You could go to the kitchen or head upstairs.
                            ''')

                    def house_interior():
                        ans = input(">>> ").lower()
                        if 'kitchen' in ans:
                            print('''
                                    Rot has started to take over the kitchen.... Maybe it's time to get the house refurnished.
                                    
                                    You get a flashback of you and Yen, your sister, messing about in the kitchen, making absolutely horrible dishes while giggling like little childr....
                                    No no... The guilt is too much.
                                    
                                    You return back to the living room. 
                                    ''')
                            house_interior()
                        elif 'upstairs' in ans:
                            print('''
                                    You find yourself in a narrow corridor and find your old room next to Yen's room. You don't dare to go into her room. 
                                    You head inside your room and are surprised to see that nothing has changed about it since you left.
                                    
                                    In the corner of your eye, you notice an old PC. Dad loved to collect old pieces of tech, must be his. 
                                    You hook it up to the power adapter and press the power button expecting nothing... but Voila! The old piece of metal booted up into life!
                                        
                                    The only application is the text-adventure game "Syyllinen".
                                    ''')
                            def boot_game():
                                ans = input(">>> ").lower()
                                if 'launch' in ans or 'play' in ans:
                                    print('''
                                            You boot up the game and are greeted with a welcome screen. You get through it and start the game.
                                            
                                            YOU GET OUT OF THE CAR AFTER REACHING YOUR FAMILY HOME THAT'S BEEN ABANDONED FOR A WHILE. YOU SEE THAT ANOTHER CAR IS ALREADY PARKED HERE.
                                            NOTHING HAS EVER BEEN THE SAME SINCE THE INCIDENT.... NOT AFTER WHAT HE DID. YOU HAVE A STRONG URGE TO STAY AND FINISH THIS.
                                            
                                            YOU BRING THE CROWBAR AND THE MAGNUM YOU BROUGHT ALONG AND STAND BEFORE THE FRONT DOOR.
                                            ''')
                                    def breakdoor():
                                        ans = input(">>> ").lower()
                                        if 'break' in ans or 'crowbar' in ans:
                                            print('''
                                                    YOU USE THE CROWBAR AND PRY OPEN THE DOOR.
                                                    
                                                    
                                                    You hear a loud crash coming from the living room....
                                                    Maybe your mind is playing tricks on you.
                                                    
                                                    
                                                    THE HOUSE SEEMS TO HAVE WORN DOWN SIGNIFICANTLY. YOU CAN'T BLAME THEM, NOT AFTER WHAT HE DID.
                                                    NOW WHY DID HE HAVE TO TAKE THAT BEER AND KEEP IT A DAMN SECRET... 
                                                    
                                                    YOU COULD GO TO THE KITCHEN OR HEAD UPSTAIRS.
                                                    ''')
                                            def game_house_interior():
                                                ans = input(">>> ").lower()
                                                if 'kitchen' in ans:
                                                    print('''
                                                            ROT HAS SERIOUSLY TAKEN OVER THE KITCHEN.... THERE'S NO POINT TRYING TO REFURNISH THIS.
                                                            
                                                            YOU REMEMBER HOW YOU USED TO MESS ABOUT IN THE KITCHEN WITH HIM, GIGGLING LIKE LITTLE CHILDREN.
                                                            THOSE DAYS ARE LONG GONE, AND ARE NEVER GONNA COME BACK. 
                                                            
                                                            YOU RETURN BACK TO THE LIVING ROOM.
                                                            ''')
                                                    game_house_interior()
                                                elif 'upstairs' in ans:
                                                    print('''
                                                            YOU RUN UP THE STAIRS AND FACE A FAMILIAR CORRIDOR.
                                                            
                                                            
                                                            You hear someone run up the stairs behind you and walking around in the corridor.
                                                            Fear and guilt run up your spine. You are afraid to swallow the bitter pill.
                                                            
                                                            
                                                            NO POINT GOING INTO YOUR ROOM, YOU KNOW HE'S TOO COWARD TO FACE HIMSELF. 
                                                            YOU STAND BEFORE HIS ROOM.
                                                            ''')
                                                    def confrontation():
                                                        ans = input(">>> ").lower()
                                                        if 'open' in ans or 'enter' in ans:
                                                            print('''
                                                                    YOU OPEN THE DOOR AND SEE HIM SITTING INFRONT OF YOUR OLD PC.
                                                                    
                                                                    You hear the door open behind you and see a shadow on the wall in front of you.
                                                                    
                                                                    YOU RAISE YOUR MAGNUM TO HIM...
                                                                    ''')
                                                            def endgame():
                                                                print('''
                                                                        CONFESS
                                                                        IT'S ALL YOUR FAULT
                                                                        IT'S ALL YOUR FAULT
                                                                        IT'S ALL YOUR FAULT
                                                                        ''')
                                                                ans = input(">>> ").lower()
                                                                if 'all my fault' in ans:
                                                                    print('''
                                                                            You break down, let it all out and spill the beans.
                                                                            
                                                                            
                                                                            You just got selected into Harvard and are off to leave in a couple of days while Yen had a flight to catch in a few hours.
                                                                            The party was a goodbye-gift set up by your parents and friends. 
                                                                            You recall getting really drunk and suddenly see Yen asking you to drive her to the airport towards the end of the party.
                                                                            She had no idea you were drunk, and you agreed to drive her there. On the drive, you notice a fancy gift box and Yen tells that it's a bottle of wine by Dad.
                                                                            You sheepishly ask for it but Yen denies it. It escalates into an argument and Yen figured out you were already drunk. 
                                                                            
                                                                            She demanded to stop the car but you didn't stop. And then it happened....
                                                                            You have a head-on collision with another driver. You wake up, having no idea how long it's been and see your sister's face completely bloody.
                                                                            You realise what you had done, and go to check on the driver. He's dead....
                                                                            
                                                                            You realise your life is over.... Unless....
                                                                            
                                                                            You grab the gift box, hoping the wine bottle didn't break. You see it intact and drown the driver's face in alcohol to make him seem 
                                                                            like the drunk driver, making sure your fingerprints dont't get on the bottle.
                                                                            You drop the bottle into his car and call for help. You soon pass out and paramedics arrive later, saving you 
                                                                            while declaring Yen and the other driver "Dead on the spot".
                                                                            
                                                                            Police reports declared the accident to be a "drunk and drive" incident, with the other driver 
                                                                            supposedly to have been the drunk one, according to the evidence with the wine bottle found in his car.
                                                                            ''')

                                                                    sleep(30)

                                                                    print('''
                                                                            
                                                                            You let out a sigh of relief after bottling up that secret for years, staying in constant denial.
                                                                            
                                                                            You notice that the PC in front of you had infact never turned on, and realise you were hallucinating the whole thing.
                                                                            You check on the front door for any damage, and see none on it.
                                                                            
                                                                            You get back into your car and get ready to leave. What you did was unforgiveable, but maybe now you can now find peace with it.
                                                                            ''')

                                                                    print('''
                                                                                        YOU GOT THE "BEAT MY INNER DEMONS" ENDING!
                                                                            ''')
                                                                    ans = input(">>> Press Enter To Exit")

                                                                elif 'not my fault' in ans or 'shoot' in ans:
                                                                    print('''
                                                                            No no no... It's not my fault. It was never my fault. I did nothing wron.....
                                                                            
                                                                                                    BANG!
                                                                            
                                                                            You slowly bleed out and notice the magnum on your hand and realise that it was infact you, who had taken the shot on yourself in hysteria.
                                                                            You take your final breath... realising that this may be the only way for you to find any form of peace.                         
                                                                            ''')

                                                                    print('''
                                                                                        YOU GOT THE "CONSUMED BY GUILT" ENDING!
                                                                            ''')
                                                                    ans = input(">>> Press Enter To Exit")

                                                                else:
                                                                    endgame()
                                                            endgame()

                                                        else:
                                                            confrontation()
                                                    confrontation()

                                                else:
                                                    game_house_interior()
                                            game_house_interior()

                                        else:
                                            breakdoor()
                                    breakdoor()

                                else:
                                    boot_game()
                            boot_game()

                        else:
                            house_interior()
                    house_interior()

                else:
                    opendoor()
            opendoor()


        elif 'leave' in ans:
            print('''
                    This is not worth it, you say to yourself... Let bygones be bygones, and you leave the place.
                    
                                    YOU GOT THE "BURY THE SECRETS" ENDING!
                    
                                                Game Over
                ''')

            print("WHY DID YOU PLAY THIS GAME IF ALL YOU WANTED TO DO WAS FINISH IT ASAP?")
            ans = input(">>> Press Enter To Exit")
        else:
            generator()
    generator()

def menu():
    print('''
                            WELCOME TO "SYYLLINEN"
                A TEXT-BASED ADVENTURE GAME, INSPIRED BY "Stories Untold"
                THERE'S 3 ENDINGS TO THIS, GOOD LUCK FINDING THEM ALL!
            ''')
    ans = input(">>> Press Enter To Begin!")
    start()

menu()