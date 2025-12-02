from machine import Pin

sensor = Pin(4, Pin.IN)  # Pin an euren Anschluss anpassen

def wait_for_impact(timeout_ms=5000, quiet_after_ms=300):
    start = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start) < timeout_ms:
        if sensor.value() == 1:  # ggf. invertieren
            last_high = time.ticks_ms()
            while time.ticks_diff(time.ticks_ms(), last_high) < quiet_after_ms:
                if sensor.value() == 1:
                    last_high = time.ticks_ms()
                time.sleep_ms(5)
            return True
        time.sleep_ms(5)
    return False

def read_throws(num_throws=3):
    results = []
    for wurf_index in range(num_throws):
        print("Warte auf Wurf", wurf_index + 1)
        hit = wait_for_impact(timeout_ms=7000)
        if hit:
            print("Wurf", wurf_index + 1, "TRAF -> 1")
            results.append(1)
        else:
            print("Wurf", wurf_index + 1, "KEIN Treffer -> 0")
            results.append(0)
        time.sleep(1000/1000)
    return results[0], results[1], results[2]