# gTTS requires an internet connection
from gtts import gTTS

mytext = """
Hi there! How's your day going?

Hi! It's going well, thanks. How about you?

Not too bad, just busy with work. Did you do anything fun over the weekend?

Yes, actually! I went hiking in the mountains. The weather was perfect for it. How about you?

That sounds great! I just relaxed at home and watched a couple of movies. Sometimes a quiet weekend is just what you need.

Absolutely, a little downtime is always nice. Have you seen any good movies lately?

I watched a new action movie that came out recently. It was pretty entertaining. Do you have any favorite genres?

I enjoy a bit of everything, but I'm particularly fond of comedies. They always put me in a good mood.

Same here! Have you heard about the new comedy show that just started?

Yes, I've heard some good things about it. Maybe I'll check it out this weekend.

You should! Well, I better get back to work, but it was nice chatting with you.

You too! Have a great rest of your day.

Thanks, you too!
"""

tts = gTTS(text=mytext, lang='en', tld='ca')

tts.save("output.mp3")


