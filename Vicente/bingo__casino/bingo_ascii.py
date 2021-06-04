def premio_linea():
    print('''
                                            ██      ██ ███    ██ ███████  █████  
                                            ██      ██ ████   ██ ██      ██   ██ 
                                            ██      ██ ██ ██  ██ █████   ███████ 
                                            ██      ██ ██  ██ ██ ██      ██   ██ 
                                            ███████ ██ ██   ████ ███████ ██   ██ 
                                ''')

def premio_bingo():
    print('''
                                            ██████  ██ ███    ██  ██████   ██████  
                                            ██   ██ ██ ████   ██ ██       ██    ██ 
                                            ██████  ██ ██ ██  ██ ██   ███ ██    ██ 
                                            ██   ██ ██ ██  ██ ██ ██    ██ ██    ██ 
                                            ██████  ██ ██   ████  ██████   ██████                        
                                ''')

def premio_linea_cpu():
    print('''
                        ██   ██  █████  ███    ██      ██████  █████  ███    ██ ████████  █████  ██████   ██████  
                        ██   ██ ██   ██ ████   ██     ██      ██   ██ ████   ██    ██    ██   ██ ██   ██ ██    ██ 
                        ███████ ███████ ██ ██  ██     ██      ███████ ██ ██  ██    ██    ███████ ██   ██ ██    ██ 
                        ██   ██ ██   ██ ██  ██ ██     ██      ██   ██ ██  ██ ██    ██    ██   ██ ██   ██ ██    ██ 
                        ██   ██ ██   ██ ██   ████      ██████ ██   ██ ██   ████    ██    ██   ██ ██████   ██████  
                                                                                                                  
                                                                                                                
                                            ██      ██ ███    ██ ███████  █████                                   
                                            ██      ██ ████   ██ ██      ██   ██                                  
                                            ██      ██ ██ ██  ██ █████   ███████                                  
                                            ██      ██ ██  ██ ██ ██      ██   ██                                  
                                            ███████ ██ ██   ████ ███████ ██   ██                                                                                            
    ''')

def premio_bingo_cpu():
    print('''
                        ██   ██  █████  ███    ██      ██████  █████  ███    ██ ████████  █████  ██████   ██████  
                        ██   ██ ██   ██ ████   ██     ██      ██   ██ ████   ██    ██    ██   ██ ██   ██ ██    ██ 
                        ███████ ███████ ██ ██  ██     ██      ███████ ██ ██  ██    ██    ███████ ██   ██ ██    ██ 
                        ██   ██ ██   ██ ██  ██ ██     ██      ██   ██ ██  ██ ██    ██    ██   ██ ██   ██ ██    ██ 
                        ██   ██ ██   ██ ██   ████      ██████ ██   ██ ██   ████    ██    ██   ██ ██████   ██████  
                                                                                                                  
                                                                                                                
                                            ██████  ██ ███    ██  ██████   ██████  
                                            ██   ██ ██ ████   ██ ██       ██    ██ 
                                            ██████  ██ ██ ██  ██ ██   ███ ██    ██ 
                                            ██   ██ ██ ██  ██ ██ ██    ██ ██    ██ 
                                            ██████  ██ ██   ████  ██████   ██████                                                                                             
    ''')

def titulo_menu_bingo(fichas):
    if fichas > 100 and fichas < 1000:
        fichas = str(fichas)
        fichas = fichas+'  '
    
    elif fichas >= 1000 and fichas < 10000:
        fichas = str(fichas)
        fichas = fichas+' '

    print('''
╔══════════════╗        ██████  ██ ███████ ███    ██ ██    ██ ███████ ███    ██ ██ ██████   ██████         ╔══════════════╗  
  SALIR  (ESC)          ██   ██ ██ ██      ████   ██ ██    ██ ██      ████   ██ ██ ██   ██ ██    ██          FICHAS: ''',fichas,'''   
╚══════════════╝        ██████  ██ █████   ██ ██  ██ ██    ██ █████   ██ ██  ██ ██ ██   ██ ██    ██        ╚══════════════╝ 
                        ██   ██ ██ ██      ██  ██ ██  ██  ██  ██      ██  ██ ██ ██ ██   ██ ██    ██ 
                        ██████  ██ ███████ ██   ████   ████   ███████ ██   ████ ██ ██████   ██████  
                                                                                                    
                                                                                                    
                                 █████  ██          ██████  ██ ███    ██  ██████   ██████           
                                ██   ██ ██          ██   ██ ██ ████   ██ ██       ██    ██          
                                ███████ ██          ██████  ██ ██ ██  ██ ██   ███ ██    ██          
                                ██   ██ ██          ██   ██ ██ ██  ██ ██ ██    ██ ██    ██          
                                ██   ██ ███████     ██████  ██ ██   ████  ██████   ██████   
  
                    ┌─┐┬  ┬┌─┐┌─┐  ┌─┐┬ ┬┌─┐┌┐┌┌┬┐┌─┐┌─┐  ┌─┐┌─┐┬─┐┌┬┐┌─┐┌┐┌┌─┐┌─┐  ┌─┐ ┬ ┬┬┌─┐┬─┐┌─┐┌─┐
                    ├┤ │  ││ ┬├┤   │  │ │├─┤│││ │ │ │└─┐  │  ├─┤├┬┘ │ │ ││││├┤ └─┐  │─┼┐│ ││├┤ ├┬┘├┤ └─┐
                    └─┘┴─┘┴└─┘└─┘  └─┘└─┘┴ ┴┘└┘ ┴ └─┘└─┘  └─┘┴ ┴┴└─ ┴ └─┘┘└┘└─┘└─┘  └─┘└└─┘┴└─┘┴└─└─┘└─┘  
    ''')

def boton_jugar():
    print('''
                                         ╔═════════════════════════════════════════╗
                                         ║              ┬┬ ┬┌─┐┌─┐┬─┐              ║
                                         ║              ││ ││ ┬├─┤├┬┘              ║
                                         ║              ┘└─┘└─┘┴ ┴┴└─       (ENTER)║
                                         ╚═════════════════════════════════════════╝    
    ''')
