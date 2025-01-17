from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

import nltk
nltk.download('stopwords')
nltk.download('punkt')

stopwords = set(stopwords.words("english"))

text = """Are school uniforms necessary? In private school, uniforms are often the norm—but in 
public school most students have the option of wearing casual dress when they come to 
class. While uniforms may be restrictive and clash with personal preference, they 
actually do have some good points. For example, it’s one less thing that students have to 
worry about when they get ready for school in the morning. This paper will show why 
mandatory school uniforms can actually make life easier for students and schools.
First of all, school uniforms can help to eliminate the problem of peer pressure that 
students often face when trying to decide what they should wear. Considering the fact 
that not every student has money to spend on the latest trends in fashion, school uniforms 
offer a less expensive alternative that can eliminate the peer pressure that goes with 
having to dress according to the latest styles. Students can focus more on studies and less 
on trying to stand out, fit in, or be respected and admired based on the quality of their 
fashion statements. True, students who want to express themselves stylistically will have 
to find another way to assert themselves; however, for the majority of students, uniforms 
would be a welcome change as there is never a question of having to decide what to wear 
or fearing that one’s wardrobe isn’t good enough. Everyone is wearing the same thing!
Secondly, school uniforms can help to promote a more formal environment in the 
school. That means students are more likely to adhere to the rules and regulations of the 
school, as uniforms promote the concept of conformity and regularity—which is good for 
schools! Uniforms suggest that everyone is on the same page and everyone is expected 
to show up and do one’s duty. Uniforms encourage propriety, good form and good 
manners. Uniformed students are more likely to show respect for their teachers than 
students who are used to asserting themselves, demonstrating their own will and desire in 
their dress, and showing off.
Finally, school uniforms foster school spirit. They help students to identify themselves as 
members who owe allegiance to the school. They instill in students a sense of belonging 
and the knowledge that they themselves represent the school. By wearing a uniform that 
sports the logo or emblem of the school and the school’s colors, the students show that 
they are willing to reflect the values and mission of the school in their own person. In 
other words, uniforms help students to stifle their own self-centeredness and be part of 
something bigger than themselves.
In conclusion, school uniforms offer a lot of positive qualities. Students who wear the 
school uniform are less likely to face peer pressure about their fashion preferences than 
students who do not have a uniform and must pick out their own wardrobe on a daily 
basis. They are also more likely to respect authority and the rules of the school, and have 
school pride. School uniforms might not be to everyone’s taste, but the benefits of 
having them certainly cannot be denied."""

# Splitting text in words
words = word_tokenize(text)

# Counting the frequency of each word which is not a stopWord
wordFreq = dict()
for word in words:
    word = word.lower()
    if word in stopwords:
        continue
    if word in wordFreq:
        wordFreq[word] += 1
    else:
        wordFreq[word] = 1

# Sliptting text in sentences
sentences = sent_tokenize(text)

# Calculating importance of sentence => checking sentences with words which have high freqency
def getSentenceImp():
    sentImp = dict()
    for sentence in sentences:
        sentImp[sentence] = 0
        for word, freq in wordFreq.items():
            if word in sentence.lower():
                sentImp[sentence] += freq
            else:
                sentImp[sentence] = freq
    return sentImp

sentenceImportance = getSentenceImp()

# Calculating average of all the sentence importance in the dictonay
def getSentAvg():
    total = 0
    for sentence in sentenceImportance:
        total += sentenceImportance[sentence]
        avg = int(total / len(sentenceImportance))
    return avg

average = getSentAvg()

# Creating summary by sorting
summary = ''
for sentence in sentences:
    if (sentence in sentenceImportance) and (sentenceImportance[sentence] > 1 * average):
        summary += " " + sentence

print("\n\n", summary, "\n\n")