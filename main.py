import discord
from discord.ext import commands
from discord import app_commands

SELECT_OPTIONS = [
    discord.SelectOption(
        label="PA - 1", value="1", description="Periodic Assessment 1", emoji="📝"
    ),
    discord.SelectOption(
        label="PA - 2", value="2", description="Periodic Assessment 2", emoji="📝"
    ),
    discord.SelectOption(
        label="HALF YEARLY", value="3", description="Half Yearly", emoji="📝"
    ),
    discord.SelectOption(
        label="PA - 3", value="4", description="Periodic Assessment 3", emoji="📝"
    ),
    discord.SelectOption(label="FINALS", value="5", description="Annuals", emoji="📝"),
]


class Client(commands.Bot):

    async def on_ready(self):
        print(f"Logged on as {self.user}!")

        try:
            guild = discord.Object(id=1152174166385111040)
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")
        except Exception as e:
            print(f"error syncing commands: {e}")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.lower().startswith("hello"):
            await message.channel.send(f"Hi there {message.author}")


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
    embed = discord.Embed(
        title="this is a title",
        url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        description="this is the description",
        color=discord.Colour.teal(),
    )
    embed.set_thumbnail(
        url="https://letsenhance.io/static/73136da51c245e80edc6ccfe44888a99/1015f/MainBefore.jpg"
    )
    embed.add_field(name="bleh bleh", value="bleh bleh bleh")
    embed.add_field(name="yada yada", value="bleh fleh bleh")
    embed.set_footer(text="terms and conditions applied")
    embed.set_author(name=interaction.user.name)
    await interaction.response.send_message(embed=embed)


class View(discord.ui.View):
    @discord.ui.button(
        label="ritvik has a skill issue", style=discord.ButtonStyle.danger, emoji="🗿"
    )
    async def button_callback(self, button, interaction):
        await button.response.send_message(f"yes")


@client.tree.command(name="buttons", description="displaying a button", guild=GUILD_ID)
async def button(interaction: discord.Interaction):
    await interaction.response.send_message(view=View())


class Dropdown(discord.ui.View):
    answer1 = None

    @discord.ui.select(
        placeholder="Select a category", options=SELECT_OPTIONS, max_values=1
    )
    async def select_option_callback(
        self, interaction: discord.Interaction, select: discord.ui.Select
    ):
        self.answer1 = select.values
        exam_data = {
            "1": {
                "title": "PA-1 Exams",
                "color": discord.Colour.dark_teal(),
                "fields": [
                    ("Science", "28th April"),
                    ("Social Science", "5th May"),
                    ("II Language", "13th May"),
                    ("Mathematics", "19th May"),
                    ("English", "23rd May"),
                    ("AI", "26th May"),
                ],
            },
            "2": {
                "title": "PA-2 Exams",
                "color": discord.Colour.purple(),
                "fields": [
                    ("Science", "14th July"),
                    ("Social Science", "21st July"),
                    ("II Language", "28th July"),
                    ("Mathematics", "4th August"),
                    ("English", "11th August"),
                    ("AI", "14th August"),
                ],
            },
            "3": {
                "title": "Half Yearly Exams",
                "color": discord.Colour.dark_magenta(),
                "fields": [
                    ("II Language", "2nd September"),
                    ("Mathematics", "4th September"),
                    ("Social Science", "8th September"),
                    ("English", "10th September"),
                    ("Science", "12th September"),
                    ("AI", "15th September"),
                ],
            },
            "4": {
                "title": "PA-3 Exams",
                "color": discord.Colour.yellow(),
                "fields": [
                    ("Science", "13th October"),
                    ("Social Science", "17th October"),
                    ("II Language", "27th October (Rachit's birthday)"),
                    ("Mathematics", "30th October"),
                    ("English", "3rd November"),
                    ("AI", "10th November"),
                ],
            },
            "5": {
                "title": "Annual Exams",
                "color": discord.Colour.dark_blue(),
                "fields": [
                    ("Social Science", "2nd February"),
                    ("II Language", "4th February"),
                    ("Mathematics", "6th February"),
                    ("English", "9th February"),
                    ("Science", "11th February"),
                    ("AI", "13th February"),
                ],
            },
        }
        if select.values[0] not in ["1", "2", "3", "4", "5"]:
            await interaction.response.send_message(
                f"Invalid option: {select.values[0]}"
            )
        embed = discord.Embed(
            title=exam_data[select.values[0]]["title"],
            description="",
            color=exam_data[select.values[0]]["color"],
        )
        for field in exam_data[select.values[0]]["fields"]:
            embed.add_field(name=field[0], value=field[1])
        embed.set_footer(text="terms and conditions applied")
        embed.set_author(name=interaction.user.name)
        await interaction.response.send_message(embed=embed)


@client.tree.command(name="exams", description="List dates for exams", guild=GUILD_ID)
async def button(interaction: discord.Interaction):
    await interaction.response.send_message(view=Dropdown())


client.run("private info")
