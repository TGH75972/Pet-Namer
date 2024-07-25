import random

class PetNamer:
    def __init__(self):
        self.pet_types = {
            'dog': ['Rover', 'Buddy', 'Max', 'Bella', 'Lucy'],
            'cat': ['Whiskers', 'Shadow', 'Mittens', 'Simba', 'Nala'],
            'bird': ['Tweety', 'Sky', 'Buddy', 'Kiwi', 'Pepper'],
            'fish': ['Goldie', 'Bubbles', 'Splash', 'Finn', 'Marlin'],
            'hamster': ['Nibbles', 'Gizmo', 'Squeaky', 'Teddy', 'Pip']
        }
        self.characteristics = {
            'playful': ['Bouncy', 'Happy', 'Peppy', 'Joyful', 'Lively'],
            'quiet': ['Calm', 'Serene', 'Peaceful', 'Mellow', 'Tranquil'],
            'mischievous': ['Rascal', 'Bandit', 'Trouble', 'Trickster', 'Imp'],
            'loyal': ['Faithful', 'True', 'Steady', 'Constant', 'Devoted'],
            'adventurous': ['Brave', 'Bold', 'Fearless', 'Daring', 'Heroic']
        }
        self.saved_names = []

    def get_pet_name(self, pet_type, characteristic):
        if pet_type not in self.pet_types or characteristic not in self.characteristics:
            return "Invalid pet type or characteristic."
        
        pet_name = random.choice(self.pet_types[pet_type])
        char_name = random.choice(self.characteristics[characteristic])
        
        return f'{char_name} {pet_name}'

    def save_pet_name(self, pet_name):
        self.saved_names.append(pet_name)

    def view_saved_names(self):
        if not self.saved_names:
            return "No saved names."
        return '\n'.join(self.saved_names)

    def add_custom_name(self, pet_type, name):
        if pet_type in self.pet_types:
            self.pet_types[pet_type].append(name)
        else:
            self.pet_types[pet_type] = [name]

    def add_custom_characteristic(self, characteristic, description):
        if characteristic in self.characteristics:
            self.characteristics[characteristic].append(description)
        else:
            self.characteristics[characteristic] = [description]

def main():
    pet_namer = PetNamer()

    while True:
        print("\nPet Naming App Menu:")
        print("1. Generate Pet Name")
        print("2. Save Generated Pet Name")
        print("3. View Saved Pet Names")
        print("4. Add Custom Pet Name")
        print("5. Add Custom Characteristic")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Choose a type of pet:")
            print("1. Dog")
            print("2. Cat")
            print("3. Bird")
            print("4. Fish")
            print("5. Hamster")

            pet_choice = int(input("Enter the number corresponding to your choice: "))
            pet_types = {
                1: 'dog',
                2: 'cat',
                3: 'bird',
                4: 'fish',
                5: 'hamster'
            }

            if pet_choice not in pet_types:
                print("Invalid choice.")
                continue

            pet_type = pet_types[pet_choice]

            print("Choose a characteristic:")
            print("1. Playful")
            print("2. Quiet")
            print("3. Mischievous")
            print("4. Loyal")
            print("5. Adventurous")

            char_choice = int(input("Enter the number corresponding to your choice: "))
            characteristics = {
                1: 'playful',
                2: 'quiet',
                3: 'mischievous',
                4: 'loyal',
                5: 'adventurous'
            }

            if char_choice not in characteristics:
                print("Invalid choice.")
                continue

            characteristic = characteristics[char_choice]
            pet_name = pet_namer.get_pet_name(pet_type, characteristic)
            print(f"Your pet's name is: {pet_name}")

        elif choice == 2:
            pet_name = input("Enter the pet name to save: ")
            pet_namer.save_pet_name(pet_name)
            print("Pet name saved.")

        elif choice == 3:
            print("Saved Pet Names:")
            print(pet_namer.view_saved_names())

        elif choice == 4:
            pet_type = input("Enter the type of pet: ").lower()
            name = input(f"Enter a custom name for {pet_type}: ")
            pet_namer.add_custom_name(pet_type, name)
            print(f"Custom name '{name}' added for {pet_type}s.")

        elif choice == 5:
            characteristic = input("Enter a new characteristic: ").lower()
            description = input(f"Enter a description for {characteristic}: ")
            pet_namer.add_custom_characteristic(characteristic, description)
            print(f"Custom characteristic '{characteristic}' with description '{description}' added.")

        elif choice == 6:
            print("Exiting the Pet Naming App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
