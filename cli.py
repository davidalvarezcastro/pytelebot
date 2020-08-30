from src.handler import send_message
import click


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def bot(ctx, debug):
    ctx.obj['DEBUG'] = debug


@bot.command()
@click.option('--message', default='Hey there!')
@click.pass_context
def send(ctx, message):
    """ Command to send a message

    Args:
      ctx (click.core.Context)
      message (str)
    Returns:
      None
    """
    send_message(message)


if __name__ == '__main__':
    bot(obj={})
