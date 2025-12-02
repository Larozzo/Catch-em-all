def send_throws():
    w1, w2, w3 = read_throws()
    msg = f"{PLAYER_ID};{w1};{w2};{w3}"
    e.send(b'\xff\xff\xff\xff\xff\xff', msg.encode())
    print("gesendet:", msg)

def main():
    init_espnow()
    send_throws()
    print("Alle Würfe gesendet, fertig.")
  
main()
