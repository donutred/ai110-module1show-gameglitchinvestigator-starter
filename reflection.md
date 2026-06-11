# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input   | Expected Behavior | Actual Behavior | Console Output / Error |
|---------|-------------------|-----------------|------------------------|
| Guess   | Too High Hint     | Too Low Hint    | None                   |
| of 25   |                   |                 |                        |
|---------|-------------------|-----------------|------------------------|
| Press   | Starts a new game | Nothing happens | None                   |
| New Game|                   |                 |                        |
| Button  |                   |                 |                        |
|---------|-------------------|-----------------|------------------------|
| Guess of| Guess is submitted| Need to press   |   None                 |
|  50     |                   | submit button   |                        |
|         |                   | twice           |                        |
|---------|-------------------|-----------------|------------------------|


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude Haiku 4.5.

One AI suggestion that was correct was changing how the code handled finishing the game and starting a new game so that winning or losing the game did not stop the game, and instead allowed a new game to start.

One incorrect suggestion was that after attempting to fix the higher and lower bug, it incorrectly reported that it was fixed, when there was still a bug. This was fixed after changing the messages in the check guess function

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided if a bug was fixed by testing it using the pytest testcases and by expirmentally testing it in the game.

One test I ran was inputting a number lower than the secret number and seeing if it I was told that it was too low or too high. Based on the result I could tell if the hint was accurate to the actual secret number.

AI helped design a test by writing the code to test the reset game state function in the test_game_logic file.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Reruns reset the state of Streamlit to the state of a new session. The session state is a collection of all the variables being tracked in the session of Streamlit.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One strategy I would resuse, is creating tests whenever a bug is fixed to ensure that the fix actaully works.

One thing I would do differently is try to have ai work on more specific issues and tasks, so that it does not try to do to much at once which doesn't work as well and is harder to follow.

The project changed the way I think about AI generated code by showing me that it can be useful to fix bugs in projects.