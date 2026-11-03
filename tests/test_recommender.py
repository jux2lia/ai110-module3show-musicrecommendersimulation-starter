from src.recommender import Song, UserProfile, Recommender, load_songs, score_song, recommend_songs

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_load_songs_converts_numeric_values(tmp_path):
    csv_path = tmp_path / "songs.csv"
    csv_path.write_text(
        "id,title,artist,genre,mood,energy,tempo_bpm,valence,danceability,acousticness\n"
        "1,Test Song,Test Artist,pop,happy,0.8,120,0.9,0.7,0.2\n",
        encoding="utf-8",
    )

    songs = load_songs(str(csv_path))

    assert len(songs) == 1
    song = songs[0]
    assert song["id"] == 1
    assert isinstance(song["id"], int)
    for field in ("energy", "tempo_bpm", "valence", "danceability", "acousticness"):
        assert isinstance(song[field], float)


def test_score_song_returns_score_and_explanation_reasons():
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    song = {"genre": "pop", "mood": "happy", "energy": 0.6}

    score, reasons = score_song(user_prefs, song)

    assert score == 3.8
    assert reasons == [
        "genre match (+2.0)",
        "mood match (+1.0)",
        "energy similarity (+0.80)",
    ]


def test_recommend_songs_returns_top_k_sorted_with_explanation():
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    songs = [
        {"title": "Low Match", "genre": "rock", "mood": "chill", "energy": 0.2},
        {"title": "Best Match", "genre": "pop", "mood": "happy", "energy": 0.8},
        {"title": "Genre Match", "genre": "pop", "mood": "chill", "energy": 0.7},
    ]

    recommendations = recommend_songs(user_prefs, songs, k=2)

    assert [song["title"] for song, _, _ in recommendations] == ["Best Match", "Genre Match"]
    assert [score for _, score, _ in recommendations] == [4.0, 2.9]
    assert "genre match (+2.0)" in recommendations[0][2]
    assert "energy similarity (+1.00)" in recommendations[0][2]
