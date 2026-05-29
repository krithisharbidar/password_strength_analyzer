# ============================================
# PASSWORD STRENGTH ANALYZER
# By Kruthi V Sharbidar | Cyber Security Project
# ============================================

import re
from colorama import Fore, Style, init

# This line makes colors work on all computers
init(autoreset=True)

# List of most common passwords hackers try first
COMMON_PASSWORDS = [
    "password", "password123", "123456", "12345678", "qwerty",
    "abc123", "monkey", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley",
    "passw0rd", "shadow", "123123", "superman", "football",
    "welcome", "hello", "admin", "login", "princess", "secret"
]

# ── ANALYZE FUNCTION ──────────────────────────────────────
def analyze_password(password):
    score = 0
    feedback = []

    # Check 1: Length
    if len(password) >= 8:
        score += 15
    else:
        feedback.append("❌ Too short — use at least 8 characters")

    if len(password) >= 12:
        score += 10
    else:
        feedback.append("⚠️  12+ characters makes it much stronger")

    # Check 2: Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 15
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")

    # Check 3: Lowercase letters
    if re.search(r'[a-z]', password):
        score += 10
    else:
        feedback.append("❌ Add lowercase letters (a-z)")

    # Check 4: Numbers
    if re.search(r'[0-9]', password):
        score += 15
    else:
        feedback.append("❌ Add numbers (0-9)")

    # Check 5: Special symbols
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:,.<>?]', password):
        score += 20
    else:
        feedback.append("❌ Add symbols like !@#$%^&*")

    # Check 6: Common password
    if password.lower() in COMMON_PASSWORDS:
        score -= 30
        feedback.append("🚨 This is a very commonly used password!")
    else:
        score += 10

    # Check 7: Repeated characters (e.g. aaa, 111)
    if re.search(r'(.)\1{2,}', password):
        feedback.append("⚠️  Avoid repeated characters like 'aaa' or '111'")
    else:
        score += 5

    return score, feedback


# ── STRENGTH LABEL FUNCTION ───────────────────────────────
def get_strength(score):
    if score < 30:
        return "CRITICAL", Fore.RED
    elif score < 50:
        return "WEAK", Fore.LIGHTRED_EX
    elif score < 65:
        return "FAIR", Fore.YELLOW
    elif score < 80:
        return "STRONG", Fore.LIGHTGREEN_EX
    else:
        return "FORTRESS 🔒", Fore.CYAN


# ── DISPLAY RESULT FUNCTION ───────────────────────────────
def display_result(password, score, feedback):
    strength, color = get_strength(score)

    print("\n" + "=" * 50)
    print(f"  PASSWORD  : {'*' * len(password)}")
    print(f"  SCORE     : {score}/100")
    print(color + f"  STRENGTH  : {strength}" + Style.RESET_ALL)
    print("=" * 50)

    if feedback:
        print(Fore.YELLOW + "\n📋 RECOMMENDATIONS:" + Style.RESET_ALL)
        for tip in feedback:
            print(f"   {tip}")
    else:
        print(Fore.CYAN + "\n✅ ALL CHECKS PASSED! Your password is excellent." + Style.RESET_ALL)

    print()


# ── MAIN PROGRAM LOOP ─────────────────────────────────────
def main():
    print(Fore.CYAN + """
╔══════════════════════════════════════════════╗
║       PASSWORD STRENGTH ANALYZER             ║
║       By Kruthi V Sharbidar                  ║
║       Cyber Security Project | IBM Certified ║
╚══════════════════════════════════════════════╝
    """ + Style.RESET_ALL)

    while True:
        print("Options:")
        print("  [1] Check a password")
        print("  [2] Exit")
        choice = input("\nEnter choice (1 or 2): ").strip()

        if choice == "1":
            password = input("\nEnter password to analyze: ")

            if not password:
                print(Fore.RED + "⚠️  You didn't enter anything!" + Style.RESET_ALL)
                continue

            score, feedback = analyze_password(password)
            display_result(password, score, feedback)

        elif choice == "2":
            print(Fore.CYAN + "\nStay secure! Goodbye 👋" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Invalid choice. Type 1 or 2." + Style.RESET_ALL)


# This runs the program
if __name__ == "__main__":
    main()
