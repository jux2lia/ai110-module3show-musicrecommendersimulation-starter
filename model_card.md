# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

This recommender suggests songs from a small catalog that may fit a user's favorite genre, favorite mood, and target energy level. It assumes the user can describe these preferences and that the song labels and energy values are accurate. It ranks matches rather than predicting with certainty whether someone will enjoy a song. It is intended for classroom exploration of how recommendation systems use data and scoring, not as a production service for real listeners.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

For each song, the system adds points when its genre or mood matches the user's preferences. A genre match is worth two points, a mood match is worth one point, and the song receives up to one more point for having energy close to the user's target. The system then ranks songs by their total points and recommends the highest-scoring ones. Each recommendation includes the reasons for its score.

---

## 4. Data  

The catalog contains 10 songs labeled with genre, mood, energy, tempo, valence, danceability, and acousticness. Its genres are pop, lofi, rock, ambient, jazz, synthwave, and indie pop; its moods are happy, chill, intense, relaxed, moody, and focused. I used the provided catalog without adding or removing songs. This small, labeled sample does not capture all musical styles or personal taste, and it lacks information such as lyrics, language, cultural context, and an individual listener's history.

---

## 5. Strengths  

The recommender works best for users who can specify a genre, mood, and energy level that are represented in the catalog; for example, the pop/happy, energy 0.8 profile ranked “Sunrise City” first. Its results also make sense when preferences are only partial matches, because the explanations show how genre, mood, and energy each contributed to a song's ranking.

---

## 6. Limitations and Bias 

In my experiments, the system sometimes prioritized genre over mood because a genre match is worth two points while a mood match is worth one. For example, with a pop/chill profile and high target energy, the top two results were pop songs that did not match the requested chill mood, while chill lofi songs ranked lower. This could make recommendations feel less personal for users whose mood matters more than genre. The system also ignores features such as lyrics and tempo, and its small catalog may not represent the full range of genres and moods.

---

## 7. Evaluation  

I tested profiles with conflicting preferences (such as pop and chill), unmatched genre and mood, different target energy levels, and an energy value outside the expected 0–1 range. I checked that the top five were sorted by score and that the explanations reflected genre, mood, and energy contributions. The genre weight often pushed matching-genre songs above songs that matched mood, while profiles with no genre or mood matches were ranked by energy similarity alone.
---

## 8. Future Work  

I would add listener preferences for features such as tempo and acousticness, and validate inputs like energy so out-of-range values are handled clearly. I would also improve recommendation diversity by avoiding a top list dominated by one genre and explain the score contributions in a more user-friendly way.

---

## 9. Personal Reflection  

I learned that a recommender uses the scores and information we give it to decide what to suggest. Now I understand that music apps make choices like this too, and their recommendations depend on how they are designed.
