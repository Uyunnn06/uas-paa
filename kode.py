import random

def simulate_match(player1, player2):
    """Simulasi hasil pertandingan antara dua pemain."""
    return random.choice([player1, player2])

def brute_force(players):
    """Metode Brute Force: Penyusunan bagan pertandingan."""
    while len(players) > 1:
        next_round = []
        print("\nRonde Baru:")
        for i in range(0, len(players), 2):
            if i + 1 < len(players):
                print(f"{players[i]} vs {players[i+1]}")
                winner = simulate_match(players[i], players[i+1])
            else:
                winner = players[i]
                print(f"{players[i]} otomatis lolos.")
            print(f"Pemenang: {winner}")
            next_round.append(winner)
        players = next_round
    return players[0]

def divide_and_conquer(players):
    """Metode Divide and Conquer: Penyusunan bagan pertandingan."""
    if len(players) == 1:
        return players[0]
    mid = len(players) // 2
    left_winner = divide_and_conquer(players[:mid])
    right_winner = divide_and_conquer(players[mid:])
    print(f"{left_winner} vs {right_winner}")
    return simulate_match(left_winner, right_winner)

def main():
    players = ["Yuyun", "Alexa", "Mita", "Carren", "Aura", "Englin", "kerna", "ka Uli"] 
    print("Pilih Metode Penyusunan Bagan:")
    print("1. Brute Force")
    print("2. Divide and Conquer")

    choice = input("Masukkan pilihan (1/2): ").strip()
    if choice == "1":
        print("\n=== Metode Brute Force ===")
        print(f"Pemenang Final: {brute_force(players)}")
    elif choice == "2":
        print("\n=== Metode Divide and Conquer ===")
        print(f"Pemenang Final: {divide_and_conquer(players)}")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()