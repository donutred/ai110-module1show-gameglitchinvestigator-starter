def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        value = int(float(raw)) if "." in raw else int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    guess_int = int(guess)
    secret_int = int(secret)

    if guess_int == secret_int:
        return "Win", "🎉 Correct!"

    if guess_int > secret_int:
        return "Too High", "📉 Go LOWER"

    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome in {"Too High", "Too Low"}:
        return current_score - 5 if outcome == "Too Low" else current_score + 5

    return current_score


def reset_game_state():
    """Return a fresh playing state for a new game."""
    return {
        "attempts": 0,
        "score": 0,
        "status": "playing",
        "history": [],
    }