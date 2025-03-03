import logging
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional

from Organism import Organism

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def simulate_organism_life(organism: Organism) -> Optional[Organism]:
    """
    Simulate organism life
    :return:
    """
    evolution_parts_number = 3
    while evolution_parts_number:
        organism.feed()
        new_organism = organism.reproduce()
        if new_organism:
            return new_organism
        evolution_parts_number -= 1
        time.sleep(1)


def run_evolution_simulation() -> None:
    """
    Run evolution simulation
    :return:
    """
    initial_population = [Organism(random.randint(1, 10)) for _ in range(5)]
    new_population = []
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(simulate_organism_life, org): org for org in initial_population}
        for future in as_completed(futures):
            result = future.result()
            if result:
                new_population.append(result)
    logging.info(f"New organism population count: {len(new_population)}")


if __name__ == "__main__":
    run_evolution_simulation()
