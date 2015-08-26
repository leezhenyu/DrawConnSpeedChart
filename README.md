# DrawConnSpeedChart

### About this project
I want to benchmark my company's server connection speed, so I create this automation testing tool. 

### Prerequisite
  * Python 2.7+
  * NumPy
  * Matplotlib
  * speedtest-cli

You can install the last three python library by **pip** or **easy_install**.

### About Remote Speedtest Server
See the code snippet:
```
servers = [[6424,"Tokyo"],[2327,"Taipei"],[3914,"Singapore"],[5029,"New_York"],[4042,"San_Jose"],[4185,"Durham"]]
```
This Python list defined the Server ID of the speedtest server you want to create a connection. You can get the id by execute this commend:
```
speedtest-cli --list
```  
If Interne connection is exist, you can see the list of test servers. Please modify the code to change remote servers.

### Execution
```
python DarwConnSpeedChart.py
```

### Output Example
![enter image description here](https://lh3.googleusercontent.com/-BevfM0yGscY/Vd2OscLmAXI/AAAAAAABtA8/VHb2JP_NrlU/s0/2015082609Benchmark.png "2015082609Benchmark.png")




