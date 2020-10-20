import amino
import random
among_us = ("blanco ","negro ","rojo ","amarillo ","naranja ","rosa ","morado ","azul ","celeste ", "cafe ")
amongUs = ("era el impostor \n0 impostores restantes", "no era el impostor \n1 impostor restante")
client=amino.Client()
client.login(email='munir.dueik.zambrano@gmail.com',password='ab1212ab')
sub_client=amino.SubClient(comId='6795945',profile=client.profile)
comandos = ("/among.us","/stats_rb","/dado","/dato","/chiste","/ping","/reto","/puto_bot","/tank","/5","/11","/13")

lastMessages = []
while True:
	mylastchats=sub_client.get_chat_threads(start=0,size=100).chatId
	for chat in mylastchats:
		msgslist=sub_client.get_chat_messages(chatId=chat,size=2)
		chatInfo=sub_client.get_chat_thread(chatId=chat)
		for nickname,content,id in zip(msgslist.author.nickname,msgslist.content,msgslist.messageId):
			if id in lastMessages:pass
			else:
				print (nickname,content)
				content=str(content).split(" ")
				if content[0][0]=="/":
                                        
					if content[0][1:].lower()=="ping":
						sub_client.join_chat(chatId=chatInfo.chatId)
						sub_client.send_message(message="pong!",chatId=chatInfo.chatId)
                                
					if content[0][1:].lower()=="chiste":
					    sub_client.join_chat(chatId=chatInfo.chatId)
					    sub_client.send_message(message=random.choice(["Calla humano de mrd, no me sé tantos chistes ya que el idiota de mi creador no me enseño muchos","¿Cómo queda un mago después de comer? \nMagordito","¿Por qué estás hablando con esas zapatillas? \nPorque pone <converse>","¡Estás obsesionado con la comida! \nNo se a que te refieres croquetamente","¿Por qué las focas del circo miran siempre hacia arriba? \nPorque es donde están los focos.","Había una vez... TRUS", "Había un pollito que respiraba por el culo, se sentó y se murió", "¡Doctor, doctor! ¡Tengo un hueso fuera!... Entonces dígale que pase ;)"]),chatId=chatInfo.chatId)

					if content[0][1:].lower()=="dato":
					    sub_client.join_chat(chatId=chatInfo.chatId)
					    sub_client.send_message(message=random.choice(["las libelulas cazan mejor que los gatos", "el rugido de un leon se escucha a varios km de distancia", "los tardigrados son el animal más resistente del mundo, si vas a buscarlo, preparate para sorprenderte ;)"]),chatId=chatInfo.chatId)
					if content[0][1:].lower()=="dado":
					    sub_client.join_chat(chatId=chatInfo.chatId)
					    sub_client.send_message(message=str(random.randrange(1,7)),chatId=chatInfo.chatId)

					if content[0][1:].lower()=="help":
					    sub_client.join_chat(chatId=chatInfo.chatId)
					    sub_client.send_message(message="/random: ejecuta un comando random \n/among.us: juega among us XD \n/stats_rb: te lanza stats al azar para rolear contra alguien del chat \n/5-/11-/13: te devuelvo un mensaje que rime con el numero ingresado XD \n/tank: te regalo un tanque \n/puto_bot: atrevete a insultarme con este comando y te parto las piernas \n/reto: te da un desafío al azar \n/ping:responde Pong! \n/chiste:cuenta un chiste \n/dato:cuenta un dato curioso\n/dado: lanza un dado de 6 caras",chatId=chatInfo.chatId)					        
                                
					if content[0][1:].lower()=="reto":
					    sub_client.join_chat(chatId=chatInfo.chatId)
					    sub_client.send_message(message=random.choice(["tu reto es: besar al del mensaje de arriba tuyo","tu reto es: mandar un audio cantando","tu reto es: mandar un audio gimiendo", "tu reto es: ser esclavo de alguien del chat por 24 hrs;)","tu reto es: tener un perfíl furry por 2 días", "tu reto es: hablar en morse por 4 hrs", "tu reto es: nada, no hay, no existe \nPD:suertudo de mrd"]),chatId=chatInfo.chatId)
                                        
					if content[0][1:].lower()=="11":
						sub_client.join_chat(chatId=chatInfo.chatId)
						sub_client.send_message(message="Chupalo entonce",chatId=chatInfo.chatId)
					if content[0][1:].lower()=="5":
						sub_client.join_chat(chatId=chatInfo.chatId)
						sub_client.send_message(message="por el culo te la hinco",chatId=chatInfo.chatId)
					if content[0][1:].lower()=="13":
						sub_client.join_chat(chatId=chatInfo.chatId)
						sub_client.send_message(message="mientras más me la mamas, más me crece",chatId=chatInfo.chatId)
					if content[0][1:].lower()=="tank":
						sub_client.join_chat(chatId=chatInfo.chatId)
						sub_client.send_message(message="███۞███████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃ \n▂▄▅█████████▅▄▃▂ \nI███████████████████]. \n◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...",chatId=chatInfo.chatId)
					if content[0][1:].lower()=="stats_rb":
						sub_client.join_chat(chatId=chatInfo.chatId)
						sub_client.send_message(message="Fuerza:" + " " + str(random.randrange(1,11)) + "\nResistencia:" + " " + str(random.randrange(1,11)) + "\nAgilidad:" + " " + str(random.randrange(1,11)) + "\nVelocidad:" + " " + str(random.randrange(1,11)),chatId=chatInfo.chatId)
            
				
				
					if content[0][1:].lower()=="puto_bot":
						sub_client.join_chat(chatId=chatInfo.chatId)
						sub_client.send_message(message="me ofendes zorra, te voy a mandar una bomba de antimateria a la próxima a ver si te atreves a insultarme de nuevo perra CTM",chatId=chatInfo.chatId)
            
				
				
					if content[0][1:].lower()=="camion-chan":
						sub_client.join_chat(chatId=chatInfo.chatId)
						sub_client.send_message(message="*atropello ninja ha aparecido*",chatId=chatInfo.chatId)
				
				
					if content[0][1:].lower()=="among.us":
						sub_client.join_chat(chatId=chatInfo.chatId)
						sub_client.send_message(message=str(random.choice(among_us)) + str(random.choice(amongUs)),chatId=chatInfo.chatId)

					if content[0][1:].lower()=="random":
						sub_client.join_chat(chatId=chatInfo.chatId)
						sub_client.send_message(message=str(random.choice(comandos)),chatId=chatInfo.chatId)
                      
				lastMessages.append(id)

                                        
