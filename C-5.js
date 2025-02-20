const Discord = require('discord.js');
const client = new Discord.Client();
const math = require('mathjs');
const algebra = require('algebra.js');
const Hangul = require('hangul-js');

var Equation = algebra.Equation;

const { prefix, token } = require('./config.json');


client.on('ready', () => {
	console.log('봇이 켜졌습니다.')
})

client.on('message', (message) => {
	if(message.channel.type == 'dm') return
	
	if(message.content.includes("샌즈")) {
		message.channel.send('***와!!!!!!!!!!!!!!!!섽으!!!!!!!!!!!***')
	}
})

function calcSplit(str) {
    return str.split(`${prefix}계산`)[1];
}


client.on('message', message => {

    try {

        if (message.content.startsWith(`${prefix}계산`)) {

            var equation = calcSplit(message.content);

            var eString = "테스트";

            eString = equation.toString();


            if (message.content.includes('x') && message.content.includes('y') && message.content.includes('=')) {

                var expr1 = algebra.parse(eString.substring(0, equation.indexOf('=')));
                var expr2 = algebra.parse(equation.split('=')[1]);

                var eq = new Equation(expr1, expr2);

                var tempX = eq.solveFor('x');
                var tempY = eq.solveFor('y');

                var answerX = tempX.toString();
                var answerY = tempY.toString();

                message.channel.send("x = " + answerX + ", y = " + answerY);


            }

            else if (message.content.includes('x') == true && message.content.includes('y') == false && message.content.includes('=') == true) {

                var expr1 = algebra.parse(eString.substring(0, equation.indexOf('=')));
                var expr2 = algebra.parse(equation.split('=')[1]);

                var eq = new Equation(expr1, expr2);

                var temp = eq.solveFor('x');

                var answer = temp.toString();

                message.channel.send("x = " + answer);

            }

            else if (message.content.includes('y') == true && message.content.includes('x') == false && message.content.includes('=') == true) {

                var expr1 = algebra.parse(eString.substring(0, equation.indexOf('=')));
                var expr2 = algebra.parse(equation.split('=')[1]);

                var eq = new Equation(expr1, expr2);

                var temp = eq.solveFor('y');

                var answer = temp.toString();

                message.channel.send("y = " + answer);

            }

            /*else if (message.content==("도움 계산")){

                message.channel.send(
                    "1. 지수는 ^로 표기하세요.(예: 2^3)\n" +
                    "2. 루트(제곱근)은 sqrt(n)으로 표기하세요.(예: sqrt(144))" +
                    "3. 변수가 숫자가 아닐 때에는 x나 y를 사용해야 합니다.\n" +
                    "4. 로그(log)는 log(n)으로 표기하세요.(예: log(100))\n" +
                    "5. 오일러 상수(자연로그의 밑)은 e로 표기하세요.(예: 5e)\n" +
                    "6. 기타: π는 pi로(예: 2*pi) 표기하세요.(ln은 지원하지 않습니다)" 
                );
            }*/

            else {

                var answer = math.evaluate(equation);
                message.channel.send({embed: {
					color: 0xff6060,
					title: "C-5 계산기",
					description: "계산한 값: " + answer
					}});

            }
        }

    }

    catch (err) {
        console.error(err);
        message.channel.send("올바르지 않은 값입니다.");
    }

});

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
            if(x == 'ㅒ') return 'ㅞ';
            if(x == 'ㅓ') return 'ㅜ';
            if(x == 'ㅕ') return 'ㅘ';
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