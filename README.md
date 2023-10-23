# A-study-of-nighttime-vehicle-detection-algorithms  
  
This is my master thesis. Whole code is messy but right now but it could be useful for somebody.

Link to dataset: https://doi.org/10.34808/e8ht-d443 https://mostwiedzy.pl/pl/open-research-data/a-study-of-nighttime-vehicle-detection-algorithms,10070936421042877-0

Link to thesis: http://download.panjacob.pl/Badanie_algorytm%c3%b3w_wykrywania_pojazd%c3%b3w_w_porze_nocnej.pdf

### The study used 4 methods to identify vehicles:
- Detection on image  
- Classification of detection results on image  
- Image classification  
- Classification of light intensity samples  
  
  **![](https://lh4.googleusercontent.com/5rpf0Z59laU8tGHi8wlZIJ1qeBVajA2zqIryAWcZdDSB_NMw7Kn3fzD-plv41FUmadDneixGGfBKG6tzBVZeChK-j2SIS8BPUNmwntDJl_ZPIGhVJ0ACWwfsgjNIzIgTIhiU3nO2V_fGRQQSA-YaoLrUAg=s2048)**

### Testing platform

Nvidia Jetson Nano, Raspberry Pi 4 (both 4GB) and Google Coral USB Accelerator.

**![](https://lh4.googleusercontent.com/jWGVvxsZAvriwbFUVvDQMLPGlcemiVnYrjfrB5W0BQ6TxhZD3BUagSydXQfRKlcriXih_UkSBHJ2V8GPF3EHd3L1u33QRQD1fb6XMjWc9ndIVekQBGm9biq_Ov8jIolrrVuw3_GN5x5iOnLfZg3hErZhaQ=s2048)**



### Training
**![](https://lh6.googleusercontent.com/t8bDTo8isU8CPiXl9yhBvVCzCJBBgAhYkFy7kY1owlgy6c0M5hbKP065k5ArhlyI1hdjZLKwF7jUJAhEp83lZqKcrOxCFFNrFohK-fPljeL4JFFrH1nF1kmhrw6pRcyV8YZU-ruYH7-cw_lnQXJ_9jVvtA=s2048)**
![Pasted image 20231023144125](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/4ff1d66d-f09d-4394-8a2e-44c308407e0e)
![Pasted image 20231023144150](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/360d2e9d-e270-4df1-9165-616e9f357a1e)
![Pasted image 20231023144232](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/c78417c2-de15-4e81-b1ae-144ac713fa3a)
![Pasted image 20231023144259](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/a7513758-12d5-4886-b40d-7864fbd2bb11)

### Optimalisation
![Pasted image 20231023144334](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/4707c164-808b-4a4e-bfba-dab4c2a95bb2)
![Pasted image 20231023144400](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/de424b46-f50d-4d49-bb38-126f24e68880)
![Pasted image 20231023144420](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/85aad9c7-d218-4631-b88f-61707a2a2d1b)
![Pasted image 20231023144434](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/ea1b6261-74f6-4934-80de-e6081b6a559e)
### Performance of networks
![Pasted image 20231023144459](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/58002592-a196-46d8-8318-b006fb4de2b0)
The work did not take into account the braking distance of the vehicle. With breaking distance it is required that algorithms performs inference at **2.2 FPS**.
![Pasted image 20231023144658](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/543f5fb7-d439-4b4c-b914-be271cb2e046)
![Pasted image 20231023144710](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/4a961a58-7c8b-40b3-a08e-ba920f26c901)
![Pasted image 20231023144721](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/85139774-140f-41e9-8300-1414de5778a0)
![Pasted image 20231023144748](https://github.com/panjacob/A-study-of-nighttime-vehicle-detection-algorithms/assets/44145413/311601f5-e682-4345-bfb1-7c7eb684a8cf)

