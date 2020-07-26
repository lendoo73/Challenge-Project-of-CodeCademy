const prompt = require('prompt-sync')({sigint: true});

const hat = '^';
const hole = 'O';
const fieldCharacter = '░';
const pathCharacter = '*';
// https://stackoverflow.com/questions/9781218/how-to-change-node-jss-console-font-color
// Note %s is where in the string (the second argument) gets injected. \x1b[0m resets the terminal color so it doesn't continue to be the chosen color anymore after this point.
const yellow = "\x1b[33m%s\x1b[0m";
const bgRed = "\x1b[41m%s\x1b[0m";
const fgRed = "\x1b[31m%s\x1b[0m";

const clearConsole = () => {
  process.stdout.write("\033c");
};

class Field {
  constructor(field, randonStart = false, hardMode = false) {
    this.field = field;
    this.playerY = 0;
    this.playerX = 0;
    this.message = "";
    if (randonStart) this.setRandomStart();
    this.hardMode =hardMode;
  }
  setRandomStart() {
    let done = false,
      y, x;
    this.field[0][0] = fieldCharacter;
    do {
      y = Field.randY(this.field.length);
      x = Field.randX(this.field[0].length);
      if (this.field[y][x] === fieldCharacter) {
        this.playerY = y;
        this.playerX = x;
        this.field[y][x] = pathCharacter;
        done = true;
      }
    } while(!(done));
  }

  print() {
    // print field to the console:
    clearConsole();
    this.field.forEach(row => {
      //console.log(row.join().replace(/,/g, ""));
      let colors = "";
      row.forEach(char => {
        if (char === fieldCharacter) {
          colors += "\x1b[42m%s";
        } else if (char === hole) {
          colors += "\x1b[42\x1b[40m%s";
        } else if (char === hat) {
          colors += "\x1b[43m%s";
        } else colors += "\x1b[31m%s";
        colors += "\x1b[0m";
      });

      console.log(colors, ...row);
    });
    this.getInput();
  }

  getInput() {
    console.log(yellow, this.message);
    const userInput = prompt("Wich way? ").toLowerCase();
    // handle userInput:
    switch (userInput) {
      case "u":
        this.playerY --;
        this.checkStatus();
        break;
      case "d":
        this.playerY ++;
        this.checkStatus();
        break;
      case "l":
        this.playerX --;
        this.checkStatus();
        break;
      case "r":
        this.playerX ++;
        this.checkStatus();
        break;
      default:
        this.message = 'Invalid input. Please press u: up, d: down, r: right or l: left...';
        this.print();
        break;
    }
  }

  checkStatus() {
    const maxY = this.field.length;
    const maxX = this.field[0].length;
    // check coords:
    if (
      (this.playerY < 0 || this.playerY >= maxY) ||
      (this.playerX < 0 || this.playerX >= maxX)
    ) return this.endGame("out");
    // coordinates are valid, check the field:
    const currField = this.field[this.playerY][this.playerX];
    // check holes:
    if (currField === hole) return this.endGame("hole");
    // check if find the hat:
    if (currField === hat) return this.endGame("hat");

    // refresh the field with the player moving:
    this.field[this.playerY][this.playerX] = "*";
    if (this.hardMode) {
      this.createHole();
    }
    this.print();
  }

  createHole() {
    let done = false;
    do {
      let y = Field.randY(this.field.length);
      let x = Field.randX(this.field[0].length);
      if (this.field[y][x] === fieldCharacter) {
        this.field[y][x] = hole;
        done = true;
      }
    } while(!(done));
  }

  endGame(reason) {
    switch(reason) {
      case "out":
        this.message = "You are run out from the field.";
        break;
      case "hole":
        this.message = "You are falling in a hole.";
        break;
      case "hat":
        this.message = `
Congratulation! You find your hat!
`;
        break;
    }
    let bg;
    if (this.message.match("Congratulation")) {
      bg = "\x1b[42m%s\x1b[0m";
    } else bg = "\x1b[41m%s\x1b[0m";
    console.log(bg, this.message);
    console.log("\x1b[31m%s\x1b[0m", "GAME OVER");
  }

  static randNumber(min, max) {
    return Math.floor(Math.random() * (max + 1 - min)) + min;
  }

  static randX(width) {
    return Field.randNumber(0, width - 1);
  }
  
  static randY(height) {
    return Field.randNumber(0, height - 1);
  }

  static generateField(height, width, holes = 10) {
    const numsOfHoles = Math.floor((height * width - 2) * holes / 100);
    const result = [];
    let hatDone = false,
      hatX,
      hatY,
      holeX,
      holeY,
      holesDone = 0;

    // create empty field:
    if (holes > 90 || holes < 0) holes = 10;
    for (let y = 0; y < height; y ++) {
      const row = [];
      for (let x = 0; x < width; x ++) {
        row.push(fieldCharacter);
      }
      result.push(row);
    }
    
    // set player position:
    result[0][0] = "*";
    
    // set hat position:
    do {
      hatY = Field.randY(height);
      hatX = Field.randX(width);
      if (hatY !== 0 && hatX !== 0) hatDone = true;
    } while (!(hatDone));
    result[hatY][hatX] = hat;

    // set hole's positions:
    do {
      holeY = Field.randY(height);
      holeX = Field.randX(width);
      if (result[holeY][holeX] === fieldCharacter) {
        result[holeY][holeX] = hole;
        holesDone ++;
      }
    } while(holesDone < numsOfHoles);

    return result;
  }
}
/*
const myField = new Field([
  ["*", "░", "O"],
  ["░", "O", "░"],
  ["░", "^", "░"]
]);

myField.print();
*/
const field = Field.generateField(15, 15, 25);
const randField = new Field(field, true, true);
randField.print();

/*
Reset = "\x1b[0m"
Bright = "\x1b[1m"
Dim = "\x1b[2m"
Underscore = "\x1b[4m"
Blink = "\x1b[5m"
Reverse = "\x1b[7m"
Hidden = "\x1b[8m"

FgBlack = "\x1b[30m"
FgRed = "\x1b[31m"
FgGreen = "\x1b[32m"
FgYellow = "\x1b[33m"
FgBlue = "\x1b[34m"
FgMagenta = "\x1b[35m"
FgCyan = "\x1b[36m"
FgWhite = "\x1b[37m"

BgBlack = "\x1b[40m"
BgRed = "\x1b[41m"
BgGreen = "\x1b[42m"
BgYellow = "\x1b[43m"
BgBlue = "\x1b[44m"
BgMagenta = "\x1b[45m"
BgCyan = "\x1b[46m"
BgWhite = "\x1b[47m"
*/ 
