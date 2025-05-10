class Bank:
    bank_name = "Soneri Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

if __name__ == "__main__":
    user1 = Bank()
    user2 = Bank()

    print("Before changing bank name: ")
    print(f"User1's bank name: {user1.bank_name}")        
    print(f"User2's bank name: {user2.bank_name}")        

    Bank.change_bank_name("Hbl Bank")

    print("\nAfter changing bank name: ")
    print(f"User1's bank name: {user1.bank_name}")        
    print(f"User2's bank name: {user2.bank_name}")  
