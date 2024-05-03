from multiprocessing import Process, Pipe

def sender(pipe):
    message = "Hello from sender!"
    pipe.send(message)
    pipe.close()

def receiver(pipe):
    received_message = pipe.recv()
    print(f"Received message: {received_message}")

if __name__ == "__main__":
    # Creating a Pipe
    parent_conn, child_conn = Pipe()

    # Creating two processes
    sender_process = Process(target=sender, args=(parent_conn,))
    receiver_process = Process(target=receiver, args=(child_conn,))

    # Starting processes
    sender_process.start()
    receiver_process.start()

    # Waiting for processes to finish
    sender_process.join()
    receiver_process.join()