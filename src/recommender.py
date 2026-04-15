from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = []

        for song in self.songs:
            score = 0

            if song.genre.lower() == user.favorite_genre.lower():
                score += 2.0

            if song.mood.lower() == user.favorite_mood.lower():
                score += 1.0

            energy_score = 1 - abs(song.energy - user.target_energy)
            score += energy_score

            if user.likes_acoustic:
                score += song.acousticness

            scored.append((song, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return [s[0] for s in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("genre match")

        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("mood match")

        energy_score = 1 - abs(song.energy - user.target_energy)
        reasons.append(f"energy similarity ({energy_score:.2f})")

        if user.likes_acoustic:
            reasons.append("acoustic preference match")

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file."""
    songs = []

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # safe conversions (fixes your crash)
            row["energy"] = float(row.get("energy") or 0)
            row["tempo_bpm"] = float(row.get("tempo_bpm") or 0)
            row["valence"] = float(row.get("valence") or 0)
            row["danceability"] = float(row.get("danceability") or 0)
            row["acousticness"] = float(row.get("acousticness") or 0)

            songs.append(row)

    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences."""
    score = 0
    reasons = []

    # safe string handling
    song_genre = (song.get("genre") or "").lower()
    song_mood = (song.get("mood") or "").lower()

    user_genre = (user_prefs.get("genre") or "").lower()
    user_mood = (user_prefs.get("mood") or "").lower()

    if song_genre == user_genre:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song_mood == user_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    # safe numeric handling
    song_energy = float(song.get("energy") or 0)
    user_energy = float(user_prefs.get("energy") or 0)

    energy_diff = abs(song_energy - user_energy)
    energy_score = 1 - energy_diff
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    song_tempo = float(song.get("tempo_bpm") or 0)
    user_tempo = float(user_prefs.get("tempo_bpm") or 0)

    tempo_diff = abs(song_tempo - user_tempo) / 200
    tempo_score = 1 - tempo_diff
    score += tempo_score
    reasons.append(f"tempo similarity (+{tempo_score:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return top k songs ranked by match score."""
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)

    return scored_songs[:k]