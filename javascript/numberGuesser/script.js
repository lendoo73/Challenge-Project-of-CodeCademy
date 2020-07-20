let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

// This function make a random number betveen the minimum  and maximum (include both):
const randNumber = (min, max) => Math.floor(Math.random() * (max + 1 - min)) + min;

const substract = (a, b) => a - b;

// return the number of absolute value:
const abs = num => num < 0 ? num * -1 : num;

// This function will be called at the start of each new round in order to generate the new secret target number.
// return a random integer between 0 and 9:
const generateTarget = () => randNumber(0, 9);

// This function will be called each round to determine which guess is closest to the target number:
const compareGuesses = (human, computer, target) => {
    const humanAccuracy = abs(substract(target, human));
    const computerAccuracy = abs(substract(target, computer));
    return humanAccuracy <= computerAccuracy
        ? true
    : false;
};

// This function will be used to correctly increase the winner’s score after each round:
const updateScore = winner => winner === "human" ? humanScore ++ : computerScore ++;

// This function will be used to update the round number after each round:
const advanceRound = () => currentRoundNumber ++;