from google import genai

client = genai.Client(api_key="AIzaSyCTSkQsY2MCYudgvqZ6bQfQFkdgHCFCkkQ")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=""""একটি সদ্য নির্মিত বাংলা গানের জন্য একটি স্ট্যান্ডার্ড প্রম্পট তৈরি করুন। এই প্রম্পটটি এমনভাবে তৈরি করতে হবে, যাতে অন্য কোনো ব্যক্তি বা এ.আই. এই গানটির বৈশিষ্ট্যগুলো অনুসরণ করে একটি নতুন গান তৈরি করতে পারে। প্রম্পট তৈরির সময় নিম্নলিখিত বিষয়গুলো বিস্তারিতভাবে উল্লেখ করুন:

১. বিষয় (Theme): গানটির মূল বিষয়বস্তু কী? এটি কি প্রেম, প্রকৃতি, বিরহ, দেশাত্মবোধ, আধ্যাত্মিকতা, নাকি অন্য কোনো সামাজিক বা রাজনৈতিক বার্তা বহন করে? গানটির মূল বক্তব্য কয়েকটি বাক্যে লিখুন।

২. সুর ও সঙ্গীত (Melody & Music):
* গানের সুরটি কেমন? (উদাহরণ: ক্লাসিক্যাল, ফোক, আধুনিক, রক, জ্যাজ ইত্যাদি)
* গানের টেম্পো (Tempo) কেমন? (উদাহরণ: দ্রুত, ধীর, মাঝারি)
* গানের মূল যন্ত্রানুষঙ্গ (Instrumentation) কী কী? (উদাহরণ: বাঁশি, তবলা, গিটার, পিয়ানো, বেহালা ইত্যাদি)
* গানের সুরের কাঠামো (Melodic Structure) কেমন? (উদাহরণ: সরল, জটিল, পুনরাবৃত্তিমূলক)

৩. ভাষা ও শৈলী (Language & Style):
* গানের ভাষা কোন ঘরানার? (উদাহরণ: সাধু, চলিত, আঞ্চলিক)
* গানের শব্দচয়নে কোনো বিশেষত্ব আছে কি? (উদাহরণ: উপমা, রূপক, অনুপ্রাস, চিত্রকল্প)
* গানের কাব্যিক গঠন কেমন? (উদাহরণ: স্তবক, অন্তরা, সঞ্চারী, আভোগ)
* গানের সার্বিক শৈলী (Overall Style) কেমন? (উদাহরণ: বাউল, কীর্তন, রবীন্দ্রসংগীত, আধুনিক বাংলা গান)

৪. আবেগ ও অনুভূতি (Emotion & Feeling):
* গানটি কোন ধরনের আবেগ প্রকাশ করে? (উদাহরণ: আনন্দ, বিষাদ, উত্তেজনা, শান্তি, ঘৃণা, ভয়)
* গানটি শ্রোতার মনে কী ধরনের অনুভূতি জাগাতে পারে বলে আপনি মনে করেন?
* গানের কথা ও সুর কীভাবে মিলিতভাবে আবেগ তৈরি করে?

৫. লক্ষ্য শ্রোতা (Target Audience):
* এই গানটি কোন ধরনের শ্রোতাদের জন্য তৈরি করা হয়েছে? (উদাহরণ: তরুণ প্রজন্ম, বয়স্ক শ্রোতা, বিশেষ কোনো অঞ্চলের মানুষ)
* শ্রোতাদের বয়স, রুচি এবং সামাজিক প্রেক্ষাপট বিবেচনা করুন।

৬. অতিরিক্ত তথ্য (Additional Information):
* গানটির কোনো ঐতিহাসিক বা সাংস্কৃতিক তাৎপর্য আছে কি?
* গানটি লেখার পেছনের অনুপ্রেরণা কী ছিল?
* গানের কোনো বিশেষ অংশ (যেমন মুখরা বা অন্তরা) বিশেষভাবে উল্লেখযোগ্য কেন?

এই তথ্যগুলো ব্যবহার করে এমন একটি প্রম্পট তৈরি করুন, যা অন্য কেউ ব্যবহার করে আপনার গানের মতো একটি নতুন গান তৈরি করতে পারবে। প্রম্পটটি স্পষ্ট, সংক্ষিপ্ত এবং তথ্যপূর্ণ হতে হবে।"
    """,
)

print(response.text)




































