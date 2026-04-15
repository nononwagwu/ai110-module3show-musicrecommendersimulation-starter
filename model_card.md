# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  
The system relies heavily on a small set of features, especially energy and genre, which can lead to repetitive recommendations. Songs with similar energy levels are often ranked highly even if they differ in mood or genre.

The dataset is small and may not represent diverse musical tastes, which limits recommendation quality. Additionally, the system does not adapt over time or learn from user feedback, making it less personalized compared to real-world systems.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  
I tested the recommender using multiple user profiles: High Energy Pop, Chill Lofi, Intense Rock, and an Edge Case with conflicting preferences. 

The system generally behaved as expected. High energy profiles produced faster and more intense songs, while chill profiles resulted in slower, calmer recommendations. 

However, some songs appeared across multiple profiles, suggesting that energy similarity has a strong influence on ranking. The edge case profile showed that when preferences conflict, the system tends to prioritize numerical features like energy over categorical ones like mood.

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this recommender showed how simple rules and weights can turn user preferences into ranked recommendations. I learned that even basic features like genre, mood, and energy can produce reasonable results when combined with a scoring system.

One key insight was how strongly certain features, especially energy, influence the output. In some cases, songs with similar energy appeared across different user profiles, even when the mood or genre did not fully match. This showed how easily a model can become biased toward specific features.

This project also made it clear that real recommendation systems are much more complex. Human judgment still matters because users may value context, lyrics, or personal meaning in music—things this model cannot capture.
