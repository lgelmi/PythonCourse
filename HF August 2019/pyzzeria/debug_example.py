"""
An example to show how to debug code
"""
import logging

from src.pyzzeria.magazzyno import Magazzyno
from src.pyzzeria.pyzzaiolo import Pyzzaiolo

if __name__ == "__main__":
    logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger("Pyzzeria")

    magazzyno = Magazzyno({"mozzarella": 10,
                           "pomodoro": 10,
                           "basilico": 5})
    pyzzaiolo = Pyzzaiolo(magazzyno)
    while True:
        # pdb.set_trace()
        pyzzaiolo.make_custom_pizza(["mozzarella", "pomodoro", "basilico"])