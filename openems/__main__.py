"""OpenEMS CLI."""
import json

import click

from . import api


@click.group()
@click.pass_context
@click.option('--server-url', default='ws://192.168.2.79:80/websocket')
@click.option('--username', default='x')
@click.option('--password', default='owner')
def openems_cli(ctx, server_url, username, password):
    """OpenEMS CLI."""  # noqa: D403
    client = api.OpenEMSAPIClient(server_url, username, password)
    ctx.obj = {
        'client': client,
    }


@openems_cli.command()
@click.pass_context
def get_edge_list(ctx):
    """Get OpenEMS Edge List."""
    edges = ctx.obj['client'].get_edges()
    for edge in edges:
        click.echo(click.style(edge['id'], fg='green'))


@openems_cli.command()
@click.pass_context
@click.argument('edge-id')
def get_edge_config(ctx, edge_id):
    """Get OpenEMS Edge Config."""
    edge_config = ctx.obj['client'].get_edge_config('edge' + edge_id)

    click.echo(click.style(json.dumps(edge_config, indent=2), fg='green'))


@openems_cli.command()
@click.pass_context
@click.argument('edge-id')
def get_component_list(ctx, edge_id):
    """Get OpenEMS component List."""
    edge_config = ctx.obj['client'].get_edge_config('edge' + edge_id)
    for (key, values) in edge_config['components'].items():
      click.echo(click.style(f'{key}', fg='green'))


@openems_cli.command()
@click.pass_context
@click.argument('edge-id')
@click.argument('component-id')
def get_component_config(ctx, edge_id, component_id):
    """Get OpenEMS EdgeConfig for named component."""
    edge_config = ctx.obj['client'].get_edge_config('edge' + edge_id)
    for (key, values) in edge_config['components'].items():
#      print (k)
      if key == component_id:
#        for channel in values.get('properties', []):
        click.echo(click.style(f'{values}', fg='green'))


@openems_cli.command()
@click.pass_context
@click.argument('edge-id')
@click.argument('component-id')
#@click.argument('name')
#@click.argument('value')
@click.argument('name-value', nargs=-1)
def update_component_config(ctx, edge_id, component_id, name_value):
    """Update OpenEMS Component Config."""
    properties = []
    for pair in name_value:
      pair_list = pair.split("=")
      properties.append({'name' : pair_list[0], 'value' : pair_list[1]})
    print(properties)
    r = ctx.obj['client'].update_component_config('edge' + edge_id, component_id, properties)
    click.echo(click.style(f'{r}', fg='green'))


if __name__ == '__main__':
    openems_cli(auto_envvar_prefix='OPENEMS_CLI')
