#   Readability is an application that computes the approximate grade level needed to comprehend some text.
class ColemanLiauFormula():

    def __init__(self, text):
        self.text = text

    def LetterCount(self):

        """
            Counting the number of letters in the text
        """
        count = 0

        #   Counting the number of letters in the text
        for i in self.text:
            if str(i).isalpha():
                count += 1

        return count

    def WordCount(self):
        count = 0

        #   Counting the number of words in the self.text
        for i in str(self.text).split():
            count += 1

        return count

    def SentenceCount(self):
        count = 0
        sep = [".", "!", "?"]

        #   Counting the number of sentences in the text
        for i in str(self.text):
            if i in sep:
                count += 1

        return count

    def ColemanLiauFormula(self):

        #   Calculate the number of letters, words, and sentences
        l,w,s = self.LetterCount(), self.WordCount(), self.SentenceCount()

        #   Calculates the average number of letters and sentences per 100 words
        CLF = lambda a, b : (a / b) * 100
        cli = round((0.0588 *CLF(l,w)) - ( 0.296 * CLF(s,w)) - 15.8)

        #   Ensure that the grade level is not below 1 and Returns the grade level
        if cli < 1:
            return "Before Grade 1"
        
        #   Ensure that the grade level is not Above 15 and Returns the grade level
        elif cli > 15:
            return "Grade 16+"
        
        #   Returns the grade level
        else:
            return f"Grade {cli}"

def main():

    #   Returns the grade level
    readability = ColemanLiauFormula(input("Calculate Sentence: "))
    return print(readability.ColemanLiauFormula())

if __name__ == "__main__":
    main()
