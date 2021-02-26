const Discord = require('discord.js');
const myIntents = new Discord.Intents(['GUILDS','GUILD_MESSAGES','GUILD_MEMBERS','GUILD_INVITES','GUILD_PRESENCES']);
const bot = new Discord.Client({ws:{intents:myIntents}});

bot.on ("ready", async () => {
	console.log('\nReady!\n');
});

bot.on("message", async message => {
	
	// Checks if the message author is not a bot and isn't sent in a DM channel
	if(message.author.bot) return;
	if(message.channel.type === "dm") return;
	
	let messageArray = message.content.split(" ");
	let command = messageArray[0];
	let args = messageArray.slice(1);
	let com = command.toLowerCase();
	var sender = message.author;

if(message.content.startsWith("^^유저 정보")) {
	// Checks if a user is mentioned
	let ment = message.mentions.users.first();
		if(!ment) {
			message.channel.send('유저를 멘션하세요.')
		}
	// Creats an embed with information about the mentioned user
		if (ment.presence.status === 'dnd') ment.presence.status = '다른 용무 중'
		if (ment.presence.status === 'idle') ment.presence.status = '자리 비움'
		if (ment.presence.status === 'offline') ment.presence.status = '오프라인'
		if (ment.presence.status === 'online') ment.presence.status = '온라인'
		
		let embed = new Discord.MessageEmbed()
		.setTitle("C-5 사용자 정보")
		.setColor("FF6060")
		.addField("닉네임", ment.tag)
		.addField("ID", ment.id)
		.addField("상태", ment.presence.status)
		.addField("생성일", ment.createdAt)
		.setImage(ment.avatarURL)
		message.channel.send(embed)
	// Displays a message in the console if the command was used
		return console.log(`> 유저 정보가 ${message.author.username} 에 의해 조회되었습니다.`);
	}

if(message.content.startsWith("^^서버 정보")) {
	let serverembed = new Discord.MessageEmbed()
	.setTitle("C-5 서버 정보")
	.setColor("FF6060")
	.setThumbnail(message.guild.iconURL)
	.addField('서버명', `${message.guild.name} (${message.guild.nameAcronym})`, true)
	.addField('서버장', message.guild.owner.user.tag, true)
	.addField("서버 생성일", message.guild.createdAt, true)
	.addField("멤버 수", message.guild.memberCount, true)
	message.channel.send(serverembed)
	return console.log(`> 서버 정보가 ${message.author.username} 에 의해 조회되었습니다.`);
}
});


bot.login("NTg5NDcxMDgxMzU0NDk0MDEy.XfJRWw.fMTsYTwslIRP_e88Kx7u5P3D_cg");