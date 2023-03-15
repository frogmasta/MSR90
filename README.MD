## MSR90 Card Reader

This project provides a direct interface to the MSR90 Magnetic Card Reader from Deftun. It sniffs the bytes coming through the USB port and converts them into useable characters. 

THIS HAS ONLY BEEN TESTED ON WINDOWS. SUPPORT FOR OTHER OPERATING SYSTEMS IS NON-EXISTENT. 

Product Link: 
https://www.amazon.com/MSR90-Magnetic-Credit-Reader-Deftun/dp/B01DUB4GVO/ref=sr_1_8?crid=22JU63A4X32Z8&keywords=deftun&qid=1678852639&sprefix=deftun%2Caps%2C92&sr=8-8

## Build

On Windows, you must replace the HidUsb backend with a libusb backend for pyUSB to function properly. This can be accomplished by installing and using the [Zadig](https://zadig.akeo.ie/) software. Please select the libusbK driver from the list. Other drivers might not work with the provided code.

## Issues

Feel free to open a GitHub issue if you encounter any problems with the codebase or open a PR.

## Maintainers

Eric Roth