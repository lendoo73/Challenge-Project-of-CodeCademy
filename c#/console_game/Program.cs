using System;

namespace ConsoleGame
{
    class Program
    {
        static void Main(string[] args)
        {
            Random rand = new Random();
            Console.CursorVisible = false;

            // Determine bounds and set starting positions
            int rows = Console.BufferHeight;
            int cols = Console.BufferWidth;
            char cursor = '<';
            int characterRow = rows / 2;
            int characterCol = cols / 2;
            char fruit = '@';
            int fruitRow = rand.Next(1, rows);
            int fruitCol = rand.Next(1, cols);
            int score = 0;

            // Code in this loop executes infinitely
            // unless Q or CTRL + C is pressed
            while (true)
            {
                // Draw score, character, and fruit
                Console.Clear();
                Console.SetCursorPosition(0, 0);
                Console.Write($"Score: {score}");
                Console.SetCursorPosition(characterCol, characterRow);
                Console.Write(cursor);
                Console.SetCursorPosition(fruitCol, fruitRow);
                Console.Write(fruit);

                // Capture user input
                ConsoleKeyInfo cki = Console.ReadKey(false);

                // End game if Q is pressed
                if (cki.Key == ConsoleKey.Q)
                {
                    Console.Clear();
                    Console.SetCursorPosition(0, 0);
                    Console.CursorVisible = true;
                    break; 
                }

                // Change character position based on key
                // Uses UpdatePosition()
                string key = cki.Key.ToString();
                int colChange = 0;
                int rowChange = 0;
                Game.UpdatePosition(key, out colChange, out rowChange);
                characterCol += colChange;
                characterRow += rowChange;

                // Update character symbol
                // Uses UpdateCursor()
                cursor = Game.UpdateCursor(key);

                // Keep character in bounds
                // Uses KeepInBounds()
                characterCol = Game.KeepInBounds(characterCol, cols);
                characterRow = Game.KeepInBounds(characterRow, rows);

                // Update score and fruit if player scored
                // Uses DidScore()
                if (Game.DidScore(characterCol, characterRow, fruitCol, fruitRow))
                {
                    score++;
                    fruitCol = rand.Next(cols);
                    fruitRow = rand.Next(rows);
                }
            }
        }
    }
}
