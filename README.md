# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Each song includes features such as genre, mood, energy, tempo, and acousticness. A user profile stores preferred genre and mood, target energy, and acoustic preference. The recommender will score songs by rewarding genre and mood matches and energy similarity, then rank them and return the highest-scoring songs.


Algorithm Recipe:
Score = Genre + Mood + Energy 
Genre: 0 or 2 
Mood: 0 or 1 
Energy: 1.0 - abs(song energy - user's target energy)


Potential Biases:
Genre matches are worth twice as much as mood matches, so the system may over-prioritize a user's favorite genre and overlook songs that fit their mood or energy better.



---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:


```
Top Recommendations                                         
========================================         
1. Sunrise City                                                                  
   Final score: 3.98                      
   Reasons:                                               
     - genre match (+2.0)                            
     - mood match (+1.0)                                                         
     - energy similarity (+0.98)
----------------------------------------
2. Gym Hero
   Final score: 2.87
   Reasons:
     - genre match (+2.0)
     - mood mismatch (+0.0)
     - energy similarity (+0.87)
----------------------------------------
3. Rooftop Lights
   Final score: 1.96
   Reasons:
     - genre mismatch (+0.0)
     - mood match (+1.0)
     - energy similarity (+0.96)
----------------------------------------
4. Night Drive Loop
   Final score: 0.95
   Reasons:
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy similarity (+0.95)
----------------------------------------
5. Storm Runner
   Final score: 0.89
   Reasons:
     - genre mismatch (+0.0)
     - mood mismatch (+0.0)
     - energy similarity (+0.89)
----------------------------------------
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

I ran the recommender with several profiles, including conflicting preferences, no matching genre or mood, energy targets at both ends of the 0–1 scale, and an out-of-range energy target. Results below show the top five songs for each profile.

| Profile | Top five recommendations (score) |
|---|---|
| Rock, sad, energy 0.9 | Storm Runner (2.99), Gym Hero (0.97), Sunrise City (0.92), Rooftop Lights (0.86), Night Drive Loop (0.85) |
| Pop, chill, energy 0.9 | Gym Hero (2.97), Sunrise City (2.92), Midnight Coding (1.52), Library Rain (1.45), Spacewalk Thoughts (1.38) |
| Ambient, intense, energy 0.2 | Spacewalk Thoughts (2.92), Storm Runner (1.29), Gym Hero (1.27), Library Rain (0.85), Coffee Shop Stories (0.83) |
| No matching genre or mood, energy 0.5 | Midnight Coding (0.92), Focus Flow (0.90), Coffee Shop Stories (0.87), Library Rain (0.85), Spacewalk Thoughts (0.78) |
| Lofi, chill, energy 0.0 | Library Rain (3.65), Midnight Coding (3.58), Focus Flow (2.60), Spacewalk Thoughts (1.72), Coffee Shop Stories (0.63) |
| Lofi, chill, energy 1.0 | Midnight Coding (3.42), Library Rain (3.35), Focus Flow (2.40), Spacewalk Thoughts (1.28), Gym Hero (0.93) |
| Pop, happy, energy 1.5 (out of range) | Sunrise City (3.32), Gym Hero (2.43), Rooftop Lights (1.26), Storm Runner (0.41), Night Drive Loop (0.25) |

The tests showed that when genre and mood do not match, energy similarity alone determines the ranking. With conflicting preferences, the 2-point genre match can outweigh a mood match. At the two energy extremes, the same lofi/chill songs remain near the top because their genre and mood matches contribute three points, while their order shifts with energy similarity. An out-of-range energy target still produces scores, but it is not a meaningful 0–1 preference and should be validated. I did not test changing the genre weight or adding tempo or valence to the scoring formula.



## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


