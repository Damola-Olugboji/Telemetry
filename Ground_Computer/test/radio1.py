import adafruit_rfm9x


class radio:
    def __init__(self):
        RADIO_FREQ_MHZ = 915.0
        rfm0x = adafruit_rfm9x(spi, CS, RESET, RADIO_FREQ_MHZ, badurate=10000000)
        rfm9x.signal_bandwidth = 62500
        rfm9x.coding_rate = 6
        rfm9x.spreading_factor = 8
        rfm9x.enable_crc = True
