# TFM Project - Gestural interface for interaction with generative music

This is a project developed by Manuel Muriel Molina as the final master project for the studies in the Internet of Things master's degree in UCM (Universidad Complutense de Madrid).

In this project we have developed an interactive music system controlled by the position of the hand seen by a camera and the gestures made in the air. The position of the hand, detected by the camera and processed with MediaPipe, will allow us to interact with different parameters such as tone, volume or distribution. The gestures we make with the whole hand, detected with the Nicla Sense ME board, allow us to pause the music or resume it.

The music on which we will do this interaction is a piece of generative music, that is, a composition produced in real time in an algorithmic way, according to a specific set of logical control rules. Starting from a generative music code we will be able to change parameters of this code to modify the sound that is generated.

This project aims to bring the applications of the Internet of Things to a field of entertainment, thus seeing the possibilities that this technology can bring when applied to music and develop our creativity as we interact with it in various ways. It is mainly an exploratory work to investigate about this musical interaction using elements and tools seen during this master.

Although the main objective is entertainment, it also serves as a demonstration of the potential of the different tools used such as the Nicla Sense ME board, which is able to perform the inference of a previously trained gesture in a matter of milliseconds, highlighting the importance of edge computing. In addition, the backbone of this project is a Raspberry Pi 4, an inexpensive and portable mini-computer capable of supporting a complex IoT system.

The codes that must be run on the Raspberry Pi for the project to work are the following ones:

 - /ESP_osc/esp_sc_notify.py -> This code connects the Raspberry to the ESP32 via BLE and receives the gestures detected by the Nicla Sense ME.
 - /mediapipe/mediapIndexOSC.py -> This code opens a preview of the camera detecting the position of the hand and creating the gestural interface.
 - /pyo/musicmediap.py -> The last code starts the generative melody and receives the OSC messages from the other scripts making the melody interactive.

Some videos displaying the functionality of this project can be found in the following link: https://drive.google.com/drive/folders/1_9UT8cEXszJINwEwA9QMOgJ64275WEkR?usp=sharing
