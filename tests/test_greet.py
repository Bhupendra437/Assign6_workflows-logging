from app.plugins.greet import GreetCommand

def test_greet_command(capsys):
    # Instantiate GreetCommand
    greet_command = GreetCommand()
    # Execute the command
    greet_command.execute(["World"])
    # Check if the correct greeting message is printed
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"

