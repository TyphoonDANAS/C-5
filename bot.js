const Discord = require('discord.js');
const client = new Discord.Client();
const Token = 'NTg5NDcxMDgxMzU0NDk0MDEy.XfJRWw.fMTsYTwslIRP_e88Kx7u5P3D_cg'


client.on('ready', () => {
	console.log('봇이 켜졌습니다.')
})

client.on('message', (message) => {
	if(message.channel.type == 'dm') return
	
	if(message.content.includes("샌즈")) {
		message.channel.send('***와!!!!!!!!!!!!!!!!섽으!!!!!!!!!!!***')
	}
})

client.login(Token);