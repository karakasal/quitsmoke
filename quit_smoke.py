#----------
# https://www.webmd.com/smoking-cessation/what-happens-body-quit-smoking
#----------

import datetime

q_start = datetime.datetime(year=2024, month=9, day=3, hour=2, minute=36)
current_time = datetime.datetime.now()
q_time = (current_time-q_start).total_seconds()
q_minutes, q_hours, q_days = abs(int(q_time // 60)), abs(int(q_time // 3600)), abs(int(q_time // 86400))

phase_one = 20
phase_two = 8
phase_three = 12
phase_four = 24
phase_five = 2
phase_six = 3
phase_seven = 14
phase_eight = 90
phase_nine = 365
phase_ten = phase_nine *5
phase_eleven = phase_nine *10
phase_twelve = phase_nine *15


if q_time>0:
    print(f'{int(phase_one - q_minutes)} minutes left for phase one.') if int(phase_one - q_minutes)>0 else print('''20 Minutes - In less time than it takes to watch a sitcom, your body’s already getting better. After 20 minutes, your pulse and blood pressure start to drop back to normal. And your hands and feet warm up to their usual temperature.\n''')
    print(f'{int(phase_two - q_hours)} hours left for phase two.') if int(phase_two - q_hours)>0 else print('''8 Hours - By the end of a work day, you have half the amount of nicotine and carbon monoxide in your blood. Why does that matter? Carbon monoxide is a chemical in cigarettes, and it crowds out oxygen in your blood. That causes problems from your muscles to your brain because they don’t get the oxygen they need.
But as the chemical’s levels drop, your oxygen gets back to normal.
On the flip side, it’s likely you already feel some early cravings and doubts. That’s normal. But they usually last just 5-10 minutes. To get you through, try to find ways to distract yourself until the feeling passes. You could try making a craving playlist, chewing gum, or sipping water.\n''')
    print(f'{int(phase_three - q_hours)} hours left for phase three.') if int(phase_three - q_hours)>0 else print('''12 Hours - Halfway through your first day, your carbon monoxide level is back to normal. And your heart will thank you. Now it doesn’t have to pump so hard to try to get enough oxygen to your body.\n''')
    print(f'{int(phase_four - q_hours)} hours left for phase four.') if int(phase_four - q_hours)>0 else print('''24 Hours - If you smoke a pack a day, you’re twice as likely to have a heart attack as a nonsmoker. But go one full day without a cigarette, and you’ve lowered your chances. That’s huge.\n''')
    print(f'{int(phase_five - q_days)} days left for phase five.') if int(phase_five - q_days)>0 else print('''48 Hours - With 2 days down, treat yourself to something tasty. By this point, your senses of taste and smell get sharper as your nerve endings start to heal.
Your body’s also busy with a lot of cleanup. Your lungs kick out mucus and other gunk left from cigarettes. And you don’t have any more nicotine in your body.
This is also about the time when the toughest withdrawal symptoms show up. You might feel anxious, dizzy, hungry, or tired. You might get headaches or feel bored or depressed. It’s normal, but it also makes it a lot harder to keep from lighting up.\n''')
    print(f'{int(phase_six - q_days)} days left for phase six.') if int(phase_six - q_days)>0 else print('''3 Days - By the end of day 3, you breathe easier and have more energy. Your lungs start to recover and will keep getting better.\n''')
    print(f'{int(phase_seven - q_days)} days left for phase seven.') if int(phase_seven - q_days)>0 else print('''2 Weeks - 3 Months - During this time, you make huge strides. You can do more because your lungs are stronger and clearer, and your blood flow has improved. You can exercise without getting as winded. And your risk of a heart attack goes down even more.
You’ve also made it through the hardest part of withdrawal.
Even so, you’ll probably still get cravings. Everyone has different triggers for wanting to smoke. You can’t stop all of them, but you can stick to your plan. Ask for help if you need it. Think about the money you’re saving. Or try 10 deep breaths, nice and slow.\n''')
    print(f'{int(phase_eight - q_days)} days left for phase eight.') if int(phase_eight - q_days)>0 else print('''3-9 Months - At this point, you can take deeper, clearer breaths. Instead of hacking, you cough in a helpful way that actually clears things out. That helps you get fewer colds and other illnesses.
You’ll also have more energy.\n''')
    print(f'{int(phase_nine - q_days)} days left for phase nine.') if int(phase_nine - q_days)>0 else print('''1 Year - At the end of year 1, treat yourself. You’ve reached a milestone. And your risk of heart disease is now half of what it was a year ago.\n''')
    print(f'{int(phase_ten - q_days)} days left for phase ten.') if int(phase_ten - q_days)>0 else print('''5 Years - Your chances of a stroke and cervical cancer are now the same as a nonsmoker. And compared to when you first quit, you’re half as likely to get cancer of the mouth, throat, esophagus, or bladder.\n''')
    print(f'{int(phase_eleven - q_days)} days left for phase eleven.') if int(phase_eleven - q_days)>0 else print('''10 Years - Compared to someone who still smokes, you’re now half as likely to die from lung cancer. And the chances you’ll get cancer of the larynx (voice box) and pancreas both drop.\n''')
    print(f'{int(phase_twelve - q_days)} days left for phase twelve.') if int(phase_twelve - q_days)>0 else print('''15 Years - Finally, after 15 years of not smoking, the chances that you’ll get heart disease are the same as if you never smoked. Your body has done a ton of recovery and healing.
When you start out, it seems like a long road. But at 15 years, the headaches and discomfort of those first few weeks are a hazy memory. They can seem unbearable at the time, but you can get through it. The rewards are very real and clear.\n''')

else:
    print(f'{q_minutes} minutes to start!')