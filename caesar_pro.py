# Save as: caesar_pro.py
import datetime
import string

class AdvancedCaesarCipher:
    def __init__(self):
        self.history = []
    
    def caesar_cipher(self, text, shift, mode='encrypt'):
        """Advanced Caesar Cipher"""
        if mode == 'decrypt':
            shift = -shift
        
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                result += new_char
            else:
                result += char
        return result
    
    def brute_force_decrypt(self, text):
        """Try all 25 possible shifts"""
        print("\n🔓 BRUTE FORCE RESULTS:")
        print("=" * 50)
        for shift in range(1, 26):
            decrypted = self.caesar_cipher(text, shift, 'decrypt')
            print(f"Shift {shift:2d}: {decrypted}")
    
    def frequency_analysis(self, text):
        """Analyze letter frequency"""
        letters = [char.lower() for char in text if char.isalpha()]
        if not letters:
            return "No letters to analyze"
        
        freq = {}
        for letter in letters:
            freq[letter] = freq.get(letter, 0) + 1
        
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        print("\n📊 FREQUENCY ANALYSIS:")
        print("=" * 30)
        for letter, count in sorted_freq[:10]:
            percentage = (count / len(letters)) * 100
            print(f"'{letter}': {count} times ({percentage:.1f}%)")
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "="*60)
        print("🔐 ADVANCED CAESAR CIPHER PRO - CONSOLE EDITION")
        print("="*60)
        print("1. 🔒 Encrypt Text")
        print("2. 🔓 Decrypt Text (with known shift)")
        print("3. 🕵️ Brute Force Decrypt (unknown shift)")
        print("4. 📊 Frequency Analysis")
        print("5. 📜 Show History")
        print("6. 🚪 Exit")
        print("="*60)
    
    def add_to_history(self, operation, original, result, shift):
        """Add operation to history"""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {operation}: '{original}' → '{result}' (Shift: {shift})"
        self.history.append(entry)
    
    def show_history(self):
        """Display operation history"""
        print("\n📜 OPERATION HISTORY:")
        print("=" * 50)
        if not self.history:
            print("No operations yet!")
            return
        
        for i, entry in enumerate(self.history[-10:], 1):
            print(f"{i}. {entry}")
    
    def run(self):
        """Main program loop"""
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                self.encrypt_text()
            elif choice == '2':
                self.decrypt_text()
            elif choice == '3':
                self.brute_force_text()
            elif choice == '4':
                self.analyze_text()
            elif choice == '5':
                self.show_history()
            elif choice == '6':
                print("\n👋 Goodbye! Thanks for using Advanced Caesar Cipher!")
                break
            else:
                print("❌ Invalid choice! Please enter 1-6.")
    
    def encrypt_text(self):
        """Encrypt text"""
        text = input("\nEnter text to encrypt: ")
        try:
            shift = int(input("Enter shift value: "))
            encrypted = self.caesar_cipher(text, shift, 'encrypt')
            print(f"\n✅ ENCRYPTED: {encrypted}")
            print(f"🔑 Shift used: {shift}")
            self.add_to_history("ENCRYPT", text, encrypted, shift)
        except ValueError:
            print("❌ Error: Shift must be a number!")
    
    def decrypt_text(self):
        """Decrypt text with known shift"""
        text = input("\nEnter text to decrypt: ")
        try:
            shift = int(input("Enter shift value: "))
            decrypted = self.caesar_cipher(text, shift, 'decrypt')
            print(f"\n✅ DECRYPTED: {decrypted}")
            print(f"🔑 Shift used: {shift}")
            self.add_to_history("DECRYPT", text, decrypted, shift)
        except ValueError:
            print("❌ Error: Shift must be a number!")
    
    def brute_force_text(self):
        """Brute force decrypt"""
        text = input("\nEnter encrypted text for brute force: ")
        self.brute_force_decrypt(text)
        self.add_to_history("BRUTE_FORCE", text, "Multiple possibilities", "Auto")
    
    def analyze_text(self):
        """Analyze text frequency"""
        text = input("\nEnter text to analyze: ")
        self.frequency_analysis(text)
        self.add_to_history("ANALYZE", text, "Frequency analysis", "N/A")

# Run the program
if __name__ == "__main__":
    print("🚀 Starting Advanced Caesar Cipher Pro...")
    cipher = AdvancedCaesarCipher()
    cipher.run()