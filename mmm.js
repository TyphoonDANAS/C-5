const Discord = require('discord.js');
const client = new Discord.Client();
const Hangul = require('hangul-js');
const {
	prefix,
	token,
} = require('./config.json');


client.on('ready', () => {
	console.log('봇이 켜졌습니다.')
})

client.on('message', (message) => {
	var args = message.content.split(/ +/).slice(1);
	const input = args.join(' ');
	
	if(message.channel.type == 'dm') return
	
	if(message.content.startsWith("^^멈뭄미")) {
		
		function mmm(x){
			if(x == 'ㅇ') return 'ㅁ';
			return x;
		}
		
		message.channel.send(Hangul.a(Hangul.d(input).map(mmm)))
};
		
	if(message.content.startsWith("^^엉엉이")) {
		
		function mmm(x){
			if(x == 'ㅁ') return 'ㅇ';
			return x;
		}
		
		message.channel.send(Hangul.a(Hangul.d(input).map(mmm)))
};

	if(message.content.startsWith("^^병든앵무새")) {
		
		function mmm(x){
			if(x == 'ㄱ') return 'ㄹ';
			if(x == 'ㄴ') return 'ㅋ';
			if(x == 'ㄲ') return 'ㅉ';
			if(x == 'ㅥ') return 'ㆀ';
			if(x == 'ㄷ') return 'ㄴ';
			if(x == 'ㄸ') return 'ㅃ';
			if(x == 'ㄹ') return 'ㅍ';
			if(x == 'ㅁ') return 'ㅊ';
			if(x == 'ㅂ') return 'ㅈ';
			if(x == 'ㅅ') return 'ㅎ';
			if(x == 'ㅆ') return 'ㄲ';
			if(x == 'ㅇ') return 'ㄱ';
			if(x == 'ㅈ') return 'ㄷ';
			if(x == 'ㅉ') return 'ㅆ';
			if(x == 'ㅊ') return 'ㅁ';
			if(x == 'ㅋ') return 'ㅌ';
			if(x == 'ㅌ') return 'ㅂ';
			if(x == 'ㅍ') return 'ㅅ';
			if(x == 'ㅎ') return 'ㅇ';
			if(x == 'ㅏ') return 'ㅡ';
			if(x == 'ㅑ') return 'ㅝ';
			if(x == 'ㅐ') return 'ㅢ';
			return x;
		}
		
		message.channel.send(Hangul.a(Hangul.d(input).map(mmm)))
};

	if(message.content.startsWith("^^도리스탕스")) {
		
		function mmm(x){
			if(x == '도리') return '볶음';
			return x;
		}
		
		message.channel.send(Hangul.a(Hangul.d(input).map(mmm)))
};

	if(message.content.startsWith("^^메호")) {
		
		function mmm(x){
			if(x == 'ㅎ' && x == 'ㅗ') return '메';
			return x;
		}
		
		message.channel.send(Hangul.a(Hangul.d(input).map(mmm)))
};
});

client.login(token);

	