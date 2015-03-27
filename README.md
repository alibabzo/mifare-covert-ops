# mifare-covert-ops
Python code for covert-ish RFID capturing (and later emulation*) on a Raspberry Pi.
Or at least that's what I'm using it for.

### You will need:
* [This GPIO setup](http://razzpisampler.oreilly.com/images/rpck_1101.png)
* [libnfc](http://nfc-tools.org/index.php?title=Libnfc)
* An ACR122U reader or similar
* Python 2.7

### How to use
* Activate the script with `sudo python capture.py`
* Press the button when you think your reader is over a card
* The script saves the UID of that card to a file

\* I'm not entirely sure if emulation is possible with this setup (I tested it and no luck). Will be buying a UID changeable Mifare card as I think this will work better.
