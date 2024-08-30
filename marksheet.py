def mark(**m):
    print('MARKSHEET')
    print('English: ',m['a'])
    print('Hindi: ',m['b'])
    print('Maths: ',m['c'])
    print('Science: ',m['d'])
    print('Marathi: ',m['e'])
    print('Total Marks: 500')
    print('Marks Obtained: ',m['a']+m['b']+m['c']+m['d']+m['e'])
    print('Percentage: ',(m['a']+m['b']+m['c']+m['d']+m['e'])/5,'%')
mark(a=96 , b=90 , c=95 , d=96 , e=93)    

