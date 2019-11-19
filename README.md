# ITER

It's a web application for travelers who wish to explore various places around them. 
  
## FEATURES
Sorts places for travellers who are cautious about the distance of travelling and the weather and temperature it pin points and displays the locations
* Displays weather 
* Displays distance
* Displays temperature
* Points on map
  * waterfalls
  * hills 
  * point of intrest
  * tourist attraction
        
      
     
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install .

```bash
pip install requests
```
#### Use your own openweather and google places api in the place of YOUR_API in repo
---
## Skills used 
### Framework:
![django](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTU6FqsVwmNWCT1HtzHhk97JLuv3hxQoDw_gNSHJw0UoqS6indX&s)
---
### API used: 
![openweathermap](https://openweathermap.org/themes/openweathermap/assets/img/openweather-negative-logo-RGB.png)![google Places](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYb8iQ15_2yyq5V9HxdXy_ofCSUDPt0i4NVSS5oJjXvtwVcqVr&s)
### Language: 
![python](https://www.freepngimg.com/thumb/python_logo/5-2-python-logo-png-image-thumb.png) ![HTML 5](https://www.freeiconspng.com/uploads/html5-icon-5.png)    ![jQuerry](http://pluspng.com/img-png/jquery-logo-png-jquery-320.png)
### Web development technique: 
  ![Ajax](https://www.intelegain.com/wp-content/uploads/2015/07/ajax.png.pagespeed.ce.GYgbrzG4-W.png)
## CRUX
We get the current location of the user and places info from the google API around the user. Since nearby API shows places around 50KM radius so we calculate the farthest point from the current location for all 8 directions and then we calculate from the farthest place of all 8 directions .(Distance and Directions are calculated using co-ordinates) 
![CRUX](https://i.imgur.com/Kr4Vin6.jpg)
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
