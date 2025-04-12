import discord
from discord.ext import commands
from discord import app_commands

SELECT_OPTIONS = [
    discord.SelectOption(label='PA - 1', value="1", description='Periodic Assessment 1', emoji='✅'),
    discord.SelectOption(label='PA - 2', value="2", description='work in progress', emoji='⚠️'),
    discord.SelectOption(label='HALF YEARLY', value="3", description='work in progress', emoji='⚠️'),
    discord.SelectOption(label='PA - 3', value="4", description='work in progress', emoji='⚠️'),
    discord.SelectOption(label='FINALS', value="5", description='work in progress', emoji='⚠️')
]


class Client(commands.Bot):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=1152174166385111040)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'error syncing commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1152174166385111040)


@client.tree.command(name="hello", description="testing purposes", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")


@client.tree.command(name="printer", description="print text", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(f'the message was "{printer}"')


@client.tree.command(name="embed", description="embed demo", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    embed = discord.Embed(title="this is a title", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                          description="this is the description", color=discord.Colour.teal())
    embed.set_thumbnail(url="https://letsenhance.io/static/73136da51c245e80edc6ccfe44888a99/1015f/MainBefore.jpg")
    embed.add_field(name='bleh bleh', value='bleh bleh bleh')
    embed.add_field(name='yada yada', value='bleh fleh bleh')
    embed.set_footer(text='terms and conditions applied')
    embed.set_author(name=interaction.user.name)
    await interaction.response.send_message(embed=embed)


class View(discord.ui.View):
    @discord.ui.button(label="ritvik has a skill issue", style=discord.ButtonStyle.danger, emoji="🗿")
    async def button_callback(self, button, interaction):
        await button.response.send_message(f'yes')


@client.tree.command(name="buttons", description="displaying a button", guild=GUILD_ID)
async def button(interaction: discord.Interaction):
    await interaction.response.send_message(view=View())


class Dropdown(discord.ui.View):
    answer1 = None

    @discord.ui.select(placeholder='Select a category', options=SELECT_OPTIONS, max_values=1)
    async def select_option_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.answer1 = select.values
        if select.values == ['1']:
            embed = discord.Embed(title='PA-1 Exams', description='', color=discord.Colour.dark_teal())
            embed.add_field(name='Science', value='28th April')
            embed.add_field(name='Social Science', value='5th May')
            embed.add_field(name='II Language', value='13th May')
            embed.add_field(name='Mathematics', value='19th May')
            embed.add_field(name='English', value='23rd May')
            embed.add_field(name='AI', value='26th May')
            embed.set_footer(text='terms and conditions applied')
            embed.set_author(name=interaction.user.name)
            await interaction.response.send_message(embed=embed)

        elif select.values == ['2']:
            embed = discord.Embed(title='PA-2 Exams', description='', color=discord.Colour.red())
            embed.add_field(name='Science', value='14th July')
            embed.add_field(name='Social Science', value='21st July')
            embed.add_field(name='II Language', value='28th July')
            embed.add_field(name='Mathematics', value='4th August')
            embed.add_field(name='English', value='11th August')
            embed.add_field(name='AI', value='14th August')
            embed.set_footer(text='terms and conditions applied')
            embed.set_author(name=interaction.user.name)
            await interaction.response.send_message(embed=embed)

        elif select.values == ['3']:
            embed = discord.Embed(title='Half Yearly Exams', description='', color=discord.Colour.red())
            embed.add_field(name='II Language', value='2nd September')
            embed.add_field(name='Mathematics', value='4th September')
            embed.add_field(name='Social Science', value='8th September')
            embed.add_field(name='English', value='10th September')
            embed.add_field(name='Science', value='12th September')
            embed.add_field(name='AI', value='15th September')
            embed.set_footer(text='terms and conditions applied')
            embed.set_author(name=interaction.user.name)
            await interaction.response.send_message(embed=embed)

        elif select.values == ['4']:
            embed = discord.Embed(title='PA-3 Exams', description='', color=discord.Colour.red())
            embed.add_field(name='Science', value='13th October')
            embed.add_field(name='Social Science', value='17th October')
            embed.add_field(name='II Language', value='27th October(rachits bday)')
            embed.add_field(name='Mathematics', value='30th October')
            embed.add_field(name='English', value='3rd November')
            embed.add_field(name='AI', value='10th November')
            embed.set_footer(text='terms and conditions applied')
            embed.set_author(name=interaction.user.name)
            await interaction.response.send_message(embed=embed)

        elif select.values == ['5']:
            embed = discord.Embed(title='Annual Exams', description='', color=discord.Colour.red())
            embed.add_field(name='Social Science', value='2nd February')
            embed.add_field(name='II Language', value='4th February')
            embed.add_field(name='Mathematics', value='6th February')
            embed.add_field(name='English', value='9th February')
            embed.add_field(name='Science', value='11th February')
            embed.add_field(name='AI', value='13th February')
            embed.set_footer(text='terms and conditions applied')
            embed.set_author(name=interaction.user.name)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message('error')
            print(select.values)
        pass


@client.tree.command(name="exams", description="List dates for exams", guild=GUILD_ID)
async def button(interaction: discord.Interaction):
    await interaction.response.send_message(view=Dropdown())


client.run('secret stuff')
