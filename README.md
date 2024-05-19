# UAB_THE_HACK_FGC_JOM
Jordi Longaron, Óscar Arrocha, Mustapha El Aichouni
Google Doc:https://docs.google.com/document/d/1Ll9R5XAYoTHUCwEV8KzYTdw_3HK_IC27BYRpO9AhbOc/edit?usp=sharing
## Abstract
This project aims to further assist the blind navigate their way through their daily use of public transport, by employing YOLO algorithms along with TTS. 
## Key words
Blind, Vision, Object segmentation, YOLO, Trains
## Introduction
Throughout history, inequalities have ran rampant, and with few who wanted to help and even fewer ways to bring about actual, substantial, help. Nowadays however, accessibility is much easier to give to clients through tools, software... This project in particular aims to help the blind navigate their way through the subway by notifying them of what appears in their phone through TTS, and for the partially blind or severely visually impaired, we also prepared a mode of the camera that greys out everything except the relevant information, such as obstacles or means to get around.

### Relevance of the device
Even when trying to look at it from a sympathetic perspective, people with good sight likely have no way of knowing just hwo daunting the prospect of moving around using public transport can be, and it is likely that much of the already given aids are not enough. This project, from a social and emotional standpoint, aims to help that. Even if it may not be fully enough, we genuinely hope this can help them to make this smoother than before. 
### What problem it solves?
It aims to alleviate the problems that the blind regularly face when using public transporr in their daily lives by helping them navigate through the subway and helping them know what is beyond the pole.  
## Context
### What has done in the field before? 
We've been made aware that there are QR codes that give directions of where to go from where the QR is placed, but this, however, is a stationary solution to a mobile agent. We whole heartedly believe that a tool that they can bring and actively adapts to their movements can be extremely helpful to this plight, and thus this project came to be. 
### What similar devices have worked or not and why?
Due to the circumstances of this project, we haven't been able to contact any blind people or associations to ask them what other devices they use or what other  tools they use to navigate in their daily life other than the QR.
## Methods
We employed YOLOv8 along with TTS. We fine-tunned our model in order to be able to detect the ticket machines with beter accuracy and from closer. 

### How to employ it
Up until now, for testing we've been using IP Webcam in order to connect our phones to a code.

## Device

### What is your device in context?

#### A) Technical data sheet

#### B) Actors involved
- Blind people and their relatives, since they are the ones most concerned for their (and their own) safety
- FGC staff: Since they are the ones in site to resolve any issues, this project also involves them
- Blind associaitons: We believe that they can benefit from this project, especially if they can rework it for their needs.  
## Conclusion
### Opinion
We believe that this project of ours has been fairly successful considering the time constraints and conditions of the project. We have managed to...:
- 
### Precautions in deployment
As much as we believe that this project has been successful, it hasn't been tested on site, we are especially concerned on how it will perform in an open area or a really frequented area. 
### Futures ideas
There are quite a few features we would have liked to implement in due time: 
- A way to connect with the intercom by looking up to the screen so that they read out loud the train timings
- A way to guide them better within the station, such as where they must go to reach a line in particular, or where does the train for a destination arrive within a station, possibly through a color code and when the camera detects that color they tell them which way that color leads to.
- A better way to detect train gates and if they are open or not. 

### Learnings from the process

references:
https://www.youtube.com/watch?v=skN1o6Fb2P8,
https://github.com/CASIA-IVA-Lab/FastSAM,
https://github.com/ChaoningZhang/MobileSAM,
https://github.com/KdaiP/MobileSAM-fast-finetuning
