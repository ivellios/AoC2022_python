import importlib

import click

from utils import run_with_file


@click.command()
@click.option("--day", default="1", help="Day of the Advent")
@click.option(
    "--task", default="1", type=click.Choice(["1", "2"]), help="Number of the task"
)
def run(day, task):
    import_path = f"day{day}.day{day}_{task}"
    mod = importlib.import_module(import_path)
    fun = getattr(mod, f"run")

    click.echo(f"Running Day {day}, task {task}: ")

    if hasattr(fun, "no_file_wrapping") and fun.no_file_wrapping:
        fun(f"data/day{day}.txt")
        return

    ltr = fun.lines_to_read if hasattr(fun, "lines_to_read") else 1

    run_with_file(fun, f"data/day{day}.txt", lines_to_read=ltr)


if __name__ == "__main__":
    run()
