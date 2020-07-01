# boot.py - - runs on boot-up
import gc
import esp
esp.osdebug(None)
gc.collect()
