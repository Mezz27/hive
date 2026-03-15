from .agent import run_real_time
from .config import DEFAULT_POLL_INTERVAL_SECONDS


if __name__ == "__main__":
    try:
        run_real_time(DEFAULT_POLL_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nAgent stopped by user.")