from gtts import gTTS

mytext = """
English for Beginners is a 6-week elementary ESL course, corresponding to level A2 on the CEFR scale. English for Beginners is an integrated skills program. The development of language skills and grammatical and lexical resources will enable students to engage in daily conversations about a variety  of topics . Their listening and reading comprehension and spoken  and written  communication of main  ideas and details will also  be enhanced . Students will have the opportunity to expand and improve all language skills in academic contexts that relate to their interests. Assessments  include module quizzes  and task completion. Students who complete this mastery -based course will receive a certificate of completion.
"""

tts = gTTS(text=mytext, lang='en', tld='ca')

tts.save("output.mp3")


