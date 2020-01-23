import discord
from discord.ext import commands

async def check_permissions(ctx, perms, *, check=all):
	return check(getattr(ctx.channelpermissions_for(ctx.author), name, None) == value for name, value in perms.items())
	
def has_permissions(*, check=all, **perms):
	async def pred(ctx):
		return await check_permissions(ctx, perms, check=check)
	return commands.check(pred)
	
def has_role(ctx, RoleID):
	Role = ctx.guild.get_role(RoleID)
	if Role in ctx.author.roles:
		return True
	else:
		return False

def can_send(ctx):
	return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).send_messages
	
def can_embed(ctx):
	return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).embed_links
	
def can_upload(ctx):
	return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).attach_files
	
def can_react(ctx):
	return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).add_reactions
	
def is_nsfw(ctx):
	return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.is_nsfw()