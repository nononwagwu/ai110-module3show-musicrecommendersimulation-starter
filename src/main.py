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

    # Starter example profile
    user_prefs = {
        "genre": "Afrobeats",
        "mood": "Happy",
        "energy": 0.8,
        "tempo_bpm": 100
}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")

    for song, score, explanation in recommendations:
        print(f"{song.get('title', 'Unknown')} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print("-" * 40)


if __name__ == "__main__":
    main()
