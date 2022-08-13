import os,time
path=os.path.dirname(__file__)+"/App_data/"

tt=int(input('Enter ur choice- 1 for WEEK_TT, 2 for SAT_TT, 3 for SUN_TT, 1111 to update database: '))
if tt==1:
	from App_data import WeekTripsData,WeekKmData
	d=WeekTripsData.weektrips
	d1=WeekKmData.weekkms
	file=open(path+'WeekSignOnOff.txt','r'); SignOnOff=file.readlines(); file.close()
	dutyno=int(input('enter WEEK duty no: '))
	dutyname='WEEK'+str(dutyno)+'  '+SignOnOff[dutyno-1].split('\t')[1]+'/'+SignOnOff[dutyno-1].split('\t')[2]+\
	' - '+SignOnOff[dutyno-1].split('\t')[3]+'/'+SignOnOff[dutyno-1].split('\t')[4]+'-'+'\n'
elif tt==2:
	from App_data import SatTripsData,SatKmData
	d=SatTripsData.sattrips
	d1=SatKmData.satkms
	file=open(path+'SatSignOnOff.txt','r'); SignOnOff=file.readlines(); file.close()
	dutyno=int(input('enter SAT duty no: '))
	dutyname='SAT'+str(dutyno)+'  '+SignOnOff[dutyno-1].split('\t')[1]+'/'+SignOnOff[dutyno-1].split('\t')[2]+\
	' - '+SignOnOff[dutyno-1].split('\t')[3]+'/'+SignOnOff[dutyno-1].split('\t')[4]+'-'+'\n'
elif tt==3:
	from App_data import SunTripsData,SunKmData
	d=SunTripsData.suntrips
	d1=SunKmData.sunkms
	file=open(path+'SunSignOnOff.txt','r'); SignOnOff=file.readlines(); file.close()
	dutyno=int(input('enter SUN duty no: '))
	dutyname='SUN'+str(dutyno)+'  '+SignOnOff[dutyno-1].split('\t')[1]+'/'+SignOnOff[dutyno-1].split('\t')[2]+\
	' - '+SignOnOff[dutyno-1].split('\t')[3]+'/'+SignOnOff[dutyno-1].split('\t')[4]+'-'+'\n'
elif tt==1111:
	import urllib.request 
	c=int(input('Enter 1 to update WeekData, 2 to update SatData, 3 to update SunData: '))
	print('Updating databse, please wait...')
	if c==1:
		try:		
			link= "https://drive.google.com/uc?id=1yFSfYm5Bx6w1hOGwAmQc_pfgWiZtsDTa&export=download"
			request_url = urllib.request.urlopen(link)
			f=open(path+'WeekTripsData.py','w') 
			f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
			f.close()
			link= "https://drive.google.com/uc?id=1V9rOUSyuQrYxisnqANZRHtx0NI_64r53&export=download"
			request_url = urllib.request.urlopen(link)
			f=open(path+'WeekKmData.py','w') 
			f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
			f.close()
			link= "https://drive.google.com/uc?id=1PCup_pbVkgyVKKtukOnpIVOTISlLkQwk&export=download"
			request_url = urllib.request.urlopen(link)
			f=open(path+'WeekSignOnOff.txt','w') 
			f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
			f.close()
		except:
			input('Could not connect to database, check your connection, press enter to exit')
			quit()
	elif c==2:
		try:
			link= "https://drive.google.com/uc?id=12Oq6aR0PDcrxkzDyzsF-4rnztT-GZIXa&export=download"
			request_url = urllib.request.urlopen(link)
			f=open(path+'SatTripsData.py','w') 
			f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
			f.close()
			link= "https://drive.google.com/uc?id=1q1UrR7KSmPOm5dbc1WhKv_U8ac2eVGxM&export=download"
			request_url = urllib.request.urlopen(link)
			f=open(path+'SatKmData.py','w') 
			f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
			f.close()
			link= "https://drive.google.com/uc?id=1QXo-jApdcRcWHO_mCB7JGdEuqavzMIiZ&export=download"
			request_url = urllib.request.urlopen(link)
			f=open(path+'SatSignOnOff.txt','w') 
			f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
			f.close()
		except:
			input('Could not connect to database, check your connection, press enter to exit')
			quit()
	elif c==3:
		try:
			link= "https://drive.google.com/uc?id=1HGevb4belecQqfqoBGAxA2SSQtkrpV77&export=download"
			request_url = urllib.request.urlopen(link)
			f=open(path+'SunTripsData.py','w') 
			f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
			f.close()
			link= "https://drive.google.com/uc?id=12nXAUGA6eU78DEdmJeFEL4oBnMpkGYFG&export=download"
			request_url = urllib.request.urlopen(link)
			f=open(path+'SunKmData.py','w') 
			f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
			f.close()
			link= "https://drive.google.com/uc?id=1D2-bZu57jFaEKawssR75m3u2QmK_tosc&export=download"
			request_url = urllib.request.urlopen(link)
			f=open(path+'SunSignOnOff.txt','w') 
			f.write(request_url.read().decode('utf-8').replace('\r\n','\n'))
			f.close()
		except:
			input('Could not connect to database, check your connection, press enter to exit')
			quit()
	else:
		input('Wrong choice, Press enter to exit')
		quit()
	
	input('Database successfully updated, Press enter to exit')
	quit()
else:
	input('Wrong choice, Press enter to exit')
	quit()

print('')
trips=''
for i in range(len(d[dutyno])):
	trips=trips+d[dutyno][i][0]+'    '+d[dutyno][i][1]+'    '+d[dutyno][i][2]+'\n'
	if d[dutyno][i][0]=="Deboard":
		trips=trips+'-'+'\n'
trips=trips+'KM: '+str(d1[dutyno])+'\n'
print(dutyname+trips)

# import pyperclip
# pyperclip.copy(dutyname+trips)

input('Press enter to exit')

# import androidhelper
# droid=androidhelper.Android()
# print('Data also copied in clip')
# droid.setClipboard(str(time.strftime('%d/%m/%Y'))+' Duty Data\n\n'+dutyname+trips)
