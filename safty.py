import random
import time

class SafetyMeasures:
    @staticmethod
    def human_like_delay(min_seconds: float = 2, max_seconds: float = 8):
        """Add random delays to mimic human behavior"""
        delay = random.uniform(min_seconds, max_seconds)
        time.sleep(delay)

    @staticmethod
    def randomize_actions(actions: list):
        """Randomize the order of actions"""
        random.shuffle(actions)
        return actions

    @staticmethod
    def get_user_agent():
        """Get random user agent"""
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        ]
        return random.choice(user_agents)

# Example usage with safety measures
safety = SafetyMeasures()
safety.human_like_delay()