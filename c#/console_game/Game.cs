using System;

namespace ConsoleGame {
    class Game : SuperGame {
        public new static void UpdatePosition(string keyPressed, out int coordX, out int coordY) {
            switch(keyPressed) {
                case "DownArrow":
                case "S":
                    coordX = 0;
                    coordY = 1; 
                    break;
                case "UpArrow":
                case "W":
                    coordX = 0;
                    coordY = -1; 
                    break;
                case "LeftArrow":
                case "A":
                    coordX = -1;
                    coordY = 0; 
                    break;
                case "RightArrow":
                case "D":
                    coordX = 1;
                    coordY = 0; 
                    break;
                default:
                    coordX = 0;
                    coordY = 0;
                    break;
            }
        }

        public new static char UpdateCursor(string keyPress) {
            switch(keyPress) {
                case "DownArrow":
                    return 'v';
                case "UpArrow":
                    return '^';
                case "LeftArrow":
                    return '<';
                case "RightArrow":
                    return '>';
                case "S":
                    return '\u23EC';
                case "W":
                    return '\u23EB';
                case "A":
                    return '\u23EA';
                case "D":
                    return '\u23E9';
                default:
                    return 'v';
            }
        }

        // maxValue is exclusive!!! 
        public new static int KeepInBounds(int coord, int maxValue) {
            return 
                /*
        coord < 0
          ? 0
        : coord >= maxValue
          ? maxValue - 1
        : coord;
        */
                coord < 0
                ? maxValue - 1
                : coord >= maxValue
                    ? 0
                    : coord;
        }

        public new static bool DidScore(int xCurrent, int yCurrent, int xFruit, int yFruit) {
            bool isXEqual = xCurrent == xFruit;
            bool isYEqual = yCurrent == yFruit;
            return isXEqual && isYEqual;
        }
    }
}