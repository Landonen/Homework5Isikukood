
user_input = None
while True:
    if not user_input: # not проверяет если выражение возвращает False. То приложение запускается
        ######################################################################################################
        while True:
            user_input = input('Enter ID: ')
            try:
                int(user_input)
                if len(user_input) != 11:
                    raise UserWarning
            except ValueError:
                print('Code is not numeric')
            except UserWarning:
                if len(user_input) > 11:
                    print('Code is too long')
                else:
                    print('Code is too short')
            else:
                print(user_input)
                break
        ######################################################################################################
    user_choice = input('Please choose:\n'
                        '1.Get gender\n' 
                        '2.Get date of birth\n'
                        '3.Get region of birth\n'
                        '4.Validate ID\n'
                        '5.Change ID\n'
                        '0.Exit\n'
                        '--> ')
    if user_choice == '1': # input - строка поэтому '1'
        if int(user_input[0]) in range(1, 9):
            if int(user_input[0]) % 2 == 0:
                print('Female')
            else:
                print('Male')
        else:
            print('Can\'t determmine gender')
    elif user_choice == '2': # dd.mm.yyyy
        if user_input[0] in ['1', '2']:
            bcent = '18'
        elif user_input[0] in ['3', '4']:
            bcent = '19'
        elif user_input[0] in ['5', '6']:
            bcent = '20'
        elif user_input[0] in ['7', '8']:
            bcent = '21'
        else:
            bcent = None
        print(f'You were born in {user_input[5:7]}.{user_input[3:5]}.{bcent}{user_input[1:3]}')
    elif user_choice == '3':
        if int(user_input[7:10]) in range(1, 10):
            area = 'in Kuressaare haigla'
        elif int(user_input[7:10]) in range(11, 19):
            area = 'in Tartu Ülikooli Naistekliinik'
        elif int(user_input[7:10]) in range(21, 150):
            area = 'in Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
        elif int(user_input[7:10]) in range(151, 160):
            area = 'in Keila haigla'
        elif int(user_input[7:10]) in range(161, 220):
            area = 'in Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
        elif int(user_input[7:10]) in range(221, 270):
            area = 'in Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
        elif int(user_input[7:10]) in range(271, 370):
            area = 'in Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
        elif int(user_input[7:10]) in range(371, 420):
            area = 'in Narva Haigla'
        elif int(user_input[7:10]) in range(421, 470):
            area = 'in Pärnu haigla'
        elif int(user_input[7:10]) in range(471, 490):
            area = 'in Haapsalu haigla'
        elif int(user_input[7:10]) in range(491, 520):
            area = 'in Järvamaa haigla (Paide)'
        elif int(user_input[7:10]) in range(521, 570):
            area = 'in Rakvere haigla, Tapa haigla'
        elif int(user_input[7:10]) in range(571, 600):
            area = 'in Valga haigla'
        elif int(user_input[7:10]) in range(601, 650):
            area = 'in Viljandi haigla'
        elif int(user_input[7:10]) in range(651, 700):
            area = 'in Lõuna-Eesti haigla (Võru), Põlva haigla'
        else:
            area = 'not in Estonia'
        print(f'You were born {area}')
    elif user_choice == '4':
        pass
    elif user_choice == '5':
        user_input = None
    elif user_choice == '0':
        print('Good bye')
        break
    else:
        print('Choice is out of range!')