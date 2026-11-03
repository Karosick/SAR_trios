import csv
from collections import defaultdict
import sys

def check_squads_from_stdin(max_players=3):
    print("📋Paste the table (TSV) into the terminal below.")
    print("when you are finished, press Ctrl+D\n")

    reader = csv.DictReader(sys.stdin, delimiter='\t')
    rows = list(reader)

    if not rows:
        print("❌ No data. Please insert the table and finish input (Ctrl+D).")
        return

    squad_players = defaultdict(list)
    for row in rows:
        if 'SquadID' not in row or 'Player' not in row:
            print("❌ incorect data")
            return
        squad_id = row['SquadID']
        player_name = row['Player']
        if player_name:
            squad_players[squad_id].append(player_name)

    has_overflow = False
    for squad_id, players in squad_players.items():
        if len(players) > max_players:
            has_overflow = True
            print(f"\n⚠️ team SquadID = {squad_id} fulled: {len(players)} players (limit {max_players})")
            print("  participants:")
            for p in players:
                print(f"    - {p}")

    if not has_overflow:
        print(f"\n✅ everything alr ({max_players} max players).")

if __name__ == '__main__':
    check_squads_from_stdin()