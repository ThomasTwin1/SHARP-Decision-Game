# SHARP Stand Up - Army Training Text Adventure
# Developer: TT1 Games (Sherrard Thomas II)
# Version: 1.0
# Purpose: Educational SHARP scenario-based decision game

import os
import time

TITLE_ART = r"""
███████╗██╗  ██╗ █████╗ ██████╗ ██████╗     ███████╗████████╗ █████╗ ███╗   ██╗██████╗     ██╗   ██╗██████╗ 
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗    ██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔══██╗    ██║   ██║██╔══██╗
███████╗███████║███████║██████╔╝██████╔╝    ███████╗   ██║   ███████║██╔██╗ ██║██║  ██║    ██║   ██║██████╔╝
╚════██║██╔══██║██╔══██║██╔══██╗██╔═══╝     ╚════██║   ██║   ██╔══██║██║╚██╗██║██║  ██║    ██║   ██║██╔═══╝ 
███████║██║  ██║██║  ██║██║  ██║██║         ███████║   ██║   ██║  ██║██║ ╚████║██████╔╝    ╚██████╔╝██║     
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝         ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝      ╚═════╝ ╚═╝     

                         A SHARP Scenario Training Game by TT1 Games
"""

MENU_TEXT = """
=====================================================
                      MAIN MENU
=====================================================
[ 1 ] Start Training Game
[ 2 ] Credits
[ 3 ] SHARP Reminder
[ 4 ] Quit
"""

DISCLAIMER = """
=====================================================
                    TRAINING NOTE
=====================================================
This game is for Army SHARP awareness training only.
It is not a substitute for official SHARP instruction,
victim advocacy, legal guidance, command guidance, or
emergency response.

If someone is in immediate danger, call emergency services
or contact the chain of command / law enforcement as appropriate.
"""

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, delay=0.01):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def show_score(score, trust):
    stars = "★ " * score
    shields = "🛡️ " * trust
    print(f"\nReadiness Score: {stars}({score})")
    print(f"Trust Level    : {shields}({trust})")


def pause():
    input("\nPress Enter to continue...")


def show_credits():
    clear_screen()
    print(TITLE_ART)
    print("""
==================== CREDITS ====================

Game Title : SHARP Stand Up
Genre      : Text Adventure / Scenario Training
Developer  : TT1 Games (Sherrard Thomas II)
Engine     : Python + Terminal
Purpose    : Practice bystander intervention, reporting options,
             empathy, privacy, and leader response.

Thank you for building training that protects Soldiers.
""")
    pause()


def show_reminder():
    clear_screen()
    print(TITLE_ART)
    print("""
==================== SHARP REMINDER ====================

Key ideas to remember:

1. Intervene safely when you see concerning behavior.
2. Believe, listen, and support Soldiers who disclose harm.
3. Do not investigate on your own.
4. Protect privacy. Share only with people who need to know.
5. Know the difference between restricted and unrestricted reporting.
6. Contact a SHARP professional, victim advocate, SARC, chain of command,
   law enforcement, or medical support as appropriate.

Leadership principle:
Create a climate where Soldiers know they are protected, respected,
and taken seriously.
""")
    pause()


def wrong_choice(message, teaching_point):
    slow_print(message)
    print("\nTraining Feedback:")
    print(teaching_point)


def good_choice(message, teaching_point):
    slow_print(message)
    print("\nTraining Feedback:")
    print(teaching_point)


def play_game():
    clear_screen()
    print(TITLE_ART)
    print(DISCLAIMER)
    player = input("Enter your name or call sign:\n> ").strip()
    if not player:
        player = "Leader"

    score = 0
    trust = 3
    choices_made = 0

    slow_print(f"\nWelcome, {player}. You are the team leader on duty during a unit training week.")
    slow_print("Your mission: protect the team, make sound decisions, and build a climate of trust.")
    show_score(score, trust)

    # =====================
    # Scenario 1 – Barracks Hallway
    # =====================
    while True:
        choice = input('''\nSCENARIO 1: Barracks Hallway
You hear a Soldier making sexual comments toward another Soldier who looks uncomfortable.
The Soldier being targeted is trying to walk away.

What do you do?
[ A ] Laugh it off because it is probably just joking
[ B ] Interrupt safely, separate the Soldiers, and check on the targeted Soldier
[ C ] Ignore it because nobody reported anything

Your choice: ''').strip().lower()
        choices_made += 1

        if choice in ("b", "interrupt", "safe"):
            good_choice("\nYou step in calmly: 'Hey, that's not okay. Move out.' You separate the situation and check on the Soldier privately.",
                        "Correct. Safe bystander intervention can stop harm early. Check on the Soldier without forcing details.")
            score += 1
            break
        elif choice in ("a", "laugh"):
            wrong_choice("\nYou laugh it off. The targeted Soldier becomes quiet and avoids the team for the rest of the day.",
                         "Not best. Joking along can normalize harassment and reduce trust in leadership.")
            trust -= 1
            show_score(score, trust)
        elif choice in ("c", "ignore"):
            wrong_choice("\nYou ignore it. Other Soldiers notice that no one corrected the behavior.",
                         "Not best. Leaders and teammates should address concerning behavior early, even before a formal report.")
            trust -= 1
            show_score(score, trust)
        else:
            print("\n❌ Invalid response. Please choose A, B, or C.")

        if trust <= 0:
            print("\nTrust dropped too low. The team no longer believes leadership will act. Training failed.")
            print(f"Total choices made: {choices_made}")
            return

    show_score(score, trust)

    # =====================
    # Scenario 2 – Disclosure
    # =====================
    while True:
        choice = input('''\nSCENARIO 2: Private Disclosure
Later, a Soldier asks to speak with you privately. They say something happened at a party and they do not know what to do.
They are nervous and ask, 'Will everyone find out?'

What do you do first?
[ A ] Ask detailed investigative questions so you can find out exactly what happened
[ B ] Listen, ensure they are safe, explain reporting options, and connect them with SHARP support
[ C ] Tell the whole squad to find out who was involved

Your choice: ''').strip().lower()
        choices_made += 1

        if choice in ("b", "listen", "support"):
            good_choice("\nYou stay calm, listen, ask if they are safe, and explain that a SHARP professional can explain restricted and unrestricted reporting options.",
                        "Correct. Support first. Do not investigate. Connect the Soldier with trained SHARP resources and protect privacy.")
            score += 1
            break
        elif choice in ("a", "questions"):
            wrong_choice("\nYou begin asking for every detail. The Soldier becomes overwhelmed and stops talking.",
                         "Not best. Do not conduct your own investigation. Ask only what is needed for immediate safety and support.")
            trust -= 1
            show_score(score, trust)
        elif choice in ("c", "squad"):
            wrong_choice("\nYou involve the squad. Rumors spread quickly and the Soldier feels exposed.",
                         "Wrong move. Protect privacy. Share information only with the correct people who need to know.")
            trust -= 2
            show_score(score, trust)
        else:
            print("\n❌ Invalid response. Please choose A, B, or C.")

        if trust <= 0:
            print("\nTrust dropped too low. The Soldier no longer feels safe seeking help. Training failed.")
            print(f"Total choices made: {choices_made}")
            return

    show_score(score, trust)

    # =====================
    # Scenario 3 – Social Media
    # =====================
    while True:
        choice = input('''\nSCENARIO 3: Group Chat
A screenshot appears in a team group chat. It includes rumors about a Soldier and mocking comments.
Several people are reacting with laughing emojis.

What do you do?
[ A ] Tell everyone to delete the post, stop the comments, preserve what is needed, and report through the proper channel
[ B ] Add a laughing emoji so you do not seem uptight
[ C ] Message the Soldier named in the rumor and demand they explain what happened

Your choice: ''').strip().lower()
        choices_made += 1

        if choice in ("a", "delete", "report"):
            good_choice("\nYou stop the chat, direct Soldiers not to spread rumors, preserve what leadership/SHARP may need, and move it to the proper channel.",
                        "Correct. Stop retaliation, gossip, and humiliation. Protect the person involved and notify the correct support channels.")
            score += 1
            break
        elif choice in ("b", "laugh"):
            wrong_choice("\nYou react with a laughing emoji. The chat gets worse and the Soldier hears about it.",
                         "Not best. Online comments can become harassment, retaliation, or evidence of a harmful climate.")
            trust -= 1
            show_score(score, trust)
        elif choice in ("c", "demand"):
            wrong_choice("\nYou demand an explanation from the Soldier. They feel cornered and stop responding.",
                         "Not best. Do not pressure the Soldier for details. Focus on safety, support, privacy, and proper reporting.")
            trust -= 1
            show_score(score, trust)
        else:
            print("\n❌ Invalid response. Please choose A, B, or C.")

        if trust <= 0:
            print("\nTrust dropped too low. The online climate became harmful. Training failed.")
            print(f"Total choices made: {choices_made}")
            return

    show_score(score, trust)

    # =====================
    # Scenario 4 – Leader Response
    # =====================
    while True:
        choice = input('''\nSCENARIO 4: Leader Decision
Your PSG asks what happened. You know privacy matters, but leadership may need enough information to keep people safe.

What is the best response?
[ A ] Give only necessary information through the proper channel and ask for SHARP guidance
[ B ] Share every detail you heard so everyone knows the full story
[ C ] Keep everything to yourself and do nothing else

Your choice: ''').strip().lower()
        choices_made += 1

        if choice in ("a", "necessary", "proper"):
            good_choice("\nYou share only what is necessary with the appropriate leader/support channel and ask for SHARP guidance.",
                        "Correct. Balance privacy, safety, and command responsibility. Do not spread details beyond those who need to know.")
            score += 1
            break
        elif choice in ("b", "details"):
            wrong_choice("\nYou share unnecessary details. The story starts moving around the unit.",
                         "Not best. Oversharing can damage trust, violate privacy, and increase harm.")
            trust -= 1
            show_score(score, trust)
        elif choice in ("c", "nothing"):
            wrong_choice("\nYou keep everything to yourself and take no action. The Soldier does not receive support.",
                         "Not best. Leaders must connect Soldiers to the right resources and respond appropriately.")
            trust -= 1
            show_score(score, trust)
        else:
            print("\n❌ Invalid response. Please choose A, B, or C.")

        if trust <= 0:
            print("\nTrust dropped too low. The response failed to protect the Soldier and the team climate. Training failed.")
            print(f"Total choices made: {choices_made}")
            return

    # =====================
    # Final Results
    # =====================
    clear_screen()
    print(TITLE_ART)
    slow_print("Final AAR: You completed the SHARP Stand Up scenario lane.")
    show_score(score, trust)
    print(f"\nTotal choices made: {choices_made}")

    if score == 4 and trust >= 3:
        print("Rank: S – Trusted Leader. You protected the Soldier and strengthened the climate. 🛡️")
    elif score >= 3:
        print("Rank: A – Solid Response. Good decisions with room to tighten execution.")
    elif score >= 2:
        print("Rank: B – Needs Rehearsal. Review reporting options, privacy, and bystander intervention.")
    else:
        print("Rank: Remedial Training Needed. Revisit SHARP fundamentals before leading this lane.")

    print("\nRemember: Stop harmful behavior early. Support the Soldier. Protect privacy. Use trained SHARP resources.")


def main():
    while True:
        clear_screen()
        print(TITLE_ART)
        print(MENU_TEXT)
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            play_game()
            pause()
        elif choice == "2":
            show_credits()
        elif choice == "3":
            show_reminder()
        elif choice == "4":
            clear_screen()
            print("Thanks for playing SHARP Stand Up!\n- TT1 Games")
            break
        else:
            print("\n❌ Invalid selection. Please choose 1, 2, 3, or 4.")
            time.sleep(1.5)


if __name__ == "__main__":
    main()
