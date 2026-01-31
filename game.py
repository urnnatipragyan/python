import random
from collections import defaultdict


class TambolaTicket:
    """Represents a single Tambola ticket (3 rows x 9 columns)"""
    
    def __init__(self):
        self.ticket = self.generate_ticket()
        self.marked = [[False] * 9 for _ in range(3)]
    
    def generate_ticket(self):
        """Generate a valid Tambola ticket following standard rules"""
        ticket = [[0] * 9 for _ in range(3)]
        
        # For each column, select one number from the appropriate range
        for col in range(9):
            start = col * 10 + 1
            end = col * 10 + 10 if col < 8 else 91
            numbers = list(range(start, end))
            
            # Select 3 unique random numbers for this column
            selected = random.sample(numbers, 3)
            selected.sort()
            
            for row in range(3):
                ticket[row][col] = selected[row]
        
        
        for row in range(3):
            
            row_data = [(ticket[row][col], col) for col in range(9)]
            
            keep_indices = random.sample(range(9), 5)
            
            
            new_row = [0] * 9
            for idx in sorted(keep_indices):
                val, col = row_data[idx]
                new_row[idx] = val
            
            ticket[row] = new_row
        
        return ticket
    
    def mark_number(self, number):
        """Mark a number on the ticket if it exists"""
        for row in range(3):
            for col in range(9):
                if self.ticket[row][col] == number:
                    self.marked[row][col] = True
                    return True
        return False
    
    def check_early_five(self):
        """Check if first 5 numbers are marked"""
        count = 0
        for row in range(3):
            for col in range(9):
                if self.ticket[row][col] != 0 and self.marked[row][col]:
                    count += 1
                    if count == 5:
                        return True
        return False
    
    def check_top_row(self):
        """Check if entire top row is marked"""
        for col in range(9):
            if self.ticket[0][col] != 0 and not self.marked[0][col]:
                return False
        return True
    
    def check_middle_row(self):
        """Check if entire middle row is marked"""
        for col in range(9):
            if self.ticket[1][col] != 0 and not self.marked[1][col]:
                return False
        return True
    
    def check_bottom_row(self):
        """Check if entire bottom row is marked"""
        for col in range(9):
            if self.ticket[2][col] != 0 and not self.marked[2][col]:
                return False
        return True
    
    def check_full_house(self):
        """Check if entire ticket is marked (Full House)"""
        for row in range(3):
            for col in range(9):
                if self.ticket[row][col] != 0 and not self.marked[row][col]:
                    return False
        return True
    
    def display(self):
        """Display the ticket in a formatted way"""
        print("\n" + "="*50)
        print("TAMBOLA TICKET")
        print("="*50)
        for row in range(3):
            row_display = []
            for col in range(9):
                if self.ticket[row][col] == 0:
                    row_display.append("  -")
                elif self.marked[row][col]:
                    row_display.append(f"[{self.ticket[row][col]:2d}]")
                else:
                    row_display.append(f" {self.ticket[row][col]:2d} ")
            print(" ".join(row_display))
        print("="*50 + "\n")


class TambolaGame:
    """Manages the Tambola game"""
    
    def __init__(self, num_tickets=1, players=None):
        self.tickets = [TambolaTicket() for _ in range(num_tickets)]
        self.called_numbers = []
        self.all_numbers = list(range(1, 91))
        random.shuffle(self.all_numbers)
        self.claimed_prizes = defaultdict(list)  
        self.game_over = False
        self.players = players or []
        self.winner_ticket = None
        self.winner_name = None
    
    def display_all_tickets(self):
        """Display all tickets"""
        for idx, ticket in enumerate(self.tickets):
            print(f"\n--- TICKET {idx + 1} ---")
            ticket.display()
    
    def call_number(self):
        """Call the next number"""
        if not self.all_numbers:
            print("All numbers have been called!")
            self.game_over = True
            return None
        
        number = self.all_numbers.pop(0)
        self.called_numbers.append(number)
        
        print(f"\n{'*'*40}")
        print(f"NUMBER CALLED: {number}")
        print(f"{'*'*40}")
        print(f"Total numbers called: {len(self.called_numbers)}\n")
        
        
        for idx, ticket in enumerate(self.tickets):
            if ticket.mark_number(number):
                print(f"✓ Number {number} marked on Ticket {idx + 1}")
        
        return number
    
    def check_wins(self):
        """Check for winning patterns"""
        for ticket_idx, ticket in enumerate(self.tickets):
            ticket_num = ticket_idx + 1
            
            
            if "Early Five" not in self.claimed_prizes[ticket_idx]:
                if ticket.check_early_five():
                    print(f"\n🎉 EARLY FIVE! Ticket {ticket_num} wins!")
                    self.claimed_prizes[ticket_idx].append("Early Five")
            
            
            if "Top Row" not in self.claimed_prizes[ticket_idx]:
                if ticket.check_top_row():
                    print(f"\n🎉 TOP ROW! Ticket {ticket_num} wins!")
                    self.claimed_prizes[ticket_idx].append("Top Row")
            
            
            if "Middle Row" not in self.claimed_prizes[ticket_idx]:
                if ticket.check_middle_row():
                    print(f"\n🎉 MIDDLE ROW! Ticket {ticket_num} wins!")
                    self.claimed_prizes[ticket_idx].append("Middle Row")
            
            
            if "Bottom Row" not in self.claimed_prizes[ticket_idx]:
                if ticket.check_bottom_row():
                    print(f"\n🎉 BOTTOM ROW! Ticket {ticket_num} wins!")
                    self.claimed_prizes[ticket_idx].append("Bottom Row")
            
            
            if "Full House" not in self.claimed_prizes[ticket_idx]:
                if ticket.check_full_house():
                    self.winner_ticket = ticket_num
                    
                    if self.players:
                        player_idx = ticket_idx // (len(self.tickets) // len(self.players))
                        if player_idx < len(self.players):
                            self.winner_name = self.players[player_idx]
                    
                    print(f"\n🏆 FULL HOUSE! Ticket {ticket_num} WINS THE GAME! 🏆")
                    if self.winner_name:
                        print(f"🎊 WINNER: {self.winner_name}! 🎊")
                    self.claimed_prizes[ticket_idx].append("Full House")
                    self.game_over = True
                    return True
        
        return False
    
    def display_game_status(self):
        """Display current game status"""
        print("\n" + "="*60)
        print("GAME STATUS")
        print("="*60)
        print(f"Numbers called: {len(self.called_numbers)}/90")
        print(f"Called numbers: {sorted(self.called_numbers)}")
        print(f"\nPrizes claimed:")
        for ticket_idx, prizes in self.claimed_prizes.items():
            if prizes:
                print(f"  Ticket {ticket_idx + 1}: {', '.join(prizes)}")
        print("="*60 + "\n")
    
    def play(self, auto_play=False):
        """Play the game"""
        print("\n" + "="*60)
        print("WELCOME TO TAMBOLA!")
        print("="*60)
        self.display_all_tickets()
        
        while not self.game_over and self.all_numbers:
            if auto_play:
                input("Press Enter to call next number...")
            else:
                user_input = input("\nPress Enter to call next number (or 'quit' to exit): ").strip().lower()
                if user_input == 'quit':
                    print("Game ended!")
                    break
            
            self.call_number()
            self.display_all_tickets()
            
            if self.check_wins():
                break
            
            self.display_game_status()
        
        if self.game_over:
            print("\n" + "="*60)
            print("GAME OVER!")
            print("="*60)
            self.display_game_status()
            self.display_all_tickets()
            
            
            if self.winner_name:
                print("\n" + "🏆" * 35)
                print(" " * 15 + f"🎊 CONGRATULATIONS {self.winner_name}! 🎊")
                print(" " * 18 + f"YOU ARE THE WINNER!")
                print("🏆" * 35)


def display_header():
    """Display the website-style header"""
    print("\n" + "="*70)
    print(" " * 15 + "🎰 TAMBOLA GAME ONLINE 🎰")
    print("="*70)


def display_menu():
    """Display the main menu"""
    display_header()
    print("\n" + " " * 20 + "MAIN MENU")
    print("-" * 70)
    print("  1. Play Now")
    print("  2. View Instructions")
    print("  3. Quit")
    print("-" * 70)


def get_player_names(num_players):
    """Get player names"""
    print("\n" + "="*70)
    print("ENTER PLAYER NAMES")
    print("="*70)
    players = []
    for i in range(num_players):
        while True:
            name = input(f"Enter name for Player {i + 1}: ").strip()
            if name:
                players.append(name)
                break
            else:
                print("❌ Name cannot be empty. Please try again.")
    return players


def display_instructions():
    """Display game instructions"""
    display_header()
    print("\n📖 GAME INSTRUCTIONS")
    print("-" * 70)
    print("""
WINNING PATTERNS:
  1. Early Five    - Mark 5 numbers first
  2. Top Row       - Mark all numbers in the top row
  3. Middle Row    - Mark all numbers in the middle row
  4. Bottom Row    - Mark all numbers in the bottom row
  5. Full House    - Mark all 15 numbers on your ticket

TICKET STRUCTURE:
  • 3 rows × 9 columns
  • Each row contains exactly 5 numbers and 4 empty spaces
  • Numbers range from 1 to 90
  • Organized in columns: 1-10, 11-20, 21-30, ..., 81-90

HOW TO PLAY:
  1. Enter your name(s)
  2. Select number of tickets
  3. Press Enter to call each number
  4. Numbers are automatically marked on your tickets
  5. First to achieve a winning pattern wins!
  6. Game ends when someone achieves Full House

NOTATION:
  • [ 42 ] = Marked number
  •   42  = Unmarked number
  •   -   = Empty space
""")
    print("-" * 70)


def play_game_session():
    """Main game session"""
    display_header()
    
    
    while True:
        try:
            num_players = int(input("\n🎮 Enter number of players (1-10): "))
            if 1 <= num_players <= 10:
                break
            else:
                print("❌ Please enter a number between 1 and 10.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
    
    
    players = get_player_names(num_players)
    
    
    print("\n" + "="*70)
    print("REGISTERED PLAYERS:")
    for i, player in enumerate(players, 1):
        print(f"  {i}. {player}")
    print("="*70)
    
    
    while True:
        try:
            num_tickets = int(input("\n🎫 Enter number of tickets per player (1-10): "))
            if 1 <= num_tickets <= 10:
                break
            else:
                print("❌ Please enter a number between 1 and 10.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
    
    total_tickets = num_players * num_tickets
    print(f"\n✅ Total tickets: {total_tickets}")
    print(f"   ({num_players} players × {num_tickets} tickets)")
    
    
    game = TambolaGame(total_tickets, players)
    
    
    print("\n" + "="*70)
    print("TICKET ASSIGNMENTS:")
    for i, player in enumerate(players):
        start_idx = i * num_tickets + 1
        end_idx = (i + 1) * num_tickets
        ticket_range = f"{start_idx}-{end_idx}" if num_tickets > 1 else str(start_idx)
        print(f"  {player}: Tickets {ticket_range}")
    print("="*70)
    
    input("\n🚀 Press Enter to start the game...")
    game.play()
    
    
    display_thank_you(game)


def display_thank_you(game):
    """Display thank you message after game"""
    print("\n" + "="*70)
    print(" " * 20 + "🙏 THANK YOU FOR PLAYING! 🙏")
    print("="*70)
    print("\nGame Summary:")
    print(f"  • Total numbers called: {len(game.called_numbers)}")
    if game.winner_name:
        print(f"  • Grand Prize Winner: {game.winner_name} 🏆")
    print("\nWe hope you enjoyed the game!")
    print("="*70)


def main_loop():
    """Main game loop with replay option"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            play_game_session()
            
            
            while True:
                replay = input("\n\n🎮 Do you want to play again? (yes/no): ").strip().lower()
                if replay in ['yes', 'y']:
                    break
                elif replay in ['no', 'n']:
                    print("\n" + "="*70)
                    print(" " * 15 + "👋 THANKS FOR PLAYING TAMBOLA! 👋")
                    print("="*70 + "\n")
                    return
                else:
                    print("❌ Please enter 'yes' or 'no'.")
        
        elif choice == "2":
            display_instructions()
            input("\nPress Enter to return to menu...")
        
        elif choice == "3":
            print("\n" + "="*70)
            print(" " * 15 + "👋 THANKS FOR VISITING! SEE YOU SOON! 👋")
            print("="*70 + "\n")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main_loop()
