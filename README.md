# WAP-Planner
WAP plan generator based on band, capacity, and room dimensions

Small script written in Python that calculates and displays optimal wireless access point (WAP) and channel placement 
within a room with given room dimentions (L x W), anticipated number of clients, frequency band (2.4 GHz, 5 GHz), 
and data rate requirements.

Assumptions and notable points:
* Uses square packing
* Does not take into account objects within room that may affect signal propagation
* Program relies on wireless AP rule of thumb: 20 - 30 users per AP depending on data rate requirements given 
* Power to distance calculations based upon the work of [Nigel Bowden](http://wifinigel.blogspot.ca/2014/11/effect-of-transmit-power-changes-on-ap.html)
* Uses Graphics.py for GUI and solution presenter
	
<p align="center">
 <img src="https://user-images.githubusercontent.com/8539492/30923909-3145d6be-a37b-11e7-8527-e356bc0964ba.PNG"/>
 <img src="https://user-images.githubusercontent.com/8539492/30923911-32c9adee-a37b-11e7-822c-92d16d8c437e.PNG"/>
</p>