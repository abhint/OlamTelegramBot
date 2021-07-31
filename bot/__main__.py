from .olambot import OlamBot
import logging

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.FileHandler(
                        'log.txt'), logging.StreamHandler()],
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                    )
LOGGER = logging.getLogger(__name__)
logging.getLogger("OlamBot").setLevel(logging.WARNING)

if __name__ == "__main__":
    OlamBot().run()
