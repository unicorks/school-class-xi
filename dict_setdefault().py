D = {'Name': 'Azra', 'Gender':'Male'}
D_Name = D.setdefault('Name', 'Name not available')
D_DOB = D.setdefault('DOB', 'DOB not available')
D_Gender = D.setdefault('Gender')
D_Mobile = D.setdefault('Mobile')
print('Name: ', D_Name)
print('DOB: ', D_DOB)
print('Gender: ', D_Gender)
print('Mobile: ', D_Mobile)
