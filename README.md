# Wemos-LoLin32-Lite

A project utilizing the Wemos-Mini-D1 Microprocessor. The purpose of which is to continue working with and learning Micropython and work out best practices, learn how to develop clean efficient code and hopefully do something relatively useful with it all.

# Purpose

This is a continuation of other, similar projects I work on such as

- [ESP32 Temperature](https://github.com/RedDirtBits/ESP32-Temp-To-Pushover.git)
- [TinyPico Microcontroller](https://github.com/RedDirtBits/TinyPico-ESP32-Temp-To-MQTT.git)

My hope, as with the other projects, is to continue to learn and explore [MicroPython](https://micropython.org/) as well as [Python](https://www.python.org/). This project utilizes the Wemos LoLin32 Lite. My favorite board for anything that requires battery efficiency is the [TinyPico](https://www.tinypico.com/), however, I came across this board quite by accident and it too seems to have a reputation for being a good ESP32 board to use for any kind of battery powered project. It also comes with a standard LiPo battery connector and charging circuit. Whereas the TinyPico uses the ESP32 Pico D4 chip, the Wemos LoLin32 Lite uses the ESP32-DOWDQ6.

As the TinyPico is slightly harder to get and a bit more expensive, I am going to work with this board and hope to find that it is a good compromise between the TinyPico's proven battery efficiency and something a bit more available.

The general idea for this particular board is to not only explore, to some extent, its battery utilization, but to also use it as a testing platform in which I can begin to experiment with freezing my code right into the MicroPython firmware.

I am generally comfortable, though still much to learn, with writing code for Micropython and I find it very rewarding to do so. However, its time to stretch the boundaries a little.

# Next Steps

The first step will be to simply set up the Wemos with one or two sensors and have it report data over MQTT. Once that code has been optimized as best _I_ can do, take it and freeze it into the MicroPython firmware.

After that I will probably add more sensors and see how far I can push the board and just how much I can add to the firmware.
