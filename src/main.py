"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = {
        "High Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.9,
        "tempo_bpm": 120
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.3,
        "tempo_bpm": 70
    },
    "Intense Rock": {
        "genre": "rock",
        "mood": "angry",
        "energy": 0.95,
        "tempo_bpm": 140
    },
    "Edge Case": {
        "genre": "pop",
        "mood": "sad",
        "energy": 0.9,
        "tempo_bpm": 60
    }
}

    for name, user_prefs in profiles.items():
        print(f"\n===== {name} =====\n")
        recommendations = recommend_songs(user_prefs, songs, k=5)

    for song, score, explanation in recommendations:
        print(f"{song.get('title', 'Unknown')} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print("-" * 40)


if __name__ == "__main__":
    main()
