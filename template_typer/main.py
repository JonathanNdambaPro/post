import module.others as others
import module.users as users
import typer

app = typer.Typer()
app.add_typer(users.app, name="users", help="Manage users in the app.")
app.add_typer(others.app, name="others", help="Manage users in the app.")

if __name__ == "__main__":
    app()
