const DISCORD_API_WRAPPER = require("discord.js");
const FILE_SYSTEM = require("fs");
const DISCORD_CLIENT = new DISCORD_API_WRAPPER.Client();
const DISCORD_CLIENT_CONFIGURATIONS = require("./Config");
const Datetime = new Date()

DISCORD_CLIENT.on("message", (MESSAGE) => {require("./Utils/C_Handout")(DISCORD_CLIENT, MESSAGE)})

//Events

DISCORD_CLIENT.on("ready", () => {
    console.log("---------------------\nBOT_ONLINE: TRUE\n---------------------")
})

DISCORD_CLIENT.on("guildMemberAdd", (MEMBER) => {
    ROLE = MEMBER.guild.roles.get("650646165938765825")
    CHANNEL = MEMBER.guild.channels.get("655359276948389908")
    MEMBER.addRole(ROLE, "New user")
    const EMBED_ON_JOIN = new DISCORD_API_WRAPPER.RichEmbed()
        .setColor("#25c059")
        .setTitle(MEMBER.user.tag)
        .setDescription("Information on the user.")
        .addBlankField()
        .setAuthor(DISCORD_CLIENT.user.tag, DISCORD_CLIENT.user.avatarURL)
        .addField("Date Created: ",MEMBER.user.createdAt)
        .addField("Date Joined: ",MEMBER.joinedAt)
        .addField("Join Position: ", DISCORD_CLIENT.guilds.get(DISCORD_CLIENT_CONFIGURATIONS.IDs.matrix_server).memberCount - 1)
        .setTimestamp()
        .setImage(MEMBER.user.avatarURL);
    CHANNEL.send(EMBED_ON_JOIN)
})

DISCORD_CLIENT.on("raw", packet => {
    if (!["MESSAGE_REACTION_ADD"].includes(packet.t)) return;
    if(packet.d.channel_id == "655354957486227476") {
        if (packet.d.message_id == "655418147020734513") {
            if(packet.d.emoji.name == "✅"){
                const GUILD = DISCORD_CLIENT.guilds.get(DISCORD_CLIENT_CONFIGURATIONS.IDs.matrix_server)
                const MEMBER = GUILD.members.get(packet.d.user_id)
                MEMBER.addRole(GUILD.roles.get(DISCORD_CLIENT_CONFIGURATIONS.roles.followers))
                MEMBER.removeRole(GUILD.roles.get(DISCORD_CLIENT_CONFIGURATIONS.roles.null))
            }
            if(packet.d.emoji.name == "❌"){
                const GUILD = DISCORD_CLIENT.guilds.get(DISCORD_CLIENT_CONFIGURATIONS.IDs.matrix_server)
                const MEMBER = GUILD.members.get(packet.d.user_id)
                MEMBER.kick("Didn't agree.")
            }
        }
    }
})

DISCORD_CLIENT.login(DISCORD_CLIENT_CONFIGURATIONS.bot.token)