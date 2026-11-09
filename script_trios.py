import csv
from collections import defaultdict
import io
import sys

def check_squads_from_stdin(max_players=3):
    while True:
        print("\n📋 Paste the table (TSV) below.")
        print("Finish with an EMPTY line. Type 'q' + empty line to exit.")

        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line.strip() == "":
                break
            if line.strip().lower() == "q":
            
                return
            lines.append(line)

        if not lines:
            print("No data. Please insert the table and finish with an empty line.")
            continue 

        csv_text = "\n".join(lines)
        reader = csv.DictReader(io.StringIO(csv_text), delimiter='\t')
        rows = list(reader)

        if not rows:
            print("Could not parse data. Make sure the first line contains headers (SquadID, Player, etc.).")
            continue

        squad_players = defaultdict(list)
        valid = True
        for row in rows:
            if 'SquadID' not in row or 'Player' not in row:
                print("❌ Incorrect data: missing SquadID or Player columns.")
                valid = False
                break
            squad_id = row['SquadID']
            player_name = row['Player']
            if player_name:
                squad_players[squad_id].append(player_name)

        if not valid:
            continue

        has_overflow = False
        for squad_id, players in squad_players.items():
            if len(players) > max_players:
                has_overflow = True
                print(f"\n SquadID = {squad_id} is full: {len(players)} players (limit {max_players})")
                print("  participants:")
                for p in players:
                    print(f"    - {p}")

        if not has_overflow:
            print(f"\n Everything OK ({max_players} max players).")

if __name__ == '__main__':
    check_squads_from_stdin()
