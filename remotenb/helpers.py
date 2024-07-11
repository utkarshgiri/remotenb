import time

def get_os():
    import platform
    return platform.system()

def get_browser_driver(browser):

    osname = get_os()

    if osname == 'Darwin':

        browsers = {'firefox' : "open -a /Applications/Firefox.app %s",
                    'chrome' : 'open -a /Applications/Google\ Chrome.app %s',
                    'edge': 'open -a /Applications/Microsoft\ Edge.app %s',
                    'safari': 'open -a /Applications/Safari.app %s'}
 
        return browsers[browser]

def kill_tmux(client):
    try:
        response = client.run('tmux kill-session -t jupyter')
    except: 
        pass

def start_session(client, executable):
    command = '''tmux new-session -d -s jupyter {}'''.format(executable)
    notebook = client.run(command); time.sleep(2)
    listing = f'{executable} {"list"}'
    notebooks = "{.stdout}".format(client.run(listing, hide=True)).split('\n');
    notebooks = notebooks[1:-1]
    return notebooks

def close_sessions(client, executable, ports):
    #Looping over iterable of ports
    for port in ports:
        #running the command which closes ports
        client.run('%s stop %s'%(executable, port), hide=True)



