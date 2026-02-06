from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
from app.events.call_window import call_app_window


# ----------------------
# CORE APPLICATION WINDOW CALL
# ----------------------
if __name__ == "__main__":
    call_app_window()