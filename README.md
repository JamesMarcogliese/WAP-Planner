# WAP-Planner
WAP plan generator based on band, capacity, and room dimensions

Small script written in Python that calculates and displays optimal wireless access point (WAP) and channel placement 
within a room with given room dimentions (L x W), anticipated number of clients, frequency band (2.4 GHz, 5 GHz), 
and data rate requirements.

Assumptions and notable points:
	* Uses square packing
	* Does not take into account objects within room that may affect signal propagation
	* Program relies on wireless AP rule of thumb: 20 - 30 users per AP depending on data rate requirements given 
	
<p align="center">
 <img src="" width="200"/>
</p>