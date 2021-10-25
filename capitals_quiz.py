import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quiznum in range(35):
    quefile=open('capitalsquiz%s.txt'%(quiznum+1),'w')
    ansfile=open('capitalsquiz_answers%s.txt'%(quiznum+1),'w')
    quefile.write('Name\nUsn\nDate\n\n')
    states=list(capitals.keys())
    random.shuffle(states)
    for quenum in range(50):
        correctans=capitals[states[quenum]]
        wrongans=list(capitals.values())
        del wrongans[wrongans.index(correctans)]
        wrongans=random.sample(wrongans,3)
        ansopt=wrongans+[correctans]
        random.shuffle(ansopt)
        quefile.write('%s. What is capital of %s?'%((quenum+1),states[quenum]))
        for i in range(4):
            quefile.write('%s. %s\n'%('ABCD'[i],ansopt[i]))
        ansfile.write('%s. %s\n'%(str(quenum+1),'ABCD'[ansopt.index(correctans)]))
    quefile.close()
    ansfile.close()
