#!/usr/bin/env python3
import click


@click.group()
def cli():
    """TAPIO Command-Line Interface"""
    pass


@cli.command()
def start():
    """Start TAPIO daemon."""
    print("Starting TAPIO...")


@cli.command()
@click.argument("pet")
@click.option("--message", help="Message to speak")
def speak(pet, message):
    """Make a pet say something."""
    print(f"{pet} says: {message}")


if __name__ == "__main__":
    cli()
