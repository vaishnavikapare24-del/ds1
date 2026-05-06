import time

def insecure_http():
    print("\n--- INSECURE HTTP MODE ---")
    
    name = input("Enter your name: ")
    
    try:
        amount = int(input("Enter payment amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    print("\n[Simulating data transfer over HTTP...]")
    time.sleep(1)
    
    print("Sending data in plain text...")
    time.sleep(1)
    
    print("\nAttacker is intercepting the request...")
    time.sleep(2)
    
    # Simulated attack
    hacked_amount = amount * 10
    
    print("\nATTACK DETECTED (Simulated Man-in-the-Middle Attack)")
    print("Original Amount:", amount)
    print("Modified Amount by Attacker:", hacked_amount)
    
    print("\nConclusion:")
    print("HTTP is NOT secure.")
    print("Data is sent in plain text and can be intercepted or modified.")
    print("This is a simulation. Real attacks happen over networks.\n")


def secure_https():
    print("\n--- SECURE HTTPS MODE ---")
    
    name = input("Enter your name: ")
    
    try:
        amount = int(input("Enter payment amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    print("\n[Simulating data transfer over HTTPS...]")
    time.sleep(1)
    
    print("Encrypting data using SSL/TLS...")
    time.sleep(1)
    
    print("\nData is securely transmitted...")
    time.sleep(2)
    
    print("\nSecure Transaction Completed")
    print("Name:", name)
    print("Amount:", amount)
    
    print("\nConclusion:")
    print("HTTPS is secure.")
    print("Data is encrypted and cannot be easily intercepted or modified.")
    print("This is a simulation of SSL/TLS protection.\n")


def main():
    while True:
        print("\nMini Project: HTTP vs HTTPS Simulation")
        print("1. HTTP (Insecure)")
        print("2. HTTPS (Secure)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ")
        
        if choice == '1':
            insecure_http()
        elif choice == '2':
            secure_https()
        elif choice == '3':
            print("\nExiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()