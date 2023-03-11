from os import system
opcionempanada = 1 

empanadas = []
    while opcionempanada != 0 :
        print('***Empanadas de la selva***');
        print('1.Ingresar una empanada');
        print('2.Mostrar todas las empanadas');
        print('3.Busque una empanada por ID');
        print('4.Editar una empanada');
        print('5.Eliminar una empanada por ID');
        print('0.Salir');
        print('********************************')

    opcionempanada=int(input('Escoger la Opcion :'));
    if(opcionempanada ==1):
        
        empanada = {}
        empanada['id']= int(input('Digite el id de la empanada'))
        empanada['nombre']= input('Digite el nombre de la empanada')
        empanada['precio']= float(input('Digite el precio de la empanada'))
        empanada['fechadevenciminto']= input('Digite popularidad de la empanada')
        empanadas.append(empanada)
        print('Empanada registrada...')

    elif(opcionempanada ==2):
        
        for empanada in empanadas:
            print(empanada)
        else: 
            print('Empanada no existe')
        system('cls')

    elif(opcionempanada ==3):
        buscarempanada= int(input('buscar una empanada:'))
        for empanada in empanadas:
            if(buscarempanada == empanada['id']):
                print('Empanada Existe')
                print(empanada)
            else:
                print('No existe la empanada')
        system('CLS')
    elif(opcionempanada ==4):

        buscarempanada= int(input('buscar una empanada:'))
        for empanada in empanadas:
            if(buscarempanada == empanada['id']):
                print('Empanada Existe')
                print(empanada)
            else:
                print('precio actual es:')
                print(empanada['precio'])
                precionuevo=float(input('Digite nuevo precio:'))
                empanada['precio']=  precionuevo
        
    elif(opcionempanada ==5):
        pass
    elif(opcionempanada ==0):
        pass
    else:
        print('')


diccionario = {
    'id':

}