// https://www.geeksforgeeks.org/generating-random-numbers-in-java/
import java.util.Random;
public class Magic8 {
	public static void main(String[] args) {
		System.out.println("Hello Stranger,");
		System.out.println("I see you want to find the answer to your question...");
		System.out.println("... but 100 and 100 questions swirl in your head. ");
		System.out.println("Dont't be shy, choose one: ");

		// https://www.geeksforgeeks.org/ways-to-read-input-from-console-in-java/
		// get user input:
    String myQuestion = "Hidden";
    try {
		myQuestion = System.console().readLine();
    } catch(Exception e) {
        System.out.println("Oups... this environment does not support user input. Please think a question.");
    }
		System.out.println("Hmm... Give me a minute...");

		// generate random int (0-19):
    Random rand = new Random(); 
		int replyIndex = rand.nextInt(20);

		// reply dataset:
		String[] replies = {
			"It is certain.",
			"It is decidedly so.",
			"Without a doubt.",
			"Yes – definitely",
			"You may rely on it.",
			"As I see it, yes.",
			"Most likely.",
			"Outlook good.",
			"Yes.",
			"Signs point to yes.",
			"Reply hazy, try again.",
			"Ask again later.",
			"Better not tell you now.",
			"Cannot predict now.",
			"Concentrate and ask again.",
			"Don't count on it.",
			"My reply is no.",
			"My sources say no.",
			"Outlook not so good.",
			"Very doubtful."
		};

		System.out.println("Here is my answer to your question: ");
		System.out.println(myQuestion);
		System.out.println(replies[replyIndex]);
  	}
}