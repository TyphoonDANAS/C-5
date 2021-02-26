const math = require('mathjs');
const algebra = require('algebra.js');

var Equation = algebra.Equation;

const Discord = require('discord.js');
const { prefix, token } = require('./config.json');
const client = new Discord.Client();

client.once('ready', () => {
    console.log('Ready!')
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

            else if (message.content==("도움 계산")){

                message.channel.send(
                    "1. 지수는 ^로 표기하세요.(예: 2^3)\n" +
                    "2. 루트(제곱근)은 sqrt(n)으로 표기하세요.(예: sqrt(144))" +
                    "3. 변수가 숫자가 아닐 때에는 x나 y를 사용해야 합니다.\n" +
                    "4. 로그(log)는 log(n)으로 표기하세요.(예: log(100))\n" +
                    "5. 오일러 상수(자연로그의 밑)은 e로 표기하세요.(예: 5e)\n" +
                    "6. 기타: π는 pi로(예: 2*pi) 표기하세요.(ln은 지원하지 않습니다)" 
                );
            }

            else {

                var answer = math.evaluate(equation);
                message.channel.send({embed: {
					color: 0xff6060,
					title: "DANAX 계산기",
					description: "계산한 값: " + answer
					}});

            }
        }

    }

    catch (err) {
        console.error(err);
        message.channel.send("올바르지 않은 값입니다.");
    }



})


client.login(token);