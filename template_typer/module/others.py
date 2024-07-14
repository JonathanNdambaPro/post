import time
from datetime import datetime
from enum import StrEnum

import typer
from rich.progress import track
from typing_extensions import Annotated

app = typer.Typer()


@app.command("number")
def ckecker(
    id: Annotated[int, typer.Option(min=0, max=1000)],
    rank: Annotated[int, typer.Option(max=10, clamp=True)] = 0,
    score: Annotated[float, typer.Option(min=0, max=100, clamp=True)] = 0,
):
    print(f"ID is {id}")
    print(f"--rank is {rank}")
    print(f"--score is {score}")


@app.command()
def boolean_forcing(
    force: Annotated[bool, typer.Option("--force/--no-force", "-f/-F")] = False
):
    if force:
        print("Forcing operation")
    else:
        print("Not forcing")


@app.command()
def date_checker(birth: datetime):
    print(f"Interesting day to be born: {birth}")
    print(f"Birth hour: {birth.hour}")


class NeuralNetwork(StrEnum):
    SIMPLE = "simple_str"
    CONV = "conv_str"
    LSTM = "lstm_str"


@app.command()
def choice(network: NeuralNetwork = NeuralNetwork.SIMPLE):
    print(f"Training neural network of type: {network.SIMPLE}")


@app.command()
def main():
    total = 0
    for _ in track(range(100), description="Processing..."):
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")


if __name__ == "__main__":
    app()
