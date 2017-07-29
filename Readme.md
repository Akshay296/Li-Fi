# Visible Light Communication
 What if even visible light could be used to transmit and receive data wirelessly? We developed a prototype that could do exactly that. Imagine the number of light sources around you, which is far greater than the number of radio base stations. We can use them for communication without defying their primary purpose that is illumination.

 Li-Fi.ino is a module which implements the concept using Arduino's.In this project we can communicate between two laptops via serial monitors. 
 
## Setup
 We used two arduino microcontrollers, one acts as a transmitter and the other as a receiver. Transmitter module consists of an inexpensive led which is connected to pin 22 of Arduino Due microcontroller. Receiver module consists of a LDR (Light Dependent Resistor : when light intensity is low the resistance offered is high compared to when light intensity is high) connected to analog pin A1.

## Process
####Transmitter 
1. Whatever we type on serial monitor is read using inbuilt Serial.readstring() function.
2. The string is then sent to send_data() function which converts them to bits.
3. The sending packet consists of 8 bit starting pattern (10011001) so that reciever can acknowledge that data is to be recieved. 
4. Ascii value of each character in string is then converted to 8 bit binary number using inbuilt bitRead() function. This 8 bit binary number is appended to sending packet.
5. Now this packet is processed and led's intensity is modulated as follows:
    * Starting bit pattern :
        1: Led glows for a given duration 
        0: Led is switched off for the given duration
    * Rest message bits are sent using manchester encoding to avoid flickering:
        1: Led first glows for given duration and then is switched off for the same duration (i.e 1 is represented as `HIGH-LOW`)
        0: Led is first switched off for given duration and then turned on for the same duration (i.e 0 is represented as `LOW-HIGH`)
6. The message transmitted is then shown on the serial monitor of transmitter.

####Receiver
1. The analog pin A1 is continously polled at a fixed duration and the analog value (0-1024) is averaged over 24 readings to get the threshold (i.e. room light intensity).
2. If the measured value is more then threshold it is recorded as 1 whereas if it is less than room intensity it is recorded as 0.
3. The recieved bit pattern is continously compared with starting bit pattern. If there is a match, subsequent 16 readings taken is considered as message bits.
4. The 16 bit message is grouped in pairs . If pair is:
    "10" : It is considered as 1
    "01" : It is considered as 0
5. The 8-bit pattern so obtained is converted to ascii. The character value corresponding to ascii is printed in Serial monitor of receiver.

## Modules 
### Li-Fi.ino
 This module is used to transmit and receive text using serial monitors. The message typed in Serial Monitor is converted to bit pattern which is used to drive a led. Any light pattern received using LDR is converted back to text and displayed on Serial Monitor.

### tx_CRC.py
This module uses 17 bit polynomial i.e x^16 + x^12 + x^5 + 1 to calculate CRC(Cyclic Redundancy Check). First we read the binary text to be sent from a file. The message is broken in packets of 2048 bits. Generator polynomial is represented in binary. Each 2048 bit packet is appended with 16, 0's . The packet is XORed with generator. The last 16 bit remainder is appended at the end of the packet and is sent


### rx_CRC.py
This module uses 17 bit polynomial i.e x^16 + x^12 + x^5 + 1 to verify message using CRC(Cyclic Redundancy Check). First we read the received text from a file. The recieved message is broken in packets of 2064 bits. Generator polynomial is represented in binary. Rest of packet is XORed with generator. If the resulting sequence does not consist of any 1's we conclude that the mesage sent is correct and is written in `Received_text.txt`

