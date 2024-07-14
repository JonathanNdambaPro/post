from typing import List, Optional, Tuple

import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def docs(
    name: str,
    lastname: Annotated[
        str,
        typer.Option(
            help="The lastname of the user to greet",
            rich_help_panel="Secondary Arguments",
        ),
    ],
    formal: bool = False,
):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Ms. {name} {lastname}.")
    else:
        print(f"Hello {name} {lastname}")


@app.command()
def prompting(
    name: str,
    lastname: Annotated[
        str, typer.Option("--lastname", "-l", prompt="Please tell me your last name")
    ],
):
    print(f"Hello {name} {lastname}")


@app.command()
def delete_confirm(
    project_name: Annotated[str, typer.Option(prompt=True, confirmation_prompt=True)],
):
    print(f"Deleting project {project_name}")


@app.command("password")
def password_confirm_prompting(
    name: str,
    password: Annotated[
        str, typer.Option(prompt=True, confirmation_prompt=True, hide_input=True)
    ],
):
    print(f"Hello {name}. Doing something very secure with password.")
    print(f"...just kidding, here it is, very insecure: {password}")


@app.command("multi_str")
def multiple_argument_string(
    user: Annotated[Optional[List[str]], typer.Option()] = None
):
    if not user:
        print(f"No provided users (raw input = {user})")
        raise typer.Abort()
    for u in user:
        print(f"Processing user: {u}")


@app.command("multi_float")
def multiple_argument_float(number: Annotated[List[float], typer.Option()] = []):
    print(f"The sum is {sum(number)}")


@app.command("multi_limited_differ")
def multiple_argument_limited_and_differt(
    user: Annotated[Tuple[str, int, bool], typer.Option()] = (None, None, None)
):
    username, coins, is_wizard = user
    if not username:
        print("No user provided")
        raise typer.Abort()
    print(f"The username {username} has {coins} coins")
    if is_wizard:
        print("And this user is a wizard!")


@app.command("ask")
def asking():
    person_name = typer.prompt("What's your name?")
    print(f"Hello {person_name}")


@app.command()
def confirm_abort():
    _ = typer.confirm("Are you sure you want to delete it?", abort=True)
    print("Deleting it!")


if __name__ == "__main__":
    app()
